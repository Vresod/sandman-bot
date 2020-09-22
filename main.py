#!/usr/bin/env python3

from asyncio import sleep
import discord
import extras
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
	if(message.author.id == bot_owner_id and message.channel == message.author.dm_channel):
		images = await extras.attachments_to_files(message.attachments)
		bot_owner_as_member = client.get_channel(general_channel_id).guild.get_member(bot_owner_id)
		message_send_channel = ""
		if not bot_owner_as_member.guild.get_role(dead_role_id) in bot_owner_as_member.roles:
			message_send_channel = client.get_channel(general_channel_id)
		else:
			message_send_channel = client.get_channel(dead_channel_id)
		print(f'repeating {message.content}')
		await message_send_channel.send(message.content,files=images)
		return
	global message_counter
	message_counter += 1
	if message_counter == 25:
		await message.channel.send("hooga")
		message_counter = 0
	args = message.content.replace(f"{prefix} ","")
	argslist = args.split(" ")
	if(argslist[0] == "repo"):
		await message.channel.send(f"my source code is available at {sandman_repo}")
	if not (message.author.id == bot_owner_id): # set bot_owner_id in settings.py
		return
	if not message.content.startswith(prefix):
		return
	dreamrole = message.guild.get_role(dream_role_id) # set dream_role_id in settings.py
	blindrole = message.guild.get_role(blind_role_id) # set blind_role_id in settings.py
	if(argslist[0] == "attack"):
		await message.channel.send("hoogagagagagagagagagaga")
	elif(argslist[0] == "blind"):
		if(message.mentions[0].id == bot_owner_id or message.mentions[0] == client.user):
			await message.channel.send("hooga (i act in self preservation; i cannot attack my owner or myself)")
			return
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
	elif(argslist[0] == "enter"):
		if(message.mentions[0].id == bot_owner_id or message.mentions[0] == client.user):
			await message.channel.send("hooga (i act in self preservation; i cannot attack my owner or myself)")
			return
		await client.get_channel(general_channel_id).send("hooga (knocking out {0})".format((message.mentions[0]).display_name))
		await message.mentions[0].add_roles(dreamrole,reason="knocked out by sandman")
		await sleep(90)
		if(dreamrole in message.mentions[0].roles):
			await message.mentions[0].remove_roles(dreamrole,reason="woken up from sandman enter")
			await client.get_channel(general_channel_id).send("hooga ({0} has woken up!)".format((message.mentions[0]).display_name))
			await client.get_channel(dream_channel_id).send("{0} has woken up!".format((message.mentions[0]).display_name))
	elif(argslist[0] == "release"):
		await message.mentions[0].remove_roles(dreamrole,reason="released from sandman enter")
		await client.get_channel(general_channel_id).send("hooga ({0} has been released.)".format((message.mentions[0]).display_name))
		await client.get_channel(dream_channel_id).send("{0} has been released.".format((message.mentions[0]).display_name))
	elif(argslist[0] == "echo"):
		images = await extras.attachments_to_files(message.attachments)
		await message.delete()
		await message.channel.send(message.content[len(prefix) + 6:],files=images) # adding 5 for length of " echo"
		print(f'repeating {message.content[len(prefix) + 6:]}') # read above line's comment
        

client.run(token)
