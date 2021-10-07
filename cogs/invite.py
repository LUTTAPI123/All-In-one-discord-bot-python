import os
import discord
from discord.ext import commands
import asyncio
import random
import DiscordUtils
import discord_components
from discord_components import DiscordComponents, Button, ButtonStyle
from PIL import Image
from io import BytesIO


class Invite(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['inv'])
    async def invite(self, ctx):
        em = discord.Embed(
            title="Invite me!",
            description=
            f"Invite Me In Your Discord Server also Join Our Support Server",
            timestamp=ctx.message.created_at)
        em.set_footer(text=f"Invoked by {ctx.author.name}")
        await ctx.channel.send(
            embed=em,
            components=[
                Button(
                    style=ButtonStyle.URL,
                    label="Invite Me",
                    url=
                    "https://discord.com/oauth2/authorize?client_id=874068763744546908&scope=bot&permissions=854617206"
                ),
                Button(style=ButtonStyle.URL,
                       label="Support server",
                       url="https://discord.gg/YYmKCX6gxT"),
            ],
        )

def setup(client):
    client.add_cog(Invite(client))
    print("Invite Commands Has Been Loaded")