import discord
import pathlib
import sys
import os

from discord.ext import commands

from utils.json_loader import read_json


TOKEN = os.getenv("TOKEN")


def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or("-")(bot, message)

    prefixes = read_json("prefixes")

    if str(message.guild.id) not in prefixes:
        return commands.when_mentioned_or("-")(bot, message)

    prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(prefix)(bot, message)

intents=discord.Intents.all()
bot = commands.Bot(
	command_prefix = get_prefix,
	case_insensitive = True,
	intents = intents,
	)

bot.blacklisted = []

@bot.event
async def on_ready():
    data = read_json("blacklist")
    bot.blacklisted = data["blacklisted"]
    print(
    	f"Bot is now online.\n"\
    	f"Logged in as {bot.user.name}\n"\
    	f"ID: {bot.user.id}\n"\
    	f"Invite Link: https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot"
    	)
    await bot.change_presence(
    	activity=discord.Game(name=f"-help | {len(bot.guilds)} servers")
    	)

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    elif message.author.id in bot.blacklisted:
        try:
            return await message.channel.send(
                f"{message.author.mention}, Go away! Your blacklisted from me."
            )
        except discord.errors.Forbidden:
            pass

    else:
        await bot.process_commands(message)

@bot.event
async def on_guild_join(guild):
    print(
    	f"I just joined a server!\n\n"\
    	f"Name: {guild.name}\n"\
    	f"ID: {guild.id}\n"\
    	f"Members: {guild.member_count}"
    	)
    await bot.change_presence(
    	activity = discord.Game(name = f"-help| {len(bot.guilds)} servers")
    	)

@bot.event
async def on_guild_remove(guild):
    await bot.change_presence(
    	activity = discord.Game(name = f"cb.help | {len(bot.guilds)} servers")
    	)
    print(
    	f"I just left a server!\n\n"\
    	f"Name: {guild.name}\n"\
    	f"ID: {guild.id}\n"
    	f"Members: {guild.member_count}"
    	)

for ext in[".".join(p.parts)[:-len(".py")] for p in pathlib.Path('cogs').glob('**/*.py')]:
    bot.load_extension(ext)

if not TOKEN:
    print("You need to change the token in the .env file.")
    sys.exit(0)

bot.run(TOKEN)
