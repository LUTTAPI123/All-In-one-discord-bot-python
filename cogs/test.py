import discord, random, operator
from discord.ext import commands
from contextlib import redirect_stdout
import textwrap
import traceback
import io
import asyncio
import functools
import aiohttp
import unicodedata
from datetime import datetime

class WhosPlaying(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()


    @commands.command(no_pm=True)
    async def game(self, ctx, *, game):
        """Shows who's playing a specific game"""
        if len(game) <= 1:
            await ctx.send("```The game should be at least 2 characters long...```", delete_after=5.0)
            return

        guild = ctx.message.guild
        members = guild.members
        playing_game = ""
        count_playing = 0

        for member in members:
            if not member:
                continue
            if not member.activity or not member.activity.name:
                continue
            if member.bot:
                continue
            if game.lower() in member.activity.name.lower():
                count_playing += 1
                if count_playing <= 15:
                    emote = random.choice([":trident:", ":high_brightness:", ":low_brightness:", ":beginner:", ":diamond_shape_with_a_dot_inside:"])
                    playing_game += f"{emote} {member.name} ({member.activity.name})\n"

        if playing_game == "":
            await ctx.send("```Search results:\nNo users are currently playing that game.```")
        else:
            msg = playing_game
            if count_playing > 15:
                showing = "(Showing 15/{})".format(count_playing)       
            else:
                showing = "({})".format(count_playing)

            em = discord.Embed(description=msg, colour=discord.Colour(value=0x36393e))
            em.set_author(name=f"""Who's playing "{game}"? {showing}""")
            await ctx.send(embed=em)

    @commands.command(no_pm=True)
    async def currentgames(self, ctx):
        guild = ctx.message.guild
        members = guild.members

        freq_list = {}
        for member in members:
            if not member:
                continue
            if not member.activity or not member.activity.name:
                continue
            if member.bot:
                continue
            if member.activity.name not in freq_list:
                freq_list[member.activity.name] = 0
            freq_list[member.activity.name] += 1

        sorted_list = sorted(freq_list.items(),
                             key=operator.itemgetter(1),
                             reverse=True)

        if not freq_list:
            await ctx.send("```Search results:\nNo users are currently playing any games. Odd...```")
        else:
            # Create display and embed
            msg = ""
            max_games = min(len(sorted_list), 10)

            em = discord.Embed(description=msg, colour=discord.Colour(value=0x36393e))
            for i in range(max_games):
                game, freq = sorted_list[i]
                if int(freq_list[game]) < 2:
                    amount = "1 person"
                else:
                    amount = f"{int(freq_list[game])} people"
                em.add_field(name=game, value=amount)
            em.set_thumbnail(url=guild.icon_url)
            em.set_footer(text="Do a!game <game> to see whos playing a specific game")
            em.set_author(name="Top games being played right now in the server:")
            await ctx.send(embed=em)

    @commands.command(aliases=['ui'])
    async def userinfo(self, ctx, user: discord.Member = None):
        '''Get user info for yourself or someone in the guild'''
        user = user or ctx.message.author
        guild = ctx.message.guild
        guild_owner = guild.owner
        avi = user.avatar_url
        roles = sorted(user.roles, key=lambda r: r.position)

        for role in roles:
            if str(role.color) != '#000000':
                color = role.color
        if 'color' not in locals():
            color = 0

        rolenames = ', '.join([r.name for r in roles if r != '@everyone']) or 'None'
        time = ctx.message.created_at
        desc = f'{user.name} is currently in {user.status} mode.'
        member_number = sorted(guild.members, key=lambda m: m.joined_at).index(user) + 1
        em = discord.Embed(color=color, description=desc, timestamp=time)
        em.add_field(name='Name', value=user.name),
        em.add_field(name='Member Number', value=member_number),
        em.add_field(name='Account Created', value=user.created_at.__format__('%A, %B %d, %Y')),
        em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %B %d, %Y')),
        em.add_field(name='Roles', value=rolenames)
        em.set_thumbnail(url=avi or None)
        await ctx.send(embed=em)




    @commands.command()
    async def screenshot(self, ctx, url):
          async with self.client.session.get(f'https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/{url}') as r:
              res = await r.read()

          embed = discord.Embed(title=f"Screenshot of {url}")
          embed.set_footer(text=f"Command requested by {ctx.author}", icon_url=ctx.author.avatar.url)
          embed.set_image(url="attachment://ss.png")

          if "ip" in url.lower() or "test" in url.lower() or "speed" in url.lower() or "address" in url.lower():
              await ctx.send("no.")
          else:
              await ctx.send(embed=embed, file=discord.File(io.BytesIO(res), filename="ss.png"))


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.NotOwner):
            embed = discord.Embed(title='',
                              description=f"**<:wtf:890616531392811069> You Must Own `{ctx.me.display_name}` To Use `{ctx.command}`**",
                              colour=discord.Colour(value=0x36393e))
            return await ctx.send(embed=embed)


    @commands.command(name="serverinfo", aliases=["guildinfo", "si", "gi"])
    async def server_info(self, ctx):
        embed = discord.Embed(title="Server information",
                      colour=ctx.guild.owner.colour,
                      timestamp=datetime.utcnow())

        embed.set_thumbnail(url=ctx.guild.icon_url)

        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

        fields = [("ID", ctx.guild.id, True),
                  ("Owner", ctx.guild.owner, True),
                  ("Region", ctx.guild.region, True),
                  ("Created at", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                  ("Members", len(ctx.guild.members), True),
                  ("Humans", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
                  ("Bots", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
                  ("Banned members", len(await ctx.guild.bans()), True),
                  ("Statuses", f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}", True),
                  ("Text channels", len(ctx.guild.text_channels), True),
                  ("Voice channels", len(ctx.guild.voice_channels), True),
                  ("Categories", len(ctx.guild.categories), True),
                  ("Roles", len(ctx.guild.roles), True),
                  ("Invites", len(await ctx.guild.invites()), True),
                  ("\u200b", "\u200b", True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)      
def setup(client):
    client.add_cog(WhosPlaying(client))
    print("Test Commands Has Been Loaded")