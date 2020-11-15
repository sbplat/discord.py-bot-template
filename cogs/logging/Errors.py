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

from discord.ext import commands


class Errors(commands.Cog):

    """Error Handler Cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, "original", error)

        ignored_errors = (commands.MissingRequiredArgument, commands.BadArgument, commands.TooManyArguments, commands.UserInputError)

        if isinstance(error, ignored_errors):
            return

        elif isinstance(error, commands.BotMissingPermissions):
            missing_perms = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing_perms) >= 2:
                missing_permissions = f'{"**, **".join(missing_perms[:-1])}, and {missing_perms[-1]}'
            else:
                missing_permissions = " and ".join(missing_perms)
            try:
                await ctx.send(f"{ctx.author.mention}, I need the {missing_permissions} permission(s) to execute that command.")
            except discord.errors.Forbidden:
                   await ctx.author.send(f"I dont have permissions to send messages there and I need the {missing_permissions} permission(s) to execute that command.")

def setup(bot):
    bot.add_cog(Errors(bot))
