from youtube_search import YoutubeSearch
import discord
from discord.ext import commands
import database as db
class youtube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['yt', 'youtube-search'])
    async def youtube(self, ctx, *, search):
        rgb = db.getcolor(ctx.guild.id)
        results = YoutubeSearch(search, max_results=1).to_dict()
        duration = "duration is " + results[0]['duration']
        thumbnails = results[0]['thumbnails'][-1]
        title = results[0]['title']
        channel = results[0]['channel']
        long_desc = results[0]['long_desc']
        url = "https://www.youtube.com" + results[0]['url_suffix']
        emb = discord.Embed(
            title=title,
            description=f"[{title}]({url}))",
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_author(name=ctx.author,
                       icon_url=ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
        emb.add_field(name="Channel:", value=f'{channel}')
        emb.add_field(name="long_desc:", value=long_desc)
        emb.add_field(name="duration:", value=f"Duration is {duration}")
        emb.set_image(url=thumbnails)
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(youtube(bot))