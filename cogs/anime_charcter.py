import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import database as db


class anime_char(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['char', 'anime-char'])
    async def charcter(self, ctx, *, animechar=None):
        prefix = db.get_prefix(ctx.guild.id)
        rgb = db.getcolor(ctx.guild.id)
        if animechar is not None:
            global name
            name = animechar
            url = f'https://www.anime-planet.com/characters/all?sort=likes&order=desc&name={animechar}'
            page = requests.get(url).text
            soup = BeautifulSoup(page, "lxml")
            res = soup.find('a', class_='name')['href']
            firstres = 'https://www.anime-planet.com' + res
            url1 = firstres
            page1 = requests.get(url1).text
            soup1 = BeautifulSoup(page1, "lxml")
            section = soup1.findAll('div', class_="pure-1 md-1-5")
            table = soup1.find('table', class_="pure-table striped noHeader")
            img = soup1.find('img', class_="screenshots")['src']
            img1 = 'https://www.anime-planet.com' + img
            role = table.find('a').text
            Gender = section[0].text.split(" ")[1]
            hair_colour = section[1].text.split(" ")[2]
            Rank = section[2].text.split(" ")[2]
            Rankoff = section[3].a.text
            charname = soup1.find('h1', itemprop="name").text
            emb = discord.Embed(
                title=f'{charname}',
                description=f'[{charname}]({url1})\n',
                color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
            )
            emb.set_image(url=img1)

            emb.add_field(name="Hair colour:", value=hair_colour)
            if Gender == "Male":
                emb.add_field(name="Gender:", value='Male ♂')
            else:
                emb.add_field(name="Gender:", value='Female ♀')
            emb.add_field(name="Hair colour:", value=hair_colour)
            emb.add_field(name=" ❤ Rank:", value=Rank)
            emb.add_field(name=" 💔 Rank:", value=Rankoff)
            await ctx.send(embed=emb)
        else:
            await ctx.send(f">>> {prefix}char + `CharcterName`"
                           f"\n example : `{prefix}char Kirito`")


def setup(bot):
    bot.add_cog(anime_char(bot))
