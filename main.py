import io
import os
import discord
from discord import colour
from discord import channel
from discord.ext import commands
import requests
import asyncio
import aiohttp
import random
import jishaku
from PIL import Image
from PIL import ImageFont
import asyncpg
from PIL import ImageDraw
import datetime
import DiscordUtils
import discord_components
from discord_components import *
from discord_components import ButtonStyle
from io import BytesIO
import json
import wikipedia
import random
from discord import Spotify
from googleapiclient.discovery import build
config = default.config()


client = commands.Bot(command_prefix=config['prefix'],
                      intents=discord.Intents.all())
client.remove_command('help')
client.sniped_messages = {}
client.session = aiohttp.ClientSession()
client.launch_time = datetime.datetime.utcnow()

initial_extensions = [
    'cogs.fun', 'cogs.invite', 'cogs.moderation', 'cogs.modmail', 'cogs.music',
    'cogs.members', 'cogs.general', 'cogs.test', 'cogs.public', 'cogs.images',
    'cogs.anime',  'cogs.gif' , 'cogs.spotify', 'cogs.levelling'
]

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)



@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.do_not_disturb,
        activity=discord.Game(
            f"On {len(client.guilds)} servers | {commands_prefix}help ")
    )
    print('online!')
    print(f"logged In As {client.user.name} ")
    print(f"Logged In As Id : {client.user.id}")
    DiscordComponents(client)



@client.group(invoke_without_command=True)
async def help(ctx):

    embed = discord.Embed(title="**Commands**",
                          url="",
                          description="a!help [catagories] ",
                          colour=discord.Colour(value=0x36393e))
    embed.set_thumbnail(
        url=
        "https://cdn.dribbble.com/users/32512/screenshots/4787574/light_ai_design_by_gleb.gif"
    )
    embed.add_field(name="a!report", value='Report Problems to the Admins')
    embed.add_field(name="> **MUSIC**",
                    value=" <a:arrow:890618537826205736>  Music Commands",
                    inline=False)
    embed.add_field(name="> **FUN**", value="   Fun Commands", inline=False)
    embed.add_field(name="> **General**",
                    value="<a:arrow:890618537826205736>   General Commands",
                    inline=False)
    embed.add_field(name="> **MOD**",
                    value="<a:arrow:890618537826205736>   Moderation Commands",
                    inline=False)
    embed.add_field(name="> **Activity **",
                    value="<a:arrow:890618537826205736>   Activity Commands",
                    inline=False)
    embed.add_field(name="> **Gif  **",
                    value="<a:arrow:890618537826205736>   Gif Commands",
                    inline=False)
    embed.set_footer(text=f"Requested By {ctx.author.name}",
                     icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=embed)


@help.command(aliases=["music"])
async def _lol(ctx):
    em = discord.Embed(description='**Music commands**',
                       colour=discord.Colour(value=0x36393e))
    em.add_field(
        name="> **Play**",
        value="- **`a!play`** = **Plays The Song Requested By The User**",
        inline=False)
    em.add_field(
        name="> **Stop**",
        value="- **`a!stop`** = **Stop The Song That Is Currently Playing**",
        inline=False)
    em.add_field(
        name="> **Now Playing**",
        value=
        "- **`a!np`** = **Show Information About The Song That Is Currently Playing**",
        inline=False)
    em.add_field(
        name="> **Join**",
        value="- **`a!join`** = **Connect The Bot To The Voice Channel **",
        inline=False)
    em.add_field(
        name="> **Disconnect*",
        value="- **`a!dc`** = **Disconnect The Bot From The Voice Channel**",
        inline=False)
    em.add_field(
        name="> **Loop**",
        value=
        "- **`a!loop`** = **Put A Loop To The Song Playing In The Voice Channel**",
        inline=False)
    em.add_field(
        name="> **Loop**",
        value=
        "- **`a!loop`** = **Put A Loop To The Song Playing In The Voice Channel**",
        inline=False)
    em.set_footer(text=f"Requested By {ctx.author.name}",
                  icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=em)


