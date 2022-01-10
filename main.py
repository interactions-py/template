"""
Main script to run

This script initializes cogs and starts the bot

Code taken from my contributions in:
https://github.com/savioxavier/repo-finder-bot/
Additional thanks to savioxavier
"""
import os
import sys
import logging

import interactions
from dotenv import load_dotenv

from src import logutil
from config import DEBUG, DEBUG_DISCORD

load_dotenv()

# Configure logging for this main.py handler
logger = logutil.init_logger("main.py")

# Configure logging for Discord.py (continued in on_ready)
# TODO: overwrite formatter, suppress warnings about missing attributes

logger.warning("Debug mode is %s; Discord debug is %s. This is not a warning, \
just an indicator. You may safely ignore", DEBUG, DEBUG_DISCORD)

# Instantiate environment variables
try:
    DEV_GUILD = int(os.environ.get("DEV_GUILD"))
    TOKEN = os.environ.get("TOKEN")
except TypeError:
    DEV_GUILD = None
finally:
    if TOKEN is None:
        logger.critical("TOKEN variable not set. Cannot continue")
        sys.exit(1)

# Define the client
bot = interactions.Client(token=TOKEN)


# BEGIN on_ready
@bot.event
async def on_ready():
    "Called when bot is ready to receive interactions"

    # globalize this so the user may be able to use it later on
    global bot_user
    bot_user = interactions.User(**await bot.http.get_self())

    logger.info(
        "Logged in as %s#%s" %
        (bot_user.username, bot_user.discriminator)
    )

    # Overwrite formatter for interactions loggers
    for k, v in logging.Logger.manager.loggerDict.items():
        if k in [
            "mixin",
            "dispatch",
            "http",
            "gateway",
            "client",
            "context"
        ]:
            for h in v.handlers:
                h.setFormatter(logutil.CustomFormatter)
# END on_ready


# BEGIN command_help
@bot.command(
    name="help",
    description="Display help information for this bot",
    scope=DEV_GUILD
)
async def command_help(ctx):
    "Help command"
    logger.debug("%s#%s - initiated help command",
                 ctx.author.user.username,
                 ctx.author.user.discriminator)

    help_embed = interactions.Embed(
        title="Help",
        description="Fill me in with a list of commands!",
        thumbnail=interactions.EmbedImageStruct(
            url=bot_user.avatar
        )._json,
        fields=[
            interactions.EmbedField(
                name="help",
                value="Display help command"
            ),
            interactions.EmbedField(
                name="foo",
                value="Example command"
            ),
            interactions.EmbedField(
                name="bar",
                value="Example command"
            )
        ],
        footer=interactions.EmbedFooter(text="Boilerplate Bot")._json,
    )

    await ctx.send(embeds=help_embed)
# END command_help


# BEGIN on_command_error
@bot.event
async def on_command_error(ctx, error):
    "Gets called when a command fails"
    logger.warning(
        "A discord.py command error occured:\n%s",
        error
    )
    await ctx.send(
        f"A discord.py command error occured:\n```\n{error}```",
        ephemeral=True
    )
# END on_command_error

# BEGIN cogs_dynamic_loader
# TODO: write a dynamic modular commands system
# END cogs_dynamic_loader

bot.start()
