from discord.ext import commands
import discord
from datetime import datetime as d


# New - The Cog class must extend the commands.Cog class
class Roles(commands.Cog):

    roles1 = discord.Embed(title="Designated Roles for Event")

    def __init__(self, bot):
        self.bot = bot

    # Define a new command
    @commands.command()
    async def newRole(self, name, *,message):
        global roles1
        roles1.add_field(name=name, value=message )
    @commands.command()
    async def show(self,ctx):
        await ctx.send(embed=roles1)


def setup(bot):
    bot.add_cog(Roles(bot))