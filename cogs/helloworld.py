"""
Example cog for real world use

This is safe to delete
"""
import os
import interactions

from interactions import (
    Option,
    OptionType,
    Button,
    ButtonStyle,
    ActionRow,
    SelectMenu,
    SelectOption
)

from config import DEV_GUILD
from src import logutil

# Handle user permissions
from src.permissions import Permissions, has_permission

logger = logutil.init_logger(os.path.basename(__file__))


class HelloWorld(interactions.Extension):
    def __init__(self, client: interactions.Client):
        self.client: interactions.Client = client
        logger.info(f"{__class__.__name__} cog registered")

    # These are callback responders for the components below
    @interactions.extension_component("primary_button")
    async def _button_response(self, ctx: interactions.ComponentContext):
        """Registers to the primary button"""
        await ctx.send("You pressed a button!", ephemeral=True)

    @interactions.extension_component("select_menu")
    async def _selectmenu_respone(self, ctx: interactions.ComponentContext, options: list):
        """Registers to the select menu"""
        await ctx.send(f"You picked: {options[0]}", ephemeral=True)

    # This is a subcommand organized version
    # To view regular structure, view helloworld_legacy.py
    @interactions.extension_command(
        name="hello",
        description="The base of all things good",
        scope=DEV_GUILD,
        options=[
            Option(
                type=OptionType.SUB_COMMAND,
                name="world",
                description="The simplest of commands",
                options=[
                    Option(
                        type=OptionType.STRING,
                        name="message",
                        description="The message to echo",
                        required=False
                    )
                ]
            ),
            Option(
                type=OptionType.SUB_COMMAND,
                name="admin",
                description="Only admins can execute this",
                options=[
                    Option(
                        type=OptionType.STRING,
                        name="message",
                        description="The message to echo",
                        required=False
                    )
                ]
            ),
            Option(
                type=OptionType.SUB_COMMAND_GROUP,
                name="components",
                description="Let's see some components",
                options=[
                    Option(
                        type=OptionType.SUB_COMMAND,
                        name="buttons",
                        description="Buttons!"
                    ),
                    Option(
                        type=OptionType.SUB_COMMAND,
                        name="select_menu",
                        description="Select menu!"
                    )
                ]
            )
        ]
    )
    async def hello_cmd(
            self,
            ctx: interactions.CommandContext,
            sub_command: str,
            sub_command_group: str = None,
            message: str = None
    ):
        if sub_command == "world":
            await ctx.send("Hello, world!\n```\n{}\n```".format(message))
        elif sub_command == "admin":
            if not has_permission(
                int(ctx.author.permissions),
                Permissions.ADMINISTRATOR
            ):
                await ctx.send(
                    content="Not an admin, sorry",
                    ephemeral=True
                )
            else:
                await ctx.send(
                    content="Hello admin! :sunglasses:\n```\n{}\n```".format(message),
                    ephemeral=True
                )
        elif sub_command_group == "components" and sub_command == "buttons":
            _component_btn = [
                ActionRow(components=[
                    Button(
                        style=ButtonStyle.PRIMARY,
                        label="Primary",
                        custom_id="primary_button"
                    ),
                    Button(
                        style=ButtonStyle.LINK,
                        label="Something",
                        url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                    )
                ])
            ]
            await ctx.send("Here are some buttons!", components=_component_btn)
        elif sub_command_group == "components" and sub_command == "select_menu":
            _component_selectmenu = SelectMenu(
                options=[
                    SelectOption(
                        label="1. Whoa",
                        value="choice_1",
                        description="A cool option",
                    ),
                    SelectOption(
                        label="2. Wow",
                        value="choice_2",
                        description="A new cool option"
                    )
                ],
                placeholder="Very cool things",
                custom_id="select_menu"
            )
            await ctx.send("Here's a select menu!", components=_component_selectmenu)


def setup(client: interactions.Client):
    HelloWorld(client)
