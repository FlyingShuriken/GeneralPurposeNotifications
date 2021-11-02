import discord
from discord.ext import commands
import json
import os

# Get configuration.json
with open("./app/discord/configuration.json", "r") as config:
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]
    owner_id = data["owner_id"]


# Intents
intents = discord.Intents.default()
# The bot
bot = commands.Bot(prefix, intents=intents, owner_id=owner_id)

# Load cogs
if __name__ == '__main__':
    for filename in os.listdir("./app/discord/Cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"Cogs.{filename[:-3]}")


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    print(discord.__version__)
    print(bot.cogs)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{bot.command_prefix}help"))

bot.run(token)
