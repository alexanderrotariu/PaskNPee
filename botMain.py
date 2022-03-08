import discord, requests, os, random
from dotenv import load_dotenv
from discord import Embed

#MATH (RANDOM)
randomInt = random.randint(0,4)
benRunning = False

#SETTING GIF FILES
reactYesGif = 'https://cdn.discordapp.com/attachments/809254468700471337/950618030776406026/yes.gif'
reactNoGif = 'https://cdn.discordapp.com/attachments/809254468700471337/950619058460586004/no.gif'
reactEwwGif = 'https://cdn.discordapp.com/attachments/809254468700471337/950618453126021160/eww.gif'
reactLaughGif = 'https://cdn.discordapp.com/attachments/809254468700471337/950618783419097098/laugh.gif'
reactSlamGif = 'https://cdn.discordapp.com/attachments/809254468700471337/950617818729164820/slamphone.gif'
reactPickupGif = 'https://cdn.discordapp.com/attachments/809254468700471337/950610478021869568/benring.gif'

#BEN RESPONSES
benResponses = ['Yes.', 'No.', '*Laughs*', 'Eww', '*Slams Phone*']
benResponsesGifs = [reactYesGif, reactNoGif, reactLaughGif, reactEwwGif, reactSlamGif]
benStartup = ["ben", "Ben", "BEN", "!ben", "!Ben", "!BEN", "call ben", "call Ben", "Call Ben", "!callBen", "!callben"]
benShutdown = ["stop", "shutdown", "!stop", "!shutdown", "ben stop", "Ben stop", "Stop", "Shutdown", "!Stop", "Shutdown"]

#CREDENTIALS 
load_dotenv('.env')

#BOT STARTUP
client = discord.Client()
@client.event
async def on_ready():
    print('YOOOOOOO {0.user}'.format(client))
    print('The bot is logged in.')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers!"))

#DETECTION
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
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/949844011466760254/950620476818997279/benThumb.png")

        await message.channel.send(embed=embed)

    if message.content in benStartup:
        benRunning = True
        await message.channel.send("Ben picked up the phone.")
        await message.channel.send(reactPickupGif)

    while benRunning:
        if message.content.endswith("?"):
            if randomInt == 4:
                #could remove the responses since we have text in the gifs now, just comment that line out?
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

        else:
            return

client.run(os.getenv('TOKEN'))