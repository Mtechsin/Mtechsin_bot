import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
from github import Github
import database as db
import ast


def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


class dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions()
    @commands.command(name="evel", pass_context=True)
    async def evel_(self, ctx, *, cmd):
        global insert_returns
        fn_name = "_eval_expr"

        cmd = cmd.strip("` ")

        # add a layer of indentation
        cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

        # wrap in async def body
        body = f"async def {fn_name}():\n{cmd}"

        parsed = ast.parse(body)
        body = parsed.body[0].body

        insert_returns(body)

        env = None
        exec(compile(parsed, filename="<ast>", mode="exec"), env)
        try:
            result = (await eval(f"{fn_name}()", env))
            await ctx.send(result)
        except Exception as ex:
            if type(ex) == discord.errors.HTTPException:
                await ctx.send("done in app console")

    @commands.command()
    async def decode(self, ctx, encode, *, text):
        @commands.command(aliases=['ghuser'])
        async def githubuser(self, ctx, username):
            rgb = db.getcolor(ctx.guild.id)
            g = Github("6847f3233ceba653ac5de76429a2f354e1fcf1f2")
            user = g.get_user(username)
            name = user.login.title()
            url = user.html_url
            type1 = user.type
            total_public_repos = user.public_repos
            repos_url = f'https://github.com/{user.login.title()}?tab=repositories'
            following = user.following
            followers = user.followers
            avatar = user.avatar_url
            created_at = user.created_at
            emb = discord.Embed(
                title="Github User",
                color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
            )
            emb.set_author(name=ctx.author,
                           icon_url=ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
            emb.add_field(name="name:", value=f'[{name}]({url})')
            emb.add_field(name="Type:", value=type1)
            emb.add_field(name="Created at:", value=str(created_at))
            emb.add_field(name="Total puplic repos:", value=str(total_public_repos))
            emb.add_field(name="Following:", value=str(following))
            emb.add_field(name="Followers:", value=str(followers))
            emb.add_field(name="Repos URL:", value=repos_url)
            emb.set_thumbnail(url=avatar)
            await ctx.send(embed=emb)

    @commands.command(aliases=['ghrebo'])
    async def githubrebo(self, ctx, rebo1):
        rgb = db.getcolor(ctx.guild.id)
        g = Github("6847f3233ceba653ac5de76429a2f354e1fcf1f2")
        repo = g.get_repo(rebo1)
        name = repo.name
        url = repo.html_url
        size = repo.size
        fullName = repo.full_name
        description = repo.description
        owner = repo.owner.login
        language = repo.language
        clone_url = repo.clone_url
        emb = discord.Embed(
            title="Github Repositories",
            description=f"[{name}]({url}) by({owner})",
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_author(name=ctx.author,
                       icon_url=ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
        emb.add_field(name="Full name:", value=f'[{fullName}]({url})')
        emb.add_field(name="Size:", value=str(size))
        emb.add_field(name="Language:", value=language)
        emb.add_field(name="Description:", value=description)
        emb.add_field(name="Clone URL:", value=clone_url)
        await ctx.send(embed=emb)

    @commands.command()
    async def pypi(self, ctx, pkg):
        rgb = db.getcolor(ctx.guild.id)
        url = f'https://pypi.org/search/?q={pkg}'
        page = requests.get(url).text
        soup = BeautifulSoup(page, "lxml")
        ul = soup.find("ul", class_="unstyled")
        li = ul.find("li")
        search_res = li.a['href']
        url2 = f"https://pypi.org{search_res}"
        page2 = requests.get(url2).text
        soup2 = BeautifulSoup(page2, "lxml")
        header = soup2.find("h1", class_="package-header__name").text
        pypi = soup2.find("p", class_="package-header__pip-instructions")
        released = soup2.find("p", class_="package-header__date").time.text
        pypi2 = pypi.span.text
        emb = discord.Embed(
            title="Pypi Package",
            description=f"[{header}]({page2}))",
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_author(name=ctx.author,
                       icon_url=ctx.author.avatar_url_as(format=None, static_format='png', size=1024))
        emb.add_field(name="Header:", value=f'{header}')
        emb.add_field(name="Install:", value=pypi2)
        emb.add_field(name="Released:", value=released)
        await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(dev(bot))
