import discord, requests, os, random
from dotenv import load_dotenv

#MATH (RANDOM)
randomInt = random.randint(0,3)
benRunning = False

##BEN RESPONSES
benResponses = ['Yes.', 'No.', '*Slams Phone*', 'Eww']

#CREDENTIALS 
load_dotenv('.env')

client = discord.Client()

@client.event
async def on_ready():
    print('YOOOOOOO {0.user}'.format(client))

@client.event
async def on_message(message):
    global benRunning
    global randomInt
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith("!benStartup"):
        benRunning = True
        await message.channel.send("Ben is starting up.")

    while benRunning:
        if message.content.endswith("?"):
            await message.channel.send(benResponses[randomInt])
            randomInt = random.randint(0,3)

        if message.content.startswith("!benShutdown"):
            benRunning = False
            await message.channel.send("Ben is shutting down.")

        ##if not message.content.startswith("!benShutdown"):
            ##await message.channel.send('Not a valid question, end in question marks or input \"!benShutdown\" to stop reading')

        ##if not message.content.endswith("?"):
            ##await message.channel.send('Not a valid question, end in question marks or input \"!benShutdown\" to stop reading')

        else:
            return

client.run(os.getenv('TOKEN'))