@help.command(aliases=['gif'])
async def Gif(ctx):
    em = discord.Embed(description='GIFFYY commands {beta}',
                       colour=discord.Colour(value=0x36393e))
    em.add_field(name="> **Kiss**",
                 value="**`a!kiss`** = **kiss a member** ",
                 inline=False)
    em.add_field(name="> **Pat**",
                 value="**`a!pat`** = **Pat a member** ",
                 inline=False)
    em.add_field(name="> **Hug**",
                 value="**`a!hug`** = **Hug A member** ",
                 inline=False)
    em.add_field(name="> **Lick**",
                 value="**`a!lick`** = **lick a member** ",
                 inline=False)
    em.add_field(name="> **Bonk**",
                 value="**`a!bonk`** = **Bonk a member** ",
                 inline=False)
    em.add_field(name="> **Yeet**",
                 value="**`a!yeet`** = **yeet a member** ",
                 inline=False)
    em.add_field(name="> **Wave**",
                 value="**`a!wave`** = **wave to a member** ",
                 inline=False)
    em.add_field(name="> **HighFive**",
                 value="**`a!highfive`** = **Highfive a member** ",
                 inline=False)
    em.add_field(name="> **Bite**",
                 value="**`a!bite`** = **Bite A Member** ",
                 inline=False)
    em.set_footer(text=f"Requested By {ctx.author.name}",
                  icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=em)



@help.command(aliases=['mod'])
async def Mod(ctx):
    em = discord.Embed(description='Moderation Commands',
                       colour=discord.Colour(value=0x36393e))
    em.add_field(name="> **Kick**",
                 value="**`a!kick`** = **kick A Member From The Guild** ",
                 inline=False)
    em.add_field(name="> **Ban**",
                 value="- **`a!ban`** = **Kick A Member From The Guild **",
                 inline=False)
    em.add_field(
        name="> **Clear**",
        value="- **`a!clear `** = **Clear Messages From The Channel **",
        inline=False)
    em.add_field(name="> **Dm**",
                 value="- **`a!dm `** = **Dm A Member**",
                 inline=False)
    em.add_field(name="> **Say**",
                 value="- **`a!say `** = ** Say A Message In Embed**",
                 inline=False)
    em.add_field(
        name="> **Anoouncement**",
        value=
        "- **`a!ann [mention channel] [Title] [Description] `** = **Announce**",
        inline=False)
    em.add_field(name="> **Poll**",
                 value="- **`a!poll `** = **Makes A Poll**",
                 inline=False)
    em.add_field(
        name="> **Multiple poll**",
        value=
        "- **`a!multi_choice [Question] [Ans 1] [Ans 2] `** = **Makes a Poll**",
        inline=False)

    em.add_field(
        name="> **Slowmode**",
        value="- **`a!slowmode [sec]`** = **Set A Slowmode In The Chat**",
        inline=False)

    em.add_field(
        name="> **Give Role**",
        value="- **`a!giverole [user] [role]`** = **Give A Role To The User**",
        inline=False)

    em.add_field(
        name="> **Remove Role**",
        value=
        "- **`a!removerole [user] [role]`** = **Remove A Role From The User**",
        inline=False)
    em.set_footer(text=f"Requested By {ctx.author.name}",
                  icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=em)


@help.command(aliases=['Activity'])
async def activity(ctx):
    em = discord.Embed(descrption="**Activity Commands**",
                       colour=discord.Colour(value=0x36393e))
    em.add_field(
        name="> **Spotify**",
        value=
        "- **`a!spotify [user] `** = **Shows The Song User Is Listening To**",
        inline=False)

    em.add_field(
        name="> **Game**",
        value="- **`a!game [user] `** = **Shows The Game User Is Playing**",
        inline=False)
    em.add_field(
        name="> **Current Games**",
        value=
        "- **`a!currentgames `** = **Shows The Game user is playing from whole server**",
        inline=False)
    em.set_footer(text=f"Requested By {ctx.author.name}",
                  icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=em)


