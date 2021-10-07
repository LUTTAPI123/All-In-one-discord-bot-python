import discord
from discord.ext import commands
import random
from datetime import datetime


class Modmail(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.last_timeStamp = datetime.utcfromtimestamp(0)

    @commands.command()
    async def dm(self, ctx, user: discord.Member, *, mesg):
        try:
            await user.send(f"{mesg}")
            em = discord.Embed(
                title="DM Succesfull",
                description=f"Succesfully Sended The messgae to {user.name}")
            await ctx.send(embed=em)
        except:
            await ctx.channel.send(f"Cannot DM {user.name} ")

    @commands.Cog.listener()
    @commands.dm_only()
    async def on_message(self, message: discord.Message):

        if message.author.bot:
            return

        else:
            if message.channel == message.author.dm_channel:
                self.channel_id = 883919903688622100
                self.modmail_channel = self.client.get_channel(self.channel_id)
                embed = discord.Embed(title=f"Modmail From `{message.author}`",
                                      description=f"{message.content}",
                                      color=0x2c2f33)
                if message.attachments:
                    embed.set_image(url=message.attachments[0].url)
                embed.set_footer(text=f'ID: {message.author.id}')

                await self.modmail_channel.send(embed=embed)
                self.last_timeStamp = datetime.utcnow()

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def report(self, ctx, *, msg):
        try:
          await ctx.message.delete()

          channel = self.client.get_channel(885065974540292166)

          embed = discord.Embed(colour=discord.Colour.from_rgb(255, 255, 0))

          embed.add_field(name=f'__**Report:**__',
                          value=f"<@{ctx.author.id}> Reported:",
                          inline=False)
          embed.add_field(name=msg, value="­")
          embed.set_footer(text=f"ID: {ctx.message.author.id}")

          await channel.send(embed=embed)
          await ctx.author.send(
              "Your report has been sent successfully! Action will be taken accordingly."
          )
        except:
              ctx.send('error ')



def setup(client):
    client.add_cog(Modmail(client))
    print("ModMail  Commands Has Been Loaded")
