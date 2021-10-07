from aiohttp import helpers
import discord
import random
import asyncio
import io
import datetime
import aiohttp
import pyfiglet
from discord.ext.commands import clean_content

from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ascii(self, ctx, *, text):
        if len(text) > 20:
            return await ctx.send("Your ASCII text exceeded the 20-character limit.")
        
        ascii = pyfiglet.figlet_format(text)

        embed = discord.Embed(title="ASCII", description=f"""
```
{ascii}
```
                              """)

        await ctx.send(embed=embed)

    @commands.command(help="Sends a image of the member you mention but triggered")
    @commands.cooldown(1, 5, BucketType.member)
    async def triggered(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format='png')}") as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "triggered.gif")
                    
                    embed = discord.Embed(title="" , colour=discord.Colour(value=0x36393e))
                    embed.set_image(url="attachment://triggered.gif")

                    await ctx.send(embed=embed, file=file)

    @commands.command(help="Gives the member you mentioned a license to be horny", aliases=['horny_license', 'license_horny'])
    @commands.cooldown(1, 5, BucketType.member)
    async def horny(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/canvas/horny?avatar={member.avatar_url_as(format='png')}") as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "horny.png")

                    embed = discord.Embed(title="" , colour=discord.Colour(value=0x36393e))
                    embed.set_image(url="attachment://horny.png")

                    await ctx.send(embed=embed, file=file)

    @commands.command(help="Gives the member you mentioned a license to be horny", aliases=['go_to_jail', 'in_jail'])
    @commands.cooldown(1, 5, BucketType.member)
    async def jail(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/canvas/jail?avatar={member.avatar_url_as(format='png')}") as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "jail.png")

                    embed = discord.Embed(title="" , colour=discord.Colour(value=0x36393e))
                    embed.set_image(url="attachment://jail.png")

                    await ctx.send(embed=embed, file=file)

    @commands.command(help="Gives the member you mentioned a license to be horny", aliases=['waste'])
    @commands.cooldown(1, 5, BucketType.member)
    async def wasted(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='png')}") as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "wasted.png")

                    embed = discord.Embed(title=f""  , colour=discord.Colour(value=0x36393e))
                    embed.set_image(url="attachment://wasted.png")

                    await ctx.send(embed=embed, file=file)

    @commands.command(help="Gives the member you mentioned a license to be horny", aliases=['pride', 'gay'])
    @commands.cooldown(1, 5, BucketType.member)
    async def rainbow(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format='png')}") as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "gay.png")

                    embed = discord.Embed(title="" , colour=discord.Colour(value=0x36393e))
                    embed.set_image(url="attachment://gay.png")

                    await ctx.send(embed=embed, file=file)

    @commands.command(help="Gives the member you mentioned a license to be horny")
    @commands.cooldown(1, 5, BucketType.member)
    async def glass(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://some-random-api.ml/canvas/glass?avatar={member.avatar_url_as(format='png')}") as af:
                if 300 > af.status >= 200:
                    fp = io.BytesIO(await af.read())
                    file = discord.File(fp, "glass.png")

                    embed = discord.Embed(title="" , colour=discord.Colour(value=0x36393e))
                    embed.set_image(url="attachment://glass.png")
                    
                    await ctx.send(embed=embed, file=file)

    @commands.command(help="Sends a random token of a discord bot", alises=['bottoken', 'random_token', 'random_bot_token'])
    @commands.cooldown(1, 5, BucketType.member)
    async def token(self, ctx):
        async with aiohttp.ClientSession() as session:
            request1 = await session.get('https://some-random-api.ml/bottoken')
            tokenjson = await request1.json()
        embed = discord.Embed(title="Random Bot Token", description=f"{tokenjson['token']}")
        
        await ctx.send(embed=embed)

    @commands.command(help="Shows the size of someones pp!", aliases=['banana', 'eggplant', 'egg_plant'])
    async def pp(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        length = random.randint(10, 25)

        embed = discord.Embed(title=f"PP Size - {member}", description=f"8{'=' * length}D\n{member.name}'s :eggplant: is {length} cm")

        await ctx.send(embed=embed)

    @commands.command(help="Answers with yes or no to your question", aliases=['8ball', 'magicball', 'magic_ball', 'eight_ball'])
    async def eightball(self, ctx, *, question):
        responses = ['It is certain.',
                    'It is decidedly so.',
                    'Without a doubt.',
                    'Yes – definitely.',
                    'You may rely on it.',
                    'As I see it, yes.',
                    'Most likely.',
                    'Outlook good.',
                    'Yes.',
                    'Signs point to yes.',
                    'send hazy, try again.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    'Dont count on it.',
                    'My send is no.',
                    'My sources say no',
                    'Outlook not so good.',
                    'Very doubtful.']

        embed = discord.Embed(title=f"8ball", description=f"""
Question: {question}
Answer: {random.choice(responses)}
                              """)
        
        await ctx.send(embed=embed)

    @commands.command(help="Tells you if someone is a furry or not")
    async def furrydetector(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        responses = ['is a furry.',
                    'is not a furry.']
        
        await ctx.send(f"{member} {random.choice(responses)}")

    @commands.command(help="Tells you how gay someone is")
    async def gayrate(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author

        await ctx.send(f"{member} is {random.randint(0, 100)}% gay!")

    @commands.command(help="Generates a random number", aliases=['rm'])
    async def randomnumber(self, ctx, minimum : int=None, maximum : int=None):
        if minimum == None:
            minimum = 1

        if maximum == None:
            maximum = 10

        if maximum > 1000000:
            return await ctx.send("Number cannot be more than `1000000`.")

        number = random.randint(minimum, maximum)

        await ctx.send(f"Randomly generated number between `{minimum}` and `{maximum}`: `{number}`")

    @commands.command(help="Generates a random word", aliases=['rw'])
    async def randomword(self, ctx):
        with open("./data/verifyWords.txt", "r") as file:
            allText = file.read()
            wordsList = list(map(str, allText.split()))

        randomWord = random.choice(wordsList)

        await ctx.send(f"Here's a randomly generated word: `{randomWord}`")






        


    @commands.command(help="OOF's the person you mentioned", aliases=['commitoof', 'commit_oof'])
    async def oof(self, ctx, member : discord.Member=None):
        if member == None or member == ctx.author:
            responses = [f"{ctx.author.name} was killed in Electrical.",
            f"{ctx.author.name} failed math.",
            f"{ctx.author.name} rolled down a large hill.",
            f"{ctx.author.name} cried to death.",
            f"{ctx.author.name} smelt their own socks.",
            f"{ctx.author.name} forgot to stop texting while driving. Don't text and drive, kids.",
            f"{ctx.author.name} said Among Us in a public chat.",
            f"{ctx.author.name} stubbed their toe.",
            f"{ctx.author.name} forgot to grippen their shoes when walking down the stairs.",
            f"{ctx.author.name} wasn't paying attention and stepped on a mine.",
            f"{ctx.author.name} held a grenade for too long.",
            f"{ctx.author.name} got pwned by a sweaty tryhard.",
            f"{ctx.author.name} wore a black shirt in the summer.",
            f"{ctx.author.name} burned to a crisp.",
            f"{ctx.author.name} choked on a chicken nugget.",
            f"{ctx.author.name} forgot to look at the expiration date on the food.",
            f"{ctx.author.name} ran into a wall.",
            f"{ctx.author.name} shook a vending machine too hard.",
            f"{ctx.author.name} was struck by lightning.",
            f"{ctx.author.name} chewed 5 gum.",
            f"{ctx.author.name} ate too many vitamin gummy bears.",
            f"{ctx.author.name} tried to swim in lava. Why would you ever try to do that?"]
            return await ctx.send(f"{random.choice(responses)}")
        
        else:
            responses = [f"{ctx.author.name} exploded {member.name}.",
                        f"{ctx.author.name} shot {member.name}.",
                        f"{ctx.author.name} went ham on {member.name}.",
                        f"{ctx.author.name} betrayed and killed {member.name}.",
                        f"{ctx.author.name} sent {member.name} to Davy Jones' locker.",
                        f"{ctx.author.name} no scoped {member.name}.",
                        f"{ctx.author.name} said no u and killed {member.name}.",
                        f"{ctx.author.name} blew up {member.name} with a rocket.",
                        f"{ctx.author.name} pushed {member.name} off a cliff.",
                        f"{ctx.author.name} stabbed {member.name} to death.",
                        f"{ctx.author.name} slammed {member.name} with a chair.",
                        f"{ctx.author.name} recited a magic spell and killed {member.name}.",
                        f"{ctx.author.name} electrified {member.name}.",
                        f"{member.name} was slain by {ctx.author.name}.",
                        f"{ctx.author.name} burnt {member.name} alive.",
                        f"{ctx.author.name} buried {member.name}.",
                        f"{ctx.author.name} shoved {member.name}'s head underwater for too long.",
                        f"{ctx.author.name} slid a banana peel under {member.name}'s feet. They tripped and died...",
                        f"{ctx.author.name} got a headshot on {member.name}.",
                        f"{ctx.author.name} said a hilarious joke to {member.name} and died.",
                        f"{ctx.author.name} showed old Vicente0670 videos to {member.name} and died of cringe.",
                        f"{ctx.author.name} didn't buy Panda Express for {member.name} and exploded.",
                        f"{ctx.author.name} sent {member.name} to the Nether.",
                        f"{ctx.author.name} tossed {member.name} off an airplane.",
                        f"{ctx.author.name} broke {member.name}'s neck."]

            await ctx.send(f"{random.choice(responses)}")


    @commands.command()
    async def ship(self, ctx, name1 : clean_content, name2 : clean_content):
        shipnumber = random.randint(0,100)
        if 0 <= shipnumber <= 10:
            status = "Really low! {}".format(random.choice(["Friendzone ;(", 
                                                            'Just "friends"', 
                                                            '"Friends"', 
                                                            "Little to no love ;(", 
                                                            "There's barely any love ;("]))
        elif 10 < shipnumber <= 20:
            status = "Low! {}".format(random.choice(["Still in the friendzone", 
                                                     "Still in that friendzone ;(", 
                                                     "There's not a lot of love there... ;("]))
        elif 20 < shipnumber <= 30:
            status = "Poor! {}".format(random.choice(["But there's a small sense of romance from one person!", 
                                                     "But there's a small bit of love somewhere", 
                                                     "I sense a small bit of love!", 
                                                     "But someone has a bit of love for someone..."]))
        elif 30 < shipnumber <= 40:
            status = "Fair! {}".format(random.choice(["There's a bit of love there!", 
                                                      "There is a bit of love there...", 
                                                      "A small bit of love is in the air..."]))
        elif 40 < shipnumber <= 60:
            status = "Moderate! {}".format(random.choice(["But it's very one-sided OwO", 
                                                          "It appears one sided!", 
                                                          "There's some potential!", 
                                                          "I sense a bit of potential!", 
                                                          "There's a bit of romance going on here!", 
                                                          "I feel like there's some romance progressing!", 
                                                          "The love is getting there..."]))
        elif 60 < shipnumber <= 70:
            status = "Good! {}".format(random.choice(["I feel the romance progressing!", 
                                                      "There's some love in the air!", 
                                                      "I'm starting to feel some love!"]))
        elif 70 < shipnumber <= 80:
            status = "Great! {}".format(random.choice(["There is definitely love somewhere!", 
                                                       "I can see the love is there! Somewhere...", 
                                                       "I definitely can see that love is in the air"]))
        elif 80 < shipnumber <= 90:
            status = "Over average! {}".format(random.choice(["Love is in the air!", 
                                                              "I can definitely feel the love", 
                                                              "I feel the love! There's a sign of a match!", 
                                                              "There's a sign of a match!", 
                                                              "I sense a match!", 
                                                              "A few things can be imporved to make this a match made in heaven!"]))
        elif 90 < shipnumber <= 100:
            status = "True love! {}".format(random.choice(["It's a match!", 
                                                           "There's a match made in heaven!", 
                                                           "It's definitely a match!", 
                                                           "Love is truely in the air!", 
                                                           "Love is most definitely in the air!"]))

        if shipnumber <= 33:
            shipColor = 0xE80303
        elif 33 < shipnumber < 66:
            shipColor = 0xff6600
        else:
            shipColor = 0x3be801

        emb = (discord.Embed(color=shipColor, \
                             title="Love test for:", \
                             description="**{0}** and **{1}** {2}".format(name1, name2, random.choice([
                                                                                                        ":sparkling_heart:", 
                                                                                                        ":heart_decoration:", 
                                                                                                        ":heart_exclamation:", 
                                                                                                        ":heartbeat:", 
                                                                                                        ":heartpulse:", 
                                                                                                        ":hearts:", 
                                                                                                        ":blue_heart:", 
                                                                                                        ":green_heart:", 
                                                                                                        ":purple_heart:", 
                                                                                                        ":revolving_hearts:", 
                                                                                                        ":yellow_heart:", 
                                                                                                        ":two_hearts:"]))))
        emb.add_field(name="Results:", value=f"{shipnumber}%", inline=True)
        emb.add_field(name="Status:", value=(status), inline=False)
        emb.set_author(name="Shipping", icon_url="http://moziru.com/images/kopel-clipart-heart-6.png")
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Fun(client))
