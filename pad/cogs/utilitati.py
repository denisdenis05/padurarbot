import discord
import random
import json
import datetime
from discord.ext import commands
from datetime import datetime


class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client




    @commands.command(aliases=['vocal'])
    @commands.cooldown(2, 15, commands.BucketType.user)
    async def voice(self, ctx, comanda, *, numar=None):
        guild = ctx.guild
        membru = guild.get_role(619458516356431882)
        staff = guild.get_role(619458376383856642)
        # voice limit
        if (comanda == "limit" or comanda == "LIMIT") or (comanda == "Limit" or comanda == "Limita") or (
                comanda == "limita" or comanda == "LIMITA"):
            voice_state = ctx.author.voice
            if voice_state == None:
                await ctx.reply("Nu ești conectat la vocal.")
                return
            if numar == None or int(numar) == 0:
                await ctx.reply(
                    "Ce limita sa setez mă, trebuie măcar un număr (comanda trebuie sa fie de forma: minim **.voice limit 1**, maxim **.voice limit 99**")
                return
            elif int(numar) > 99:
                await ctx.reply("Junior, maximul e 99.")
                return
            ow = ctx.author.voice.channel.overwrites_for(ctx.author)
            if ow.manage_channels is not True:
                await ctx.reply(
                    "N-ai acces sa schimbi ceva la canalul vocal. Daca cel care a facut canalul a iesit, foloseste comanda .voice claim")
                return
            await ctx.author.voice.channel.edit(user_limit=int(numar))
            embed = discord.Embed(title="", description="", color=discord.Color.green())
            embed.add_field(name=f'Gata flăcău', value=f"Ai limita de {int(numar)} persoane pe vocal.")
            await ctx.reply(embed=embed)

        # voice lock
        if (comanda == "lock" or comanda == "Lock") or (comanda == "LOCK" or comanda == "close") or (
                comanda == "Close" or comanda == "CLOSE"):
            voice_state = ctx.author.voice
            if voice_state == None:
                await ctx.reply("Nu ești conectat la vocal.")
                return
            ow = ctx.author.voice.channel.overwrites_for(ctx.author)
            if ow.manage_channels is not True:
                await ctx.reply(
                    "N-ai acces sa schimbi ceva la canalul vocal. Daca cel care a facut canalul a iesit, foloseste comanda .voice claim")
                return
            overwrites2 = {
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                guild.me: discord.PermissionOverwrite(view_channel=True),
                ctx.author: discord.PermissionOverwrite(view_channel=True, connect=True, manage_channels=True),
                membru: discord.PermissionOverwrite(view_channel=True),
                staff: discord.PermissionOverwrite(connect=True)
            }
            await ctx.author.voice.channel.edit(overwrites=overwrites2)
            embed = discord.Embed(title="", description="", color=discord.Color.green())
            embed.add_field(name=f'Gata flăcău', value=f"Nimeni altcineva nu mai poate intra pe canalul tau")
            await ctx.reply(embed=embed)

        # voice unlock
        if (comanda == "unlock" or comanda == "Unlock") or (comanda == "UNLOCK" or comanda == "deblocare") or (
                comanda == "Deblocare" or comanda == "DEBLOCARE"):
            voice_state = ctx.author.voice
            if voice_state == None:
                await ctx.reply("Nu ești conectat la vocal.")
                return
            ow = ctx.author.voice.channel.overwrites_for(ctx.author)
            if ow.manage_channels is not True:
                await ctx.reply(
                    "N-ai acces sa schimbi ceva la canalul vocal. Daca cel care a facut canalul a iesit, foloseste comanda .voice claim")
                return
            ow2 = ctx.author.voice.channel.overwrites_for(membru)
            if ow2.connect == True:
                await ctx.reply("Canalul e deja deblocat")
                return
            overwrites2 = {
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                guild.me: discord.PermissionOverwrite(view_channel=True),
                ctx.author: discord.PermissionOverwrite(view_channel=True, connect=True, manage_channels=True),
                membru: discord.PermissionOverwrite(view_channel=True),
                staff: discord.PermissionOverwrite(connect=True)
            }
            await ctx.author.voice.channel.edit(overwrites=overwrites2)
            embed = discord.Embed(title="", description="", color=discord.Color.green())
            embed.add_field(name=f'Gata flăcău', value=f"Canalul tau e deschis la lume")
            await ctx.reply(embed=embed)

        # voice name
        if (comanda == "name" or comanda == "Name") or (comanda == "NAME" or comanda == "nume") or (
                comanda == "Nume" or comanda == "NUME"):
            voice_state = ctx.author.voice
            if voice_state == None:
                await ctx.reply("Nu ești conectat la vocal.")
                return
            ow = ctx.author.voice.channel.overwrites_for(ctx.author)
            if ow.manage_channels is not True:
                await ctx.reply(
                    "N-ai acces sa schimbi ceva la canalul vocal. Daca cel care a facut canalul a iesit, foloseste comanda .voice claim")
                return
            await ctx.author.voice.channel.edit(name=numar)
            embed = discord.Embed(title="", description="", color=discord.Color.green())
            embed.add_field(name=f'Gata flăcău', value=f"Canalul tau e se numeste {numar}")
            await ctx.reply(embed=embed)

        # voice allow
        if (comanda == "allow" or comanda == "Allow") or (comanda == "ALLOW" or comanda == "permit") or (
                comanda == "Permit" or comanda == "PERMIT"):
            voice_state = ctx.author.voice
            if voice_state == None:
                await ctx.reply("Nu ești conectat la vocal.")
                return
            ow = ctx.author.voice.channel.overwrites_for(ctx.author)
            if ow.manage_channels is not True:
                await ctx.reply(
                    "N-ai acces sa schimbi ceva la canalul vocal. Daca cel care a facut canalul a iesit, foloseste comanda .voice claim")
                return
            converter = MemberConverter()
            member = await converter.convert(ctx, numar)
            overwrites2 = {
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                guild.me: discord.PermissionOverwrite(view_channel=True),
                ctx.author: discord.PermissionOverwrite(view_channel=True, connect=True, manage_channels=True),
                membru: discord.PermissionOverwrite(view_channel=True),
                staff: discord.PermissionOverwrite(connect=True),
                member: discord.PermissionOverwrite(connect=True)
            }
            await ctx.author.voice.channel.edit(overwrites=overwrites2)
            embed = discord.Embed(title="", description="", color=discord.Color.green())
            embed.add_field(name=f'Gata flăcău', value=f"Domnul {member} are acces la canalul tau")
            await ctx.reply(embed=embed)

        # voice deny
        if (comanda == "deny" or comanda == "Deny") or (comanda == "DENY" or comanda == "reject") or (
                comanda == "Reject" or comanda == "REJECT"):
            voice_state = ctx.author.voice
            if voice_state == None:
                await ctx.reply("Nu ești conectat la vocal.")
                return
            ow = ctx.author.voice.channel.overwrites_for(ctx.author)
            if ow.manage_channels is not True:
                await ctx.reply(
                    "N-ai acces sa schimbi ceva la canalul vocal. Daca cel care a facut canalul a iesit, foloseste comanda .voice claim")
                return
            converter = MemberConverter()
            member = await converter.convert(ctx, numar)
            overwrites2 = {
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                guild.me: discord.PermissionOverwrite(view_channel=True),
                ctx.author: discord.PermissionOverwrite(view_channel=True, connect=True, manage_channels=True),
                membru: discord.PermissionOverwrite(view_channel=True),
                staff: discord.PermissionOverwrite(connect=True),
                member: discord.PermissionOverwrite(connect=False)
            }
            await ctx.author.voice.channel.edit(overwrites=overwrites2)
            embed = discord.Embed(title="", description="", color=discord.Color.green())
            embed.add_field(name=f'Gata flăcău', value=f"Domnul {member} nu mai are acces la canalul tau")
            await ctx.reply(embed=embed)

        # voice claim
        if (comanda == "claim" or comanda == "Claim") or comanda == "CLAIM":
            voice_state = ctx.author.voice
            if voice_state == None:
                await ctx.reply("Nu ești conectat la vocal.")
                return
            ow = ctx.author.voice.channel.overwrites_for(ctx.author)
            if ow.manage_channels == True:
                await ctx.reply("Tu esti ownerul canalului domnule, cum adica?")
                return
            ok = 0
            members = ctx.author.voice.channel.members
            for member in members:
                if member is not ctx.author:
                    ow = ctx.author.voice.channel.overwrites_for(member)
            if ow.manage_channel == True:
                ok = 1
                apartinator = membru
            if ok == 0:
                overwrites2 = {
                    guild.default_role: discord.PermissionOverwrite(view_channel=False),
                    guild.me: discord.PermissionOverwrite(view_channel=True),
                    ctx.author: discord.PermissionOverwrite(view_channel=True, connect=True, manage_channels=True),
                    membru: discord.PermissionOverwrite(view_channel=True),
                    staff: discord.PermissionOverwrite(connect=True)
                }
                embed = discord.Embed(title="", description="", color=discord.Color.green())
                embed.add_field(name=f'Gata flăcău',
                                value=f"Canalul iti apartine. Foloseste **.help voice** sa vezi ce poti face.")
                await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="", description="", color=discord.Color.green())
                embed.add_field(name=f'Vesti proaste domnule', value=f"Canalul ii apartine lui {apartinator}.")
                await ctx.reply(embed=embed)

    @voice.error
    async def voice_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"HOOOO DOMNULE",
                               description=f" Ai de asteptat {error.retry_after:.2f} secunde pana poti face ceva iar",
                               color=discord.Color.green())
            await ctx.reply(embed=em)


def setup(client):
    client.add_cog(Utils(client))