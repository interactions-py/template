"""
This file provides a template for future commands. This file will not be loaded as a cog or module
"""

import os

from discord.ext import commands
# You will need to import cog_ext from discord_slash in order to use slash commands
from discord_slash import cog_ext

# Import required Discord libraries
# Highly recommended - we suggest providing proper debug logging
from src import logutil # pylint: disable=import-error
Cog = commands.Cog

# Change this - this labels log messages for debug mode
logger = logutil.init_logger("template.py")

# Use the DEV_GUILD environment variable to instantly load slash commands in your testing guild
# Global slash commands are usually cached for an hour due to Discord API restrictions.
DEV_GUILD = int(os.environ.get("DEV_GUILD"))


# Rename this class to whatever you'd like. Rename it again below at setup()
class Command(commands.Cog):
    "Main class for bot"
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):  # code to execute when cog has been loaded
        "Called when cog is initialized"
        logger.info("Command slash cog registered")

    # Pass all arguments as "args" and default to NoneType
    async def command(self, ctx, *, args: str = None):
        """
        Your command code goes here
        """

    # These two functions exist so that your command will respond both to the bot prefix
    # and slash commands.
    # --
    # Set this to a command name. This will be called with your server's prefix (eg. rf.command)
    @commands.command(name="command")
    async def _reg_prefixed(self, ctx):
        "This function registers your command as a normal bot command"
        # If your function name is different, change it here
        await self.command(ctx,)

    # Set this to your command name (eg: /command) and add a meaningful description.
    # Don't forget to specify a value of [DEV_GUILD] to the guild_ids argument or
    # your slash commands won't instantly load!
    @cog_ext.cog_slash(name="command",
                       description="Some description for the command",
                       guild_ids=[DEV_GUILD])
    async def _slash_prefixed(self, ctx,):
        "This function registers your command as a slash command"
        # If your function name is different, change it here
        await self.command(ctx,)


def setup(bot):
    "Called when cog is initializing"
    # Required for cog to register
    bot.add_cog(Command(bot))  # Don't forget to rename the class here!
