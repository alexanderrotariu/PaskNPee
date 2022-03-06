import discord, requests, os
from dotenv import load_dotenv

#CREDENTIALS 
load_dotenv('.env')

client = discord.Client()

@client.event
async def on_ready():
    print('YOOOOOOO {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.endswith("?"):
        await message.channel.send("detected question")

client.run(os.getenv('TOKEN'))
