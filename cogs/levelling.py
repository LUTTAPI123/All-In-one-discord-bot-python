from googletrans import Translator
import discord
from discord.ext import commands
import asyncio
import datetime
tl = Translator()
class tlate(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def tlate(self,ctx,desti,*,args):
        res = tl.translate(args,dest=desti)
        translated = res.text
        source = res.src
        destination = res.dest
        pronun = res.pronunciation
        embed = discord.Embed(
            title = 'Translate',
            description = f'Translated from {source} to {destination}',
            colour = ctx.author.top_role.colour
        )
        embed.add_field(name='Query',value = args,inline= False)
        embed.add_field(name='Result',value = translated,inline=False)
        if (str(pronun) != 'None'):
            embed.add_field(name = 'Pronunciation',value = pronun,inline=False)
        embed.set_footer(text='Powered by Google Translate')
        await ctx.send(embed = embed)
    @commands.command()
    async def dtect(self,ctx,*args):
        query = " ".join(args)
        res = tl.detect(query)
        dtlang = res.lang
        conf = res.confidence
        rconf = round(int(conf)*100,2)
        embed = discord.Embed(
            title = 'Detect',
            description = f'Query is in {dtlang}',
            colour = ctx.author.top_role.colour
        )
        embed.add_field(name='Confidence',value = rconf + '%' ,inline= False)
        embed.set_footer(text='Powered by Google Translate')
        await ctx.send(embed = embed)
def setup(client):
    client.add_cog(tlate(client))