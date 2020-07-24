#!/usr/bin/env python3

from asyncio import sleep
import discord
# having a seperate python file for bot settings is probably not the best way to do this
# but it makes things simpler on the main file. just import the file.
from settings import *
with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

istatus = discord.Status.online
cstatus = discord.Game(name="with your dreams")

client = discord.Client(status=istatus,activity=cstatus)

@client.event
async def on_ready():
	print("logged in as {0.user}".format(client))

message_counter = 0
@client.event
async def on_message(message):
	if message.author.bot:
		return
	global message_counter
	message_counter += 1
	if message_counter == 25:
		await message.channel.send("hooga")
		message_counter = 0
	if not (message.author.id == bot_owner_id): # set bot_owner_id in settings.py
		return
	if not message.content.startswith("sandman"):
		return
	args = message.content.replace("sandman ","")
	argslist = args.split(" ")
	if(argslist[0] == "attack"):
		await message.channel.send("hoogagagagagagagagagaga")
	elif(argslist[0] == "blind"):
		if(message.mentions[0].id == bot_owner_id or message.mentions[0] == client.user):
			await message.channel.send("hooga (i act in self preservation; i cannot attack my owner or myself)")
			return
		blindrole = message.guild.get_role(blind_role_id) # set blind_role_id in settings.py
		await client.get_channel(general_channel_id).send("hooga (blinding {0})".format((message.mentions[0]).display_name))
		await message.mentions[0].add_roles(blindrole,reason="blinded by sandman")
		await sleep(10)
		await message.mentions[0].remove_roles(blindrole,reason="unblinded by sandman")
		await client.get_channel(general_channel_id).send("hooga ({0} has recovered from his blindness)".format((message.mentions[0]).display_name))
	elif(argslist[0] == "status"):
		if(argslist[1] in ["online","idle","dnd","offline"]):
			await client.change_presence(status=discord.Status[argslist[1]])
		else:
			await message.channel.send("hooga (pick a valid status)")
	elif(argslist[0] == "gif"):
		await message.channel.send("hooga (hehe funny https://tenor.com/beIqe.gif )")
	elif(argslist[0] == "knockout"):
		if(message.mentions[0].id == bot_owner_id or message.mentions[0] == client.user):
			await message.channel.send("hooga (i act in self preservation; i cannot attack my owner or myself)")
			return
		await client.get_channel(general_channel_id).send("hooga (knocking out {0})".format((message.mentions[0]).display_name))
		dreamrole = message.guild.get_role(dream_role_id) # set dream_role_id in settings.py
		await message.mentions[0].add_roles(dreamrole,reason="knocked out by sandman")
		await sleep(50)
		await message.mentions[0].remove_roles(dreamrole,reason="knocked out by sandman")
		await client.get_channel(general_channel_id).send("hooga ({0} has woken up!)".format((message.mentions[0]).display_name))
		await client.get_channel(dream_channel_id).send("{0} has woken up!".format((message.mentions[0]).display_name))

client.run(token)
