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
runDir = os.path.dirname(__file__)
try:
    logging.debug("Attempting to read 'token.txt'")
    tokenPath = os.path.join(runDir, "token.txt")

    # Read 'token.txt'
    with open("token.txt", "r") as file:
        bToken = file.read().replace("\n", "")
        logging.info("Bot token was read from 'token.txt'")
except:
    # Input if no 'token.txt' found
    logging.warning("No 'token.txt' found! It is recommended to create this file and put your bot token in it.")
    bToken = input("TOKEN >> ")

# Word filter
if os.path.exists("filter.txt"):
    logging.info("filter.txt exists")
else:
    logging.warning("'filter.txt' doesn't exist")
    open("filter.txt","w+")
    logging.warning("filter.txt created")

# Read 'filter.txt'
wFilter = [i.replace("\n", "") for i in open("filter.txt").readlines()] 

# Shorten 'discord.Client()' to 'client'
client = discord.Client()

# Print bot information after connection
@client.event
async def on_ready():
    print("\nBot has logged in as {0.user} with id ???\n".format(client))

# Filters
@client.event
async def on_message(message):

    # Don't reply to self
    if message.author == client.user:
        return

    # Log messages from other users
    #print("new message from %s: %s" % (message.author, message.content))

    # Ping Command
    if message.content.startswith("!k ping"):
        await message.channel.send("Pong!")
        logging.debug("Bot was pinged by %s" % (message.author))

    # SETHBLING
    if message.content.__contains__("hey guys sethbling here") == True:
        await message.channel.send("%s\n\nhttps://youtu.be/NxNwtiDSWJ4" % (message.author.mention))
        logging.debug("%s mentioned Sethbling" % (message.author))

    # Word filter
    for bWords in wFilter:
        if bWords in message.content:
            await message.delete()
            await message.channel.send("%s don't use such words!" % (message.author.mention))
            print("%s said '%s'" % (message.author, message.content))

    # Testing command
    if message.content.startswith("!k test"):
        await message.channel.send("%s bleep bloop test done!" % (message.author.mention))
        print("Test successful, %s" % (message.author))

client.run(bToken)