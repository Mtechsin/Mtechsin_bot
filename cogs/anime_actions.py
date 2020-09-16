import random
import discord
from discord.ext import commands
import database as db

happy = [
    'https://media.tenor.com/images/d8cfad6474c16477362df878df5aba70/tenor.gif',
    'https://data.whicdn.com/images/174338423/original.gif',
    'https://i.pinimg.com/originals/c5/5e/5d/c55e5d7dca5c7a8e80d250e45593069b.gif',
    'https://media.tenor.com/images/d93523c4db7e20254c4dcd512029d51e/tenor.gif',
    'https://i.pinimg.com/originals/77/06/dd/7706dded712d1e0f6ddb38d0f6352c95.gif',
    'https://thumbs.gfycat.com/CompassionateEqualKittiwake-size_restricted.gif'
]
sad = [
    'https://media3.giphy.com/media/F6132ctb9YARa/giphy.gif?cid=ecf05e4744dfe7ca11c656d0fb458d6abe1ef8d18468a38d&rid=giphy.gif',
    'https://media1.giphy.com/media/zHGXhFJCVCbD2/200w.webp?cid=ecf05e470c8541de485916f40c67de8fd9e48f22def21ae9&rid=200w.webp',
    'https://media0.giphy.com/media/N0zizM2fKgGm4/giphy.gif?cid=ecf05e47cb13d78b38a90f47fedbf9df6f963ff30bc9a0fc&rid=giphy.gif',
    'https://media0.giphy.com/media/70egUiCHXuMdW/giphy.gif',
    'https://media2.giphy.com/media/3AhHNJikOnCuY/200w.webp?cid=ecf05e47f93d9757ff275291626088902d12a429d0f48264&rid=200w.webp'
]
angry = [
    'https://media2.giphy.com/media/hFVI29iuk2wFy/giphy.gif',
    'https://cdn.shopify.com/s/files/1/0318/2649/files/tenor-1_776d86a0-7df7-415c-b5e7-5b5af686ff5a_large.gif?v=1563936193',
    'https://media3.giphy.com/media/uXsPodwDXnitq/giphy.gif',
    'https://i.pinimg.com/originals/95/1b/ee/951bee1f1a8f7780439d82f364275b6f.gif',
    'https://media3.giphy.com/media/11raneDZtruZlm/source.gif',
    'https://68.media.tumblr.com/ad15062a5894a68e21b331e33f53c413/tumblr_of1urbUQ3O1udouqko1_500.gif'
]
punch = [
    'https://media3.giphy.com/media/AlsIdbTgxX0LC/giphy.gif',
    'https://i.pinimg.com/originals/f4/d5/99/f4d599cecf31cb538bff309811c9d23c.gif',
    'https://cdn159.picsart.com/228190013051202.gif?to=min&r=1024',
    'https://i.gifer.com/C3SI.gif',
    'https://66.media.tumblr.com/tumblr_me8y4edoGO1r6ojq0o1_500.gif'
]
confused = [
    'https://i.pinimg.com/originals/e7/65/e0/e765e06eb21f7bdd41eb6605222c4f60.gif',
    'https://i.pinimg.com/originals/bd/49/34/bd49340fdad5a8c38db46502d6e52b40.gif',
    'https://i.imgur.com/xTY4jyk.gif',
    'https://media.tenor.com/images/9a31b03fa3af17f5c4cfab4900d0b560/tenor.gif',
    'https://media.giphy.com/media/W4JuFZtyEzgMU/giphy.gif',
    'https://media.tenor.com/images/54a4ab1c0ed473db5249cd79a4d19629/tenor.gif'
]
bite = [
    'https://media1.tenor.com/images/8099a2d3e3f820ddcf96072fc33ad332/tenor.gif?itemid=8231871',
    'https://media0.giphy.com/media/OqQOwXiCyJAmA/source.gif',
    'https://media1.giphy.com/media/18C9KYCr4mgW4/source.gif',
    'https://i.imgur.com/xKJw3mX.gif',
    'https://pa1.narvii.com/6045/a9bb6d864ebe7e01ed647b78fc652f15116716c4_hq.gif',
    'https://i.pinimg.com/originals/c9/f1/53/c9f1535bb70e5e19d66d93cbcb856e14.gif'
]
clap = [
    'https://media.tenor.com/images/ed9272c81f685d9c3de214333ee08ced/tenor.gif',
    'https://thumbs.gfycat.com/RareFantasticGrebe-size_restricted.gif',
    'https://thumbs.gfycat.com/RightBigBluetickcoonhound-size_restricted.gif',
    'https://pa1.narvii.com/6047/33dc85dce586aacb707a1729d8548cc2bd610192_hq.gif',
    'https://media.tenor.com/images/07908bbd4b8336d826c733de9b2f2988/tenor.gif',
    'https://i.pinimg.com/originals/8b/f8/fe/8bf8feb807b3237c48ae65c5daa16042.gif'
]
cuddle = [
    'https://i.pinimg.com/originals/4d/89/d7/4d89d7f963b41a416ec8a55230dab31b.gif',
    'https://66.media.tumblr.com/f2a878657add13aa09a5e089378ec43d/tumblr_n5uovjOi931tp7433o1_500.gif',
    'https://i.imgur.com/wOmoeF8.gif',
]
dance = [
    'https://media1.tenor.com/images/c925511d32350cc04411756d623ebad6/tenor.gif?itemid=13462237',
    'https://cdn.lowgif.com/small/0e7bb3437e9b4f2a-are-na-anime-dance-gif-7-gif.gif',
    'https://media1.tenor.com/images/ac86c017ca70722fac3c92b03a4a4666/tenor.gif?itemid=15805017',
    'https://media1.tenor.com/images/4238f93069db01b55c459fa4219b1a2c/tenor.gif?itemid=13266384',
    'https://i.kym-cdn.com/photos/images/original/000/668/929/e84.gif',
    'https://thumbs.gfycat.com/IllinformedCostlyFritillarybutterfly-size_restricted.gif'
]
shock = [
    'https://media0.giphy.com/media/atyNuQv4pUOxG/giphy.gif',
    'https://i.imgur.com/bjXsCxP.gif',
    'https://i.imgur.com/xLbJjUE.gif',
    'https://media0.giphy.com/media/atyNuQv4pUOxG/giphy.gif',
    'https://2.bp.blogspot.com/-umiP71FyZSk/Wm_sC0yHBOI/AAAAAAABEMo/wyExcxk1IY4GcZpqIxBs7tBkE-QTlBebQCKgBGAs/s1600/Omake%2BGif%2BAnime%2B-%2BCitrus%2B-%2BEpisode%2B4%2B-%2BHimeko%2BShock.gif',
    'https://i.pinimg.com/originals/e1/0d/69/e10d69ea47659c9a721f4882f01d34c3.gif'
]
faceplam = [
    'https://i.gifer.com/YYBe.gif',
    'https://i.pinimg.com/originals/46/5c/34/465c344e842fe1705fa88211a60b3134.gif',
    'https://media.giphy.com/media/SV1tb2JXlPqkE/giphy.gif',
    'https://i.imgur.com/jgDL8eh.gif',
    'https://i.pinimg.com/originals/ca/a3/65/caa365306252b6299ce4c1269c48d774.gif'
]
greet = [
    'https://media.tenor.com/images/251d736302c3dcdb755b9aa59174556d/tenor.gif',
    'https://data.whicdn.com/images/210028482/original.gif',
    'https://pa1.narvii.com/6112/9da7b497534c63097d65890550955c17a8a0e05f_hq.gif',
    'https://i.pinimg.com/originals/b9/28/c2/b928c2502f06a584a6d1898db07b0aed.jpg',
    'https://thumbs.gfycat.com/GiganticDirtyAstarte-size_restricted.gif',
    'https://cdn105.picsart.com/203730462001202.gif?to=min&r=1024'
]
highfive = [
    'https://i.imgur.com/JEOKXFh.gif',
    'https://pa1.narvii.com/5880/0665ca3333e8f324d59f50a92a771f853062d74a_hq.gif',
    'https://media.tenor.com/images/f5d0866aef520ada41b23639d5577fbb/tenor.gif',
    'https://i.pinimg.com/originals/fc/b1/44/fcb1446b74166b0860ace50ed8b33686.gif',
    'https://media1.tenor.com/images/9730876547cb3939388cf79b8a641da9/tenor.gif?itemid=8073516',
    'https://66.media.tumblr.com/d51478d47d921d24e09cef77d2092208/tumblr_mfzwejAZvw1qce7ouo1_500.gif'
]
laugh = [
    'https://media3.giphy.com/media/pa1WaYStUKyLC/giphy.gif',
    'https://i.imgur.com/vdovi.gif',
    'https://i.gifer.com/7e45.gif',
    'https://i.pinimg.com/originals/4d/f1/8e/4df18e92e572823631919cf33de69900.gif',
    'https://media1.tenor.com/images/09d453fdea8349671b36c06746afd080/tenor.gif?itemid=12200646',
    'https://i.kym-cdn.com/photos/images/newsfeed/001/028/246/dc7.gif'
]
poke = [
    'https://i.pinimg.com/originals/b4/95/fb/b495fb19f4b9a1b04f48297b676c497b.gif',
    'https://media1.giphy.com/media/pWd3gD577gOqs/giphy.gif',
    'https://i.pinimg.com/originals/67/11/dd/6711ddf3a591bbc99aab173f3c0190de.gif',
    'https://em.wattpad.com/1146b2f416c3e82d9ba914026ae5034138aace7a/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f504d794b706358364b416a2d69413d3d2d3333383133303534322e313438613539316263323237343531623534313532393839363731362e676966',
    'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/315e10a2-158f-4563-90f9-8ee6e490dfb0/d6jf49q-f10859a5-ccc7-4a74-9330-069c97ba43f5.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvMzE1ZTEwYTItMTU4Zi00NTYzLTkwZjktOGVlNmU0OTBkZmIwXC9kNmpmNDlxLWYxMDg1OWE1LWNjYzctNGE3NC05MzMwLTA2OWM5N2JhNDNmNS5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.5LRoyjMFF90aFb5Tb2bTO0u3O8_GwP6eWZy_bxfCY-w'
]
pout = [
    'https://media1.tenor.com/images/b7e132fd3f4e110ea54ef8aa8f4eebbe/tenor.gif?itemid=15650605',
    'https://media.tenor.com/images/700c12f2a858f7eb6f3e20cc164156ee/tenor.gif',
    'https://thumbs.gfycat.com/DishonestExcitableHornet-size_restricted.gif',
    'https://thumbs.gfycat.com/ForkedKaleidoscopicCollie-size_restricted.gif',
    'https://66.media.tumblr.com/4018257a1a21e999cd1fdbcd67f38a1d/tumblr_nham95OVWg1rgfa0po1_500.gif'
]
run = [
    'https://i.pinimg.com/originals/0c/e8/be/0ce8bec2543d81ba65eefd309f0f0c5b.gif',
    'https://i.kym-cdn.com/photos/images/original/001/081/817/909.gif',
    'https://i.kym-cdn.com/photos/images/original/000/987/562/b2d.gif',
    'https://cdn.lowgif.com/small/03140d4a9537cd72-running-with-knives-anime-manga-know-your-meme.gif',
    'https://gifimage.net/wp-content/uploads/2017/09/anime-jumping-out-window-gif-3.gif',
    'https://cdn.myanimelist.net/s/common/uploaded_files/1460139914-f1109b66f45c29d770e26da53e875508.gif'
]
shot = [
    'https://media1.tenor.com/images/26893424f2b841f7427cd55f9e131383/tenor.gif?itemid=15538806',
    'https://media.tenor.com/images/a34dd7537be45df945cfd91eba72576c/tenor.gif',
    'https://cdn.lowgif.com/small/a1364798e4df8aab-intoxica-o-animentar-impress-es-sword-art-online-ii-12.gif',
    'https://media1.giphy.com/media/116gIOPlrV6ggw/giphy.gif',
    'https://cdn.lowgif.com/full/d8e477a108586443-said-it-before-girls-with-big-guns-are-hot-anime-manga-know.gif',
    'https://giffiles.alphacoders.com/148/148446.gif'
]
shurg = [
    'https://media1.tenor.com/images/94898cd48980cfc4128622300a9ba746/tenor.gif?itemid=14913933',
    'https://thumbs.gfycat.com/ReflectingHollowDuck-small.gif',
    'https://media.tenor.com/images/da7c311bcc569cf74d8755dafc8a4dbb/tenor.gif',
    'https://media.tenor.com/images/f9269d307f3c5e4ff0d37c3dfdaebb56/tenor.gif',
    'https://media.tenor.com/images/8a6ed3d685fb66e6e6d3b4b02f882ce9/tenor.gif',
    'https://em.wattpad.com/a80f62f2fe986fdf52000cef176185f64df5101c/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f734d32494243336c7843366d6a673d3d2d3639363639363938352e313538343434343563643361393437623435333435343234363232372e676966'
]
hide = [
    'https://media.tenor.com/images/da7c311bcc569cf74d8755dafc8a4dbb/tenor.gif',
    'https://i.pinimg.com/originals/bd/69/36/bd69362c627737bef489401a74aeb835.gif',
    'https://i.pinimg.com/originals/f8/eb/a7/f8eba73981eea6dd48e3630d867e6a59.gif',
    'https://66.media.tumblr.com/ce6c46fa1de32ebb01faf608d95243d8/tumblr_n4x4hb4qx81twvbvmo1_500.gif',
    'https://media3.giphy.com/media/fARFPMuspJRx6/giphy.gif'
]
slap = [
    'https://i.imgur.com/fm49srQ.gif',
    'https://i.imgur.com/oGsMYJe.gif',
    'https://i.pinimg.com/originals/4e/9e/a1/4e9ea150354ad3159339b202cbc6cad9.gif',
    'https://media1.tenor.com/images/427a88a4156db1f6ab11b3e38b0ca7d4/tenor.gif?itemid=13583613',
    'https://static.fjcdn.com/gifs/Mm_966fc2_1916375.gif'
]


