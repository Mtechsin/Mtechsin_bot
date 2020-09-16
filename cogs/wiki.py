import discord
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
import database as db
import mysql.connector as msql
import wikipedia

s = None
ms = None
auth = None
l = None

class wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['wall'])
    async def wikiall(self, ctx, lang = None, *, search):
        if lang is not None:
            l = lang
            prefix = db.get_prefix(ctx.guild.id)
            await ctx.send(content="🔃 Please wait until search finished", delete_after=1.2)
            search = wikipedia.search(search)
            global s
            s = search
            description1 = "1- " + search[0] + "\n"
            description1 += "2- " + search[1] + "\n"
            description1 += "3- " + search[2] + "\n"
            description1 += "4- " + search[3] + "\n"
            description1 += "5- " + search[4] + "\n"
            rgb = db.getcolor(ctx.guild.id)
            emb = discord.Embed(
                title=f"select from  1-5 `{prefix}`n" + "{1, 2, 3, 4, 5}",
                description=description1,
                color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
            )
            msg = await ctx.send(embed=emb)
            global auth
            auth = ctx.author
            global ms
            ms = msg
            await msg.add_reaction('1️⃣')
            await msg.add_reaction('2️⃣')
            await msg.add_reaction('3️⃣')
            await msg.add_reaction('4️⃣')
            await msg.add_reaction('5️⃣')
        else:
            lang = "en"
            l = lang

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        global ms
        global auth
        global s
        global l
        num = None
        if reaction.emoji == "1️⃣":
            num = 0
        elif reaction.emoji == "2️⃣":
            num = 1
        elif reaction.emoji == "3️⃣":
            num = 2
        elif reaction.emoji == "4️⃣":
            num = 3
        elif reaction.emoji == "5️⃣":
            num = 4
        msg12 = reaction.message.id
        msg1 = reaction.message
        rgb = db.getcolor(msg1.guild.id)
        try:
            if ms.id == msg12:
                if user == auth:
                    await msg1.channel.send(content="🔃 Please wait until search finished", delete_after=1.2)
                    if l is None:
                        page = wikipedia.page(s[num])
                        title = page.title
                        url = page.url
                        img = page.images
                        summary = page.summary
                        referance = page.references
                        s = summary[0:850]
                        emb = discord.Embed(
                            title=f"Wikipedia",
                            description=f"[{title}]({url})",
                            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
                        )
                        emb.add_field(name="preview :", value=s + ".......Read more", inline=False)
                        emb.set_thumbnail(url=img[-1])
                        emb.set_footer(text=f"If you like this bot Please use Vote or donate",
                                       icon_url=user.avatar_url_as(format=None, static_format='png', size=1024))
                        for i in range(3):
                            emb.add_field(name="References", value=referance[i])
                        await msg1.channel.send(embed=emb)
                    elif l is not None:
                        wikipedia.set_lang(l)
                        page = wikipedia.page(s[num])
                        title = page.title
                        url = page.url
                        img = page.images
                        summary = page.summary
                        referance = page.references
                        s = summary[0:850]
                        emb = discord.Embed(
                            title=f"Wikipedia",
                            description=f"[{title}]({url})",
                            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
                        )
                        emb.add_field(name="preview :", value=s + ".......Read more", inline=False)
                        emb.set_thumbnail(url=img[-1])
                        emb.set_footer(text=f"If you like this bot Please use Vote or donate",
                                       icon_url=user.avatar_url_as(format=None, static_format='png', size=1024))
                        for i in range(3):
                            emb.add_field(name="References", value=referance[i])
                        await msg1.channel.send(embed=emb)
        except AttributeError:
            pass


    @commands.command(aliases=['w'])
    async def wiki(self, ctx, lang=None, *, search):
        if lang is None:
            rgb = db.getcolor(ctx.guild.id)
            msg = await ctx.send(content="🔃 Please wait until search finished", delete_after=1.2)
            page = wikipedia.page(search)
            title = page.title
            url = page.url
            img = page.images
            summary = page.summary
            referance = page.references
            s = summary[0:850]
            emb = discord.Embed(
                title=f"Wikipedia",
                description=f"[{title}]({url})",
                color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
            )
            emb.add_field(name="preview :", value=s + ".......Read more", inline=False)
            emb.set_thumbnail(url=img[-1])
            emb.set_footer(text=f"If you like this bot Please use Vote or donate",
                           icon_url=msg.author.avatar_url_as(format=None, static_format='png', size=1024))
            for i in range(3):
                emb.add_field(name="References", value=referance[i])
            await ctx.send(embed=emb)
        elif lang is not None:
            rgb = db.getcolor(ctx.guild.id)
            msg = await ctx.send(content="🔃 Please wait until search finished", delete_after=1.2)
            wikipedia.set_lang(lang)
            page = wikipedia.page(search)
            title = page.title
            url = page.url
            img = page.images
            summary = page.summary
            referance = page.references
            s = summary[0:850]
            emb = discord.Embed(
                title=f"Wikipedia",
                description=f"[{title}]({url})",
                color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
            )
            emb.add_field(name="preview :", value=s + ".......Read more", inline=False)
            emb.set_thumbnail(url=img[-1])
            emb.set_footer(text=f"If you like this bot Please use Vote or donate",
                           icon_url=msg.author.avatar_url_as(format=None, static_format='png', size=1024))
            for i in range(3):
                emb.add_field(name="References", value=referance[i])
            await ctx.send(embed=emb)

    @wiki.error
    async def wiki_error(self, ctx, error):
        prefix = db.get_prefix(ctx.guild.id)
        rgb = db.getcolor(ctx.guild.id)
        if isinstance(error, MissingRequiredArgument):
            emb = discord.Embed(
                title="{wiki, w} command",
                color=discord.Color.from_rgb(rgb[0], rgb[1], rgb[2])
            )
            emb.add_field(name="Command:", value=f"{prefix} wiki <Lang_code> [Text_search]", inline=False)
            emb.add_field(name="Example:", value=f"{prefix} wiki de google", inline=False)
            await ctx.send(embed=emb)

    @wikiall.error
    async def wikiall_error(self, ctx, error):
        prefix = db.get_prefix(ctx.guild.id)
        rgb = db.getcolor(ctx.guild.id)
        if isinstance(error, MissingRequiredArgument):
            emb = discord.Embed(
                title="{wiki, wall} command",
                color=discord.Color.from_rgb(rgb[0], rgb[1], rgb[2])
            )
            emb.add_field(name="Command:", value=f"{prefix} wikiall <Lang_code> [Text_search]", inline=False)
            emb.add_field(name="Example:", value=f"{prefix} wikiall de google", inline=False)
            await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(wiki(bot))
