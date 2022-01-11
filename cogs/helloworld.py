"""
Example cog for real world use

This is safe to delete
"""
from interactions import (
    Option,
    OptionType,
    ApplicationCommandType,
    Button,
    ButtonStyle
)
import interactions

from src import logutil

# Handle user permissions
from src.permissions import Permissions, has_permission

logger = logutil.init_logger("helloworld.py")
# DEV_GUILD = int(os.environ.get("DEV_GUILD"))


# Your main class command that encompasses the command functions
# should end with a "CMD" (case insensitive).
# If not, your cog will not be loaded.
# This main class also gets the context passed when the command
# is triggered.
class CommandModule():
    def __init__(self, bot: interactions.Client) -> None:
        self.bot = bot

    class HelloWorldCmd():
        "Main class for the bot"
        def __init__(self, *args, **kwargs):
            # BEGIN cmd_config
            # What will your command respond to?
            self.NAME = "helloworld"

            # What does your command do?
            self.DESCRIPTION = "A simple hello world command"

            # Write your options code here
            self.OPTIONS = [
                Option(
                    name='message',
                    description='The message to echo',
                    type=OptionType.STRING,
                    required=False
                )
            ]

            # What type of command is it?
            # (default: CHAT_INPUT)
            self.TYPE = ApplicationCommandType.CHAT_INPUT
            # END cmd_config
            logger.info(f"{__class__.__name__} command class registered")

        # A "command" function must exist here as well. This is what
        # gets registered to fire when a slash command triggers
        # TODO: fix passing self
        async def command(ctx, message: str = None):
            """
            Your command code goes here
            """
            logger.info("Got helloworld command")
            await ctx.send("Hello world!\n```\n%s\n```" %
                           message)

    class HelloAdminCmd():
        "Responds only to admin"
        def __init__(self, *args, **kwargs):
            self.NAME = "helloadmin"
            self.DESCRIPTION = "Say hello to an admin"
            self.OPTIONS = [
                Option(
                    name='message',
                    description="A message",
                    type=OptionType.STRING,
                    required=False
                )
            ]
            self.TYPE = ApplicationCommandType.CHAT_INPUT
            logger.info(f"{__class__.__name__} command class registered")

        async def command(ctx, message: str = None):
            logger.info("Got admin command")
            # Check if the author has admin permissions
            if not has_permission(int(ctx.author.permissions),
                                  Permissions.ADMINISTRATOR):
                await ctx.send(
                    content="Not an admin, sorry",
                    ephemeral=True
                )
                return
            await ctx.send(content="Hello world!\n```\n%s\n```" %
                           message,
                           ephemeral=True)

    class HelloButtonsCMD():
        global button
        button = Button(
            style=ButtonStyle.PRIMARY,
            label="Hello Buttons!",
            custom_id="hello"
        )

        def __init__(self, bot: interactions.Client) -> None:
            self.NAME = "hellobuttons"
            self.DESCRIPTION = "Send components"
            self.TYPE = ApplicationCommandType.CHAT_INPUT
            self.OPTIONS = None
            self.bot = bot
            logger.info(f"{__class__.__name__} command class registered")

        async def command(ctx):
            logger.info("Got a hellobuttons command")
            await ctx.send("Hello! Here are some buttons", components=button)
