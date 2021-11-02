from .Cogs.onCommandError import OnCommandErrorCog
from .Cogs.help import HelpCog
from .Cogs.ping import PingCog
from .Cogs.settings import SettingsCog
import discord
from discord.ext import commands
import json

# Get configuration.json
with open("./app/discord_app/configuration.json", "r") as config:
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]
    owner_id = data["owner_id"]


# Intents
intents = discord.Intents.default()
# The bot
bot = commands.Bot(prefix, intents=intents, owner_id=owner_id)

# Load cogs
bot.remove_command("help")
bot.add_cog(HelpCog(bot))
bot.add_cog(OnCommandErrorCog(bot))
bot.add_cog(PingCog(bot))
bot.add_cog(SettingsCog(bot))


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    print(discord.__version__)
    print(bot.cogs)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{bot.command_prefix}help"))

bot.run(token)
