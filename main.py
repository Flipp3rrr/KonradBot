# Import modules
import discord
from discord.ext import commands
import os
import random
import time

# Set up logging
import logging

# Output log to 'bot.log'
if os.path.exists("bot.log"):
    os.remove("bot.log")
    print("bot.log removed, waiting .1 second")
    time.sleep(.1)

open("bot.log","w+")
print("bot.log created")
logging.basicConfig(filename='bot.log', filemode='w', level=logging.WARNING)

print("Started logging")

logging.info("Succesfully loaded modules")

# Get bot token
run_dir = os.path.dirname(__file__)
try:
    logging.debug("Attempting to read 'token.txt'")
    token_path = os.path.join(run_dir, "token.txt")

    # Read 'token.txt'
    with open("token.txt", "r") as file:
        bot_token = file.read().replace("\n", "")
        logging.info("Bot token was read from 'token.txt'")
except:
    # Input if no 'token.txt' found
    logging.warning("No 'token.txt' found! It is recommended to create this file and put your bot token in it.")
    bot_token = input("TOKEN >> ")

# Word filter
if os.path.exists("filter.txt"):
    logging.info("'filter.txt' exists")
else:
    logging.warning("'filter.txt' doesn't exist")
    open("filter.txt","w+")
    logging.warning("'filter.txt' created")

if os.path.exists("infractions.txt"):
    logging.info("'infractions.txt' exists")
else:
    logging.warning("'infractions.txt' doesn't exist")
    open("infractions.txt", "w+")
    logging.warning("'infractions.txt' created")

# Read 'filter.txt'
word_filter = [i.replace("\n", "") for i in open("filter.txt").readlines()] 

# Shorten a lot to just 'bot'
prefix = "!k"
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=prefix, intents=intents)

# Print bot information after connection
@bot.event
async def on_ready():
    print("\nBot has logged in as {user} with id {id}\n".format(user = bot.user.name, id = bot.user.id))

# Commands and filters
@bot.event
async def on_message(message):

    # Don't reply to self
    if message.author == bot.user.name:
        return

    # SETHBLING
    if message.content.__contains__("hey guys sethbling here") == True:
        await message.channel.send("%s\n\nhttps://youtu.be/NxNwtiDSWJ4" % (message.author.mention))
        logging.debug("%s mentioned Sethbling" % (message.author))

    # Word filter
    for bad_words in word_filter:
        if bad_words in message.content:
            await message.delete()
            await message.channel.send("%s don't use such words!" % (message.author.mention))
            print("%s in %s: %s" % (message.author, message.channel, message.content))
            logging.debug("%s in %s: %s" % (message.author, message.channel, message.content))
            with open("infractions.txt", "a") as infractionsLog:
                infractionsLog.write("%s in %s: %s\n" % (message.author, message.channel, message.content))

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await message.channel.send("Pong!")
    logging.debug("Bot was pinged by %s" % (message.author))

bot.run(bot_token)