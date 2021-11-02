# import discord
from discord.ext import commands
import json


class PingCog(commands.Cog, name="config command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot
        with open("./app/discord/configuration.json", "r") as config_file:
            self.config_file = json.load(config_file)

    @commands.command(name="cfg", usage="", description="Config the bot.", aliases=["c"])
    @commands.has_permissions(manage_guild=True)
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def cfg(self, ctx, class_, *args):
        print(args)
        for i in args:
            if "=" not in i:
                await ctx.send(f"Please add a prefix before your argument! Example: ```!cfg owner id=123456```")
                return
        arg = {}
        for i in args:
            arg[i.split("=")[0]] = i.split("=")[1]
        if class_ == "owner":
            owner_id = arg["id"]
            self.config_file["server_owner"][str(ctx.guild.id)] = owner_id
            with open("./app/discord/configuration.json", "w") as config_update:
                json.dump(self.config_file, config_update, indent=4)
            await ctx.send(content=f"Successfully set the owner of this server to: ``{owner_id}``!")
        else:
            await ctx.send("Beep! Beep! Command not found!")


def setup(bot: commands.Bot):
    bot.add_cog(PingCog(bot))
