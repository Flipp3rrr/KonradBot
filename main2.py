# Import modules
print("Importing 'discord', 'discord.ext', 'os', and 'random'...")
import discord
from discord.ext import commands
import os
import random

# Get bot token
runDir = os.path.dirname(__file__)
try:
    print("Attempting to read 'token.txt'...")
    tokenPath = os.path.join(runDir, "token.txt")

    # Read 'token.txt'
    with open("token.txt", "r") as file:
        btoken = file.read().replace("\n", "")
        print("Bot token read from 'token.txt'!")
except:
    # Input if no 'token.txt' found
    print("No 'token.txt' found!")
    btoken = input("TOKEN >> ")

client = discord.Client()

@client.event
async def on_ready():
    print("USERNAME: {0.user}".format(client))
    print("USER ID:  ???\n".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!k ping'):
        await message.channel.send('Pong!')
        print("Pinged!")

client.run(btoken)