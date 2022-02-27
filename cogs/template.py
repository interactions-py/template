"""
This file provides a template for future commands.
This file will not be loaded as a cog or module
"""
import os

import interactions

from config import DEV_GUILD

"Highly recommended - we suggest providing proper debug logging"
from src import logutil

"Uncomment if you want to check if a user has permissions"
# from src.permissions import Permissions, has_permission

"Change this if you'd like - this labels log messages for debug mode"
logger = logutil.init_logger(os.path.basename(__file__))


class TemplateCog(interactions.Extension):
    def __init__(self, client: interactions.Client):
        """Initializes the client instance so we can interact with it"""
        self.client: interactions.Client = client
        logger.info(f"{__class__.__name__} cog registered")

    @interactions.extension_command(
        name="test", description="test command", scope=DEV_GUILD
    )
    async def test_cmd(self, ctx: interactions.CommandContext):
        """Register as an extension command"""
        await ctx.send("Test")


def setup(client: interactions.Client):
    """Crucial setup script to register this cog"""
    TemplateCog(client)
