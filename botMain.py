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

client.run(os.getenv('TOKEN'))
