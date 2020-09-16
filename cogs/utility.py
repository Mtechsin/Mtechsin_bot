import discord
from discord.ext import commands
import database as db
import mysql.connector as msql


class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setcolor(self, ctx, color=None):
        if color is None:
            prefix = db.get_prefix(ctx.guild.id)
            await ctx.send(f"Please Enter your color in hex \n Example : `{prefix}` color `#DDFF1A`")
        elif color[0] == "#" and len(color) == 7:
            co = color.strip("#")
            mydb = msql.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
            cursor = mydb.cursor()
            cursor.execute(
                f"UPDATE colors set color = '{co}' WHERE guildid = '{ctx.guild.id}'")
            mydb.commit()
            cursor.close()
            mydb.close()
            await ctx.send("**Done** 😄 Please wait to see your color")
            rgb = db.getcolor(ctx.guild.id)
            emb = discord.Embed(
                title=f"{db.getcolor(ctx.guild.id)}",
                color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
            )
            await ctx.send(embed=emb)

    @commands.command()
    async def website(self):
        pass

    @commands.command()
    async def invite(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            title=f"Here you are 😇  Invite link 💌 ",
            description=
            f"[Invite Mtechsin to you server] (https://discord.com/api/oauth2/authorize?client_id=724762569432367175&permissions=8&scope=bot)",
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_author(name=ctx.author,
                       icon_url=ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
        emb.set_footer(text="IF you like the bot please help us by donating or vote and thank you", icon_url=ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
        await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(utility(bot))
