import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import json
import database as db

with open("./data.json", 'r') as f:
    prefixs = json.load(f)


async def top(url, number1, ctx1, title1):
    if number1 is not None:
        rgb = c.getcolor(ctx1.guild.id)
        url1 = url
        page1 = requests.get(url1).text
        soup1 = BeautifulSoup(page1, "lxml")
        body = soup1.find('table', class_="top-ranking-table")
        anime_name_list = body.findAll('div', class_="di-ib clearfix")
        scoure_list = body.findAll('td', class_="score ac fs14")
        info = body.findAll('div', class_="information di-ib mt4")
        inp = int(number1)
        emb = discord.Embed(
            title=title1,
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        if inp == 1:
            for i in range(0, 10):
                emb.add_field(
                    name=str(i + 1) + "-> " + anime_name_list[i].a.text + " Score :" + scoure_list[i].span.text,
                    value=info[
                        i].text)
                emb.set_footer(text=f"{1} of 5 pages 📖")
        elif inp == 2:
            for i in range(10, 20):
                emb.add_field(
                    name=str(i + 1) + "-> " + anime_name_list[i].a.text + " Score :" + scoure_list[i].span.text,
                    value=info[
                        i].text)
                emb.set_footer(text=f"{2} of 5 pages 📖")
        elif inp == 3:
            for i in range(20, 30):
                emb.add_field(
                    name=str(i + 1) + "-> " + anime_name_list[i].a.text + " Score :" + scoure_list[i].span.text,
                    value=info[
                        i].text)
                emb.set_footer(text=f"{3} of 5 pages 📖")
        elif inp == 4:
            for i in range(30, 40):
                emb.add_field(
                    name=str(i + 1) + "-> " + anime_name_list[i].a.text + " Score :" + scoure_list[i].span.text,
                    value=info[
                        i].text)
                emb.set_footer(text=f"{4} of 5 pages 📖")
        elif inp == 5:
            for i in range(40, 50):
                emb.add_field(
                    name=str(i + 1) + "-> " + anime_name_list[i].a.text + " Score :" + scoure_list[i].span.text,
                    value=info[
                        i].text)
                emb.set_footer(text=f"{5} of 5 pages 📖")
        else:
            emb.add_field(name="Sorry", value="we will add more in the future😄")
        await ctx1.send(embed=emb)


class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def topanime(self, ctx, number=None):
        if number is not None:
            await top(ctx1=ctx, number1=number, title1='🏆Top Anime at all', url='https://myanimelist.net/topanime.php')
        else:
            global prefixs
            await ctx.send(f">>> {prefixs[str(ctx.guild.id)]}topanime + `pagenumber`"
                           f"\n example : `{prefixs[str(ctx.guild.id)]}topanime 1`")

    @commands.command()
    async def topairing(self, ctx, number=None):
        if number is not None:
            await top(ctx1=ctx, number1=number, title1='🏆Top Airing Anime',
                      url='https://myanimelist.net/topanime.php?type=airing')
        else:
            global prefixs
            await ctx.send(f">>> {prefixs[str(ctx.guild.id)]}topairing + `pagenumber`"
                           f"\n example : `{prefixs[str(ctx.guild.id)]}topairing 1`")

    @commands.command()
    async def topupcoming(self, ctx, number=None):
        if number is not None:
            await top(ctx1=ctx, number1=number, title1='🏆Top Upcoming Anime',
                      url='https://myanimelist.net/topanime.php')
        else:
            global prefixs
            await ctx.send(f">>> {prefixs[str(ctx.guild.id)]}topupcoming + `pagenumber`"
                           f"\n example : `{prefixs[str(ctx.guild.id)]}topupcoming 1`")

    @commands.command()
    async def topmovies(self, ctx, number=None):
        if number is not None:
            await top(ctx1=ctx, number1=number, title1='🏆Top Anime Movies',
                      url='https://myanimelist.net/topanime.php?type=movie')
        else:
            global prefixs
            await ctx.send(f">>> {prefixs[str(ctx.guild.id)]}topmovies + `pagenumber`"
                           f"\n example : `{prefixs[str(ctx.guild.id)]}topmovies 1`")

    @commands.command()
    async def topova(self, ctx, number=None):
        if number is not None:
            await top(ctx1=ctx, number1=number, title1='🏆Top Anime OVA Series',
                      url='https://myanimelist.net/topanime.php?type=ova')
        else:
            global prefixs
            await ctx.send(f">>> {prefixs[str(ctx.guild.id)]}topova + `pagenumber`"
                           f"\n example : `{prefixs[str(ctx.guild.id)]}topova 1`")

    @commands.command()
    async def topona(self, ctx, number=None):
        if number is not None:
            await top(ctx1=ctx, number1=number, title1='🏆Top Anime ONA Series',
                      url='https://myanimelist.net/topanime.php?type=ona')
        else:
            global prefixs
            await ctx.send(f">>> {prefixs[str(ctx.guild.id)]}topona + `pagenumber`"
                           f"\n example : `{prefixs[str(ctx.guild.id)]}topona 1`")

    @commands.command()
    async def topspecial(self, ctx, number=None):
        if number is not None:
            await top(ctx1=ctx, number1=number, title1='🏆Top Anime Specials',
                      url='https://myanimelist.net/topanime.php?type=special')
        else:
            global prefixs
            await ctx.send(f">>> {prefixs[str(ctx.guild.id)]}special + `pagenumber`"
                           f"\n example : `{prefixs[str(ctx.guild.id)]}special 1`")

    @commands.command()
    async def recommend(self, ctx, number=None):
        if number is not None:
            await top(ctx1=ctx, number1=number, title1="Our recommendation",
                      url='https://myanimelist.net/topanime.php?type=special')
        else:
            global prefixs
            await ctx.send(f">>> {prefixs[str(ctx.guild.id)]}recomnd + `pagenumber`"
                           f"\n example : `{prefixs[str(ctx.guild.id)]}recomnd 1`")

    @commands.command()
    async def suggest(self, ctx, number=None):
        if number is not None:
            await top(ctx1=ctx, number1=number, title1="Our suggestion",
                      url='https://myanimelist.net/topanime.php?type=special')
        else:
            global prefixs
            await ctx.send(f">>> {prefixs[str(ctx.guild.id)]}suggest + `pagenumber`"
                           f"\n example : `{prefixs[str(ctx.guild.id)]}suggest 1`")

    @commands.command()
    async def topchar(self, ctx, number=None):
        rgb = db.getcolor(ctx.guild.id)
        if number is not None:
            url1 = "https://myanimelist.net/character.php"
            page1 = requests.get(url1).text
            soup1 = BeautifulSoup(page1, "lxml")
            body = soup1.find('table', class_="characters-favorites-ranking-table")
            anime_char_list = body.findAll('div', class_="information di-ib mt24")
            anime_list_td = body.findAll('td', class_="animeography")
            info = body.findAll('td', class_="favorites")
            inp = int(number)
            emb = discord.Embed(
                title="💕Most Favorited anime Characters",
                color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
            )
            if inp == 1:
                for i in range(0, 10):
                    emb.add_field(
                        name=str(i + 1) + "-> " + anime_char_list[i].a.text,
                        value=" Anime :" + anime_list_td[
                            i + 1].a.text + " Favorites 💗 :" + info[i].text)
                    emb.set_footer(text=f"{1} of 5 pages 📖")
            elif inp == 2:
                for i in range(10, 20):
                    emb.add_field(
                        name=str(i + 1) + "-> " + anime_char_list[i].a.text,
                        value=" Anime :" + anime_list_td[
                            i + 1].a.text + "Favorites 💗 :" + info[i].text)
                    emb.set_footer(text=f"{2} of 5 pages 📖")
            elif inp == 3:
                for i in range(20, 30):
                    emb.add_field(
                        name=str(i + 1) + "-> " + anime_char_list[i].a.text,
                        value=" Anime :" + anime_list_td[
                            i + 1].a.text + "Favorites 💗 :" + info[i].text)
                    emb.set_footer(text=f"{3} of 5 pages 📖")
            elif inp == 4:
                for i in range(30, 40):
                    emb.add_field(
                        name=str(i + 1) + "-> " + anime_char_list[i].a.text,
                        value=" Anime :" + anime_list_td[
                            i + 1].a.text + "Favorites 💗 :" + info[i].text)
                    emb.set_footer(text=f"{4} of 5 pages 📖")
            elif inp == 5:
                for i in range(40, 50):
                    emb.add_field(
                        name=str(i + 1) + "-> " + anime_char_list[i].a.text,
                        value=" Anime :" + anime_list_td[
                            i + 1].a.text + "Favorites 💗 :" + info[i].text)
                    emb.set_footer(text=f"{5} of 5 pages 📖")
            await ctx.send(embed=emb)
        else:
            global prefixs
            await ctx.send(f">>> {prefixs[str(ctx.guild.id)]}topchar + `pagenumber`"
                           f"\n example : `{prefixs[str(ctx.guild.id)]}topchar 1`")


def setup(bot):
    bot.add_cog(info(bot))
