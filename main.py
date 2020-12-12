import discord
from discord.ext import commands
import os

runDir = os.path.dirname(__file__)
try:
    tokenPath = os.path.join(runDir, "token.txt")
    with open('token.txt', 'r') as file:
        btoken = file.read().replace('\n', '')
        print(btoken)
except:
    print("No token.txt found!")
    btoken = input("TOKEN >> ")

bot = commands.Bot(command_prefix='k! ')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
    print("Pinged!")

bot.run(btoken)