class action(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def happy(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(happy))
        await ctx.send(embed=emb)

    @commands.command()
    async def sad(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(sad))
        await ctx.send(embed=emb)

    @commands.command()
    async def confused(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(confused))
        await ctx.send(embed=emb)

    @commands.command()
    async def angry(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(angry))
        await ctx.send(embed=emb)

    @commands.command()
    async def punch(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(punch))
        await ctx.send(embed=emb)

    @commands.command()
    async def confused(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(confused))
        await ctx.send(embed=emb)

    @commands.command()
    async def bite(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(bite))
        await ctx.send(embed=emb)

    @commands.command()
    async def clap(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(clap))
        await ctx.send(embed=emb)

    @commands.command()
    async def cuddle(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(cuddle))
        await ctx.send(embed=emb)

    @commands.command()
    async def shock(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(shock))
        await ctx.send(embed=emb)

    @commands.command()
    async def faceplam(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(faceplam))
        await ctx.send(embed=emb)

    @commands.command(name='hi')
    async def greet(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(greet))
        await ctx.send(embed=emb)

    @commands.command()
    async def dance(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(dance))
        await ctx.send(embed=emb)

    @commands.command()
    async def highfive(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(highfive))
        await ctx.send(embed=emb)

    @commands.command()
    async def laugh(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(laugh))
        await ctx.send(embed=emb)

    @commands.command()
    async def poke(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(poke))
        await ctx.send(embed=emb)

    @commands.command()
    async def pout(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(pout))
        await ctx.send(embed=emb)

    @commands.command()
    async def run(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(run))
        await ctx.send(embed=emb)

    @commands.command()
    async def shot(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(shot))
        await ctx.send(embed=emb)

    @commands.command()
    async def shot(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(shot))
        await ctx.send(embed=emb)

    @commands.command()
    async def hide(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(hide))
        await ctx.send(embed=emb)

    @commands.command()
    async def slap(self, ctx):
        rgb = db.getcolor(ctx.guild.id)
        emb = discord.Embed(
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb.set_image(url=random.choice(slap))
        await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(action(bot))
