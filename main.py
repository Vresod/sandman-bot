#!/usr/bin/env python3

from time import sleep
import discord

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

client = discord.Client()

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
	if not (message.author.id == 431978032094380043):
		return
	if not message.content.startswith("sandman"):
		return
	args = message.content.replace("sandman ","")
	argslist = args.split(" ")
	if(argslist[0] == "attack"):
		await message.channel.send("hoogagagagagagagagagaga")
	if(argslist[0] == "blind"):
		if(message.mentions[0].id == 431978032094380043 or message.mentions[0].id == 713221599863635978):
			await message.channel.send("i act in self preservation; i cannot attack my owner or myself")
			return
		sandmanrole = message.guild.get_role(713246200555372544) # 713246200555372544 is the sandman role in the server this bot is originally used in
		await message.channel.send("blinding {0}".format((message.mentions[0]).display_name))
		await message.mentions[0].add_roles(sandmanrole,reason="blinded by sandman")
		sleep(10)
		await message.mentions[0].remove_roles(sandmanrole,reason="unblinded by sandman")
		await message.channel.send("{0} has recovered from his blindness".format((message.mentions[0]).display_name))
	if(argslist[0] == "retreat"):
		await client.change_presence(status=discord.Status.idle)
	if(argslist[0] == "unretreat"):
		await client.change_presence(status=discord.Status.online)

client.run(token)
