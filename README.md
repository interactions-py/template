# interactions.py-boilerplate
<h3 align=center>Python boilerplate template for the interactions.py Discord API wrapper</h3>
<p align=center>A stripped down fork from contributions found in <a href="https://github.com/savioxavier/repo-finder-bot">savioxavier/repo-finder-bot</a></p>
<hr>

<table>
    <tr>
    <td>
        <b>Currently, this branch is on 4.0.1-unstable. Be warned, some code may not work as intended and is still actively being worked on. To switch to a different version, check the branches</b>
    </td>
    </tr>
    <tr>
    <td>
        If you encounter issues, open an issue in <a href="https://github.com/V3ntus/discord-py-interactions_boilerplate/issues">this repo</a>
      or in <a href="https://github.com/goverfl0w/discord-interactions/issues">goverfl0w/discord-interactions</a>
    </td>
    </tr>
</table>

![image](https://user-images.githubusercontent.com/29584664/149206003-31a184ad-89e2-4481-978b-129cdebb892f.png)

# Overview
*As of discord-py-interactions v4.0.1, cog support is still in a planned stage and not supported. Until they are added, command modules will be in place of cogs*
> `main.py:`
- A custom, dynamic command module loader is present. Write a command module following the `template.py` in `/cogs/`, place it in the `/cogs/` directory, and it will automatically be loaded when the bot boots.
- Utilizes the logging library and implements an easy to use custom logger and formatter. All you need to do is call `initLogger("script_name")` in a module, and log configuration is taken care of for you.
- Alongside the custom logging utility, exception handling is present and proper debug levels exist. You can configure the level to your liking in `config.py`.

> `src/logutil.py:`
- Functions here exist to aid the user in simplifying `logging` configuration. Here, all log messages go to standard output.
- A custom formatter also applies based on what level logging you desire, whereas DEBUG produces verbose output and is tailored to aid in debugging, showing which module the message is originating from and, in most cases, which line number. Loggging levels are categorized by color.

> `cogs/template.py:`
- This example command module is documented extensively. Please be sure to read over it. This command module will *not* be loaded on boot, so please refrain from writing your code in it.

> `config.py:`
- This module houses the basic DEBUG log configuration

# Installation
> 1. Clone this repository. To switch to a different version, `cd` into this cloned repository and run `git checkout -b [branch name/version here]`
> 2. It's generally advised to work in a Python virtual environment. Here are steps to create one *(the `discord-py-interactions` library requires python3.6 or later)*:
> > - `$` `python3 -m venv env`
> > - `$` `source env/bin/activate`
> 3. Create a Discord bot token from [here](https://discord.com/developers/applications/)  
> **Register it for slash commands:**
> - Under *OAuth2 > General*, set the Authorization Method to "In-app Authorization"
> - Tick `bot` and `applications.commands`
> - Go to *OAuth2 > URL Generator*, tick `bot` and `applications.commands`
> - Copy the generated URL at the bottom of the page to invite it to desired servers
> 4. Make a new file called `.env` inside the repo folder and paste the below code block in the file
> ```
> TOKEN="[paste Discord bot token here]"
> DEV_GUILD=[paste your bot testing server ID here]
> ```
> 5. Run `pip install -r requirements.txt` to install packages. You'll need Python 3.6.8 or later
> 6. Once that's done, run the bot by executing `python3 main.py` in the terminal
>
> <hr />
> 
> *If you aren't sure how to obtain your server ID, check out [this article](https://www.alphr.com/discord-find-server-id/)*
> 
> *If you get errors related to missing token environment variables, run `source .env`*

# FAQ
## What happened to message commands?
> As of discord-py-interactions v4, they have been removed. However, it is still possible to code them in, I have not included that option yet

## Why aren't my slash commands getting registered?
> There could be many reasons, but let's narrow it down
> - Ensure your bot token has the `applications.command` scope before you invited your bot. If not, kick the bot from your server(s), follow above directions to enable the permissions scope, and reinvite.
> - The bot uses a guild ID to register the slash commands in a single guild. This ensures it will be registered instantly. In order to use slash commands globally, set the `DEV_GUILD` in your `.env` to an empty string. But **keep in mind this may take a few hours to register.** To refresh it instantly, simply kick the bot from your server and reinvite.

<hr />

## Why am I getting a `HTTP 403 - 50001 Missing Access`?
> Again, like above, this could be caused by many different reasons, but here are a couple things you can try
> - Follow the above steps to ensure your slash commands are registering properly (making sure `applications.command` is enabled, etc.)
> - Reinvite your bot

| **Special thanks** |
| --- |
| To [savioxavier](https://github.com/savioxavier/repo-finder-bot) for authoring the `repo-finder-bot`, allowing contributors alike to make this project happen |

[![wakatime](https://wakatime.com/badge/github/V3ntus/discord-py-interactions_boilerplate.svg)](https://wakatime.com/badge/github/V3ntus/discord-py-interactions_boilerplate)
