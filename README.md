# boilerplate
<h3 align=center>Python boilerplate template for the interactions.py Discord API wrapper</h3>
<hr>

<table>
    <tr>
    <td>
        <b>Version 5.0.0 has released!</b> With this release, the library has been completely rewritten from the ground up. The new version is now a lot more stable and has a lot more features. Please check out the <a href="https://interactions-py.github.io/interactions.py/Guides/98%20Migration%20from%204.X/">migration guide</a> to learn how to migrate your bot from v4 to v5.
    </td>
    </tr>
    <tr>
    <td>
        All version branches in this repo are considered in-development
    </td>
    </tr>
    <tr><td>
        Status: <code>production-ready</code>
    </td></tr>
</table>

# Overview
*Native cog support is now here with v4.1.0!*
> `main.py:`
- A custom, dynamic cog loader is present. Write a cog following the `template.py` in `/cogs/`, place it in the `/cogs/` directory, and it will automatically be loaded when the bot boots.
- Utilizes the logging library and implements an easy to use custom logger and formatter. All you need to do is call `initLogger("script_name")` in a module, and log configuration is taken care of for you.
- Alongside the custom logging utility, exception handling is present and proper debug levels exist. You can configure the level to your liking in `config.py`.

> `src/logutil.py:`
- Functions here exist to aid the user in simplifying `logging` configuration. Here, all log messages go to standard output.
- A custom formatter also applies based on what level logging you desire, whereas DEBUG produces verbose output and is tailored to aid in debugging, showing which module the message is originating from and, in most cases, which line number. Loggging levels are categorized by color.

> `cogs/template.py:`
- This example cog is documented extensively. Please be sure to read over it. This cog will *not* be loaded on boot, so please refrain from writing your code in it.

> `config.py:`
- This module houses the basic DEBUG log configuration

# Installation
> 1. Clone this repository. To switch to a different version, `cd` into this cloned repository and run `git checkout [branch name/version here]`
> 2. It's generally advised to work in a Python virtual environment. Here are steps to create one *(the `discord-py-interactions` library requires Python 3.10.0 or later)*:
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
> 5. Run `pip install -r requirements.txt` to install packages. You'll need Python 3.8.6 or later
> 6. Once that's done, run the bot by executing `python3 main.py` in the terminal
>
> <hr />
> 
> *If you aren't sure how to obtain your server ID, check out [this article](https://www.alphr.com/discord-find-server-id/)*
> 
> *If you get errors related to missing token environment variables, run `source .env`*

