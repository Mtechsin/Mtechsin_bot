import discord, bs4, sys,requests, os
from discord.ext import commands
import json
def get_profex(bot, message):
    with open("data.json", 'r') as f :
        prefixs = json.load(f)
    return prefixs[str(message.guild.id)]
with open("data.json", 'r') as f :
        prefixs = json.load(f)
bot = commands.Bot(command_prefix = get_profex)
@bot.remove_command('help')
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('=help'))
    print("ready")

@bot.command()
async def help(ctx):
    auther = ctx.author.mention
    emb = discord.Embed(
        title=f"Mtechsin commands",
        description="Write command with prefix that is in you server \n "
                    +f"Your prefix in this server is `{prefixs[str(ctx.guild.id)]}` \n"
                    +"Note when you see \n "
                    + " this `[]` means **Commands arguments required** \n "
                    + " this `{}`means or __Example__ : `{1, 2, 3} means  1 or 2 or 3` \n"
                    + "***I will be pleased to invite me to another server*** \n"
                    + f"**using:** `{prefixs[str(ctx.guild.id)]}invite`",
        color=discord.colour.Colour.from_rgb(81, 147, 252)
    )
    emb.add_field(name="🖥️Anime search🔎 commands📝:", value=
    "**To search about any ** `anime or move` \n"
    +f"`{prefixs[str(ctx.guild.id)]}aime [Anime name]`"
    +"**To search about any ** `anime charchter` \n"
    +f"`{prefixs[str(ctx.guild.id)]}char [AnimeCharcter name]`")


    emb.add_field(name="Out recommendation commands📝:", value=
    "***We hope to enjoy our recommendation and suggestion***\n"
    +"**To get our suggestion **\n"
    + f"`{prefixs[str(ctx.guild.id)]}recommend " + '{1, 2, 3, 4, 5}`\n'
    + "**To get our suggestion **\n"
    + f"`{prefixs[str(ctx.guild.id)]}suggest " + '{1, 2, 3, 4, 5}`\n',
    )
    emb.add_field(name="Comics commands 📝:", value=
    "***This give you random anime comics from reddit***\n"
    + f"`{prefixs[str(ctx.guild.id)]}comic" + '{1, 2, 3, 4}`\n'
    + "**Note their is no space between comics and number**\n"
                  )
    emb.add_field(name="🏆Top 50 anime commands 📝:", value=
    "**To get 🏆Top 50 ** `anime or move` \n"
    + f"`{prefixs[str(ctx.guild.id)]}topanime " + '{1, 2, 3, 4, 5}`\n'
    + "**To get 🏆Top 50 ** `Airing Anime` \n"
    + f"`{prefixs[str(ctx.guild.id)]}topairing " + '{1, 2, 3, 4, 5}`\n'
    + "**To get 🏆Top 50 ** `Anime Movies` \n"
    + f"`{prefixs[str(ctx.guild.id)]}topmovies " + '{1, 2, 3, 4, 5}`\n'
    + "**To get 🏆Top 50 ** `Anime OVA` \n"
    + f"`{prefixs[str(ctx.guild.id)]}topova " + '{1, 2, 3, 4, 5}`\n'
    + "**To get 🏆Top 50 ** `Anime ONA` \n"
    + f"`{prefixs[str(ctx.guild.id)]}topona " + '{1, 2, 3, 4, 5}`\n'
    + "**To get 🏆Top 50 ** `Anime Specials` \n"
    + f"`{prefixs[str(ctx.guild.id)]}topspecial " + '{1, 2, 3, 4, 5}\n`'
    + "**To get 🏆Top 50 ** `Anime charchters` \n"
    + f"`{prefixs[str(ctx.guild.id)]}topchar " + '{1, 2, 3, 4, 5}`\n')
    emb.add_field(name="Anime Reactons  🤭:", value=
    " 😄\n"+f"`{prefixs[str(ctx.guild.id)]}`happy\n"
    +" 🙁\n"+f"`{prefixs[str(ctx.guild.id)]}`sad\n"
    +" 😡\n"+f"`{prefixs[str(ctx.guild.id)]}`angry\n"
    +" 😤\n" + f"`{prefixs[str(ctx.guild.id)]}`pout\n"
    +" 👏\n"+f"`{prefixs[str(ctx.guild.id)]}`clap\n"
    +" 😵\n"+f"`{prefixs[str(ctx.guild.id)]}`confused\n"
    +" 😒\n"+f"`{prefixs[str(ctx.guild.id)]}`faceplam\n"
    +" 🤣\n"+f"`{prefixs[str(ctx.guild.id)]}`laugh\n"
    +" 😟\n"+f"`{prefixs[str(ctx.guild.id)]}`hide\n"
    +" 👊🏻\n"+f"`{prefixs[str(ctx.guild.id)]}`punch\n"
    +" 🏃‍♀\n"+f"`{prefixs[str(ctx.guild.id)]}`run\n"
    +" 🤯‍\n"+f"`{prefixs[str(ctx.guild.id)]}`shock\n"
    +" 🔫‍\n"+f"`{prefixs[str(ctx.guild.id)]}`shot\n"
    +" 😒\n"+f"`{prefixs[str(ctx.guild.id)]}`slap\n")
    emb.add_field(name="Anime actions💪",value=
    " 👉\n" + f"`{prefixs[str(ctx.guild.id)]}`poke\n"
    + " ✋\n" + f"`{prefixs[str(ctx.guild.id)]}`hi\n"
    + " 🤗\n" + f"`{prefixs[str(ctx.guild.id)]}`cuddle\n"
    + " 💃🏼\n" + f"`{prefixs[str(ctx.guild.id)]}`dance\n"
    + " 🙌🏼\n" + f"`{prefixs[str(ctx.guild.id)]}`highfive\n"
                  )
    emb.add_field(name="⚙ Sittings",value=
    "**Change prefix for this server**\n"
    +f'`{prefixs[str(ctx.guild.id)]}prefix [newprefix]`\n'
    +"**get prefix for this serverr**\n"
    +f"`{prefixs[str(ctx.guild.id)]}getprefix`\n"
                  )
    await ctx.send(content=f"I send you commands in message {auther}",delete_after=2 )
    await ctx.author.send(embed=emb)

