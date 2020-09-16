import discord
from discord.ext import commands
import database as db


class guildinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['guild', 'server-info', 'guild-info'])
    async def server(self, ctx):
        prefix = db.get_prefix(ctx.guild.id)
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            title=f"Server Information",
            description=f"**{ctx.guild.name}** Information",
            color=discord.Colour.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.add_field(name="✏ Name:", value=f'{ctx.guild.name}           ')
        emb.add_field(name="💳 ID:", value=f"{ctx.guild.id}")
        emb.add_field(name="👑 Owner is       ", value=f"{ctx.guild.owner.mention} ({ctx.guild.owner})")
        emb.add_field(name="👨‍👩‍👧‍👦 Members is", value=f"**{ctx.guild.member_count} Users**")
        emb.add_field(name="📆 Created at", value=ctx.guild.created_at)
        emb.add_field(name=f"📚 Channels ({len(ctx.guild.channels)})", value=f"🗂️Categories ({len(ctx.guild.categories)}) \n 💬Text ({len(ctx.guild.text_channels)}) \n 🔊Voice ({len(ctx.guild.voice_channels)})")
        emb.add_field(name="🌍 Region", value=ctx.guild.region)
        emb.add_field(name="📜 Rolls", value=f"{len(ctx.guild.roles)} Role")
        emb.add_field(name="😃 Emojis", value=f"{len(ctx.guild.emojis)} Emoji")
        emb.add_field(name="🔑 verification_level", value=f"{ctx.guild.verification_level}")
        emb.set_thumbnail(url=ctx.guild.icon_url)
        print(dir(ctx.guild))
        print(ctx.guild.icon_url)
        await ctx.send(embed=emb)

    @commands.command(aliases=['av', 'usericon'])
    async def avatar(self, ctx, member : discord.Member):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            title=f"{member} ID ({member.id})",
            description="Remember the avatar for users maybe their own copyright",
            color=discord.Colour.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=member.avatar_url)
        await ctx.send(embed=emb)

    @avatar.error
    async def avatar_error(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        prefix = db.get_prefix(ctx.guild.id)
        emb = discord.Embed(
            title="{avater , av, iconuser } command ",
            color=discord.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.add_field(name="Command:", value=f"`{prefix}`av [Member]", inline=False)
        emb.add_field(name="Example:", value=f"`{prefix}`av @Mtechsin", inline=False)
        await ctx.send(embed=emb)

    @commands.command(aliases=['user', 'member'])
    async def user_info(self, ctx, member: discord.Member):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            title=f"{member} ID ({member.id})",
            description=f"Information about {member.display_name}",
            color=discord.Colour.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.add_field(name="️📝Name:", value=member.display_name)
        emb.add_field(name="🆔ID:", value=member.id)
        for i in member.roles:
            emb.add_field(name="📜Roles:", value=i)
        emb.add_field(name="📆Joined at:", value=member.joined_at)
        emb.add_field(name="📅Created at:", value=member.created_at)
        emb.add_field(name="💪Activity:", value=member.activity)
        emb.add_field(name="😌status:", value=member.status)
        emb.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=emb)

    @commands.command(aliases=['ch', 'ch-info'])
    async def channel(self, ctx , channel : discord.TextChannel):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            title=f"{channel.name} ID ({channel.id})",
            color=discord.Colour.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.add_field(name="📃 Channel topic:", value=channel.topic, inline=False)
        emb.add_field(name="️📝 Name:", value=channel.name)
        emb.add_field(name="🆔 ID:", value=channel.id, inline=False)
        emb.add_field(name="🗂️ Category:", value=channel.category)
        emb.add_field(name="🔢 Position:", value=channel.position + 1)
        emb.add_field(name="🔞 NSFW:", value=channel.is_nsfw())
        emb.add_field(name="🗞️ news:", value=channel.is_news())
        emb.add_field(name="📂 type:", value=channel.type)
        emb.add_field(name="⏱ Cooldown:", value=f"{channel.slowmode_delay} seconds")
        emb.add_field(name="📅 Created at:", value=channel.created_at , inline=False)
        await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(guildinfo(bot))