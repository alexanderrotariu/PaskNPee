import discord, requests, os, random
from dotenv import load_dotenv
from discord import Embed


#MATH (RANDOM)
randomInt = random.randint(0,4)
benRunning = False

#SETTING GIF FILES
reactYesGif = 'https://cdn.discordapp.com/attachments/949844011466760254/950527231099301909/benGifYes.gif'
reactNoGif = 'https://cdn.discordapp.com/attachments/949844011466760254/950520552815226912/benNoGif.gif'
reactEwwGif = 'https://cdn.discordapp.com/attachments/949844011466760254/950528129481469962/benGifEww.gif'
reactLaughGif = 'https://cdn.discordapp.com/attachments/949844011466760254/950537475489665104/benlaugh.gif'
reactSlamGif = 'https://cdn.discordapp.com/attachments/949844011466760254/950528268807864350/benGifSlam.gif'
reactPickupGif = 'https://cdn.discordapp.com/attachments/949844011466760254/950538217654992956/benGifPickup.gif'

#BEN RESPONSES
benResponses = ['Yes.', 'No.', '*Laughs*', 'Eww', '*Slams Phone*']
benResponsesGifs = [reactYesGif, reactNoGif, reactLaughGif, reactEwwGif, reactSlamGif]
benStartup = ["ben", "Ben", "BEN", "!ben", "!Ben", "!BEN", "call ben", "call Ben", "Call Ben", "!callBen", "!callben"]
benShutdown = ["stop", "shutdown", "!stop", "!shutdown", "ben stop", "Ben stop", "Stop", "Shutdown", "!Stop", "Shutdown"]

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

    if message.content.startswith('!benHelp'): #to do
        embed = Embed(title="Talking Ben: ", color=0xBD9A7A)
        embed.add_field(name="Commands:", value="!callBen: starts conversation with Ben\n !stop: stops conversation with Ben")

        await message.channel.send(embed=embed)

        #await message.channel.send("!callBen: starts conversation with Ben")
        #await message.channel.send("!stop: stops conversation with Ben")

    if message.content in benStartup:
        benRunning = True
        await message.channel.send("Ben picked up the phone.")
        await message.channel.send(reactPickupGif)

    while benRunning:
        if message.content.endswith("?"):
            if randomInt == 4:
                await message.channel.send(benResponses[randomInt])
                await message.channel.send(benResponsesGifs[randomInt])
                randomInt = random.randint(0,4)
                await message.channel.send("Ben has decided to shutdown.")
                benRunning = False

            else:
                await message.channel.send(benResponses[randomInt])
                await message.channel.send(benResponsesGifs[randomInt])
                randomInt = random.randint(0,4)

        if message.content in benShutdown:
            await message.channel.send("Ben is shutting down.")
            benRunning = False

        ##https://cdn.discordapp.com/attachments/949844011466760254/950520552815226912/benNoGif.gif

        ##if not message.content.startswith("!benShutdown"):
            ##await message.channel.send('Not a valid question, end in question marks or input \"!benShutdown\" to stop reading')

        ##if not message.content.endswith("?"):
            ##await message.channel.send('Not a valid question, end in question marks or input \"!benShutdown\" to stop reading')

        else:
            return

client.run(os.getenv('TOKEN'))