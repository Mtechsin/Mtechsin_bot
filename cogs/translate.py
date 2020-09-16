import discord
from discord.ext import commands
from googletrans import Translator
import database as db
import json

with open("./lang.json", 'r') as f:
    langs = json.load(f)
class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['trans', 't'])
    async def translate(self, ctx, lang=None, *, text=None):
        rgb = db.getcolor(ctx.guild.id)
        prefix = db.get(ctx.guild.id)
        if lang == None:
            await ctx.send(f"**You should use \n {prefix}trans `Language code` `Text`** \n Example: {prefix}trans `en` `Ich liebe diesen Bot`")
        elif text == None:
            await ctx.send(f"Please Enter text to translate")
        elif lang is not None and text is not None:
            msg = ctx.message
            trans = Translator()
            inp = trans.detect(text=text).lang
            out = trans.translate(text=text, dest=lang)
            emb = discord.Embed(
                title="Translation",
                color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
            )
            emb.add_field(name=f"Input text from language {inp} is: ", value=f"{text}")
            emb.add_field(name=f"Translation at language {lang} is: ", value=f"{out.text}", inline=False)
            await msg.add_reaction("🤔")
            await ctx.send(embed=emb)
    @commands.command()
    async def detect(self, ctx, *, text=None):
        rgb = db.getcolor(ctx.guild.id)
        msg = ctx.message
        trans = Translator()
        inp = trans.detect(text=text).lang
        lang2 = langs[inp]
        emb = discord.Embed(
            title=f"I think the language is",
            description=f"**{lang2}** \n and its code {inp}",
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        await msg.add_reaction("🤔")
        await ctx.send(embed=emb)

    @commands.command()
    async def langcodes(self, ctx):
        lang_1 = {
            'af': 'afrikaans',
            'sq': 'albanian',
            'am': 'amharic',
            'ar': 'arabic',
            'hy': 'armenian',
            'az': 'azerbaijani',
            'eu': 'basque',
            'be': 'belarusian',
            'bn': 'bengali',
            'bs': 'bosnian',
            'bg': 'bulgarian',
            'ca': 'catalan',
            'ceb': 'cebuano',
            'ny': 'chichewa',
            'zh-cn': 'chinese (simplified)',
            'zh-tw': 'chinese (traditional)',
            'co': 'corsican',
            'hr': 'croatian',
            'cs': 'czech',
            'da': 'danish',
            'nl': 'dutch',
            'en': 'english',
            'eo': 'esperanto',
            'et': 'estonian',
            'tl': 'filipino'
        }
        lang_2 = {
            'ko': 'korean',
            'ku': 'kurdish (kurmanji)',
            'ky': 'kyrgyz',
            'lo': 'lao',
            'la': 'latin',
            'lv': 'latvian',
            'lt': 'lithuanian',
            'lb': 'luxembourgish',
            'mk': 'macedonian',
            'mg': 'malagasy',
            'ms': 'malay',
            'ml': 'malayalam',
            'mt': 'maltese',
            'mi': 'maori',
            'mr': 'marathi',
            'mn': 'mongolian',
            'my': 'myanmar (burmese)',
            'ne': 'nepali',
            'no': 'norwegian',
            'ps': 'pashto',
            'fa': 'persian',
            'pl': 'polish',
            'pt': 'portuguese',
            'pa': 'punjabi',
            'ro': 'romanian',
            'ru': 'russian',
            'sm': 'samoan',
            'gd': 'scots gaelic',
            'sr': 'serbian',
            'st': 'sesotho',
            'sn': 'shona',
            'sd': 'sindhi',
            'si': 'sinhala',
            'sk': 'slovak',
            'sl': 'slovenian',
            'so': 'somali',
            'es': 'spanish',
            'su': 'sundanese',
            'sw': 'swahili',
            'sv': 'swedish',
            'tg': 'tajik',
            'ta': 'tamil',
            'te': 'telugu',
            'th': 'thai',
            'tr': 'turkish',
            'uk': 'ukrainian',
            'ur': 'urdu',
            'uz': 'uzbek',
            'vi': 'vietnamese',
            'cy': 'welsh',
            'xh': 'xhosa',
            'yi': 'yiddish',
            'yo': 'yoruba',
            'zu': 'zulu',
            'fil': 'Filipino',
            'he': 'Hebrew'
        }
        LANGUAGES = {
            'fi': 'finnish',
            'fr': 'french',
            'fy': 'frisian',
            'gl': 'galician',
            'ka': 'georgian',
            'de': 'german',
            'el': 'greek',
            'gu': 'gujarati',
            'ht': 'haitian creole',
            'ha': 'hausa',
            'haw': 'hawaiian',
            'iw': 'hebrew',
            'hi': 'hindi',
            'hmn': 'hmong',
            'hu': 'hungarian',
            'is': 'icelandic',
            'ig': 'igbo',
            'id': 'indonesian',
            'ga': 'irish',
            'it': 'italian',
            'ja': 'japanese',
            'jw': 'javanese',
            'kn': 'kannada',
            'kk': 'kazakh',
            'km': 'khmer',

        }
        emb = discord.Embed(
            title=f"Languages codes 1",
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb2 = discord.Embed(
            title=f"Languages codes 2",
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        emb3 = discord.Embed(
            title=f"Languages codes 3",
            color=discord.colour.Color.from_rgb(rgb[0], rgb[1], rgb[2])
        )
        for k, v in lang_1.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
            emb.add_field(name=f'The code is {k}', value=f'For language \n **{v}**')
        for k, v in LANGUAGES.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
            emb2.add_field(name=f'The code is {k}', value=f'For language \n **{v}**')
        for k, v in lang_2.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
            emb3.add_field(name=f'The code is {k}', value=f'For language \n **{v}**')
        await ctx.send(embed=emb)
        await ctx.send(embed=emb2)
        await ctx.send(embed=emb3)
def setup(bot):
    bot.add_cog(Translate(bot))