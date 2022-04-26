"""
Main script to run

This script initializes cogs and starts the bot

Code taken from my contributions in:
https://github.com/savioxavier/repo-finder-bot/
Additional thanks to savioxavier
"""
import os
import sys

import interactions
from dotenv import load_dotenv
from interactions import MISSING

from config import DEBUG, DEV_GUILD
from src import logutil

load_dotenv()

# Configure logging for this main.py handler
logger = logutil.init_logger("main.py")
logger.debug(
    "Debug mode is %s; This is not a warning, \
just an indicator. You may safely ignore",
    DEBUG,
)

# Instantiate environment variables
TOKEN = None
try:
    if not (TOKEN := os.environ.get("TOKEN")):
        TOKEN = None
    if not DEV_GUILD or (DEV_GUILD := int(os.environ.get("DEV_GUILD"))):
        DEV_GUILD = MISSING
except TypeError:
    pass
finally:
    if TOKEN is None:
        logger.critical("TOKEN variable not set. Cannot continue")
        sys.exit(1)

# presence is for the activity of the bot (can be watching, playing, listening, etc)
# type=interactions.PresenceActivityType is the type of presence (GAME, STREAMING, LISTENING, WATCHING, etc.)
# name="" is the custom displays next to the ActiviType text.
# status=interactions.StatusType is the status (ONLINE, DND, IDLE, etc.) 
# Set disable_sync to True when not editing your commands (name, description, options, etc.)
client = interactions.Client(
    token=TOKEN,
    presence=interactions.ClientPresence(
        activities=[
            interactions.PresenceActivity(
                type=interactions.PresenceActivityType.WATCHING,
                name="you."
            )
        ],
        status=interactions.StatusType.ONLINE
    ),
    disable_sync=False
)


# BEGIN on_ready
@client.event
async def on_ready():
    """Called when bot is ready to receive interactions"""
    logger.info("Logged in")


# BEGIN cogs_dynamic_loader
# Fill this array with Python files in /cogs.
# This omits __init__.py, template.py, and excludes files without a py file extension
cogs = [
    module[:-3]
    for module in os.listdir(f"{os.path.dirname(__file__)}/cogs")
    if module not in ("__init__.py", "template.py") and module[-3:] == ".py"
]

if cogs or cogs == []:
    logger.info("Importing %s cogs: %s", len(cogs), ", ".join(cogs))
else:
    logger.warning("Could not import any cogs!")

for cog in cogs:
    try:
        client.load("cogs." + cog)
    except Exception:  # noqa
        logger.error("Could not load a cog: {}".format(cog), exc_info=DEBUG)

# END cogs_dynamic_loader

client.start()
