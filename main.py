# Import modules
import discord
from discord.ext import commands
import os
import random

# Set up logging
import logging
logging.basicConfig(level=logging.WARNING)

# Output log to 'discord.log'
logger = logging.getLogger("discord")
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

logging.info("Succesfully loaded modules")

# Get bot token
runDir = os.path.dirname(__file__)
try:
    logging.debug("Attempting to read 'token.txt'")
    tokenPath = os.path.join(runDir, "token.txt")

    # Read 'token.txt'
    with open("token.txt", "r") as file:
        btoken = file.read().replace("\n", "")
        logging.info("Bot token was read from 'token.txt'")
except:
    # Input if no 'token.txt' found
    logging.warning("No 'token.txt' found! It is recommended to create this file and put your bot token in it.")
    btoken = input("TOKEN >> ")

client = discord.Client()

# Print bot information after connection
@client.event
async def on_ready():
    print("\nBot has logged in as {0.user} with id ???\n".format(client))

# Regular commands
@client.event
async def on_message(message):

    # Don't reply to self
    if message.author == client.user:
        return

    # Ping Command
    if message.content.startswith("!k ping"):
        await message.channel.send("Pong!")
        logging.debug("Bot was pinged by ", message.author)

client.run(btoken)