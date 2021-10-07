import os
import discord
from discord.ext import commands
import asyncio

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def lock(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        role = ctx.guild.default_role

        if role not in channel.overwrites:
            overwrites = {
                role: discord.PermissionOverwrite(send_messages=False)
            }
            await channel.edit(overwrites=overwrites)
            if ctx.channel != channel:
                await ctx.send(f"I have put {channel.mention} on lockdown.")
            else:
                await ctx.message.delete()
            await channel.send(
                embed=discord.Embed(title="This channel is now under lockdown",
                                    color=discord.Colour.orange()))
        elif channel.overwrites[role].send_messages is True or \
                channel.overwrites[role].send_messages is None:
            overwrites = channel.overwrites[role]
            overwrites.send_messages = False
            await channel.set_permissions(role, overwrite=overwrites)
            if ctx.channel != channel:
                await ctx.send(f"I have put {channel.mention} on lockdown.")
            else:
                await ctx.message.delete()
            await channel.send(embed=discord.Embed(
                title="This channel is now under lockdown.",
                color=discord.Colour.orange()))
        else:
            overwrites = channel.overwrites[role]
            overwrites.send_messages = True
            await channel.set_permissions(role, overwrite=overwrites)
            if ctx.channel != channel:
                await ctx.send(
                    f"I have removed {channel.mention} from lockdown.")
            else:
                await ctx.message.delete()
            await channel.send(embed=discord.Embed(
                title="This channel is no longer under lockdown.",
                color=discord.Colour.orange()))

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def clear(self, ctx, amount: int = 5 ):
        await ctx.channel.purge(limit=amount)
        await ctx.channel.send(f'**`{amount}`** **Messages Has Been Cleared !** :ballot_box_with_check:')
        await ctx.message.delete()



    
    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self,
                   context,
                   member: discord.Member,
                   *,
                   reason="Not specified"):
        """
        Kick a user out of the server.
        """
        if member.guild_permissions.administrator:
            embed = discord.Embed(title="Error!",
                                  description="User has Admin permissions.",
                                  color=0xE02B2B)
            await context.send(embed=embed)
        else:
            try:
                await member.kick(reason=reason)
                embed = discord.Embed(
                    title="User Kicked!",
                    description=
                    f"**{member}** was kicked by **{context.message.author}**!",
                    color=0x42F56C)
                embed.add_field(name="Reason:", value=reason)
                await context.send(embed=embed)
                try:
                    await member.send(
                        f"You were kicked by **{context.message.author}**!\nReason: {reason}"
                    )
                except:
                    pass
            except:
                embed = discord.Embed(
                    title="Error!",
                    description=
                    "An error occurred while trying to kick the user. Make sure my role is above the role of the user you want to kick.",
                    color=0xE02B2B)
                await context.message.channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, context, member: discord.Member, *, nickname=None):
        try:
            await member.edit(nick=nickname)
            embed = discord.Embed(
                title="Changed Nickname!",
                description=f"**{member}'s** new nickname is **{nickname}**!",
                color=0x42F56C)
            await context.send(embed=embed)
        except:
            embed = discord.Embed(
                title="Error!",
                description=
                "An error occurred while trying to change the nickname of the user. Make sure my role is above the role of the user you want to change the nickname.",
                color=0xE02B2B)
            await context.message.channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,
                  context,
                  member: discord.Member,
                  *,
                  reason="Not specified"):
        try:
            if member.guild_permissions.administrator:
                embed = discord.Embed(
                    title="Error!",
                    description="User has Admin permissions.",
                    color=0xE02B2B)
                await context.send(embed=embed)
            else:
                await member.ban(reason=reason)
                embed = discord.Embed(
                    title="User Banned!",
                    description=
                    f"**{member}** was banned by **{context.message.author}**!",
                    color=0x42F56C)
                embed.add_field(name="Reason:", value=reason)
                await context.send(embed=embed)
                await member.send(
                    f"You were banned by **{context.message.author}**!\nReason: {reason}"
                )
        except:
            embed = discord.Embed(
                title="Error!",
                description=
                "An error occurred while trying to ban the user. Make sure my role is above the role of the user you want to ban.",
                color=0xE02B2B)
            await context.send(embed=embed)



    @commands.command()
    async def testing(ctx):
        await ctx.send("working")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name,
                                                   member_discriminator):

                embed = discord.Embed(title="Unbanned Member ",
                                      description=f"{user} has been unbanned.")
                await ctx.guild.unban(user)
                await ctx.send(embed=embed)


    @commands.command(aliases=['slowmo'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, seconds: int=0):
        if seconds > 120:
            return await ctx.send(":no_entry: Amount can't be over 120 seconds")
        if seconds is 0:
            await ctx.channel.edit(slowmode_delay=seconds)
            a = await ctx.send("**Slowmode is off for this channel**")
            await a.add_reaction("☑️")
        else:
            if seconds is 1:
                numofsecs = "second"
            else:    
                numofsecs = "seconds"
            await ctx.channel.edit(slowmode_delay=seconds)
            embed = discord.Embed(title= 'SlowMode' , description = f"**Set the channel slow mode delay to `{seconds}` {numofsecs}\nTo turn this off, do a!slowmode**", colour=discord.Colour(value=0x36393e))
            confirm = await ctx.send(embed = embed)
            await confirm.add_reaction
            ("☑️")


    @commands.guild_only()
    @commands.bot_has_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def giverole(self, ctx, user : discord.Member, *, role : discord.Role):
        if ctx.author.top_role > user.top_role or ctx.author == ctx.guild.owner:
            await user.add_roles(role)
            em = discord.Embed(title = "" , description = f"**Gave {user.mention} `{role}`**", colour=discord.Colour(value=0x36393e) )
            msg = await ctx.send(embed = em)
            await msg.add_reaction("☑️")

    @commands.guild_only()
    @commands.bot_has_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def removerole(self, ctx, user : discord.Member, *, role : discord.Role):
        if ctx.author.top_role >= user.top_role or ctx.author == ctx.guild.owner:
            await user.remove_roles(role)
            em = discord.Embed(title = "" , description = f"**Ok, `{role}` was removed from {user.mention}**" , colour=discord.Colour(value=0x36393e))
            msg = await ctx.send(embed = em)
            await msg.add_reaction("☑️")





    @commands.command(aliases=['role'])
    async def roleinfo(self, ctx, *, rolename):
        '''Get information about a role. Case Sensitive!'''
        try:
            role = discord.utils.get(ctx.message.guild.roles, name=rolename)
        except:
            return await ctx.send(f"Role could not be found. The system IS case sensitive!")

        em = discord.Embed(description=f'Role ID: {str(role.id)}', color=role.color or discord.Color.green())
        em.title = role.name
        perms = ""
        if role.permissions.administrator:
            perms += "Administrator, "
        if role.permissions.create_instant_invite:
            perms += "Create Instant Invite, "
        if role.permissions.kick_members:
            perms += "Kick Members, "
        if role.permissions.ban_members:
            perms += "Ban Members, "
        if role.permissions.manage_channels:
            perms += "Manage Channels, "
        if role.permissions.manage_guild:
            perms += "Manage Guild, "
        if role.permissions.add_reactions:
            perms += "Add Reactions, "
        if role.permissions.view_audit_log:
            perms += "View Audit Log, "
        if role.permissions.read_messages:
            perms += "Read Messages, "
        if role.permissions.send_messages:
            perms += "Send Messages, "
        if role.permissions.send_tts_messages:
            perms += "Send TTS Messages, "
        if role.permissions.manage_messages:
            perms += "Manage Messages, "
        if role.permissions.embed_links:
            perms += "Embed Links, "
        if role.permissions.attach_files:
            perms += "Attach Files, "
        if role.permissions.read_message_history:
            perms += "Read Message History, "
        if role.permissions.mention_everyone:
            perms += "Mention Everyone, "
        if role.permissions.external_emojis:
            perms += "Use External Emojis, "
        if role.permissions.connect:
            perms += "Connect to Voice, "
        if role.permissions.speak:
            perms += "Speak, "
        if role.permissions.mute_members:
            perms += "Mute Members, "
        if role.permissions.deafen_members:
            perms += "Deafen Members, "
        if role.permissions.move_members:
            perms += "Move Members, "
        if role.permissions.use_voice_activation:
            perms += "Use Voice Activation, "
        if role.permissions.change_nickname:
            perms += "Change Nickname, "
        if role.permissions.manage_nicknames:
            perms += "Manage Nicknames, "
        if role.permissions.manage_roles:
            perms += "Manage Roles, "
        if role.permissions.manage_webhooks:
            perms += "Manage Webhooks, "
        if role.permissions.manage_emojis:
            perms += "Manage Emojis, "

        if perms is None:
            perms = "None"
        else:
            perms = perms.strip(", ")

        em.add_field(name='Hoisted', value=str(role.hoist))
        em.add_field(name='Position from bottom', value=str(role.position))
        em.add_field(name='Managed by Integration', value=str(role.managed))
        em.add_field(name='Mentionable', value=str(role.mentionable))
        em.add_field(name='People in this role', value=str(len(role.members)))

        pages = []
        pages.append(em)

        em2 = discord.Embed(description=f'Role ID: {str(role.id)}', color=role.color or discord.Color.green())
        em2.title = role.name
        em2.add_field(name='Permissions', value=perms)

        pages.append(em2)

        thing = str(role.created_at.__format__('%A, %B %d, %Y'))

        p_session = PaginatorSession(ctx, footer=f'Created At: {thing}', pages=pages)
        await p_session.run()

def setup(client):
    client.add_cog(Moderation(client))
    print("Moderation Commands Has Been Loaded")
