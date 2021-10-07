import datetime
import os
import discord
from datetime import datetime, timedelta
from discord.ext import commands
import asyncio
import time



class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @property
    def reactions(self):
        return {
            1: '1️⃣',
            2: '2️⃣',
            3: '3️⃣',
            4: '4️⃣',
            5: '5️⃣',
            6: '6️⃣',
            7: '7️⃣',
            8: '8️⃣',
            9: '9️⃣',
            10: '🔟'
        }

    @commands.command()
    async def ping(self, ctx):
        latency = self.client.latency
        truelatency = latency * 1000
        embed = discord.Embed(
            description=
            f"**<a:latency:890627299131678782> Pong ! The latency Is **`{round(truelatency)}`** ms**",
            colour=discord.Colour(value=0x36393e))
        await ctx.send(embed=embed)

    @commands.command(aliases=["suggestion", "suggest"])
    async def poll(self, ctx, *, suggestion: str):
        await ctx.message.delete()
        embed = discord.Embed(description=suggestion , colour=discord.Colour(value=0x36393e))
        embed.set_author(name=f"Poll by {ctx.author.display_name}",
                         icon_url=ctx.author.avatar_url)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        user = payload.member
        if user.bot: return
        msg = await self.client.get_guild(payload.guild_id).get_channel(
            payload.channel_id).fetch_message(payload.message_id)
        emoji = payload.emoji
        users = []
        if msg.author.bot and ("👍" and "👎") in [str(i) for i in msg.reactions]:
            for react in msg.reactions:
                if str(react) == "👍":
                    async for reactor in react.users():
                        if reactor.bot: continue
                        if reactor in users:
                            await msg.remove_reaction(emoji, user)
                            return
                        users.append(reactor)
                elif str(react) == "👎":
                    async for reactor in react.users():
                        if reactor.bot: continue
                        if reactor in users:
                            await msg.remove_reaction(emoji, user)
                            return
                    return

    @commands.command()
    async def multi_choice(self, ctx, desc: str, *choices):
        await ctx.message.delete()

        if len(choices) < 2:
            ctx.command.reset_cooldown(ctx)
            if len(choices) == 1:
                return await ctx.send("Can't make a poll with only one choice")
            return await ctx.send(
                "You have to enter two or more choices to make a poll")

        if len(choices) > 10:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send(
                "You can't make a poll with more than 10 choices")

        embed = discord.Embed(
            description=f"**{desc}**\n\n" +
            "\n\n".join(f"{str(self.reactions[i])}  {choice}"
                        for i, choice in enumerate(choices, 1)),
            timestamp=datetime.datetime.utcnow(),
            color=discord.colour.Color.gold())
        embed.set_footer(text=f"Poll by {str(ctx.author)}")
        msg = await ctx.send(embed=embed)
        for i in range(1, len(choices) + 1):
            await msg.add_reaction(self.reactions[i])


    @commands.command(aliases=["av", "pfp"])
    async def avatar(self, ctx, *, member: discord.Member = None):
        if not member: member = ctx.message.author

        message = discord.Embed(title=str(member),
                                colour=discord.Colour(value=0x36393e))
        message.set_image(url=member.avatar_url)

        await ctx.send(embed=message)

    @commands.command()
    @commands.is_owner()
    @commands.has_permissions(kick_members=True)
    async def say(self, ctx, *, say):
        await ctx.message.delete()
        sayembed = discord.Embed(description=f"{say}", colour=discord.Colour(value=0x36393e))
        await ctx.send(embed=sayembed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def ann(self, ctx, channel: discord.TextChannel, title, *, text):
        em = discord.Embed(title=f"{title}",
                           description=f"{text}",
                           timestamp=ctx.message.created_at,
                           colour=discord.Colour(value=0x36393e))
        em.set_image(
            url=
            "https://media.discordapp.net/attachments/559357612068700183/566999873430355968/13-26-52-nitro_1.gif"
        )
        em.set_thumbnail(url=f"{ctx.guild.icon_url}")
        em.set_footer(text=f"By moderator {ctx.author.name}",
                      icon_url=f"{ctx.author.avatar_url}")
        await channel.send(embed=em)



    @commands.command(aliases=["stats", "activity", "messages"])
    async def check(self,
                    ctx,
                    timeframe=7,
                    channel: discord.TextChannel = None,
                    *,
                    user: discord.Member = None):
        if timeframe > 1968:
            await ctx.channel.send(
                "Sorry. The maximum of days you can check is 1968.")
        elif timeframe <= 0:
            await ctx.channel.send(
                "Sorry. The minimum of days you can check is one.")

        else:
            if not channel:
                channel = ctx.channel
            if not user:
                user = ctx.author

            async with ctx.channel.typing():
                msg = await ctx.channel.send('Calculating...')
                await msg.add_reaction('🔎')

                counter = 0
                async for message in channel.history(
                        limit=5000,
                        after=datetime.today() - timedelta(days=timeframe)):
                    if message.author.id == user.id:
                        counter += 1

                await msg.remove_reaction('🔎', member=message.author)

                if counter >= 5000:
                    await msg.edit(
                        content=
                        f'{user} has sent over 5000 messages in the channel "{channel}" within the last {timeframe} days!'
                    )
                else:
                    await msg.edit(
                        content=
                        f'{user} has sent {str(counter)} messages in the channel "{channel}" within the last {timeframe} days.'
                    )


def setup(client):
    client.add_cog(General(client))
    print("General Commands Has Been Loaded")
