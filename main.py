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
    with open('token.txt', 'r') as file:
        btoken = file.read().replace('\n', '')
        print("Bot token read from 'token.txt'!")
except:
    print("No 'token.txt' found!")
    btoken = input("TOKEN >> ")

# Prefix
bot = commands.Bot(command_prefix='k! ')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# Ping command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
    print("Pinged!")

print("All set! Running bot...\n")
bot.run(btoken)