import discord
import random
import json
import asyncio
import re
import datetime
import discord_components
from discord_components import DiscordComponents, Button, ButtonStyle, ActionRow
from discord.ext import commands
from discord.ext import tasks
from datetime import datetime
from main import topxplist, paginaxp, timpdelatop


class Rank(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['voturi'])
    @commands.cooldown(2, 10, commands.BucketType.user)
    async def votes(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"voturi{member.id}" not in data:
            voturi = 0
        else:
            voturi = int(data[f"voturi{member.id}"])
        if f"voturis{member.id}" not in data:
            voturis = 0
        else:
            voturis = int(data[f"voturis{member.id}"])
        embed = discord.Embed(title="",
                              description="**Numarul de [voturi pentru Pădurar](https://top.gg/bot/790607817128017920): **",
                              color=discord.Color.green())
        embed.add_field(name=f'Voturi totale:', value=voturi)
        embed.add_field(name=f'Voturi in această săptămână:', value=voturis)
        embed.set_footer(text=member, icon_url=member.avatar_url)
        embed.timestamp = datetime.utcnow()
        await ctx.reply(embed=embed)

    @votes.error
    async def votes_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"HOOOO DOMNULE",
                               description=f" Ai de asteptat {error.retry_after:.2f} secunde pana poti vedea voturile iar",
                               color=discord.Color.green())
            await ctx.reply(embed=em)

    @commands.command(aliases=['rank'])
    @commands.cooldown(2, 10, commands.BucketType.user)
    async def xp(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"xp{ctx.guild.id}" not in data or data[f"xp{ctx.guild.id}"] == 0:
            embed = discord.Embed(title="Nu ai activat xp-ul pe acest server",
                                  description="Daca vrei sa il activezi, foloseste comanda `.setxp`",
                                  color=discord.Color.green())
            await ctx.reply(embed=embed)
            return
        embed = discord.Embed(title="", description="", color=discord.Color.green())
        if f"{ctx.guild.id}XP{member.id}" not in data:
            xp = 0
        else:
            xp = data[f"{ctx.guild.id}XP{member.id}"]
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"{ctx.guild.id}eventxp" in data:
            eventxp = int(data[f"{ctx.guild.id}eventxp"])
        else:
            eventxp = 1
        if f"{ctx.guild.id}xpdublu{member.id}" in data:
            if data[f"xpdublu{member.id}"] == 1 and eventxp <= 2:
                eventxp = 2
        if eventxp == 1:
            textxp = ""
        elif eventxp == 2:
            textxp = " (primești XP dublu momentan)"
        elif eventxp == 3:
            textxp = " (primești XP triplu momentan)"
        if ctx.author.id == member.id:
            embed.add_field(name=f'Xp' + textxp, value=f"Domnule {member.mention}, ai {xp} puncte.")
        else:
            embed.add_field(name=f'Xp' + textxp, value=f"Domnul {member.mention} are {xp} puncte.")


        match_keys={key:val for key, val in data.items() if key.startswith(f"{ctx.guild.id}rol")}
        lista=()
        for k in match_keys:
          if data[k]!=0:
            lista=lista+(k,)
        match_keys=lista
        dictionar={}
        for key in match_keys:
          dictionar[int(data[key])]=int(data[f"rol{data[key]}"])
        sort = dict(sorted(dictionar.items(), key=lambda x: x[1]))
        for key in sort.items():
          puncte=key[1]
          if xp<puncte:
            embed.set_footer(text=f"Urmatorul rol e deblocat la {puncte} puncte", icon_url=member.avatar_url)
            await ctx.reply(embed=embed)
            return
        embed.set_footer(text="Ai deblocat toate rolurile", icon_url=member.avatar_url)
        await ctx.reply(embed=embed)

    @xp.error
    async def xp_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"HOOOO DOMNULE",
                               description=f" Ai de asteptat {error.retry_after:.2f} secunde pana poti cere rankul iar",
                               color=discord.Color.green())
            await ctx.reply(embed=em)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def transferxp(self, ctx):
        return
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        match_keys = {key: val for key, val in data.items() if key.startswith("XP")}
        for key in match_keys:
            xp = data[key]
            print(key, xp)
            data[f"619454105869352961{key}"] = xp
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def addxp(self, ctx, member: discord.Member = None, xp: int = 0):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"xp{ctx.guild.id}" not in data or data[f"xp{ctx.guild.id}"] == 0:
            embed = discord.Embed(title="Nu ai activat xp-ul pe acest server",
                                  description="Daca vrei sa il activezi, foloseste comanda `.setxp`",
                                  color=discord.Color.green())
            await ctx.reply(embed=embed)
            return
        if member == None:
            await ctx.send("Cui dai xp?")
        if xp == 0:
            await ctx.send("Zgarcit esti ma, cat xp dai?")
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"{ctx.guild.id}XP{member.id}" not in data or data[f"{ctx.guild.id}XP{member.id}"] == 0:
            await ctx.send("k")
            data[f"{ctx.guild.id}XP{member.id}"] = xp
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
        else:
            await ctx.send("k")
            data[f"{ctx.guild.id}XP{member.id}"] = int(data[f"{ctx.guild.id}XP{member.id}"]) + xp
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def settxp(self, ctx, member: discord.Member = None, xp: int = 0):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"xp{ctx.guild.id}" not in data or data[f"xp{ctx.guild.id}"] == 0:
            embed = discord.Embed(title="Nu ai activat xp-ul pe acest server",
                                  description="Daca vrei sa il activezi, foloseste comanda `.setxp`",
                                  color=discord.Color.green())
            await ctx.reply(embed=embed)
            return
        if member == None:
            await ctx.send("Cui dai xp?")
        if xp == 0:
            await ctx.send("Zgarcit esti ma, cat xp dai?")
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        data[f"{ctx.guild.id}XP{member.id}"] = xp
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()
        await ctx.send("k")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def setidxp(self, ctx, member: int, xp: int = 0):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"xp{ctx.guild.id}" not in data or data[f"xp{ctx.guild.id}"] == 0:
            embed = discord.Embed(title="Nu ai activat xp-ul pe acest server",
                                  description="Daca vrei sa il activezi, foloseste comanda `.setxp`",
                                  color=discord.Color.green())
            await ctx.reply(embed=embed)
            return
        if xp == 0:
            await ctx.send("Zgarcit esti ma, cat xp dai?")
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        data[f"{ctx.guild.id}XP{member}"] = xp
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()
        await ctx.send("k")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def top(self, ctx, nr: int = 1):
        mesaj = await ctx.send("generez topul...")
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"xp{ctx.guild.id}" not in data or data[f"xp{ctx.guild.id}"] == 0:
            embed = discord.Embed(title="Nu ai activat xp-ul pe acest server",
                                  description="Daca vrei sa il activezi, foloseste comanda `.setxp`",
                                  color=discord.Color.green())
            await ctx.reply(embed=embed)
            return
        timpbun=0
        if ctx.guild.id in timpdelatop:
          ultimtimp=datetime.strptime(timpdelatop[ctx.guild.id], '%Y-%m-%d %H:%M:%S.%f')
          datacurenta=datetime.now()
          timp=datacurenta-ultimtimp
          if timp.seconds <180:
            sort=topxplist[ctx.guild.id]
            timpbun=1
            print("sort preluat")
        if timpbun==0:
          match_keys = {key: val for key, val in data.items() if key.startswith(f"{ctx.guild.id}XP")}
          dictionar = {}
          for k in match_keys:
            key = k.replace(f"{ctx.guild.id}XP", "")
            dictionar[f"<@{key}>"] = data[k]
          sort = sorted(dictionar.items(), key=lambda x: x[1], reverse=True)
          topxplist[ctx.guild.id]=sort
          timpdelatop[ctx.guild.id]=str(datetime.now())
          print("sort refacut")
        paginaxp[ctx.guild.id]=int(nr)
        i = (nr - 1) * 10
        j = nr * 10
        if len(sort) < j:
            j = len(sort)
        embed = discord.Embed(title="", description="", color=discord.Color.green())
        embed.set_author(name="Top puncte in padure",icon_url="https://cdn.discordapp.com/attachments/745384647885848594/864852166433570856/89a9a37af2f4387bc8293ae4dacfb4c4.jpg")
        # embed = discord.Embed(title="Top puncte ", description="in padurea Baneasa", color=discord.Color.green())
        if i >= j:
            ctx.eroare
        while i < j:
            sortat = (str(sort[i]).replace("',", "b")).replace(")", "n")
            # print(sortat)
            id = re.search('<@(.*?)>', sortat).group(1)
            start = sortat.index("b") + len("b")
            end = sortat.index("n", start)
            xp = sortat[start:end]
            id = int(id)
            xp = int(xp)
            print(id)
            print(xp)
            user = await self.client.fetch_user(id)
            embed.add_field(name=f"#{i + 1}", value=f"**🌲 {user.display_name}** are {xp} xp")
            i = i + 1
        await mesaj.delete()
        embed.set_footer(
            text=f"foloseste sagetile de mai jos sau comanda .top {nr + 1} pentru a vede următoarea pagina",
            icon_url="https://freepikpsd.com/media/2019/11/emoji-meme-png-4-Transparent-Images.png")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/745384647885848594/864473500257353788/830009449011871754.gif")
        if nr == 1:
            row = ActionRow(Button(label="⏮", style=3, custom_id="primultop", disabled=True),
                            Button(label="⏪", style=3, custom_id="backtop", disabled=True),
                            Button(label="⏩", style=3, custom_id="nexttop"),
                            Button(label="⏭", style=3, custom_id="ultimultop"))
        elif nr == int((len(sort) - 1) / 10):
            row = ActionRow(Button(label="⏮", style=3, custom_id="primultop", disabled=True),
                            Button(label="⏪", style=3, custom_id="backtop"),
                            Button(label="⏩", style=3, custom_id="nexttop", disabled=True),
                            Button(label="⏭", style=3, custom_id="ultimultop", disabled=True))
        else:
            row = ActionRow(Button(label="⏮", style=3, custom_id="primultop", disabled=True),
                            Button(label="⏪", style=3, custom_id="backtop"),
                            Button(label="⏩", style=3, custom_id="nexttop"),
                            Button(label="⏭", style=3, custom_id="ultimultop"))
        msg = await ctx.send(embed=embed, components=[row])
        await asyncio.sleep(180)
        await msg.edit(embed=embed, components=[row])
        okk = 0
        

    @top.error
    async def top_error(self, ctx, error):
        print(error)
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"HOOOO DOMNULE",
                               description=f" Ai de asteptat {error.retry_after:.2f} secunde pana poti cere topul iar pe acest server",
                               color=discord.Color.green())
            await ctx.reply(embed=em)
        else:
            await ctx.reply("Ceva n-a mers bine. Probabil ai introdus un numar de pagina prea mare sau prea mic")

    @commands.command(aliases=['topbump'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def topbumps(self, ctx, nr: int = 1):
        mesaj = await ctx.send("generez topul...")
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        match_keys = {key: val for key, val in data.items()
                      if key.startswith("bump")}
        dictionar = {}
        for k in match_keys:
            key = k.replace("bump", "")
            dictionar[f"<@{key}>"] = data[k]
        sort = sorted(dictionar.items(), key=lambda x: x[1], reverse=True)
        i = (nr - 1) * 5
        j = nr * 5
        if len(sort) < j:
            j = len(sort)
        embed = discord.Embed(title="Top bumps ", description="in padurea Baneasa", color=discord.Color.green())
        if i >= j:
            ctx.eroaree
        while i < j:
            try:
                sortat = (str(sort[i]).replace("',", "b")).replace(")", "n")
                print(sortat)
                id = re.search('<@(.*?)>', sortat).group(1)
                start = sortat.index("b") + len("b")
                end = sortat.index("n", start)
                xp = sortat[start:end]
                id = int(id)
                xp = int(xp)
                print(id)
                print(xp)
                user = await self.client.fetch_user(id)
                if xp == 1:
                    embed.add_field(name=f"#{i + 1}", value=f"**{user.display_name}** are {xp} bump")
                else:
                    embed.add_field(name=f"#{i + 1}", value=f"**{user.display_name}** are {xp} bump-uri")
                i = i + 1
            except AttributeError:
                i = j + 1
        await mesaj.delete()
        embed.set_footer(text=f"foloseste comanda .topbumps {nr + 1} pentru a vede următoarea pagina")
        await ctx.send(embed=embed)

    @topbumps.error
    async def top_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"HOOOO DOMNULE",
                               description=f" Ai de asteptat {error.retry_after:.0f} secunde pana poti cere topul iar",
                               color=discord.Color.green())
            await ctx.reply(embed=em)
        else:
            await ctx.send("Lmao nu cred ca sunt asa multe pagini")

    @commands.command()
    async def bumps(self, ctx, membru: discord.Member = None):
        if ctx.guild.id != 619454105869352961:
            await ctx.reply("Comanda doar pentru serverul In Padure la Băneasa")
            return
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if membru == None:
            membru = ctx.author
        if f"bump{membru.id}" not in data or data[f"bump{membru.id}"] == 0:
            if membru.id == ctx.author.id:
                await ctx.reply("N-ai dat niciun bump patroane.")
            else:
                await ctx.reply(f"{membru} n-a dat niciun bump.")
        else:
            if membru.id == ctx.author.id:
                bumps = data[f"bump{membru.id}"]
                await ctx.reply(f"Ai dat {bumps} bump-uri.")
            else:
                bumps = data[f"bump{membru.id}"]
                await ctx.reply(f"{membru} a dat {bumps} bump-uri.")


def setup(client):
    client.add_cog(Rank(client))