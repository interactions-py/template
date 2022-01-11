"""
This file provides a template for future commands.
This file will not be loaded as a cog or module
"""

import os
import interactions

# Highly recommended - we suggest providing proper debug logging
from src import logutil

# Change this if you'd like - this labels log messages for debug mode
logger = logutil.init_logger(os.path.basename(__file__))

# Use the DEV_GUILD environment variable to instantly
# load slash commands in your testing guild.
# Global slash commands are usually cached for an hour
# due to Discord API restrictions.
DEV_GUILD = int(os.environ.get("DEV_GUILD")) or None


# Create a data struct to store the current interactions.Client
# instance. Don't remove this
# class BotObject:
#     def __init__(self, bot: interactions.Client) -> None:
#         self.bot = bot


# Rename this class to whatever you'd like.
#
# Your main class command that encompasses the command functions
# should end with a "CMD" (case insensitive).
# If not, your cog will not be loaded.
# This main class also gets the context passed when the command
# is triggered.
class CommandCMD():
    "Main class for bot"
    def __init__(self, client):
        # BEGIN cmd_config
        # What will your command respond to?
        self.NAME = "helloworld"

        # What does your command do?
        self.DESCRIPTION = "A simple hello world command"

        # Write your options code here
        # (not required. Can be empty)
        self.OPTIONS = [
            interactions.Option(
                name='message',
                description='The message to echo',
                type=interactions.OptionType.STRING,
                required=False
            )
        ]

        # What type of command is it?
        # (default: CHAT_INPUT)
        self.TYPE = interactions.ApplicationCommandType.CHAT_INPUT
        # END cmd_config
        logger.info("%s command module registered" %
                    __class__.__name__)

    # Pass all arguments as "args" and default to NoneType
    async def command(ctx):
        """
        Your command code goes here
        """
        await ctx.send("Hello!")

# You can have multiple classes for each command
# Just define another ClassCMD() below
