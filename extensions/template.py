"""
This file provides a template for future commands.
This file will not be loaded as a cog or module
"""
import os

import interactions

from config import DEV_GUILD

"Highly recommended - we suggest providing proper debug logging"
from src import logutil

"Change this if you'd like - this labels log messages for debug mode"
logger = logutil.init_logger(os.path.basename(__file__))


class TemplateCog(interactions.Extension):
    @interactions.slash_command(
        "test", description="test command", scopes=[DEV_GUILD] if DEV_GUILD else None
    )
    async def test_cmd(self, ctx: interactions.SlashContext):
        """Register as an extension command"""
        await ctx.send("Test")
