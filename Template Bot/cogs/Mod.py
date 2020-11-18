# MIT License

# Copyright (c) 2020 really-noob

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


class Mod(commands.Cog):

    """Mod Commands Cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["k"], brief="Kick")
    @commands.guild_only()
    @commands.bot_has_permissions(kick_members=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member):
        """Kick someone from the server."""

        reason = " ".join(
            ctx.message.content.split()[2:]
        )  # Gets the reason if one is specified
        reason += f" Banned by {ctx.author.display_name} (ID: {ctx.author.id})"
        if len(reason) > 512:
            return await ctx.send(
                "Your reason is too long. Your reason must be "
                f"**{len(reason) - 512}** characters shorter."
            )

        if (
            ctx.author == user
        ):  # Checks if the person invoking the command is trying to kick themselves
            return await ctx.send("Why are you trying to kick yourself?")

        try:
            await ctx.guild.kick(user, reason=reason)  # Kicks the user out
            await ctx.send(f"Kicked {user.mention}!")
        except discord.errors.Forbidden:
            return await ctx.send(
                f"{ctx.author.mention}, There role is higher than mine "
                "so I cannot kick them."
            )

    @commands.command(aliases=["b"], brief="Ban")
    @commands.guild_only()
    @commands.bot_has_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member):
        """Ban someone from the server."""
        reason = " ".join(ctx.message.content.split()[2:])
        reason += f" Banned by {ctx.author.display_name} (ID: {ctx.author.id})"
        if len(reason) > 512:
            return await ctx.send(
                "Your reason is too long. Your reason must be "
                f"**{len(reason) - 512}** characters shorter."
            )

        if (
            ctx.author == user
        ):  # Checks if the person invoking the command is trying to ban themselves
            return await ctx.send("Why are you trying to ban yourself?")

        try:
            await ctx.guild.ban(user, reason=reason)  # Bans the user
            await ctx.send(f"Banned {user.mention}!")
        except discord.errors.Forbidden:
            return await ctx.send(
                "I dont have the ban members permission or their role "
                "is higher than mine."
            )


def setup(bot):
    bot.add_cog(Mod(bot))
