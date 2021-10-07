import time
import discord
import psutil
import os
import sys
from datetime import datetime
from discord.ext import commands
import default


class Public(commands.Cog, name='Ranks'):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def about(self, ctx):
        ramUsage = psutil.Process().memory_full_info().uss / 1024 ** 2
        avgmembers = round(len(self.client.users) / len(self.client.guilds))
        cpu_usage = psutil.cpu_percent()

        embedColour = discord.Embed.Empty
        if hasattr(ctx, 'guild') and ctx.guild is not None:
            embedColour = ctx.me.top_role.colour

        embed = discord.Embed(colour=embedColour)
        embed.add_field(name="Library", value="discord.py", inline=True)
        embed.add_field(name="RAM", value=f"{ramUsage:.2f} MB", inline=True)
        embed.add_field(name="RAM", value=f"{cpu_usage}", inline=True)

        await ctx.send( embed=embed)
    @commands.command()
    @commands.is_owner()
    async def reloadall(self, ctx):
        """ Reloads all extensions. """
        error_collection = []
        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                name = file[:-3]
                try:
                    self.client.reload_extension(f"cogs.{name}")
                except Exception as e:
                    error_collection.append(
                        [file, default.traceback_maker(e, advance=False)]
                    )

        if error_collection:
            output = "\n".join([f"**{g[0]}** ```diff\n- {g[1]}```" for g in error_collection])
            return await ctx.send(
                f"Attempted to reload all extensions, was able to reload, "
                f"however the following failed...\n\n{output}"
            )

        await ctx.send("Successfully reloaded all extensions")

    @commands.command()
    @commands.is_owner()
    async def reboot(self, ctx):
        """ Reboot the client """
        await ctx.send('Rebooting now...')
        time.sleep(1)
        sys.exit(0)

def setup(client):
    client.add_cog(Public(client))
    print('Public is Loaded')