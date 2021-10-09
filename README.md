<h1 align="center">
  <img src="./images/Discord.py Template Bot Splash.svg" alt="Discord.py Template Bot" width="800px">
  <br>
  Discord.py Template Bot
</h1>
<h4 align="center">Make sure to join my <a href="https://discord.gg/CYcNNXP">Discord Server</a> if you need any help with this template bot!</h4>
<p align="center">
  <a href="https://discord.gg/CYcNNXP">
    <img src="https://img.shields.io/discord/757944575594725428?color=2cc3d4&label=Discord%20Support%20Server" alt="Discord Support Server">
  </a>
</p>
<p align="center">
  <a href="https://github.com/sbplat/discord.py-bot-template/blob/master/Template%20Bot/main.py">
    <img src="https://img.shields.io/badge/python-3.6|3.7|3.8|3.9-blue" alt="Python Version">
  </a>
  <a href="https://github.com/sbplat/discord.py-bot-template">
    <img src="https://img.shields.io/badge/Maintained%3F-yes-green" alt="Maintained? no">
  </a>
  <a href="https://github.com/sbplat/discord.py-bot-template/commits/master">
    <img src="https://img.shields.io/github/last-commit/sbplat/discord.py-bot-template" alt="Last GitHub Commit">
  </a>
  <a href="https://github.com/sbplat/discord.py-bot-template/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/sbplat/discord.py-bot-template" alt="GitHub LICENSE">
  </a>
</p>

# Prerequisites
 - [Python](https://www.python.org/downloads/) 3.6 or up
 - Familiar with [Python](https://www.python.org/) and some familiarity with the [discord.py](https://discordpy.readthedocs.io/en/stable/index.html) library
 - Have a [Discord](https://discord.com/) account

# Setting up the bot
1. Download this [repository](https://github.com/sbplat/discord.py-bot-template) and extract it. All the bot files are in the `Template Bot` folder.
![Download Bot](/images/Download.PNG)
2. Visit the [Discord Developer Portal here](https://discord.com/developers/applications).
3. Create a new application and give it a name (this is not the bots name).
![New Application](./images/New%20Application.png)
4. Navigate to the "Bot" tab, then click "Add Bot" and finally click "Yes, do it!" to create your bot.
![Make the Bot](./images/Make%20Bot.PNG)
5. Copy the token. Check the public bot option if you want other people to be able to invite your bot. You can also change your bot's profile picture and name here.
![Copy Bot Token](/images/Copy%20Token.PNG)

| :warning: Your bot token should be kept private at all times. You should immediately regenerate your token into a new one in the [Discord Developers page](https://discord.com/developers/applications) if you ever happen to leak it. Your bot token should be kept private at all times. |
| --- |

6. Open the `.env` file and paste the token in the token field. Make sure not to add any quotes around it.
7. Install all the dependencies required using `pip install -r requirements.txt`. If that doesn't work then run it as administrator and try again.
8. Run the `main.py` file. Congratulations, your Discord bot now online!

# FAQ and Troubleshooting
Question: How do I invite my bot to my server?
Answer: When you run your bot, an invite link will be printed in the console. That is your bots invite link.
