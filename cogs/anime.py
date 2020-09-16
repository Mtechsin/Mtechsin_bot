import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
import database as db

res1 = None
anm = None
auth = None
ms = None


class test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.has_permissions()
    @commands.command()
    async def anime(self, ctx, *, animename):
        global auth
        global ms
        auth = ctx.author
        prefix = db.get_prefix(ctx.guild.id)
        rgb = db.getcolor(ctx.guild.id)
        await ctx.send(content="🔃 Please wait until search finished", delete_after=1.2)
        url = f'https://myanimelist.net/anime.php?q={animename}'
        page = requests.get(url).text
        soup = BeautifulSoup(page, "lxml")
        reslust = soup.findAll('a', class_="hoverinfo_trigger fw-b fl-l")
        description1 = "1- " + reslust[0].text + "\n"
        description1 += "2- " + reslust[1].text + "\n"
        description1 += "3- " + reslust[2].text + "\n"
        description1 += "4- " + reslust[3].text + "\n"
        description1 += "5- " + reslust[4].text + "\n"
        global anm
        anm = animename
        emb = discord.Embed(
            title=f"choose from 1 to 5 by write `{prefix}`n" + " {1, 2, 3, 4, 5}",
            description=description1,
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        msg = await ctx.send(embed=emb)
        ms = msg
        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        await msg.add_reaction('3️⃣')
        await msg.add_reaction('4️⃣')
        await msg.add_reaction('5️⃣')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        global ms
        global auth
        global anm
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
                    url = f'https://myanimelist.net/anime.php?q={anm}'
                    page = requests.get(url).text
                    soup = BeautifulSoup(page, "lxml")
                    reslust = soup.findAll('a', class_="hoverinfo_trigger fw-b fl-l")
                    inp_d = int(num)
                    titel = reslust[inp_d].text
                    webpage = reslust[inp_d]['href']
                    url1 = webpage
                    page1 = requests.get(url1).text
                    soup1 = BeautifulSoup(page1, "lxml")
                    td = soup1.find('td', class_='borderClass')
                    div = td.find('div')
                    divs = div.findAll('div')
                    type1 = divs[9].text.split(":")[1]
                    status = divs[11].text.split(":")[1]
                    aired = divs[12].text.split(":")[1]
                    premiered = divs[13].text.split(":")[1]
                    geners = divs[19]
                    a = geners.findAll('a')
                    rank = soup1.find('span', class_="numbers ranked").strong.text
                    scoure = soup1.find('div', class_="score-label").text
                    popularity = soup1.find('span', class_="numbers popularity").strong.text
                    imga = soup1.find('td', class_="borderClass")
                    img = imga.find('img')['data-src']
                    episodes = soup1.find('div', class_="spaceit").text.split(":")[1]
                    all2 = soup1.findAll('div', class_="spaceit")
                    source = all2[4].text.split(":")[1]
                    duration = all2[5].text.split(":")[1]
                    emb1 = discord.Embed(
                        title=titel,
                        description=f'[{titel}]({url1})',
                        color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
                    )
                    emb1.set_image(url=img)
                    emb1.add_field(name="🖥️Episodes:", value=episodes)
                    emb1.add_field(name="📚Source:", value=source)
                    emb1.add_field(name="✨Rating:", value=f'**{scoure} of 10.0**')
                    emb1.add_field(name="🛠️Status:", value=f'{status}', inline=True)
                    emb1.add_field(name="💞Popularity:", value=f'**{popularity}**')
                    emb1.add_field(name="💯Rank:", value=rank)
                    emb1.add_field(name="📅Aired:", value=aired, inline=True)
                    emb1.add_field(name="⏲Premiered:", value=premiered)
                    emb1.add_field(name="⌚Duration:", value=f'{duration}')
                    emb1.add_field(name="📁Type:", value=type1)
                    #   emb1.add_field(name="⚠classification:", value=Rating)
                    for i in range(len(a)):
                        emb1.add_field(name="📋Geners:", value=a[i].text + ",")
                    await msg1.channel.send(embed=emb1)
        except AttributeError:
            pass
    """
    @commands.command()
    async def n(self, ctx, number=None):
        rgb = db.getcolor(ctx.guild.id)
        if number is not None:
            await ctx.send(content="🔃 Please wait until search finished", delete_after=1.2)
            url = f'https://myanimelist.net/anime.php?q={anm}'
            page = requests.get(url).text
            soup = BeautifulSoup(page, "lxml")
            reslust = soup.findAll('a', class_="hoverinfo_trigger fw-b fl-l")
            inp_d = int(number) - 1
            titel = reslust[inp_d].text
            webpage = reslust[inp_d]['href']
            url1 = webpage
            page1 = requests.get(url1).text
            soup1 = BeautifulSoup(page1, "lxml")
            td = soup1.find('td', class_='borderClass')
            div = td.find('div')
            divs = div.findAll('div')
            type1 = divs[9].text.split(":")[1]
            status = divs[11].text.split(":")[1]
            aired = divs[12].text.split(":")[1]
            premiered = divs[13].text.split(":")[1]
            geners = divs[19]
            a = geners.findAll('a')
            rank = soup1.find('span', class_="numbers ranked").strong.text
            scoure = soup1.find('div', class_="score-label").text
            popularity = soup1.find('span', class_="numbers popularity").strong.text
            imga = soup1.find('td', class_="borderClass")
            img = imga.find('img')['data-src']
            episodes = soup1.find('div', class_="spaceit").text.split(":")[1]
            all2 = soup1.findAll('div', class_="spaceit")
            source = all2[4].text.split(":")[1]
            duration = all2[5].text.split(":")[1]
            emb1 = discord.Embed(
                title=titel,
                description=f'[{titel}]({url1})',
                color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
            )
            emb1.set_image(url=img)
            emb1.add_field(name="🖥️Episodes:", value=episodes)
            emb1.add_field(name="📚Source:", value=source)
            emb1.add_field(name="✨Rating:", value=f'**{scoure} of 10.0**')
            emb1.add_field(name="🛠️Status:", value=f'{status}', inline=True)
            emb1.add_field(name="💞Popularity:", value=f'**{popularity}**')
            emb1.add_field(name="💯Rank:", value=rank)
            emb1.add_field(name="📅Aired:", value=aired, inline=True)
            emb1.add_field(name="⏲Premiered:", value=premiered)
            emb1.add_field(name="⌚Duration:", value=f'{duration}')
            emb1.add_field(name="📁Type:", value=type1)
            #   emb1.add_field(name="⚠classification:", value=Rating)
            for i in range(len(a)):
                emb1.add_field(name="📋Geners:", value=a[i].text + ",")
            await ctx.send(embed=emb1)
        else:
            await ctx.send("please enter number")
"""

def setup(bot):
    bot.add_cog(test(bot))
