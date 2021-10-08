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


class General(commands.Cog):

    """General Commands Cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Ping")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ping(self, ctx):
        """Get the bots connection latency from Discord."""

        embed = discord.Embed(
            title="Pong!",
            description=f"Connection Speed:\n__**{round(self.bot.latency * 1000)}ms**__",
            color=discord.Color.dark_blue(),
        )  # Creates the embed
        await ctx.send(embed=embed)

    @commands.command(aliases=["echo"], brief="Echo")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def say(self, ctx, *, message):
        """Echoes the message you say."""

        try:
            await ctx.message.delete()  # Deletes the message
        except discord.HTTPException:
            pass

        message = (
            message.replace("@", "\u200B@\u200B")
            .replace("&", "\u200B&\u200B")
            .replace("# ", "\u200B# \u200B")
        )
        # You can also use commands.clean_text to clean the message

        await ctx.send(f"{ctx.author.mention}: {message}")

    @commands.command(aliases=["av"], brief="Avatar")
    @commands.guild_only()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def avatar(self, ctx, member: discord.Member = None):
        """Get a users avatar image."""

        member = (
            member or ctx.author
        )  # If user is not specified then the user is the person who invoked the command

        avatar = member.avatar_url_as(static_format="png")  # Gets the avatar url

        embed = discord.Embed(title=str(member))  # Creates the embed
        embed.set_image(url=avatar)  # Puts the avatar in the embed
        await ctx.send(embed=embed)

    @commands.command(aliases=["id"], brief="ID")
    @commands.guild_only()
    @commands.cooldown(2, 2, commands.BucketType.user)
    async def userid(self, ctx, member: discord.Member = None):
        """Get a members Discord id."""

        member = member or ctx.author

        embed = discord.Embed(
            title=f"{member.display_name}'s ID:",
            description=f"{member.id}",
            color=0x0EC2E1,
        )  # You can also use discord colours
        await ctx.send(embed=embed)

    @commands.command(aliases=["github", "code", "sourcecode"], brief="Source Code")
    @commands.guild_only()
    async def source(self, ctx):
        """View my source code!"""

        await ctx.send(
            f"{ctx.author.mention}, **{self.bot.user.mention}** is powered by "
            "the **discord.py-bot-template**, which is open source on GitHub. "
            "https://github.com/sbplat/discord.py-bot-template/"
        )

    @commands.command(aliases=["join", "inv", "i"], brief="Invite Me")
    @commands.guild_only()
    @commands.cooldown(2, 2, commands.BucketType.user)
    async def invite(self, ctx):
        """Invite me to another server!"""

        link = "https://discord.com/oauth2/authorize?client_id="
        embed = discord.Embed(
            title="Invite",
            description="Want me in your own server? "
            f"Click [here]({link}{self.bot.user.id}&scope=bot) "
            "to add it to your own server!\n\n"
            "Also, don't forget to invite Corded Bot - an awesome multipurpose bot!\n\n"
            f"Click [here]({link}736922979815915631&scope=bot&permissions=2146958847) "
            "to add it to your own server!\n\n"
            "This bot is open source on GitHub. View it on Github with this link! "
            "https://github.com/sbplat/discord.py-bot-template",
            color=0x20D2DF,
        )
        embed.set_author(
            name=f"{self.bot.user.name}", icon_url=f"{self.bot.user.avatar_url}"
        )
        embed.set_thumbnail(url=f"{self.bot.user.avatar_url}")
        embed.set_footer(text=f"{self.bot.user}")
        await ctx.send(content=f"{ctx.author.mention}", embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
