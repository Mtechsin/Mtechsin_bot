import discord
from discord.ext import commands
import database as db

class support(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['donate'])
    async def support(self, ctx):
        prefix = db.get_prefix(ctx.guild.id)
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            title=f"Hi support us",
            description="You can support this bot by Donating or join ourserver or voting my bot",
            color=discord.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.add_field(name="Patreon link", value="https://www.patreon.com/mtechson" + " This if you want to donate me every month and you will get some rewards", inline=False)
        emb.add_field(name="ko-fi link", value="https://ko-fi.com/mtechson" + " This if you want to make one time support dont forget to enter your discord name to contact with you", inline=False)
        emb.add_field(name="Another Kind of support", value=".")
        emb.add_field(name="Join our server", value="you can join our server by clicking [here](https://discord.gg/hWXYFXs)", inline=False)
        emb.add_field(name="You can vote me ", value=f"you can vote me up by using `{prefix}`vote")
        emb.set_author(name=ctx.author,
                       icon_url=ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
        await ctx.send(embed=emb)

    @commands.command()
    async def voit(self, ctx):
        prefix = db.get_prefix(ctx.guild.id)
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            title=f"Vote me",
            description="",
            color=discord.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(support(bot))