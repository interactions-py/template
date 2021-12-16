"""
Example cog for real world use

This is safe to delete
"""

import os

from discord.ext import commands
from discord_slash import cog_ext

from src import logutil # pylint: disable=import-error
Cog = commands.Cog

logger = logutil.init_logger("helloworld.py")

DEV_GUILD = int(os.environ.get("DEV_GUILD"))


class HelloWorld(commands.Cog):
    "Main class for the bot"
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        "Called when cog is loaded"
        logger.info("HelloWorld slash cog registered")

    async def command(self, ctx):
        """
        Your command code goes here
        """
        await ctx.send("Hello world!")

    @commands.command(name="helloworld")
    async def _reg_prefixed(self, ctx):
        "This function registers your command as a normal bot command"
        await self.command(ctx,)

    @cog_ext.cog_slash(name="helloworld",
                       description="Hello world!",
                       guild_ids=[DEV_GUILD])
    async def _slash_prefixed(self, ctx,):
        "This function registers your command as a slash command"
        await self.command(ctx,)


def setup(bot):
    "Called when this cog initializes"
    bot.add_cog(HelloWorld(bot))
