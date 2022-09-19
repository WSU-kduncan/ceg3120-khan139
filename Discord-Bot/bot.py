import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    discord_quotes = [
        'Hello World!',
        'Hey!',
        'Have a good day!',
    ]

    if message.content == 'greeting!':
        #response = random.choice(brooklyn_99_quotes)
        response = random.choice(discord_quotes)
        await message.channel.send(response)

client.run(TOKEN)
