import discord
from discord.ext import commands
import mysql.connector as msql
import database as db

class welcomer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(aliases=['welmsg', 'wmsg'])
    async def welcomemessage(self, ctx, *, message):
        mydb = msql.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
        cursor = mydb.cursor()
        sql = "INSERT INTO messages (guildid, message) VALUES (%s, %s)"
        data = (ctx.guild.id, message)
        cursor.execute(sql, data)
        mydb.commit()
        cursor.close()
        mydb.close()
        msg = ctx.message
        await msg.add_reaction("👌")
        await ctx.send("**Done** 🥳")

    @welcomemessage.error
    async def welcomemessage_error(self, error, ctx):
        prefix = db.get_prefix(ctx.guild.id)
        rgb = db.getcolor(ctx.guild.id)
        if isinstance(error, commands.MissingPermissions):
            emb = discord.Embed(
                title="Error 🚫",
                description="You dont have the Permission",
                color=discord.Color.red()
            )
            emb.set_author(name=ctx.author,
                           icon_url=ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
            await ctx.send(embed=emb)
        elif isinstance(error, commands.MissingRequiredArgument):
            emb = discord.Embed(
                title="{welcomemessage , welmsg, wmsg } command ",
                color=discord.Color.from_rgb(rgb[0], rgb[1], rgb[2])
            )
            emb.add_field(name="Command:", value=f"`{prefix}`Welmsg [message]", inline=False)
            emb.add_field(name="Example:", value=f"`{prefix}`Welmsg welcome", inline=False)
            await ctx.send(embed=emb)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        mydb = msql.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
        cursor = mydb.cursor()
        cursor.execute(f"SELECT channelid from channels WHERE guildid = '{member.guild.id}'")
        l = cursor.fetchall()
        cursor.close()
        mydb.close()
        if len(l) == 0:
            if channel is not None:
                mydb = msql.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
                cursor = mydb.cursor()
                cursor.execute(f"SELECT message FROM messages WHERE guildid = '{member.guild.id}'")
                l = cursor.fetchall()
                cursor.close()
                mydb.close()
                if len(l) == 0:
                    await channel.send(f'Welcome {member.mention}. you will love our community')
                else:
                    await channel.send(f"{member.mention} " + str(l[0][0]))
        else:
            ch = member.guild.get_channel(int(l[0][0]))
            mydb = msql.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
            cursor = mydb.cursor()
            cursor.execute(f"SELECT message FROM messages WHERE guildid = '{member.guild.id}'")
            l = cursor.fetchall()
            cursor.close()
            mydb.close()
            if len(l) == 0:
                await ch.send(f'Welcome {member.mention}. you will love our community')
            else:
                await ch.send(f"{member.mention} " + str(l[0][0]))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel
        mydb = msql.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
        cursor = mydb.cursor()
        cursor.execute(f"SELECT channelid from channels WHERE guildid = '{member.guild.id}'")
        l = cursor.fetchall()
        cursor.close()
        mydb.close()
        if len(l) == 0:
            if channel is not None:
                emb = discord.Embed(
                    title="Member leave 👋",
                    color=discord.colour.Color.dark_red()
                )
                emb.add_field(name="Member id:", value=member.id, inline=False)
                emb.add_field(name="Member name:", value=member.name, inline=False)
                emb.add_field(name="Members count:", value=member.guild.member_count, inline=False)
                await channel.send(embed=emb)
        else:
            ch = member.guild.get_channel(int(l[0][0]))
            emb = discord.Embed(
                title="Member leave 👋",
                color=discord.colour.Color.dark_red()
            )
            emb.add_field(name="Member id:", value=member.id, inline=False)
            emb.add_field(name="Member name:", value=member.name, inline=False)
            emb.add_field(name="Members count:", value=member.guild.member_count, inline=False)
            await ch.send(embed=emb)

    @commands.has_permissions(administrator=True)
    @commands.command(aliases=['welch', 'wchannel'])
    async def welcomechannel(self, ctx, channel: discord.TextChannel):
        msg = ctx.message
        mydb = msql.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
        cursor = mydb.cursor()
        sql = f"INSERT INTO channels (guildid, channelid) VALUES (%s, %s)"
        data = (ctx.guild.id, channel.id)
        cursor.execute(sql, data)
        mydb.commit()
        cursor.close()
        mydb.close()
        await msg.add_reaction("👌")
        await ctx.send(f"**Done** Welcome message is {channel.name} 🥳")

    @welcomechannel.error
    async def welcomechannel_error(self, error, ctx):
        prefix = db.get_prefix(ctx.guild.id)
        rgb = db.getcolor(ctx.guild.id)
        if isinstance(error, commands.MissingPermissions):
            emb = discord.Embed(
                title="Error 🚫",
                description="You dont have the Permission",
                color=discord.Color.red()
            )
            emb.set_author(name=ctx.author,
                           icon_url=ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
            await ctx.send(embed=emb)
        elif isinstance(error, commands.MissingRequiredArgument):
            emb = discord.Embed(
                title="{Welcomechannel , wchannel, welch } command ",
                color=discord.Color.from_rgb(rgb[0], rgb[1], rgb[2])
            )
            emb.add_field(name="Command:", value=f"`{prefix}`wchannel [Channel]", inline=False)
            emb.add_field(name="Example:", value=f"`{prefix}`wchannel #welcome", inline=False)
            await ctx.send(embed=emb)
        elif isinstance(error, commands.BadArgument):
            emb = discord.Embed(
                title="Error 🚫",
                description="You dont have the Permission",
                color=discord.Color.red()
            )
            emb.set_author(name=ctx.author,
                           icon_url=ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
            await ctx.send(embed=emb)

    @commands.has_permissions(administrator=True)
    @commands.command(aliases=['rwelcomechannel', 'rwchannel'])
    async def removerwelcomechannel(self, ctx, channel: discord.TextChannel):
        msg = ctx.message
        mydb = msql.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
        cursor = mydb.cursor()
        sql = f"DELET FROM channels WHERE guildid = '{ctx.guild.id}'"
        cursor.execute(sql)
        mydb.commit()
        cursor.close()
        mydb.close()
        await msg.add_reaction("🗑️")
        await ctx.send(f"**Done** I wont welcome in {channel.name} again ")


def setup(bot):
    bot.add_cog(welcomer(bot))
