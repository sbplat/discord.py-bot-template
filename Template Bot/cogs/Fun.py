#MIT License

#Copyright (c) 2020 really-noob

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import discord
import random

from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType


class Fun(commands.Cog):

    """Fun Commands Cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['flip'], brief="Coin Flip")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def coinflip(self, ctx):
        """Flip a Coin (Coin Flip)."""
        
        responses = ["Heads", "Tails"]
        rancoin = random.choice(responses)

        embed=discord.Embed(title="Flip:", description=f"{rancoin}", color=random.randint(0x000000, 0xffffff))
        await ctx.send(embed=embed)


    @commands.command(aliases=['rev'], brief="Reverse Text")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def reverse(self, ctx, *, text: str):
        """Reverse your text completely backwards."""
        
        reversed = text[::-1]

        embed=discord.Embed(title="Reversed Message:", description=f"{reversed}", color=random.randint(0x000000, 0xffffff))
        await ctx.send(embed=embed)


    @commands.command(brief="Uppercase")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def uppercase(self, ctx, *, message: commands.clean_content):
        """Converts your message into uppercase. Every single letter regardless of its case will be converted to uppercase."""

        embed=discord.Embed(title="Uppercase:", description=f"{message.upper()}", color=random.randint(0x000000, 0xffffff))
        await ctx.send(embed=embed)


    @commands.command(brief="Lowercase")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def lowercase(self, ctx, *, message: commands.clean_content):
        """Converts your message into lowercase. Every single letter regardless of its case will be converted to lowercase."""

        embed=discord.Embed(title="Lowercase:", description=f"{message.lower()}", color=random.randint(0x000000, 0xffffff))
        await ctx.send(embed=embed)


    @commands.command(aliases=['8ball'], brief="8ball")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def eightball(self, ctx, *, question):
        """Ask the magic 8ball a question and hopefully receive an accurate answer."""

        responses = ['It is certain.',
                    'It is decidedly so.',
                    'Without a doubt.',
                    'Yes - definitely.',
                    'You may rely on it.',
                    'As I see it, yes.',
                    'Most likely.',
                    'Outlook good.',
                    'Yes.',
                    'Signs point to yes.',
                    'Reply hazy, try again.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    'Don\'t count on it.',
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Very doubtful.']

        embed = discord.Embed(description=f'{ctx.author} asked: {question}\nAnswer: {random.choice(responses)}', color=random.randint(0x000000, 0xffffff))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))
