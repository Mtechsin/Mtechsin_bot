import random
import praw
import discord
from discord.ext import commands
import database as db


class ReddIt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='comic1')
    async def c_hot(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        reddit = praw.Reddit(client_id='',
                             client_secret='',
                             username='',
                             password='',
                             user_agent='')
        subreddit = reddit.subreddit('anime_irl')
        ran = [1, 2, 4, 5, 6, 7, 8, 9, 10]
        num = random.choice(ran)
        rising_anime = subreddit.rising(limit=num)
        for sub in rising_anime:
            title = sub.title
            url = sub.preview
            url2 = sub.url
            img = url['images'][0]
            src = img['source']['url']
        emb = discord.Embed(
            title=title,
            description=f'[{title}]({url2})',
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=src)
        await ctx.send(embed=emb)

    @commands.command(name='comic2')
    async def rising_comics(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        global title
        reddit = praw.Reddit(client_id='',
                             client_secret='',
                             username='',
                             password='',
                             user_agent='')
        subreddit = reddit.subreddit('anime_irl')
        ran = [1, 2, 4, 5, 6, 7, 8, 9, 10]
        num = random.choice(ran)
        hot_anime = subreddit.hot(limit=num)
        for sub in hot_anime:
            title = sub.title
            url = sub.preview
            url2 = sub.url
            img = url['images'][0]
            src = img['source']['url']
        emb = discord.Embed(
            title=title,
            description=f'[{title}]({url2})',
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=src)
        await ctx.send(embed=emb)

    @commands.command(name='comic3')
    async def new_comics(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        reddit = praw.Reddit(client_id='',
                             client_secret='',
                             username='',
                             password='',
                             user_agent='')
        subreddit = reddit.subreddit('animemes')
        ran = [1, 2, 4, 5, 6, 7, 8, 9, 10]
        num = random.choice(ran)
        new_anime = subreddit.new(limit=num)
        for sub in new_anime:
            title = sub.title
            url = sub.preview
            url2 = sub.url
            img = url['images'][0]
            src = img['source']['url']
        emb = discord.Embed(
            title=title,
            description=f'[{title}]({url2})',
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=src)
        await ctx.send(embed=emb)

    @commands.command(name='comic4')
    async def top_comics(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        reddit = praw.Reddit(client_id='',
                             client_secret='',
                             username='',
                             password='',
                             user_agent='')
        subreddit = reddit.subreddit('animemes')
        ran = [1, 2, 4, 5, 6, 7, 8, 9, 10]
        num = random.choice(ran)
        top_anime = subreddit.top(limit=num)

        for sub in top_anime:
            title = sub.title
            url = sub.preview
            url2 = sub.url
            img = url['images'][0]
            src = img['source']['url']
        emb = discord.Embed(
            title=title,
            description=f'[{title}]({url2})',
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=src)
        await ctx.send(embed=emb)

    @commands.command()
    async def gifs1(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        reddit = praw.Reddit(client_id='',
                             client_secret='',
                             username='',
                             password='',
                             user_agent='')

        subreddit = reddit.subreddit('animegifs')
        ran = [1, 2, 4, 5, 6, 7, 8, 9, 10]
        num = random.choice(ran)
        rising_anime = subreddit.hot(limit=num)

        for sub in rising_anime:
            title = sub.title
            url2 = sub.url
        if not sub.is_video:
            emb = discord.Embed(
                title=title,
                description=f'[{title}]({url2})',
                color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
            )
            emb.set_image(url=url2)
            await ctx.send(embed=emb)
        else:
            await ctx.send(title)
            await ctx.send(sub.media['reddit_video']['fallback_url'])

    @commands.command()
    async def gifs2(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        reddit = praw.Reddit(client_id='',
                             client_secret='',
                             username='',
                             password='',
                             user_agent='')

        subreddit = reddit.subreddit('animegifs')
        ran = [1, 2, 4, 5, 6, 7, 8, 9, 10]
        num = random.choice(ran)
        rising_anime = subreddit.top(limit=num)

        for sub in rising_anime:
            title = sub.title
            url2 = sub.url
        if not sub.is_video:
            emb = discord.Embed(
                title=title,
                description=f'[{title}]({url2})',
                color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
            )
            emb.set_image(url=url2)
            await ctx.send(embed=emb)
        else:
            await ctx.send(title)
            await ctx.send(sub.media['reddit_video']['fallback_url'])

    @commands.command()
    async def gifs3(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        reddit = praw.Reddit(client_id='',
                             client_secret='',
                             username='',
                             password='',
                             user_agent='')

        subreddit = reddit.subreddit('animegifs')
        ran = [1, 2, 4, 5, 6, 7, 8, 9, 10]
        num = random.choice(ran)
        rising_anime = subreddit.new(limit=num)

        for sub in rising_anime:
            title = sub.title
            url2 = sub.url
        if not sub.is_video:
            emb = discord.Embed(
                title=title,
                description=f'[{title}]({url2})',
                color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
            )
            emb.set_image(url=url2)
            await ctx.send(embed=emb)
        else:
            await ctx.send(title)
            await ctx.send(sub.media['reddit_video']['fallback_url'])


def setup(bot):
    bot.add_cog(ReddIt(bot))
