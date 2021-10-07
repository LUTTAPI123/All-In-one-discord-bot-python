from aiohttp import helpers
import discord
import random
import asyncio
import io
import datetime
import aiohttp
import pyfiglet
from discord.ext.commands import clean_content
from discord.ext import *
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType


class Gifff(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(help="Let's you hug someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def hug(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't hug yourself!")
            
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/hug')
            json = await request.json()

        embed = discord.Embed(title="", colour=discord.Colour(value=0x36393e))
        embed.set_image(url=json['url'])
        
        await ctx.send(embed=embed)

    @commands.command(help="Let's you pat someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def pat(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't pat yourself!")
            
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/pat')
            json = await request.json()

        embed = discord.Embed(title="" , colour=discord.Colour(value=0x36393e))
        embed.set_image(url=json['url'])
        
        await ctx.send(embed=embed)
        
    @commands.command(help="Let's you kiss someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def kiss(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't kiss yourself!")
            
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/kiss')
            json = await request.json()

        embed = discord.Embed(title="", colour=discord.Colour(value=0x36393e))
        embed.set_image(url=json['url'])
        
        await ctx.send(embed=embed)

        
    @commands.command(help="Let's you lick someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def lick(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't lick yourself!")
            
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/lick')
            json = await request.json()

        embed = discord.Embed(title="" , colour=discord.Colour(value=0x36393e))
        embed.set_image(url=json['url'])
        
        await ctx.send(embed=embed)
        
    @commands.command(help="Let's you bonk someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def bonk(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't bonk yourself!")
            
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/bonk')
            json = await request.json()

        embed = discord.Embed(title='' , colour=discord.Colour(value=0x36393e))
        embed.set_image(url=json['url'])
        
        await ctx.send(embed=embed)
        
    @commands.command(help="Let's you yeet someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def yeet(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't yeet yourself!")

        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/yeet')
            json = await request.json()

        embed = discord.Embed(title="" , colour=discord.Colour(value=0x36393e))
        embed.set_image(url=json['url'])
        
        await ctx.send(embed=embed)
        
    @commands.command(help="Let's you wave at someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def wave(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't hug yourself!")

        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/wave')
            json = await request.json()

        embed = discord.Embed(title='' , colour=discord.Colour(value=0x36393e))
        embed.set_image(url=json['url'])
        
        await ctx.send(embed=embed)
        
    @commands.command(help="Let's you high five someone!", aliases=['high_five'])
    @commands.cooldown(1, 5, BucketType.member)
    async def highfive(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't high five yourself!")

        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/highfive')
            json = await request.json()

        embed = discord.Embed(title="" , colour=discord.Colour(value=0x36393e))
        embed.set_image(url=json['url'])
        
        await ctx.send(embed=embed)

    @commands.command(help="Let's you bite someone!")
    @commands.cooldown(1, 5, BucketType.member)
    async def bite(self, ctx, member : discord.Member=None):
        if member == None:
            if ctx.message.reference:
                member = ctx.message.reference.resolved.author
            else:
                member = ctx.author
                return await ctx.send("You can't bite yourself!")

        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.pics/sfw/bite')
            json = await request.json()

        embed = discord.Embed(title="" , colour=discord.Colour(value=0x36393e) )
        embed.set_image(url=json['url'])
        
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Gifff(client))
