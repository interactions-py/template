"""
Example cog for real world use

This is safe to delete
"""
import interactions


class HelloWorld(interactions.Extension):
    @interactions.slash_command("hello", description="Say hello!")
    async def hello(self, ctx: interactions.SlashContext):
        """A simple hello world command"""
        await ctx.send("Hello, world!")

    @interactions.slash_command(
        "base_command", description="A base command, to expand on"
    )
    async def base_command(self, ctx: interactions.SlashContext):
        ...

    @base_command.subcommand(
        "sub_command", sub_cmd_description="A sub command, to expand on"
    )
    async def sub_command(self, ctx: interactions.SlashContext):
        """A simple sub command"""
        await ctx.send("Hello, world! This is a sub command")

    @interactions.slash_command("options", description="A command with options")
    @interactions.slash_option(
        "option_str",
        "A string option",
        opt_type=interactions.OptionType.STRING,
        required=True,
    )
    @interactions.slash_option(
        "option_int",
        "An integer option",
        opt_type=interactions.OptionType.INTEGER,
        required=True,
    )
    @interactions.slash_option(
        "option_attachment",
        "An attachment option",
        opt_type=interactions.OptionType.ATTACHMENT,
        required=True,
    )
    async def options(
        self,
        ctx: interactions.SlashContext,
        option_str: str,
        option_int: int,
        option_attachment: interactions.Attachment,
    ):
        """A command with lots of options"""
        embed = interactions.Embed(
            "There are a lot of options here",
            description="Maybe too many",
            color=interactions.BrandColors.BLURPLE,
        )
        embed.set_image(url=option_attachment.url)
        embed.add_field(
            "String option",
            option_str,
            inline=False,
        )
        embed.add_field(
            "Integer option",
            str(option_int),
            inline=False,
        )
        await ctx.send(embed=embed)

    @interactions.slash_command("components", description="A command with components")
    async def components(self, ctx: interactions.SlashContext):
        """A command with components"""
        await ctx.send(
            "Here are some components",
            components=interactions.spread_to_rows(
                interactions.Button(
                    label="Click me!",
                    custom_id="click_me",
                    style=interactions.ButtonStyle.PRIMARY,
                ),
                interactions.StringSelectMenu(
                    "Select me!",
                    "No, select me!",
                    "Select me too!",
                    placeholder="I wonder what this does",
                    min_values=1,
                    max_values=2,
                    custom_id="select_me",
                ),
            ),
        )

    @interactions.component_callback("click_me")
    async def click_me(self, ctx: interactions.ComponentContext):
        """A callback for the click me button"""
        await ctx.send("You clicked me!")

    @interactions.component_callback("select_me")
    async def select_me(self, ctx: interactions.ComponentContext):
        """A callback for the select me menu"""
        await ctx.send(f"You selected {' '.join(ctx.values)}")
