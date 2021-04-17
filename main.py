import discord
import os
import config

cfg = config.Config(".config")
TOKEN = cfg["TOKEN"]


client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    

@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    else:

        if(message.content.startswith("$hello")):
            await message.channel.send("Que paza chavale")
            
client.run(TOKEN)