@help.command(aliases=['fun'])
async def Fun(ctx):
    em = discord.Embed(description='**Fun Commands**',
                       colour=discord.Colour(value=0x36393e))
    em.add_field(
        name="> **Emojify**",
        value="- **`a!emojify`** = **Send A emoji Of The Secific Alphabet **",
        inline=False)
    em.add_field(name="> **Meme**",
                 value="- **`a!meme `** = **Send A Random Meme **",
                 inline=False)
    em.add_field(name="> **Wanted**",
                 value="- **`a!wanted `** = **Send A Wanted Meme **",
                 inline=False)
    em.add_field(
        name="> **Wikipedia**",
        value="- **`a!wiki `** = **Search Somenthing For You in Wiki**",
        inline=False)

    em.add_field(name="> **8ball**",
                 value="- **`a!8ball `** = **Aswer Your Question**",
                 inline=False)
    em.add_field(name="> **Show Image**",
                 value="- **`a!show `** = **Show An Image**",
                 inline=False)
    em.add_field(name="> **Show A Gif**",
                 value="- **`a!gif `** = **Shows A Random Gif**",
                 inline=False)
    em.add_field(
        name="> **RelationShip**",
        value="- **`a!ship [1] [2] `** = **Show The Relation With Users**",
        inline=False)
    em.add_field(
        name="> **Gay Scanner**",
        value="- **`a!gay [member] `** = **Shows The Gay Percentage**",
        inline=False)
    em.add_field(name="> **oof**",
                 value="- **`a!oof [user] `** = **Idk test ur own**",
                 inline=False)
    em.add_field(
        name="> **Snipe**",
        value="- **`a!snipe `** = **Shows The Recelntly Deleted Message**",
        inline=False)
    em.add_field(name="> **GIF**",
                 value="- **`a!gif [search] `** = **Send A Gif **",
                 inline=False)
    em.set_footer(text=f"Requested By {ctx.author.name}",
                  icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=em)


@help.command(aliases=['general'])
async def General(ctx):
    em = discord.Embed(description='**General Commands**',
                       colour=discord.Colour(value=0x36393e))
    em.add_field(name="> **Ping**",
                 value="- **`a!ping `** = **Show The Latency Of The Bot **",
                 inline=False)
    em.add_field(
        name="> **Server Info**",
        value="- **`a!server `** = **Shows The Information About The Guild **",
        inline=False)
    em.add_field(
        name="> **Members**",
        value=
        "- **`a!members `** = **Shows The Number Of Members In A Guild **",
        inline=False)
    em.add_field(name="> **Avatar**",
                 value="- **`a!av `** = **Shows The Avatar **",
                 inline=False)
    em.add_field(
        name="> **Check Messages**",
        value=
        "- **`a!check `** = **Checks The Count Of Messages In Past 7 Days **",
        inline=False)
    em.add_field(
        name="> Whois",
        value="- **`a!whois`** = **Check The Information About A User**",
        inline=False)
    em.set_footer(text=f"Requested By {ctx.author.name}",
                  icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=em)


@client.command()
async def wanted(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    wanted = Image.open("wanted.png")
    asset = user.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((177, 177))
    wanted.paste(pfp, (136, 245))

    wanted.save("profile.png")
    await ctx.send(file=discord.File("profile.png"))


@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (message.content,
                                                message.author,
                                                message.channel.name,
                                                message.created_at)


@client.command()
async def snipe(ctx):
    try:
        contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]
    except:
        await ctx.channel.send("Couldn't find a message to snipe!")
        return
    embed = discord.Embed(description=contents , colour=discord.blue(), timestamp=time)
    embed.set_author(name=f"{author.name}#{author.discriminator}",icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")
    await ctx.channel.send(embed=embed)


api_key = "AIzaSyC9kpu_Dl3HLBXxEwDJS9ub8NRXuz3NhQk"


@client.command(aliases=["show"])
async def showpic(ctx, *, search):
    ran = random.randint(0, 9)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(q=f"{search}",
                           cx="8cc1ebe8675cea131",
                           searchType="image").execute()
    url = result["items"][ran]["link"]
    embed1 = discord.Embed(title=f"**{search}**",
                           colour=discord.Colour(value=0x36393e))
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)





@client.command()
async def uptime(ctx):
    delta_uptime = datetime.datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)

    embed = discord.Embed(title=" Status",
                          description='**Bots Uptime**',
                          colour=discord.Colour(value=0x36393e))
    embed.add_field(name="Days", value=f"{days} Days ", inline=True)
    embed.add_field(name="Hours", value=f"{hours} Hours", inline=True)
    embed.add_field(name="minutes", value=f"{minutes} Minutes", inline=True)
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def hello(ctx):
    await ctx.send("foda fatti")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"{round(error.retry_after, 2)} seconds left")


@client.command()
async def status(ctx):
    activity1 = ctx.author.activities[0].name
    await ctx.send(activity1)


@client.listen('on_message')
async def on_message(message):
    if client.user.mentioned_in(message):
        em = discord.Embed(
            title="",
            description=
            "**<:mochathug:889793675020886016> Type a!help To See The List Of Commands**",
            colour=discord.Colour(value=0x36393e))
        await message.channel.send(embed=em)
        await client.process_commands(message)


