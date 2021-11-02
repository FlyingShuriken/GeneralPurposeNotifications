import discord
from discord.ext import commands
import json

from discord.ext.commands.errors import MissingRequiredArgument


class SettingsCog(commands.Cog, name="config command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot
        with open("./app/discord_app/configuration.json", "r") as config_file:
            self.config_file = json.load(config_file)

    @commands.command(name="config", usage="", description="Config the bot.", aliases=["c", "cfg"])
    @commands.has_permissions(manage_guild=True)
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def cfg(self, ctx, class_, *args):
        for i in args:
            if "=" not in i:
                await ctx.send(f"Please add a prefix before your argument! Example: ```{ctx.message.content.split(' ')[0]} owner id=123456```")
                return
        arg = {}
        for i in args:
            arg[i.split("=")[0]] = i.split("=")[1]
        if class_ == "owner":
            if arg == {}:
                await ctx.send("Missing requirement(s): ```id```")
                return
            owner_id = arg["id"]
            self.config_file["server_owner"][str(ctx.guild.id)] = owner_id
            with open("./app/discord_app/configuration.json", "w") as config_update:
                json.dump(self.config_file, config_update, indent=4)
            await ctx.send(content=f"Successfully set the owner of this server to: ``{owner_id}``!")
        else:
            await ctx.send("Beep! Beep! Command not found!")
