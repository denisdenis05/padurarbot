import discord
import random
import json
import re
import asyncio
import datetime
from datetime import timedelta
from discord.ext import commands
from discord.utils import get
from main import default_color

class KickBan(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason=""):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if member == None:
            embed = discord.Embed(title="",
                                  description="",
                                  color=default_color)
            embed.add_field(
                name="Comanda .kick",
                value=
                """Descriere: Folosind această comandă dai afară pe cineva de pe server.
Folosire: .kick [membru] [motiv]
Exemplu: 
   .kick @Optimus Prime 
   .kick @lil dani nbn de la kuweit nmw Ieși mă de aici""")
            await ctx.reply(embed=embed)
            return
        guild = member.guild
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title="",
                              description="",
                              color=default_color)
        if reason != "":
            embed.add_field(name="O luat kick!!!!!!", value=f'Domnul {member} a fost dat afara. Motiv : {reason} ',
                            inline=True)
        else:
            embed.add_field(name="O luat kick!!!!!!", value=f'Domnul {member} a fost dat afara.', inline=True)

        embed.set_image(url="https://tenor.com/view/horny-jail-bonk-dog-hit-head-stop-being-horny-gif-17298755")
        await member.kick(reason=reason)
        await ctx.send(embed=embed)
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"logs{guild.id}" in data:
            idlogs = data[f"logs{guild.id}"]
            channel = self.client.get_channel(int(idlogs))
            embedd = discord.Embed(title="",
                                   description="",
                                   color=discord.Color.red())
            embedd.add_field(name=f"{ctx.author} i-a dat kick lui {member}",
                             value=f"Motivul pentru kick : {reason}")
            embedd.set_footer(text=f"Id: {member.id}")
            embedd.set_thumbnail(
                url=
                "https://cdn.discordapp.com/attachments/745384647885848594/810105249477558272/K-300.png"
            )
            await channel.send(embed=embedd)
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"{ctx.guild.id}kicks{ctx.author.id}" not in data:
            data[f"{ctx.guild.id}kicks{ctx.author.id}"] = 1
        else:
            data[f"{ctx.guild.id}kicks{ctx.author.id}"] = int(data[f"{ctx.guild.id}kicks{ctx.author.id}"]) + 1
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def setnick(self, ctx, member: discord.Member = None, *, nick=None):
        if member == None:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green(""))
            embed.add_field(
                name="Comanda .setnick",
                value="Descrierea va fi disponibila curand...")
            await ctx.reply(embed=embed)
            return
        if member != None and nick == None:
            embed = discord.Embed(
                title="", description="", color=default_color)
            embed.add_field(name="Wtf", value="Ce nickname dai ?")
            await ctx.reply(embed=embed)
            return
        lastnick = member.display_name
        await member.edit(nick=nick)
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Nickname schimbat", value=f"Ai schimbat numele lui {member}")
        await ctx.reply(embed=embed)
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        guild = ctx.guild
        if f"logs{guild.id}" in data:
            idlogs = int(data[f"logs{guild.id}"])
            channel = self.client.get_channel(idlogs)
        embed = discord.Embed(
            title="", description="", color=discord.Color.red())
        embed.add_field(
            name=f"{ctx.author} a schimbat numele lui {member}",
            value=f"Din : {lastnick} in {nick}")
        embed.set_footer(text=f"Id: {member.id}")
        await channel.send(embed=embed)

    @setnick.error
    async def setnick_error(self, ctx, error):
        embed = discord.Embed(title="", description="", color=default_color)
        embed.add_field(name="Unde te crezi mă???", value=f'Mânuța că nu e voie !!!!', inline=True)
        await ctx.reply(embed=embed)



    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def nick(self, ctx, *, nick=None):
        member=ctx.author
        if member != None and nick == None:
            embed = discord.Embed(
                title="", description="", color=default_color)
            embed.add_field(name="Wtf", value="Ce nickname iei?")
            await ctx.reply(embed=embed)
            return
        lastnick = member.display_name
        await member.edit(nick=nick)
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Nickname schimbat", value=f"Ti-ai schimbat numele in {nick}")
        await ctx.reply(embed=embed)
    @nick.error
    async def nick_error(self, ctx, error):
        embed = discord.Embed(title="", description="", color=default_color)
        embed.add_field(name="HAHAHAHAHAH??", value=f'N-ai permisiune prietene.', inline=True)
        await ctx.reply(embed=embed)

    @commands.command(aliases=['roleadd', 'addr', 'radd', 'roeladd'])
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, member: discord.Member = None, *, role=""):
        if member == None:
            embed = discord.Embed(
                title="", description="", color=default_color)
            embed.add_field(
                name="Comanda .addrole/.roleadd",
                value=
                """Descriere: Folosind această comandă îi adaugi un grad unui membru.
    Folosire: .addrole [nume] [grad]
    Exemplu: 
       .addrole @lil dani nbn de la kuweit nmw Helper""")
            await ctx.reply(embed=embed)
            return
        if "<@&" in role:
            try:
                rol = re.search('<@&(.+?)>', role).group(1)
            except:
                await ctx.send("wtf")
                return
            roldeadaugat = ctx.guild.get_role(int(rol))
            rol = roldeadaugat.name
            await member.add_roles(roldeadaugat)
        else:
            await member.add_roles(discord.utils.get(member.guild.roles, name=role))
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Rol adaugat", value=f"I-ai dat lui {member} rolul de {role}")
        await ctx.reply(embed=embed)
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        guild = ctx.guild
        if f"logs{guild.id}" in data:
            idlogs = data[f"logs{guild.id}"]
        channel = self.client.get_channel(int(idlogs))
        embed = discord.Embed(
            title="", description="", color=discord.Color.red())
        embed.add_field(
            name=f"{ctx.author} a adaugat un rol lui {member}",
            value=f"Rolul dat : {role}")
        embed.set_footer(text=f"Id: {member.id}")
        await channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        embed = discord.Embed(
            title="", description="", color=default_color)
        if seconds == 0:
            embed.add_field(
                name="Okok nu mai e slowmode",
                value=f"Acest canal nu mai are slowmode")
        elif seconds == 1:
            embed.add_field(
                name="Na ca ai slowmode",
                value=f"Mai usor sefule , acest canal are slowmode de o secunda")
        else:
            embed.add_field(
                name="Na ca ai slowmode",
                value=f"Mai usor sefule , acest canal are slowmode de {seconds} secunde")
        await ctx.reply(embed=embed)

    @commands.command(aliases=['roleremove', 'rrem', 'remr'])
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, member: discord.Member = None, *, role=""):
        if member == None:
            embed = discord.Embed(
                title="", description="", color=default_color)
            embed.add_field(
                name="Comanda .removerole/.roleremove",
                value=
                """Descriere: Cu ajutorul acestei comenzi îi scoți unui membru un grad, la alegerea ta.
    Folosire: .removerole [nume] [gradul ales]
    Exemplu: 
       .removerole @lil dani nbn de la kuweit nmw Helper
       .roleremove @Optimus Prime Helper""")
            await ctx.reply(embed=embed)
            return
        if "<@&" in role:
            try:
                rol = re.search('<@&(.+?)>', role).group(1)
            except:
                await ctx.send("wtf")
                return
            roldesters = ctx.guild.get_role(int(rol))
            rol = roldesters.name
            await member.remove_roles(roldesters)
        else:
            await member.remove_roles(discord.utils.get(member.guild.roles, name=role))
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Rol sters", value=f"I-ai sters lui {member} rolul de {role}")
        await ctx.reply(embed=embed)
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        guild = ctx.guild
        if f"logs{guild.id}" in data:
            idlogs = data[f"logs{guild.id}"]
        channel = self.client.get_channel(int(idlogs))
        embed = discord.Embed(
            title="", description="", color=discord.Color.red())
        embed.add_field(
            name=f"{ctx.author} a sters un rol lui {member}",
            value=f"Rolul sters : {role}")
        embed.set_footer(text=f"Id: {member.id}")
        await channel.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        embed = discord.Embed(title="",
                              description="",
                              color=default_color)
        embed.add_field(name="Unde te crezi mă???",
                        value=f'Mânuța că nu e voie !!!!',
                        inline=True)
        await ctx.reply(embed=embed)

    @commands.command(aliases=['banraid'])
    @commands.has_permissions(ban_members=True)
    async def raidban(self, ctx):
        if member == None:
            embed = discord.Embed(title="",
                                  description="",
                                  color=default_color)
            embed.add_field(
                name="Comanda .raidban",
                value=
                """Descriere: Îi privezi unor membrii veniti la raid libertatea cam permanent.
Folosire: .raidban
""")
            await ctx.send(embed=embed)
            return
        guild = member.guild

        suspectraid = guild.get_role(883708244256751626)
        await ctx.channel.purge(limit=1)
        for member in guild.members:
            if suspectraid in member.roles:
                embed = discord.Embed(title="",
                                      description="",
                                      color=default_color)
                await member.ban(reason="RAID")
                embed.add_field(name="A fost banat!!!!",
                                value=f'Domnul {member} a luat ban . Motiv : RAID',
                                inline=True)
                await ctx.send(
                    "https://cdn.discordapp.com/attachments/735155822736179201/803883710784864266/Screenshot_20210127-090645_Discord.jpg")
                await ctx.send(embed=embed)
                with open("pad/data/data.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                    jsonFile.close()
                if f"logs{guild.id}" in data:
                    idlogs = data[f"logs{guild.id}"]
                channel = self.client.get_channel(int(idlogs))
                embedd = discord.Embed(title="", description="", color=discord.Color.red())
        embedd.add_field(name=f"(RAIDBAN) {ctx.author} i-a dat ban lui {member} (RAIDBAN)",
                         value=f"Motivul pentru ban : RAIDBAN")
        embedd.set_thumbnail(
            url=
            "https://cdn.discordapp.com/attachments/745384647885848594/810105249669840906/B-300.png"
        )
        await channel.send(embed=embedd)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=""):
        if member == None:
            embed = discord.Embed(title="",
                                  description="",
                                  color=default_color)
            embed.add_field(
                name="Comanda .ban",
                value=
                """Descriere: Îi privezi unui membru libertatea cam permanent.
Folosire: .ban [membru] [motiv]
Exemplu: 
   .ban @Optimus Prime 15m Ai fost obraznic !!!
   .ban @lil dani nbn de la kuweit nmw""")
            await ctx.send(embed=embed)
            return
        guild = member.guild
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title="",
                              description="",
                              color=default_color)
        await member.ban(reason=reason)
        if reason != "":
            embed.add_field(name="A fost banat!!!!",
                            value=f'Domnul {member} a luat ban . Motiv : {reason}',
                            inline=True)
        else:
            embed.add_field(name="A fost banat!!!!",
                            value=f'Domnul {member} a luat ban .',
                            inline=True)
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/735155822736179201/803883710784864266/Screenshot_20210127-090645_Discord.jpg")
        await ctx.send(embed=embed)
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"logs{guild.id}" in data:
            idlogs = data[f"logs{guild.id}"]
            channel = self.client.get_channel(int(idlogs))
            embedd = discord.Embed(title="",
                                   description="",
                                   color=discord.Color.red())
            embedd.add_field(name=f"{ctx.author} i-a dat ban lui {member}",
                             value=f"Motivul pentru ban : {reason}")
            embedd.set_thumbnail(
                url=
                "https://cdn.discordapp.com/attachments/745384647885848594/810105249669840906/B-300.png"
            )
            await channel.send(embed=embedd)
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"{ctx.guild.id}bans{ctx.author.id}" not in data:
            data[f"{ctx.guild.id}bans{ctx.author.id}"] = 1
        else:
            data[f"{ctx.guild.id}bans{ctx.author.id}"] = int(data[f"{ctx.guild.id}bans{ctx.author.id}"]) + 1
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()

    @ban.error
    async def ban_error(self, ctx, error):
        embed = discord.Embed(title="",
                              description="",
                              color=default_color)
        embed.add_field(name="Unde te crezi mă???",
                        value=f'Mânuța că nu e voie !!!!',
                        inline=True)
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def softban(self, ctx, member: discord.Member = None, *, reason=""):
        if member == None:
            embed = discord.Embed(title="",
                                  description="",
                                  color=default_color)
            embed.add_field(
                name="Comanda .softban",
                value=
                """Descriere: Dai afara un membru si ii stergi toate mesajele.
Folosire: .softban [membru] [motiv] 
Exemplu: 
   .softban @Optimus Prime Ai fost obraznic !!!
   .softban @lil dani nbn de la kuweit nmw""")
            await ctx.reply(embed=embed)
            return
        guild = member.guild
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title="",
                              description="",
                              color=default_color)
        await member.ban(reason=reason)
        await member.unban(reason=reason)
        if reason != "":
            embed.add_field(
                name="A fost banat!!!!",
                value=f'Domnul {member} a luat softban . Motiv : {reason}',
                inline=True)
        else:
            embed.add_field(
                name="A fost banat!!!!",
                value=f'Domnul {member} a luat softban .',
                inline=True)
        embed.set_image(url=
                        "https://tenor.com/view/spongebob-scared-afraid-gif-15550732")
        await ctx.reply(embed=embed)
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"logs{ctx.guild.id}" in data:
            idlogs = data[f"logs{ctx.guild.id}"]
        channel = self.client.get_channel(int(idlogs))
        embedd = discord.Embed(title="",
                               description="",
                               color=discord.Color.red())
        embedd.add_field(name=f"{ctx.author} i-a dat softban lui {member}",
                         value=f"Motivul pentru softban : {reason}")
        embedd.set_thumbnail(
            url=
            "https://cdn.discordapp.com/attachments/745384647885848594/810105249669840906/B-300.png"
        )
        await channel.send(embed=embedd)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int = 0, *, reason=""):
        if id == 0:
            embed = discord.Embed(
                title="", description="", color=default_color)
            embed.add_field(
                name="Comanda .unban",
                value=
                """Descriere: Îi înapoiezi cuiva accessul de a putea intra pe server
    Folosire: .unban [id] [motiv opțional]
    La alegerea voastră puteți să spuneți și motivul pentru care respectivul a primit unban
    Exemplu: 
       .unban 470995082145824798
       .unban 470995082145824798  a fost cuminte""")
            await ctx.reply(embed=embed)
            return
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title="", description="", color=default_color)
        user = await self.client.fetch_user(id)
        embed.add_field(
            name="Unban", value=f'Domnul {user} a primit unban .', inline=True)
        await ctx.guild.unban(user)
        await ctx.reply(embed=embed)
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"logs{guild.id}" in data:
            idlogs = data[f"logs{guild.id}"]
        channel = self.client.get_channel(int(idlogs))
        embed = discord.Embed(
            title="", description="", color=discord.Color.red())
        embed.add_field(
            name=f"{ctx.author} i-a dat unban lui {member}",
            value=f"Motivul pentru unban : {reason}")
        await channel.send(embed=embed)

    @unban.error
    async def unban_error(self, ctx, error):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Unde te crezi mă???",
            value=f'Mânuța că nu e voie !!!!',
            inline=True)
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def searchpurge(self, ctx, *, cuvant=None):
        if cuvant == None:
            return
        if len(cuvant) < 4:
            return
        async for x in ctx.message.channel.history(limit=1000000):
            if cuvant.upper() in x.content.upper():
                await x.delete()

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def purge(self, ctx, ammount=0):
        if ammount == 0:
            embed = discord.Embed(
                title="", description="", color=default_color)
            embed.add_field(
                name="Comanda .purge",
                value=
                """Descriere: Această comandă îți este de folos în cazul în care ai nevoie să stergi mai multe mesaje simultan.
    Folosire: .purge [număr de mesaje]
    Exemplu: 
       .purge 5""")
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Mesaje sterse",
            value=f'{ammount} mesaje au fost șterse',
            inline=True)
        ammount = ammount + 1
        await ctx.channel.purge(limit=ammount)
        await ctx.send(embed=embed, delete_after=3)
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"logs{guild.id}" in data:
            idlogs = data[f"logs{guild.id}"]
        channel = self.client.get_channel(int(idlogs))
        embed = discord.Embed(
            title="", description="", color=discord.Color.red())
        embed.add_field(
            name=f"{ctx.author} a folosit comanda purge in {ctx.channel}",
            value=f"Numarul de mesaje sterse : {ammount - 1}")
        await channel.send(embed=embed)

    @purge.error
    async def purge_error(self, ctx, error):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Unde te crezi mă???",
            value=f'Mânuța că nu e voie !!!!',
            inline=True)
        await ctx.reply(embed=embed)

    @softban.error
    async def sotban_error(self, ctx, error):
        embed = discord.Embed(title="",
                              description="",
                              color=default_color)
        embed.add_field(name="Unde te crezi mă???",
                        value=f'Mânuța că nu e voie !!!!',
                        inline=True)
        await ctx.reply(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self,ctx: commands.Context, member: discord.Member = None, mute_minutes=None, *, reason=""):
      if member == None:
        embed = discord.Embed(title="", description="", color=default_color)
        embed.add_field(name="Comanda .mute", value="""Descriere: Este folosită în cazul în care un membru încalcă regulamentul intern al acestui server, este setat în minute.
    Folosire: .mute [nume] [timpul sancțiunii+u.m.] [motiv]
    Exemplu:
       .mute @Optimus Prime 5m Spam
       .mute @lil dani nbn de la kuweit nmw 70s injurii""")
        await ctx.reply(embed=embed)
        return
      if mute_minutes == "0":
        return
      if mute_minutes == None:
        secunde = 300
      elif "SEC" in mute_minutes.upper():
        mute_minutes = mute_minutes.upper()
        mute_minutes = mute_minutes.replace("SEC", "")
        secunde = int(mute_minutes)
      elif "S" in mute_minutes.upper():
        mute_minutes = mute_minutes.upper()
        mute_minutes = mute_minutes.replace("S", "")
        secunde = int(mute_minutes)
      elif "MIN" in mute_minutes.upper():
        mute_minutes = mute_minutes.upper()
        mute_minutes = mute_minutes.replace("MIN", "")
        secunde = 60 * int(mute_minutes)
      elif "M" in mute_minutes.upper():
        mute_minutes = mute_minutes.upper()
        mute_minutes = mute_minutes.replace("M", "")
        secunde = 60 * int(mute_minutes)
      elif "HOURS" in mute_minutes.upper():
        mute_minutes = mute_minutes.upper()
        mute_minutes = mute_minutes.replace("HOURS", "")
        secunde = 3600 * int(mute_minutes)
      elif "HOUR" in mute_minutes.upper():
        mute_minutes = mute_minutes.upper()
        mute_minutes = mute_minutes.replace("HOUR", "")
        secunde = 3600 * int(mute_minutes)
      elif "H" in mute_minutes.upper():
        mute_minutes = mute_minutes.upper()
        mute_minutes = mute_minutes.replace("H", "")
        secunde = 3600 * int(mute_minutes)
      elif "ORE" in mute_minutes.upper():
        mute_minutes = mute_minutes.upper()
        mute_minutes = mute_minutes.replace("ORE", "")
        secunde = 3600 * int(mute_minutes)
      elif "O" in mute_minutes.upper():
        mute_minutes = mute_minutes.upper()
        mute_minutes = mute_minutes.replace("O", "")
        secunde = 3600 * int(mute_minutes)
      minute=secunde/60
      await member.edit(timed_out_until=discord.utils.utcnow()+timedelta(seconds=secunde))
      embed = discord.Embed(title="", description="", color=default_color)
      if (secunde <= 60):
          if reason!="":
            embed.add_field(name="Shhh",value=f'Domnul {member} a fost redus la tacere pentru {secunde:.0f} secunde. \nMotiv: {reason} ',inline=True)
          else:
            embed.add_field(name="Shhh",value=f'Domnul {member} a fost redus la tacere pentru {secunde:.0f} secunde.',inline=True)
      elif (secunde <= 3600):
          if reason!="":
            embed.add_field(name="Shhh",value=f'Domnul {member} a fost redus la tacere pentru {(secunde / 60):.0f} minute. \nMotiv: {reason} ',inline=True)
          else:
            embed.add_field(name="Shhh",value=f'Domnul {member} a fost redus la tacere pentru {(secunde / 60):.0f} minute.',inline=True)
      else:
          if reason!="":
            embed.add_field(name="Shhh",value=f'Domnul {member} a fost redus la tacere pentru {(secunde / 3600):.0f} ore. \nMotiv: {reason} ',inline=True)
          else:
            embed.add_field(name="Shhh",value=f'Domnul {member} a fost redus la tacere pentru {(secunde / 3600):.0f} ore . ',inline=True)
      embed.set_image(url= "https://cdn.discordapp.com/attachments/745384647885848594/855856582700695572/200_d.gif") 
      await ctx.send(embed=embed)
      with open("pad/data/data.json", "r") as jsonFile:
          data = json.load(jsonFile)
          jsonFile.close()
      if f"logs{ctx.guild.id}" in data:
          idlogs = int(data[f"logs{ctx.guild.id}"])
          channel = self.client.get_channel(int(idlogs))
          embedd = discord.Embed(title=f"{ctx.author} i-a dat mute lui {member}", description="",color=discord.Color.red())
          embedd.add_field(name=f"Motiv:", value=reason)
          if (secunde <= 60):
            embedd.add_field(name="Timp:", value=f"{secunde} secunde")
          elif (secunde <= 3600):
            embedd.add_field(name="Timp:", value=f"{secunde / 60} minute")
          else:
            embedd.add_field(name="Timp:", value=f"{secunde / 3600} ore")
          embedd.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/810105248793755648/M-400.png")
          try:
            await channel.send(embed=embedd)
          except:
            pass
      return
    @mute.error
    async def mute_error(self,ctx, error):
     print(error)
     embed = discord.Embed(title="", description="", color=default_color)
     embed.add_field(name="Unde te crezi mă???",value=f'Mânuța că nu e voie!!!!',inline=True)
     await ctx.send(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self,ctx: commands.Context, member: discord.Member = None, *, reason=""):
      if member == None:
        embed = discord.Embed(title="", description="", color=default_color)
        embed.add_field(name="Comanda .unmute",value="""Comanda: .unmute
Descriere: Îi redai cuiva accessul de  a putea conversa cu ceilalți membri
Folosire: .unmute [membru] 
La alegerea voastră puteți scrie și motivul pentru care respectivul a primit unmute
Exemplu: 
   .unmute @Optimus Prime 
   .unmute @lil dani nbn de la kuweit nmw mute greșit""")
        await ctx.reply(embed=embed)
        return
      await member.edit(timed_out_until=discord.utils.utcnow())
      embed = discord.Embed(title="", description="", color=default_color)
      if reason!="":
          embed.add_field(name="Ok poti vorbi",value=f'Domnul {member} a fost eliberat. Motiv : {reason} ',inline=True)
      else:
          embed.add_field(name="Ok poti vorbi",value=f'Domnul {member} a fost eliberat.',inline=True)

      embed.set_image(url=
            "https://cdn.discordapp.com/attachments/735155822736179201/808694837628895282/20210209_154425.jpg") 
      await ctx.send(embed=embed)
      with open("pad/data/data.json", "r") as jsonFile:
          data = json.load(jsonFile)
          jsonFile.close()
      if f"logs{ctx.guild.id}" in data:
          idlogs = int(data[f"logs{ctx.guild.id}"])
          channel = self.client.get_channel(int(idlogs))
          embedd = discord.Embed(title=f"{ctx.author} i-a dat unmute lui {member}", description="",color=discord.Color.red())
          embedd.add_field(name=f"Motiv:", value=reason)
          embedd.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/810105249973010442/U-300.png")
          try:
            await channel.send(embed=embedd)
          except:
            pass
      return
    @unmute.error
    async def unmute_error(self,ctx, error):
     print(error)
     embed = discord.Embed(title="", description="", color=default_color)
     embed.add_field(name="Unde te crezi mă???",value=f'Mânuța că nu e voie!!!!',inline=True)
     await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(KickBan(client))