buttons = [
    [
        Button(style=ButtonStyle.grey, label='1'),
        Button(style=ButtonStyle.grey, label='2'),
        Button(style=ButtonStyle.grey, label='3'),
        Button(style=ButtonStyle.blue, label='×'),
        Button(style=ButtonStyle.red, label='Exit')
    ],
    [
        Button(style=ButtonStyle.grey, label='4'),
        Button(style=ButtonStyle.grey, label='5'),
        Button(style=ButtonStyle.grey, label='6'),
        Button(style=ButtonStyle.blue, label='÷'),
        Button(style=ButtonStyle.red, label='←')
    ],
    [
        Button(style=ButtonStyle.grey, label='7'),
        Button(style=ButtonStyle.grey, label='8'),
        Button(style=ButtonStyle.grey, label='9'),
        Button(style=ButtonStyle.blue, label='+'),
        Button(style=ButtonStyle.red, label='Clear')
    ],
    [
        Button(style=ButtonStyle.grey, label='00'),
        Button(style=ButtonStyle.grey, label='0'),
        Button(style=ButtonStyle.grey, label='.'),
        Button(style=ButtonStyle.blue, label='-'),
        Button(style=ButtonStyle.green, label='=')
    ],
]
 
#calculates answer
def calculate(exp):
    o = exp.replace('×', '*')
    o = o.replace('÷', '/')
    result = ''
    try:
        result = str(eval(o))
    except:
        result = 'An error occurred.'
    return result
 

@client.command()
async def calc(ctx):
    em = discord.Embed(description="Loading calculator..")
    m = await ctx.send(embed=em)
    expression = 'None'
    delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    e = discord.Embed(
        title=f'{ctx.author.name}\'s calculator | {ctx.author.id}',
        description=expression,
        timestamp=delta)
    await m.edit(components=buttons, embed=e)
    while m.created_at < delta:
        res = await client.wait_for('button_click')
        if res.author.id == int(res.message.embeds[0].title.split(
                '|')[1]) and res.message.embeds[0].timestamp < delta:
            expression = res.message.embeds[0].description
            if expression == 'None' or expression == 'An error occurred.':
                expression = ''
            if res.component.label == 'Exit':
                await res.respond(content='Calculator Closed', type=7)
                await asyncio.sleep(2)
                await m.delete()
                break
            elif res.component.label == '←':
                expression = expression[:-1]
            elif res.component.label == 'Clear':
                expression = 'None'
            elif res.component.label == '=':
                expression = calculate(expression)
            else:
                expression += res.component.label
            f = discord.Embed(
                title=f'{res.author.name}\'s calculator|{res.author.id}',
                description=expression,
                timestamp=delta)
            await res.respond(content='', embed=f, components=buttons, type=7)


def checkForWin(board):
    win = (
        board[0] == board[1] and board[1] == board[2]
        or board[3] == board[4] and board[4] == board[5]
        or board[6] == board[7] and board[7] == board[8]
        or board[0] == board[4] and board[4] == board[8]
        or board[2] == board[4] and board[4] == board[6]
    )
    if not any(i.isdigit() for i in board) and not win:
        return 2
    else:
        return win
    

@client.command()
async def challenge(ctx, user: discord.Member):

    if ctx.author == user:
        await ctx.send(f"{ctx.author.mention} You can't challenge yourself!")
        return
    if user.client:
        await ctx.send(f"{ctx.author.mention} I don't think bot's know how to play tic-tac-toe...")
        return

    components = [
        [Button(style=ButtonStyle.gray,label=str(ia+i)) for ia in range(3)] for i in range(1,9,3)
    ]
    gamemsg = await ctx.send(f'{user.mention}, {ctx.author.name} has challenged thee to tic-tac-toe! You go first.', components=components)

    turn = 'X'
    players = {
        'X': user,
        'O': ctx.author
    }

    def checkEvent(event):
        component = event.component
        if type(component) is not dict:
            component = event.component.to_dict()
        return (
            (component['label'] != 'X' and component['label'] != 'O')
            and event.message.id == gamemsg.id
            and (event.user == players[turn])
        )

    def getButtonStyle(value):
        if value == 'X':
            return ButtonStyle.blue
        elif value == 'O':
            return ButtonStyle.red
        else:
            return ButtonStyle.gray

    while True:
        boardClick = await client.wait_for('button_click', check=checkEvent)
        moveComponent = boardClick.component
        if type(moveComponent) is not dict:
            moveComponent = boardClick.component.to_dict()
        board = [button.label for button in boardClick.message.components]
        squareClicked = board.index(moveComponent["label"])
        board[squareClicked] = turn

        gameWon = checkForWin(board)

        components = [[Button(style=getButtonStyle(board[i+ia-1]),label=board[i+ia-1],disabled=bool(gameWon)) for ia in range(3)] for i in range(1,9,3)]

        if gameWon:
            if gameWon == 2:
                await boardClick.respond(type=7,content=f'Game Over! It is a tie!', components = components)
            else:
                await boardClick.respond(type=7,content=f'Game Over! {players[turn].mention} has won!', components = components)
            break

        if (turn == 'X'):
            turn = 'O'
        else:
            turn = "X"
        
        await boardClick.respond(type=7,content=f"It is {players[turn].mention}'s turn.", components = components) 

