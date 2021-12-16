"""
Main script to run

This script initializes cogs and starts the bot

Code taken from my contributions in:
https://github.com/savioxavier/repo-finder-bot/
Additional thanks to savioxavier
"""
import os
import sys

import discord
from discord.ext import commands
from discord.ext.commands.errors import ExtensionFailed, NoEntryPointError
from discord_slash import SlashCommand
from dotenv import load_dotenv

from src import logutil
from config import DEBUG, DEBUG_DISCORD
from config import PREFIX as bot_prefix

load_dotenv()

# Configure logging for this main.py handler
logger = logutil.init_logger("main.py")

# Configure logging for Discord.py
if DEBUG:
    logging = logutil.get_logger("discord")

logger.warning("Debug mode is %s; Discord debug is %s", DEBUG, DEBUG_DISCORD)

# Instantiate environment variables
DEV_GUILD = [int(os.environ.get("DEV_GUILD"))]
TOKEN = os.environ.get("TOKEN")

intents = discord.Intents.default()
intents.members = True  # pylint: disable=assigning-non-slot # noqa

# Define the client
client = commands.Bot(command_prefix=bot_prefix,
                      case_insensitive=True,
                      intents=intents,
                      help_command=None,
                      )

# Define the slash command handler
slash = SlashCommand(client,
                     sync_commands=True,
                     sync_on_cog_reload=True,)


# BEGIN on_ready
async def on_ready():
    "Called when bot is ready to receive interactions"
    logger.info(
        "Logged in as %s#%s",
        client.user.name,
        client.user.discriminator
    )
# END on_ready

# BEGIN command_help
async def command_help(ctx):
    "Help command"
    logger.debug("%s - initiated help command",
                 ctx.message.author)

    try:
        _created_at = ctx.message.created_at
    except AttributeError:
        _created_at = ctx.created_at

    help_embed = discord.Embed(
        title="Help",
        description="Fill me in!",
        timestamp=_created_at
    )

    help_embed.set_thumbnail(url=client.user.avatar_url)
    help_embed.set_footer(text="Boilerplate Bot")

    await ctx.send(embed=help_embed)
# END command_help

# BEGIN on_command_error
async def on_command_error(ctx: commands.Context, error):
    "Gets called when a command fails"
    if isinstance(error, commands.CommandOnCooldown):
        # handle cooldown
        logger.debug(
            "%s - initiated a command on cooldown [!]"
        )
        await ctx.send(
            f"This command is on cooldown. Try again after `{round(error.retry_after)}` seconds.",
            delete_after=5
        )
    else:
        # handle anything else
        logger.warning(
            "A discord.py command error occured:\n%s",
            error
        )
        await ctx.send(
            f"A discord.py command error occured:\n{error}",
            delete_after=10
        )
# END on_command_error

# BEGIN cogs_dynamic_loader

# Fill this array with Python files in /cogs
# This omits __init__.py, template.py, and excludes files without a py file extension
command_modules = [
    module[:-3]
    for module in os.listdir(f"{os.path.dirname(__file__)}/cogs")
    if module not in ("__init__.py", "template.py") and module[-3:] == ".py"
]

if command_modules or command_modules == []:
    logger.info(
        "Importing %s cogs: %s",
        len(command_modules),
        ', '.join(command_modules)
    )
else:
    logger.warning("Could not import any cogs!")

for module in command_modules:
    try:
        client.load_extension("cogs." + module)
    except NoEntryPointError:
        logger.error(
            "Could not import cog %s: The cog has no setup function - NoEntryPointError",
            module
        )
        logger.debug(str(sys.exc_info()[2]))
    except ExtensionFailed:
        logger.error(
            "Could not import cog %s: The cog failed to execute",
            module
        )
        logger.debug(str(sys.exc_info()[2]))
    except Exception as e: # pylint: disable=broad-except
        logger.error(
            "Could not import cog %s:\n%s",
            module,
            e
        )

logger.info("Cog initialization complete")
logger.debug(
    "Cogs incoming:\n%s\n",
    ',\n'.join(command_modules)
)
# END cogs_dynamic_loader

client.run(TOKEN)
