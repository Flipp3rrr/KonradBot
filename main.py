import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='k! ')
btoken = input("TOKEN>> ")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(btoken)