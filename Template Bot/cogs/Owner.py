# MIT License

# Copyright (c) 2020 sbplat

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import discord

from discord.ext import commands

from utils.json_loader import read_json, write_json


class Owner(commands.Cog):

    """Owner Commands Cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["bl"], brief="Blacklist")
    @commands.is_owner()
    async def blacklist(self, ctx, user: discord.User):
        """Blacklist someone from using me."""

        if (
            ctx.message.author.id == user.id
        ):  # Checks if the user is the person who invoked the command
            return await ctx.send("You can't blacklist yourself.")

        self.bot.blacklisted.append(user.id)  # Adds the blacklist to the bot list
        data = read_json("blacklist")  # Reads the json file information

        if str(user.id) in data["blacklisted"]:  # Check if they are already blacklisted
            return await ctx.send("They are already blacklisted from me.")

        data["blacklisted"].append(
            user.id
        )  # Adds the blacklist to the json list for the future
        write_json(data, "blacklist")  # Saves the json list

        await ctx.send(f"{user.name} is now blacklisted from me.")  # Sends the message

    @commands.command(aliases=["ubl"], brief="Unblacklist")
    @commands.is_owner()
    async def unblacklist(self, ctx, user: discord.User):
        """Unblacklist someone from using me."""

        self.bot.blacklisted.remove(user.id)  # Removes the blacklist from the bot list
        data = read_json("blacklist")  # Reads the json file information

        try:
            data["blacklisted"].remove(user.id)
        except ValueError:  # If they are not blacklisted then it raises an error
            return await ctx.send(
                "They are not blacklisted from me. You cant unblacklist "
                "someone that's currently not already blacklisted."
            )
        write_json(data, "blacklist")  # Saves the json list

        await ctx.send(
            f"{user.name} is no longer blacklisted from me."
        )  # Sends the message

    @commands.command(aliases=["disconnect", "close", "shutdown"], brief="Logout")
    @commands.is_owner()
    async def logout(self, ctx):
        """Log me out of Discord."""

        await ctx.send(
            f"{ctx.author.mention}, I am logging out now. Run the "
            "`main.py` file to turn me back on!"
        )  # Sends the message
        await self.bot.logout()  # Logs out


def setup(bot):
    bot.add_cog(Owner(bot))
