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


class Prefix(commands.Cog):

    """Prefix Commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, brief="Prefix Options")
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def prefix(self, ctx):
        """Prefix Commands group."""

        prefixes = read_json("prefixes")
        try:
            prefix = prefixes[str(ctx.guild.id)]
        except KeyError:
            prefix = "-"

        embed = discord.Embed(
            title="Prefix Commands",
            description=f"My prefix for this server is `{prefix}`. "
            "I will also respond if you mention me.",
            color=0x0DD9FD,
        )
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(
            name="Changing your servers prefix",
            value="To change your servers prefix, "
            f"run `{prefix}prefix change <newprefix>` "
            "(If it contains a space, you need to surround it with quotations)",
            inline=False,
        )
        embed.add_field(
            name="Resetting your servers prefix",
            value=f"To reset your servers prefix, "
            f"run `{prefix}prefix reset` and your prefix will be changed back to `-`.",
            inline=False,
        )
        await ctx.send(embed=embed)

    @prefix.command(aliases=["change", "new", "swap", "switch"], brief="Change prefix")
    @commands.guild_only()
    @commands.has_permissions(manage_guild=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def changeprefix(self, ctx, prefix):
        """Change my prefix for this server."""

        if len(prefix) > 6:
            return await ctx.send(
                "The prefix must be less than 6 characters in length."
            )

        prefixes = read_json("prefixes")
        prefixes[str(ctx.guild.id)] = prefix
        write_json(prefixes, "prefixes")

        await ctx.send(f"Prefix changed to: {prefix}")

    @prefix.command(aliases=["delete", "reset", "remove"], brief="Reset Prefix")
    @commands.guild_only()
    @commands.has_permissions(manage_guild=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def deleteprefix(self, ctx):
        """Reset my prefix for this server."""

        prefixes = read_json("prefixes")

        try:
            prefixes.pop(str(ctx.guild.id))
        except KeyError:
            return await ctx.send("This servers prefix is already `-`.")

        write_json(prefixes, "prefixes")

        await ctx.send(
            "Reverted this servers prefix back to `-`. "
            "If you ever want to change it, run `-prefix change <newprefix>`"
        )


def setup(bot):
    bot.add_cog(Prefix(bot))
