#!/usr/bin/env python3

import time
import discord

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

client = discord.Client()

@client.event
async def on_ready():
	print("logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	if not (message.author.id == 431978032094380043):
		return
	if not message.content.startswith("sandman"):
		return
	args = message.content.replace("sandman ","")
	argslist = args.split(" ")
	if(argslist[0] == "attack"):
		await message.channel.send("hoogagagagagagagagagaga")

client.run(token)
