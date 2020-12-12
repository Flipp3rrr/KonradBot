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
    print("No 'token.txt' found!")
    btoken = input("TOKEN >> ")

# Prefix
bot = commands.Bot(command_prefix="k! ")

@bot.event
async def on_ready():
    print("USERNAME: ", bot.user.name)
    print("USER ID:  ", bot.user.id, "\n")

# Member joined
try:
    @bot.command()
    async def joined(ctx, member: discord.Member):
        await ctx.send('{0.name} joined in {0.joined_at}'.format(member))
except:
    exception = sys.exc_info()[0]
    print("Exception: %s" % exception)

# Ping command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
    print("Pinged!")

# Repeat
@bot.command()
async def repeat(ctx, content="repeating..."):
    filterContent = content.replace("@", "[@]")
    await ctx.send(filterContent)
    print("Repeated >", filterContent)
    print("Original >", content)

print("All set! Running bot...\n")
bot.run(btoken)