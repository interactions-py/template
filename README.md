# discord-py-interactions_boilerplate
<h3 align=center>Boilerplate template for the discord-py-interactions library</h3>
<p align=center>A stripped down fork from contributions found in <a href="https://github.com/savioxavier/repo-finder-bot">savioxavier/repo-finder-bot</a></p>
<hr>

- **Currently, this boilerplate supports `discord-py-interactions==3.0.2` but will be updated for future version later on. To switch to a different version, check the branches**

![image](https://user-images.githubusercontent.com/29584664/146406854-88c2dfa8-d346-437e-a57b-1fc73be45b65.png)

# Overview
> `main.py:`
- A custom, dynamic cog loader is present. Write a cog following the `template.py` in `/cogs/`, place it in the `/cogs/` directory, and it will automatically be loaded when the bot boots.
- Utilizes the logging library and implements an easy to use custom logger and formatter. All you need to do is call `initLogger("script_name")` in a module or cog, and log configuration is taken care of for you.
- Alongside the custom logging utility, exception handling is present and proper debug levels exist. You can configure the level to your liking in `config.py`. Also, this handles command cooldown if you define it in your cogs.

> `src/logutil.py:`
- Functions here exist to aid the user in simplifying `logging` configuration. Here, all log messages go to standard output.
- A custom formatter also applies based on what level logging you desire, whereas DEBUG produces verbose output and is tailored to aid in debugging, showing which module the message is originating from and, in most cases, which line number. Loggging levels are categorized by color.

> `cogs/template.py:`
- This example cog is documented extensively. Please be sure to read over it. This cog will *not* be loaded on boot, so please refrain from writing your code in it.

> `config.py:`
- This module houses the basic configuration options for your bot, including DEBUG switches and the bot prefix.

# Installation
> 1. Clone this repository. To switch to a different version, `cd` into this cloned repository and run `git checkout -b [branch name/version here]`
> 2. Create a Discord bot token from [here](https://discord.com/developers/applications/)  
> **Register it for slash commands:**
> - Under *OAuth2 > General*, set the Authorization Method to "In-app Authorization"
> - Tick `bot` and `applications.commands`
> - Go to *OAuth2 > URL Generator*, tick `bot` and `applications.commands`. For Bot Permissions, tick:
> > - General: Read Messages/View Channels  
> > - Text Permissions: Send Messages, Manage Messages, and Embed Links
> - Copy the generated URL at the bottom of the page to invite it to desired servers
> 3. Make a new file called `.env` inside the repo folder and paste the below code block in the file
> ```
> TOKEN="[paste Discord bot token here]"
> DEV_GUILD=[paste your bot testing server ID here]
> ```
> 4. Run `pip install -r requirements.txt` to install packages. You'll need Python 3.6.8 or later
> 5. Once that's done, run the bot by executing `python3 main.py` in the terminal
>
> <hr />
> 
> *If you aren't sure how to obtain your server ID, check out [this article](https://www.alphr.com/discord-find-server-id/)*
> 
> *If you get errors related to missing token environment variables, run `source .env`*

# FAQ
## Why aren't my slash commands getting registered?
> There could be many reasons, but let's narrow it down
> - Ensure your bot token has the `applications.command` scope before you invited your bot. If not, kick the bot from your server(s), follow above directions to enable the permissions scope, and reinvite.
> - The bot uses a guild ID to register the slash commands in a single guild. This ensures it will be registered instantly. In order to use slash commands globally, remove the `guild_ids=[]` in your `@cog_ext.cog_slash` decorators. But **keep in mind this may take a few hours to register.** To refresh it instantly, simply kick the bot from your server and reinvite.

<hr />

## Why am I getting a `HTTP 403 - 50001 Missing Access`?
> Again, like above, this could be caused by many different reasons, but here are a couple things you can try
> - Follow the above steps to ensure your slash commands are registering properly (making sure `applications.command` is enabled, etc.)
> - Reinvite your bot

| **Special thanks** |
| --- |
| To [savioxavier](https://github.com/savioxavier/repo-finder-bot) for authoring the `repo-finder-bot`, allowing contributors alike to make this project happen |