@client.listen()
async def  on_command_error(ctx, error):
  error = getattr(error, "original", error)
  if isinstance(error, commands.MissingPermissions):
    embed = discord.Embed(title = "MissingPermissions" , description = f"**{ctx.author} Dont Have The Permission To Run `{ctx.command.name}` Command**")
    await ctx.send(embed =embed)
  elif isinstance(error, commands.MissingRequiredArgument):
     embed = discord.Embed(title = "" , description = "Please enter all the required arguements")
     await ctx.send(embed = embed)
  elif isinstance(error, commands.MemberNotFound):
    await ctx.send("Member not found, Please mention a valid user!")
  elif isinstance(error, commands.BotMissingPermissions):
    await ctx.send("I don't have the permissions to do that!")
  elif isinstance(error, commands.MissingPermissions):
    await ctx.send("I don't have the permissions to do that!")
    
  else:
    raise error




api_key_weather = config["weather_api"]
base_url = "http://api.openweathermap.org/data/2.5/weather?"


@client.command()
async def weather(ctx, *, city: str):

        city_name = city
        complete_url = base_url + "appid=" + api_key_weather + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        channel = ctx.message.channel

        if x["cod"] != "404":

                y = x["main"]
                current_temperature = y["temp"]
                current_temperature_celsiuis = str(round(current_temperature - 273.15))
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]

                embed = discord.Embed(
                    title=f"Weather forecast - {city_name}",
                    color=0x7289DA,
                    timestamp=ctx.message.created_at,
                )
                embed.add_field(
                    name="Description",
                    value=f"**{weather_description}**",
                    inline=False)
                embed.add_field(
                    name="Temperature(C)",
                    value=f"**{current_temperature_celsiuis}°C**",
                    inline=False)
                embed.add_field(
                    name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
                embed.add_field(
                    name="Atmospheric Pressure(hPa)",
                    value=f"**{current_pressure}hPa**",
                    inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}")

                await channel.send(embed=embed)

        else:
                await channel.send(
                    f"There was no results about this place!")

current_language = "en"
@client.command(pass_context=True)
async def wiki(ctx):

    #Load current lang for picture
    global current_language

    #Get user input
    msg = ctx.message.content.split(" ")
    request = msg[2:]
    request = " ".join(request)
    error = None


    try:

        wikicontent = wikipedia.search(request, results=20, suggestion=False) #Wikipedia search request
        print(wikicontent)
        print(" ".join(wikicontent))

        #If there are no results
        if not wikicontent:
            wikicontent ="Sorry, there are no search results for '{}'.".format(request)
            embed = discord.Embed(title="Wikipedia search results:", color=0xe74c3c, description=wikicontent)
            embed.set_thumbnail(url="https://www.wikipedia.org/static/images/project-logos/{}wiki.png".format(current_language))
            await ctx.send(embed=embed)

        #If there are do:
        else:
            embed = discord.Embed(title="Wikipedia search results:", color=0, description="\n".join(wikicontent))
            embed.set_thumbnail(url="https://www.wikipedia.org/static/images/project-logos/{}wiki.png".format(current_language))
            await ctx.send(embed=embed)


    except Exception as error:
        error = str(error)
        await ctx.send("Sorry, a random error occurred. Please try again.")
        print(error)






client.load_extension('jishaku')
client.run(config["token"])
