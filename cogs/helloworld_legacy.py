"""
Example cog for real world use

This is safe to delete
"""
import os

import interactions
from interactions import (
    ActionRow,
    Button,
    ButtonStyle,
    Option,
    OptionType,
    SelectMenu,
    SelectOption,
)

from config import DEV_GUILD
from src import logutil

# Handle user permissions
from src.permissions import Permissions, has_permission

logger = logutil.init_logger(os.path.basename(__file__))


class HelloWorldOld(interactions.Extension):
    def __init__(self, client: interactions.Client):
        self.client: interactions.Client = client
        logger.info(f"{__class__.__name__} cog registered")

    # These are callback responders for the components below
    @interactions.extension_component("primary_button")
    async def _button_response(self, ctx: interactions.ComponentContext):
        """Registers to the primary button"""
        await ctx.send("You pressed a button!", ephemeral=True)

    @interactions.extension_component("select_menu")
    async def _selectmenu_respone(
        self, ctx: interactions.ComponentContext, options: list
    ):
        """Registers to the select menu"""
        await ctx.send(f"You picked: {options[0]}", ephemeral=True)

    # Now the actual commands
    @interactions.extension_command(
        name="helloworld",
        description="The simplest of commands",
        scope=DEV_GUILD,
        options=[
            Option(
                type=OptionType.STRING,
                name="message",
                description="Message to echo",
                required=False,
            )
        ],
    )
    async def helloworld(self, ctx: interactions.CommandContext, message: str = None):
        """A simple hello world command that presents a message option and echoes it back as a reply"""
        await ctx.send("Hello world!\n```\n{}\n```".format(message))

    @interactions.extension_command(
        name="helloadmin", description="Only admins can execute this", scope=DEV_GUILD
    )
    async def helloadmin(self, ctx: interactions.CommandContext):
        """A command that checks for admin perms before it continues"""
        if not has_permission(int(ctx.author.permissions), Permissions.ADMINISTRATOR):
            await ctx.send(content="Not an admin, sorry", ephemeral=True)
        else:
            await ctx.send(content="Hello, admin!", ephemeral=True)

    @interactions.extension_command(
        name="hellocomponents",
        description="A demo of components",
        scope=DEV_GUILD,
        options=[
            Option(
                type=OptionType.SUB_COMMAND,
                name="buttons",
                description="Buttons!",
                options=[
                    Option(
                        type=OptionType.STRING,
                        name="option",
                        description="Test",
                        required=False,
                    )
                ],
            ),
            Option(
                type=OptionType.SUB_COMMAND,
                name="selectmenu",
                description="Select menu!",
                options=[
                    Option(
                        type=OptionType.STRING,
                        name="option",
                        description="I do nothing. I just fix a bug",
                        required=False,
                    )
                ],
            ),
        ],
    )
    async def hellocomponents(
        self, ctx: interactions.CommandContext, sub_command: str = None
    ):
        """Demo components and sub commands"""
        _component_btn = [
            ActionRow(
                components=[
                    Button(
                        style=ButtonStyle.PRIMARY,
                        label="Primary",
                        custom_id="primary_button",
                    ),
                    Button(
                        style=ButtonStyle.LINK,
                        label="Something",
                        url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                    ),
                ]
            )
        ]
        _component_selectmenu = SelectMenu(
            options=[
                SelectOption(
                    label="1. Whoa",
                    value="choice_1",
                    description="A cool option",
                ),
                SelectOption(
                    label="2. Wow", value="choice_2", description="A new cool option"
                ),
            ],
            placeholder="Very cool things",
            custom_id="select_menu",
        )
        if sub_command == "buttons":
            await ctx.send("Here are some buttons!", components=_component_btn)
        else:
            await ctx.send("Here is a select menu!", components=_component_selectmenu)


def setup(client: interactions.Client):
    """Skip loading this
    HelloWorldOld(client)
    """
    pass
