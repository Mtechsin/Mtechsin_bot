import discord
from discord.ext import commands
import aiml
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")


class AI(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chat(self, ctx, *, talk):
        global kernel
        response = kernel.respond(talk)
        emb = discord.Embed(
            title=f'AI chat bot taking with {ctx.author}',
            description=f'{response}',
            color=discord.colour.Colour.from_rgb(81, 147, 252)
        )
        await ctx.send(embed=emb)
def setup(bot):
    bot.add_cog(AI(bot))