@bot.event
async def on_guild_join(guild):
    with open("data.json", 'r') as f :
        prefixs = json.load(f)
    prefixs[str(guild.id)] = "="
    with open('data.json', 'w') as f :
        json.dump(prefixs, f, indent=4)
    print('done')
@bot.event
async def on_guild_remove(guild):
    with open("data.json", 'r') as f:
        prefixs = json.load(f)
    prefixs.pop(str(guild.id))
    with open('data.json', 'w') as f:
        json.dump(prefixs, f, indent=4)
@bot.command()
async def prefix(ctx, add_prifex):
    with open("data.json", 'r') as f :
        prifexs = json.load(f)
    prifexs[str(ctx.guild.id)] = add_prifex
    with open('data.json', 'w') as f :
        json.dump(prifexs, f, indent=4)
    await ctx.send('i will lestin to this prefix' + add_prifex)
@bot.command()
async def ping(ctx):
    emb = discord.Embed(
        colour=discord.colour.Colour.from_rgb(81, 147, 252)
    )
    emb.add_field(name="Your Ping is ", value=f'```{round(bot.latency*1000)} ms              ```')
    await ctx.send("🏓 Pong!  ")
    await ctx.send(embed = emb)
@bot.command()
async def getprefix(ctx):
    with open("data.json", 'r') as f :
        prefixs = json.load(f)
    await ctx.send(f"prefix for this server is`{prefixs[str(ctx.guild.id)]}`")
@bot.command()
async def clear(ctx, ammount = 5):
    if ammount == 0:
        print('error')
    else:
        await ctx.channel.purge(limit=ammount)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


##home = os.environ['Toked']
bot.run("NzI0NzYyNTY5NDMyMzY3MTc1.XvE5vQ.AszmuWm1cDAyeExb4XqV0pe1xmM")



