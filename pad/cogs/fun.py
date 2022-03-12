import discord
import random
import json
import datetime
import re
import os
import asyncio
import discord_components
from discord_components import DiscordComponents, Button, ButtonStyle,Select, SelectOption
from discord.ext import commands
from discord.utils import get
from random import randint
from datetime import datetime
from aiohttp import ClientSession
from io import BytesIO
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def birthday(self, ctx, day=None, month=None, year: int = 0):
      with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()

      #birthdaydate{id}
      try:
        try:
          membruid = re.search('<@(.+?)>', day).group(1)
          membruid=int(membruid)
        except Exception as ex:
          print(ex)
          membruid = re.search('<@!(.+?)>', day).group(1)
        member=await ctx.guild.fetch_member(int(membruid))
        if f"birthdaydate{member.id}" not in data:
          embed = discord.Embed(title="Wtf bro", description=f"Se pare ca {member} nu si-a setat ziua de nastere!", color=discord.Color.green())
          await ctx.reply(embed=embed)
          return
        else:
          calendar=data[f"birthdaydate{member.id}"]
          if calendar=="temp":
            calendar=data[f"tempbirthdaydate{member.id}"]
          day,month,year=calendar.split(".")
          if day==0 or month==0:
            embed = discord.Embed(title="Wtf bro", description=f"Se pare ca {member} nu si-a setat ziua de nastere!", color=discord.Color.green())
            await ctx.reply(embed=embed)
            return
          if int(day)<10:
            day="0"+str(day)
          if int(month)<10:
            month="0"+str(month)
          if int(year)==0:
            year=""
          else:
            year="."+year
          embed = discord.Embed(title="Nice!", description=f"{member} s-a nascut pe **{day}.{month}{year}**", color=discord.Color.green())
          await ctx.reply(embed=embed)
          return
      except Exception as ex:
        print(ex)
        pass

      if day==None:
        embed = discord.Embed(title=f"Ce doresti sa faci?", description=f"Reactioneaza mai jos pentru:\n\n👁️: a vedea ziua ta de nastere\n🇸: a seta data ta de nastere\n⛔: a renunta", color=discord.Color.from_rgb(105, 105, 105))
        #\n :ruler: : a vedea cate zile mai sunt pana la ziua ta
        mesaj = await ctx.reply(embed=embed)
        eye = '👁️'
        ruler = '📏'
        s='🇸'
        nu='⛔'
        await mesaj.add_reaction(eye)
        #await mesaj.add_reaction(ruler)
        await mesaj.add_reaction(s)
        await mesaj.add_reaction(nu)

        def check1(reaction, user):
          return reaction.message.id == mesaj.id and user.id == ctx.author.id and (str(reaction.emoji) == s or str(reaction.emoji) == eye or str(reaction.emoji) == ruler or str(reaction.emoji) == nu)
        def check2(m):
          return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id


        try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=25, check=check1)
                if str(reaction.emoji) == nu:
                    raise Exception("nu")
                await mesaj.delete()
                if str(reaction.emoji) == eye:
                  if f"birthdaydate{ctx.author.id}" not in data:
                    embed = discord.Embed(title="Wtf bro", description=f"Se pare ca nu ti-ai setat ziua de nastere!", color=discord.Color.green())
                    await ctx.reply(embed=embed)
                    return
                  else:
                    calendar=data[f"birthdaydate{ctx.author.id}"]
                    if calendar=="temp":
                      calendar=data[f"tempbirthdaydate{ctx.author.id}"]
                    day,month,year=calendar.split(".")
                    if day==0 or month==0:
                      embed = discord.Embed(title="Wtf bro", description=f"Se pare ca nu ti-ai setat ziua de nastere!", color=discord.Color.green())
                      await ctx.reply(embed=embed)
                      return
                    if int(day)<10:
                      day="0"+str(day)
                    if int(month)<10:
                      month="0"+str(month)
                    if int(year)==0:
                      year=""
                    else:
                      year="."+year
                    embed = discord.Embed(title="Nice!", description=f"Te-ai nascut pe **{day}.{month}{year}**", color=discord.Color.green())
                    await ctx.reply(embed=embed)
                    return
                elif str(reaction.emoji) == ruler:
                  if f"birthdaydate{ctx.author.id}" not in data:
                    embed = discord.Embed(title="Wtf bro", description=f"Se pare ca nu ti-ai setat ziua de nastere!", color=discord.Color.green())
                    await ctx.reply(embed=embed)
                    return
                  else:
                    calendar=data[f"birthdaydate{ctx.author.id}"]
                    if calendar=="temp":
                      calendar=data[f"tempbirthdaydate{ctx.author.id}"]
                    day,month,year=calendar.split(".")
                    if day==0 or month==0:
                      embed = discord.Embed(title="Wtf bro", description=f"Se pare ca nu ti-ai setat ziua de nastere!", color=discord.Color.green())
                      await ctx.reply(embed=embed)
                      return
                    #data-data actuala, +12 daca e pe -
                    #ramane de continuat
                elif str(reaction.emoji) == s:
                  embed = discord.Embed(title="Ok, spune-mi data ta de nastere!", description=f"Exemple: 17 Ianuarie, 20 Aprilie 1889", color=discord.Color.green())
                  mesaj = await ctx.send(embed=embed)
                  try:
                    msg = await self.client.wait_for('message', check=check2, timeout=40)
                    try:
                      day,month,year=str(msg.content).split(" ")
                      day=int(day)
                      year=int(year)
                    except:
                      day,month=str(msg.content).split(" ")
                      day=int(day)
                      year=0
                    try:
                      month=int(month)
                    except:
                      if str(month).upper() == "IANUARIE":
                        month = 1
                      elif str(month).upper() == "FEBRUARIE":
                        month = 2
                      elif str(month).upper() == "MARTIE":
                        month = 3
                      elif str(month).upper() == "APRILIE":
                        month = 4
                      elif str(month).upper() == "MAI":
                        month = 5
                      elif str(month).upper() == "IUNIE":
                        month = 6
                      elif str(month).upper() == "IULIE":
                        month = 7
                      elif str(month).upper() == "AUGUST":
                        month = 8
                      elif str(month).upper() == "SEPTEMBRIE":
                        month = 9
                      elif str(month).upper() == "OCTOMBRIE":
                        month = 10
                      elif str(month).upper() == "NOIEMBRIE":
                        month = 11
                      elif str(month).upper() == "DECEMBRIE":
                        month = 12
                    if year>=2017:
                      await msg.reply("https://www.youtube.com/watch?v=4gVDf_U-VEk")
                      return
                    elif year<= 1950 and year!=0:
                      await msg.reply("https://www.youtube.com/watch?v=CMSfPEJob30")
                      return
                    data[f"birthdaydate{ctx.author.id}"]=str(day)+"."+str(month)+"."+str(year)
                    with open("pad/data/data.json", "w") as jsonFile:
                      json.dump(data, jsonFile)
                      jsonFile.close()
                    embed = discord.Embed(title="Gata frate.", description=f"Voi tine minte", color=discord.Color.green())
                    await ctx.reply(embed=embed)
                    return

                  except Exception as ex:
                    print(ex)
                    await mesaj.delete()
                    return
                  
                  


            
        except Exception as ex:
              print(ex)
              try:
                await mesaj.delete()
              except:
                pass
              pass











    @commands.command(name="Urban dictionary",aliases=["urban", "urband",'ud'])
    async def urbandictionary(self, ctx,*, term):
        url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        querystring = {"term":term}

        headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "69a5c25a1cmsh3c114be44d227fcp1137c8jsn688eaf3bf591"
        }
        async with ClientSession() as session:
            async with session.get(url, headers=headers, params=querystring) as response:
                r = await response.json()
                definition = r['list'][0]['definition']
                embed = discord.Embed(title=f"Urban Dictionary", description=f"Primul rezultat:",color=discord.Color.from_rgb(0,191,255))
                embed.set_thumbnail(url='https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2018-01-11/297387706245_85899a44216ce1604c93_512.jpg')
                embed.add_field(name=term, value=definition, inline=False)
                await ctx.reply(embed=embed)


    @commands.command(aliases=['creare', 'creează', 'creeate', 'create', 'crează'])
    async def creeaza(self, ctx, *, clan):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if clan.startswith("clan"):
            clan = clan.replace("clan ", "")
            with open("pad/data/data.json", "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()
            if f"detinatorclan{ctx.author.id}" in data and data[f"detinatorclan{ctx.author.id}"] != 0:
                clandetinut = data[f"detinatorclan{ctx.author.id}"]
                await ctx.reply(
                    f"deja detii clanul {clandetinut}, foloseste mai intai comanda `.inchide clan` daca doresti sa iti creezi alt clan.")
                return
            if f"membruclan{ctx.author.id}" in data and data[f"membruclan{ctx.author.id}"] != 0:
                clanmembru = data[f"membruclan{ctx.author.id}"]
                await ctx.reply(
                    f"deja esti in clanul {clanmembru}, foloseste comanda `.iesire clan` daca doresti sa iti creezi propriul clan")
                return
            if len(clan) > 35:
                await ctx.reply(f"wtf, nu iti pot numi clanul `{clan}`, alege un nume mai scurt")
                return
            data[f"detinatorclan{ctx.author.id}"] = clan
            data[f"membriiclan{ctx.author.id}"] = 1
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()

            await ctx.send(
                f"bun, daca vrei sa recrutezi pe cineva in clan, pune-l sa foloseasca comanda `.intra clan {clan}`")

    @commands.command(aliases=['join', 'intră'])
    async def intra(self, ctx, *, clan):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if clan.startswith("clan"):
            clan = clan.replace("clan ", "")
            match_keys = {key: val for key, val in data.items() if key.startswith("detinatorclan")}
            for key in match_keys:
                if str(data[key]).upper() == clan.upper():
                    data[f"cerereclan{ctx.author.id}"] = int(key.replace("detinatorclan", ""))
                    lider = ctx.guild.get_member(int(key.replace("detinatorclan", "")))
                    await lider.send(
                        f"{ctx.author} (id:{ctx.author.id}) a cerut sa intre in clanul tau de pe serverul `{ctx.guild}`. Pentru a il accepta, foloseste comanda `.accept clan @{ctx.author}` pe server.")
                    await ctx.reply(f"bun, am trimis o cerere pt clanul `{clan}`")
                    with open("pad/data/data.json", "w") as jsonFile:
                        json.dump(data, jsonFile)
                        jsonFile.close()
                    return
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            await ctx.reply(f"n-am gasit niciun clan `{clan}`, asigura-te ca ai scris corect.")

    @commands.command(aliases=['accepta'])
    async def accept(self, ctx, clan, member: discord.Member = None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if clan == "clan":
            if member == None:
                await ctx.send("wtf")
                return
            if f"cerereclan{member.id}" in data and int(data[f"cerereclan{member.id}"]) == ctx.author.id:
                if f"membruclan{member.id}" in data and int(data[f"membruclan{member.id}"]) != 0:
                    await ctx.send("domnul deja a intrat intr-un clan.")
                    return
                data[f"membruclan{member.id}"] = ctx.author.id
                data[f"membriiclan{ctx.author.id}"] = int(data[f"membriiclan{ctx.author.id}"]) + 1
                await ctx.reply(f"felicitari, {member.mention}, esti in clanul domnului {ctx.author.mention}.")
                data[f"cerereclan{member.id}"] = 0
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()

            else:
                await ctx.reply("wtf nu ti-a dat cerere in clan")
                return

    @commands.command(aliases=['exit', 'iesi'])
    async def iesire(self, ctx, clan):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if clan == "clan":
            if f"detinatorclan{ctx.author.id}" in data and data[f"detinatorclan{ctx.author.id}"] != 0:
                await ctx.send(
                    "detii un clan, nu-l poti abandona. foloseste comands `.inchide clan` pentru a-ti inchide clanul.")
                return
            if f"membruclan{ctx.author.id}" not in data or data[f"membruclan{ctx.author.id}"] == 0:
                await ctx.reply("nu esti in niciun clan.")
                return
            idlider = int(data[f"membruclan{ctx.author.id}"])
            clan = data[f"detinatorclan{idlider}"]
            await ctx.reply(f"esti sigur ca vrei sa iesi din `{clan}`?")

            def is_correct(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

            msg = await self.client.wait_for('message', check=is_correct, timeout=30)
            if "NU" in str(msg.content).upper() or "NO" in str(msg.content).upper() or "NAH" in str(
                    msg.content).upper():
                await ctx.repl("ok")
                return
            elif "DA" in str(msg.content).upper() or "YES" in str(msg.content).upper():
                data[f"membruclan{ctx.author.id}"] = 0
                data[f"membriiclan{idlider}"] = int(data[f"membriiclan{idlider}"]) - 1
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()

    @commands.command(aliases=['închide', 'close'])
    async def inchide(self, ctx, clan):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if clan == "clan":
            if f"detinatorclan{ctx.author.id}" not in data or data[f"detinatorclan{ctx.author.id}"] == 0:
                await ctx.reply("n-ai niciun clan, wtf")
                return
            await ctx.reply(f"esti sigur ca vrei sa iti inchizi permanent clanul?")

            def is_correct(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

            msg = await self.client.wait_for('message', check=is_correct, timeout=30)
            if "NU" in str(msg.content).upper() or "NO" in str(msg.content).upper() or "NAH" in str(
                    msg.content).upper():
                await ctx.repl("ok")
                return
            elif "DA" in str(msg.content).upper() or "YES" in str(msg.content).upper():
                match_keys = res = {key: val for key, val in data.items()
                                    if key.startswith("membruclan")}
                for key in match_keys:
                    if int(data[key]) == ctx.author.id:
                        data[key] = 0;
                data[f"membriiclan{ctx.author.id}"] = 0
                data[f"detinatorclan{ctx.author.id}"] = 0
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()

                await ctx.send("gata maestre, clanul nu mai exista.")

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.guild)
    async def clan(self, ctx, *, clan=None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        idlider = None
        if clan == None:
            if (f"detinatorclan{ctx.author.id}" not in data or data[f"detinatorclan{ctx.author.id}"] == 0) and (
                    f"membruclan{ctx.author.id}" not in data or data[f"membruclan{ctx.author.id}"] == 0):
                await ctx.send(f"Nu esti intr-un clan. Foloseste comanda `.help clan` pentru a afla mai multe despre comanda.")
                return
            if f"detinatorclan{ctx.author.id}" in data and data[f"detinatorclan{ctx.author.id}"] != 0:
                idlider = ctx.author.id
            elif f"membruclan{ctx.author.id}" in data or data[f"membruclan{ctx.author.id}"] != 0:
                idlider = int(data[f"membruclan{ctx.author.id}"])
        elif "<@" in clan or "<@!" in clan:
            try:
                membruid = re.search('<@(.+?)>', clan).group(1)
            except:
                membruid = re.search('<@!(.+?)>', clan).group(1)
            membru = ctx.guild.get_member(int(membruid))
            if (f"detinatorclan{membru.id}" not in data or data[f"detinatorclan{membru.id}"] == 0) and (
                    f"membruclan{membru.id}" not in data or data[f"membruclan{membru.id}"] == 0):
                await ctx.send(f"{membru.mention} nu e intr-un clan")
                return
            if f"detinatorclan{membru.id}" in data and data[f"detinatorclan{membru.id}"] != 0:
                idlider = membru.id
            elif f"membruclan{membru.id}" in data or data[f"membruclan{membru.id}"] != 0:
                idlider = int(data[f"membruclan{membru.id}"])
        else:
            match_keys = res = {key: val for key, val in data.items()
                                if key.startswith("detinatorclan")}
            for key in match_keys:
                if str(data[key]).upper() == clan.upper():
                    idlider = int(key.replace("detinatorclan", ""))
        if idlider == None:
            await ctx.reply("ceva n-a mers bine, ruleaza din nou comanda si ai grija sa scrii bine numele clanului")
            return
        numeclan = data[f"detinatorclan{idlider}"]
        mesaj = await ctx.send("un moment, strang informatii despre clan...")
        embed = discord.Embed(title="DETALII CLAN", description=f"Nume clan: `{numeclan}`", color=discord.Color.green())
        try:
            lid = ctx.guild.get_member(int(idlider))
        except:
            lid = "n-am putut gasi liderul acestui clan, probabil a iesit de pe server."
        if lid!=None:
          text = f"**{lid}** (lider)\n"
        else:
          text = f"**Liderul clanului nu este pe acest server**\n"
        if f"xpsaptamanal{idlider}" in data:
            xptotal = int(data[f"xpsaptamanal{idlider}"])
        else:
            xptotal = 0
        liders=1
        match_keys = {key: val for key, val in data.items() if key.startswith("membruclan")}
        membriiiesiti=0
        for key in match_keys:
            if int(data[key]) == int(idlider):
                k = key
                key = key.replace("membruclan", "")
                try:
                    mem = ctx.guild.get_member(int(key))
                    if (mem == None):
                        membriiiesiti=1
                        raise Exception("nu")
                except:
                    pass
                if mem!=None:
                  if liders==0:
                    text = text + f", {mem}"
                  else:
                    text = text + f"{mem}"
                    liders=0
                if f"xpsaptamanal{key}" in data:
                    xptotal = xptotal + int(data[f"xpsaptamanal{key}"])
        membriiclan = int(data[f"membriiclan{idlider}"])
        embed.add_field(name="Numarul de membrii:", value=membriiclan,inline=False)
        embed.add_field(name="Xp-ul acumulat saptamana asta:", value=xptotal,inline=False)
        embed.add_field(name="Membrii:", value=text,inline=False)
        if membriiiesiti==1:
          embed.set_footer(text="Cativa membrii din clan nu sunt pe acest server, astfel nu vor aparea pe lista.")
        await mesaj.delete()
        await ctx.reply(embed=embed)

    @clan.error
    async def clan_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            timp = error.retry_after
            em = discord.Embed(title=f"HOOOO DOMNULE",
                               description=f" Ai de asteptat {timp:.0f} secunde pana se poate utiliza comanda clan pe acest server",
                               color=discord.Color.green())
            await ctx.reply(embed=em)

    @commands.command(aliases=['hug', 'îmbrățișare'])
    async def imbratisare(self, ctx, member: discord.Member = None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if member == None:
            await ctx.reply("Pe cine îmbrățișezi?")
            return
        if member.id == ctx.author.id:
            await ctx.reply("inteleg da nu te imbratisezi singur lmao 😆")
            return
        situatie = randint(1, 10)
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"muted{ctx.guild.id}" in data:
            idmute = int(data[f"muted{ctx.guild.id}"])
            muted_role = ctx.guild.get_role(idmute)
        if f"membru{ctx.guild.id}" in data:
            idmembru = int(data[f"membru{ctx.guild.id}"])
            membru_role = ctx.guild.get_role(idmembru)
        if situatie == 1:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name="Damn man",
                            value=f"{member.mention} ti-a refuzat imbratisarea, de rușine nu mai poți vorbi 30 secunde.",
                            inline=True)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/812370952075477053.png?v=1&size=40')
            await ctx.send(embed=embed)
            await ctx.author.add_roles(muted_role)
            await ctx.author.remove_roles(membru_role)
            await asyncio.sleep(30)
            await ctx.author.add_roles(membru_role)
            await ctx.author.remove_roles(muted_role)
            return
        elif situatie == 2:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name="Uhh", value=f"A fost ciudata îmbrățișarea", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/868620731355902013.png?v=1&size=40')
        elif situatie == 3:
            embed = discord.Embed(
                title="", description="", color=discord.Color.from_rgb(255, 182, 193))
            embed.add_field(name="Suflete pereke 🎉", value=f"Ar trebui sa va căsătoriți", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/860476850773295114.png?v=1&size=40')
        elif situatie == 4:
            embed = discord.Embed(
                title="", description="", color=discord.Color.from_rgb(255, 182, 193))
            embed.add_field(name="Woah woah", value=f"Ce drăguț!!", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/777941656934154281.png?v=1&size=40')
        elif situatie == 5:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name="Mirosi urat 🤮🤮🤮", value=f"Mai spala-te", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/858476756863549491.png?v=1&size=40')
        elif situatie >= 6:
            embed = discord.Embed(
                title="", description="", color=discord.Color.from_rgb(255, 182, 193))
            embed.add_field(name="Wow!", value=f"Ce dragut!!", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/862108740869029898.png?v=1&size=40')
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        embed.timestamp = datetime.utcnow()
        await ctx.reply(embed=embed)

    @commands.command(aliases=['blbl', 'linge', 'limba', 'limbă'])
    async def blblbl(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.reply("Huh da si un nume")
            return
        if member.id == ctx.author.id:
            await ctx.reply("nu")
            return
        situatie = randint(1, 10)
        if situatie <= 9:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name="Hahaha", value=f"I-ai aratat limba lui {member.mention} lmao⁉️", inline=True)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/828280567904075806.gif?v=1&size=40')
        elif situatie > 9:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name="Uhh", value=f"L-ai lins pe {member.mention} ciudatule", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/874999910863364177.gif?v=1&size=40')
        await ctx.reply(embed=embed)

    @commands.command(aliases=['pumni'])
    async def pumn(self, ctx, member: discord.Member = None):
        await ctx.reply("mai bine dă-i o palmă ca nu esti la box")

    @commands.command(aliases=['palma', 'palmă'])
    async def slap(self, ctx, member: discord.Member = None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if member == None:
            await ctx.reply("Pe cine lovesti?")
            return
        if member.id == ctx.author.id:
            await ctx.reply("Cum sa te lovești singur wtf")
            return
        situatie = randint(1, 6)
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"muted{ctx.guild.id}" in data:
            idmute = int(data[f"muted{ctx.guild.id}"])
            muted_role = ctx.guild.get_role(idmute)
        if f"membru{ctx.guild.id}" in data:
            idmembru = int(data[f"membru{ctx.guild.id}"])
            membru_role = ctx.guild.get_role(idmembru)
        if situatie == 1:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name="Karate", value=f"{member.mention} ti-a scos dintii. Nu poți vorbi 20 secunde.",
                            inline=True)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/695954095814475776.png?v=1&size=40')
            await ctx.send(embed=embed)
            await ctx.author.add_roles(muted_role)
            await ctx.author.remove_roles(membru_role)
            await asyncio.sleep(20)
            await ctx.author.add_roles(membru_role)
            await ctx.author.remove_roles(muted_role)
            return
        elif situatie == 2:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name="Vai mama", value=f"Ramane cu traume {member.mention}", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/823653939395166208.gif?v=1&size=40')
        elif situatie == 3:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name="Te-ai razgandit", value="Cam laș", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/836776375649304576.png?v=1&size=40')
        elif situatie == 4:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name="HOOO BAA", value="NU MAI DA CA-L OMORI", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/830008622188331020.gif?v=1&size=40')
        elif situatie == 5:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name="I-ai dat de l-ai julit", value="Pai na", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/833705700097523732.gif?v=1&size=40')
        elif situatie == 6:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name="Hahahahahhhahahahh", value=f"{member.mention} eu i-as da un pumn înapoi in locul tau",
                            inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/828281668628119604.gif?v=1&size=40')
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        embed.timestamp = datetime.utcnow()
        await ctx.reply(embed=embed)

    @commands.command()
    async def tttest(self, ctx):
        embed = discord.Embed(
            title="Ceva", description="[ceva](https://youtube.com)", color=discord.Color.green())
        await ctx.send(embed=embed)

    @commands.command(aliases=['alegere', 'alege'])
    async def choose(self, ctx, *, alegeri):
        try:
            alegere1, alegere2 = alegeri.split(',')
        except:
            await ctx.reply("Te rog delimiteaza prin virgula ce trebuie sa aleg. (ex: `.alege smecherie, jmecherie`)")
            return
        random = randint(1, 2)
        embed = discord.Embed(title="", description=f"", color=discord.Color.green())
        if random == 1:
            variante = randint(1, 4)
            if variante == 1:
                embed.add_field(name="Hmmm", value=f"Cred ca **{alegere1}**")
            elif variante == 2:
                embed.add_field(name="Hmmm", value=f"Aleg **{alegere1}**")
            elif variante == 3:
                embed.add_field(name="Hmmm", value=f"Greu de ales, da zic că **{alegere1}**")
            elif variante == 4:
                embed.add_field(name="Uh oh", value=f"Presupun că **{alegere1}**")
        elif random == 2:
            variante = randint(1, 4)
            if variante == 1:
                embed.add_field(name="Hmmm", value=f"Cred ca **{alegere2}**")
            elif variante == 2:
                embed.add_field(name="Hmmm", value=f"Aleg **{alegere2}**")
            elif variante == 3:
                embed.add_field(name="Hmmm", value=f"Greu de ales, da zic că **{alegere2}**")
            elif variante == 4:
                embed.add_field(name="Uh oh", value=f"Presupun că **{alegere2}**")
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_author(icon_url="https://cdn.discordapp.com/emojis/830008622188331020.gif?v=1&size=40",
                         name="Alegător suprem")
        await ctx.reply(embed=embed)

    @commands.command(aliases=['penis', "pula", "pulă"])
    async def pp(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        random = randint(0, 17)
        embed = discord.Embed(
            title="", description="", color=discord.Color.green())
        embed.set_footer(text="In caz de e mica, nu sunt stricat. Doar o ai mica .")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/783472322022998016.png?v=1")
        embed.set_author(name="Măsurător", icon_url="https://cdn.discordapp.com/emojis/794221782596452423.gif?v=1")
        if random == 0:
            embed.add_field(name="Huh", value=f"N-am gasit nimic acolo jos , {member}")
        else:
            ppp = "8"
            for i in range(random):
                ppp = ppp + "="
            ppp = ppp + "D"
            embed.add_field(name=f"Penisul lui {member}", value=f"{ppp}")
        await ctx.reply(embed=embed)

    @commands.command()
    async def party(self, ctx):
        await ctx.channel.purge(limit=1)
        guild = self.client.get_guild(619454105869352961)
        party1 = get(guild.emojis, name='pd_party1')
        party2 = get(guild.emojis, name='pd_party2')
        party3 = get(guild.emojis, name='pd_party3')
        party4 = get(guild.emojis, name='pd_party4')
        party5 = get(guild.emojis, name='pd_party5')
        party6 = get(guild.emojis, name='pd_party6')
        await ctx.send(f"{party1}{party2}{party3}{party4}{party5}{party6}")

    def not_everyone(ctx):
        return not any(m in ctx.message.content.lower() for m in
                       ["@here", "@everyone", "discord.gg", "http", ".com", ".net", ".ro", "nigga"])

    @commands.command(aliases=['say'])
    @commands.check(not_everyone)
    async def spune(self, ctx, *, text=None):
        if text == None:
            await ctx.reply(f"{ctx.author.mention} e prost tare")
            return
        await ctx.channel.purge(limit=1)
        await ctx.send(f"{text}")

    @commands.command(aliases=['adminsay'])
    @commands.has_permissions(administrator=True)
    async def adminspune(self, ctx, *, text=None):
        await ctx.channel.purge(limit=1)
        await ctx.send(f"{text}")

    @commands.command(aliases=['anunt', 'anunț'])
    @commands.has_permissions(administrator=True)
    async def announcement(self, ctx, *, text=None):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title="", description="", color=discord.Color.green())
        embed.add_field(
            name="Roluri xp",
            value=text
        )
        embed.set_footer(text="Pentru a vedea cat xp ai, foloseste comanda .xp")
        await ctx.send(embed=embed)


    @commands.command()
    async def trivia(self, ctx):
      with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
      intrebari={"Al cui caine este Scooby Doo?":"Freddie,Shaggy,Daphne,Velma","Ale cui erau caprele de la care Nica a luat raie?": "Smarandei,Matusei Marioara,Irinucai,Isabelei","Amnezia este pierderea . . .":"poftei de mancare,auzului,vederii,memoriei","Aproximativ in ce procent se gaseste Oxigenul in aer?":"21%,15%,16%,75%","Cand a avut loc revolutia in urma careia a fost inlaturat Nicolae Ceausescu?":"decembrie 1990,decembrie 1989,decembrie 1991,decembrie 1988","Care a fost capitala Imperiului Bizantin ?":"Roma,Ierusalim,Atena,Constantinopol","Care a fost a treia proba pe care Aleodor imparat a trebui sa o treaca pentru fata lui Verde Imparat?":"sa separe graul de orz,sa aduca capul omului Span,sa se ascunda de ea,sa o gaseasca","Care a fost numele initial al lui Muhammad Ali inainte sa treaca la islamism?":"Cassius Clay,Muhammad John,Sam Longford,Joe Louis","Care a fost prima persoana care a pasit pe luna?":"Yuri Gagarin,Neil Armstrong,Edward H. White,niciuna","Care a fost prima persoana care a pasit pe marte?":"Yuri Gagarin,Neil Armstrong,Edward H. White,niciuna","Care a fost prima persoana ce a facut inconjurul lumii?":"Amerigo Vespuci,Jules Verne,Phileas Fogg,Ferdinand Magellan","Care a fost primul aparat care putea inregistra si reproduce sunetele?":"casetofonul,fonograful,gramofonul,diapazonul","Care a fost primul model de masina Dacia?":"Dacia 100,Dacia1310,Dacia 1100,Dacia 1001","Care a fost profesorul de limba romana a lui Mihai Eminescu?":"Iosif Vulcan,Titu Maiorescu,Matei Millo,Aron Pumnul","Care din personajele romanului Ion s-a spazurat?":"Ana,Florica,Ion,George","Care din urmatoarele cuvinte este o forma corecta?":"amindurora,amindurora,amindurura,amandoura","Care din urmatoarele cuvinte este un sinonim pentru “solomonit”?":"fastuos,morocanos,dizolvabil,fermecat","Care din urmatoarele elemente nu este o ramura a biologiei?":"Virusologie,Biochimie,Micologie,Zoologie","Care din urmatoarele personaje de animatie nu au fost creatia lui Joseph Barbera?":"Scooby Doo,Familia Flinstone,Bambi,The Jetsons","Care din urmatoarele personaje nu apartin operei Vrajitorul din oz":"Geppetto,Dorothy Gale,Totto,Ozma","Care din urmatoarele personaje nu apartine filmului Mica sirena?":"Regele Triton,Ursula,Orland,Scuttle","Care din urmatoarele personaje nu face parte din “Povestea lui Harap-Alb”?":"Omul Span,Verde-Imparat,Omul Ros,Imparatul de la Miazanoapte","Care din urmatoarele personaje nu face parte din nuvela “Padureanca”?":"Simona,Busuioc,Iorgovan,Sofron","Care din urmatoarele personaje nu face parte din romanul “La Medeleni”?":"Olguta,Daut,Alina,Monica","Care dintre urmatoarele planete NU este numita “superioara”?":"Mercur,Jupiter,Neptun,Uranus","Ce este Modemul?":"Modulator/Demodulator,Modulator,Megaondulator,Miniondulator"}
      raspunsuri={"Al cui caine este Scooby Doo?":2,"Ale cui erau caprele de la care Nica a luat raie?":3,"Amnezia este pierderea . . .":4,"Aproximativ in ce procent se gaseste Oxigenul in aer?":1,"Cand a avut loc revolutia in urma careia a fost inlaturat Nicolae Ceausescu?":2,"Care a fost capitala Imperiului Bizantin ?":4,"Care a fost a treia proba pe care Aleodor imparat a trebui sa o treaca pentru fata lui Verde Imparat?":3,"Care a fost numele initial al lui Muhammad Ali inainte sa treaca la islamism?":1,"Care a fost prima persoana care a pasit pe luna?":2,"Care a fost prima persoana care a pasit pe marte?":4,"Care a fost prima persoana ce a facut inconjurul lumii?":4,"Care a fost primul aparat care putea inregistra si reproduce sunetele?":2,"Care a fost primul model de masina Dacia?":3,"Care a fost profesorul de limba romana a lui Mihai Eminescu?":4,"Care din personajele romanului Ion s-a spazurat?":1,"Care din urmatoarele cuvinte este o forma corecta?":2,"Care din urmatoarele cuvinte este un sinonim pentru solomonit?":4,"Care din urmatoarele elemente nu este o ramura a biologiei?":2,"Care din urmatoarele personaje de animatie nu au fost creatia lui Joseph Barbera?":3,"Care din urmatoarele personaje nu apartin operei Vrajitorul din oz":1,"Care din urmatoarele personaje nu apartine filmului “Mica sirena”?":3,"Care din urmatoarele personaje nu face parte din “Povestea lui Harap-Alb”?":4,"Care din urmatoarele personaje nu face parte din nuvela Padureanca?":1,"Care din urmatoarele personaje nu face parte din romanul “La Medeleni”?":3,"Care dintre urmatoarele planete NU este numita “superioara”?":1,"Ce este Modemul?":1}
      n=randint(1,len(intrebari))
      i=1
      for key in intrebari.items():
        if i==n:
          embed = discord.Embed(title="Trivia", description="Alege rapsunul corect! Ai 15 secunde", color=discord.Color.green())
          embed.set_thumbnail(url="https://www.brightful.me/content/images/2021/06/1.jpg")
          embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
          embed.timestamp = datetime.utcnow()
          embed.add_field(name=f"Intrebarea este:", value=key[0])
          b=key[1]
          print(b)
          x,y,z,k=b.split(",")
          components = [Select(
            placeholder = 'Alege raspunsul de aici',
            options = [
              SelectOption(label=x, value="1"),
              SelectOption(label=y, value="2"),
              SelectOption(label=z, value="3"),
              SelectOption(label=k, value = "4")
            ])]
          msg=await ctx.reply(embed=embed,components=components)
          def check(msg):
            return msg.author.id == ctx.author.id and msg.channel.id == ctx.channel.id
          ok=1
          while ok==1:
            try:
              res = await self.client.wait_for("select_option", check=check, timeout=15)
              label = res.values[0]
              ok=0
              if int(label)==int(raspunsuri[key[0]]):
                await res.respond(content="Felictari! Ai raspuns corect")
                embed.add_field(name=f"✅ Raspuns corect", value="gg")
                await msg.edit(embed=embed,components=[])
                return
              else:
                await res.respond(content="Gresit patroane.")
                embed.add_field(name=f"⛔ Raspuns gresit", value="ehh")
                await msg.edit(embed=embed,components=[])
                return
            except asyncio.TimeoutError:
                await ctx.send("A trecut timpul.")
                embed.add_field(name=f"⛔ Timp expirat", value="ghinion")
                await msg.edit(embed=embed,components=[])
                return
            except discord.NotFound:
                await msg.edit(embed=embed,components=[])
                print("error")
                return
        else:
          i=i+1







    @commands.command()
    async def porumbel(self, ctx, member: discord.Member = None, *, text=None):
        if member == None:
            await ctx.reply("Cui ii trimiți un porumbel?")
            return
        lista = text.split(" ")
        for k in lista:
            cuvant = k
        if cuvant.upper() == "(ANONIM)":
            embed = discord.Embed(
                title="Un anonim iti transmite:", description=text[:-len(cuvant)], color=discord.Color.green())
            embed.set_footer(
                text="Poti folosi si tu comanda .porumbel + mesaj (lasa '(Anonim)' la sfarsitul mesajului daca vrei sa fi anonim")
            await member.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f"{ctx.author.name} iti transmite:", description=text, color=discord.Color.green())
            embed.set_footer(
                text="Poti folosi si tu comanda .porumbel + mesaj (lasa '(Anonim)' la sfarsitul mesajului daca vrei sa fi anonim")
            await member.send(embed=embed)
        await ctx.message.delete()
        mesaj = await ctx.send("que's-ce tu feit")
        await mesaj.delete()

    @commands.command(aliases=['gayrate'])
    async def howgay(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        random = randint(0, 100)
        embed = discord.Embed(
            title="", description="", color=discord.Color.green())
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        embed.timestamp = datetime.utcnow()
        embed.add_field(name=f"Cat de gay e {member}", value=f"{member.mention} e atat de gay : {random}%")
        await ctx.reply(embed=embed)

    @commands.command()
    async def simp(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        random = randint(0, 100)
        embed = discord.Embed(
            title="", description="", color=discord.Color.green())
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        embed.timestamp = datetime.utcnow()
        embed.add_field(name=f"Cat de simp e {member}", value=f"{member.mention} e atat de simp : {random}%")
        await ctx.reply(embed=embed)

    @commands.command()
    async def ship(self, ctx, member1: discord.Member = None, member2: discord.Member = None):
        if member1 == None and member2 == None:
            embed = discord.Embed(title="", description="", color=discord.Color.green())
            embed.add_field(name="???", value="Pe cine combini ma")
            await ctx.reply(embed=embed)
            return
        elif member2 == None:
            member2 = ctx.author
        guild = member1.guild
        if member1.id == 790607817128017920 or member2.id == 790607817128017920:
            await ctx.reply("Ma voi vreti scandal")
            return
        padurar = discord.utils.get(guild.roles, name='Padurar la Băneasa')
        if padurar in member1.roles:
            await ctx.reply("0%, am gagica fa-ti si tu.")
            return
        if padurar in member2.roles:
            await ctx.reply("0%, am gagica faceti-va si voi 😤.")
            return
        random = randint(0, 100)
        if ctx.author.id == 306769101592985610 and (
                member1.id == 306769101592985610 or member2.id == 306769101592985610):
            random = randint(50, 100)
        if (member1.id == 610574071629086746 and member2.id == 744336324865294356) or (
                member2.id == 610574071629086746 and member1.id == 744336324865294356):
            random = randint(0, 69)
        if (member1.id == 306769101592985610 and member2.id == 470995082145824798) or (
                member2.id == 306769101592985610 and member1.id == 470995082145824798):
            random = 0
        if random <= 50:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name=f"Calculator de combinații",
                            value=f"{member1.mention} e compatibil cu {member2.mention} in proportie de {random}%")
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/735155822736179201/831858603899486229/unknown.png')
            embed.set_footer(text="Va combinati pe discord wtf.")
        else:
            embed = discord.Embed(
                title="", description="", color=discord.Color.from_rgb(255, 182, 193))
            embed.add_field(name=f"Calculator de combinații",
                            value=f"{member1.mention} e compatibil cu {member2.mention} in proportie de {random}%")
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/735155822736179201/831857865312305222/807012569750437888.gif')
            embed.set_footer(text="V-ar sta bine cred.")
        await ctx.reply(embed=embed)

    @commands.command()
    async def fraier(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        random = randint(0, 100)
        embed = discord.Embed(
            title="", description="", color=discord.Color.green())
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        embed.timestamp = datetime.utcnow()
        embed.add_field(name="Calculator de prostie", value=f"{member.mention} e atat de fraier : {random}%")
        await ctx.reply(embed=embed)

    @commands.command(aliases=['kiss', 'pwp'])
    async def pup(self, ctx, member: discord.Member = None):
        if member == None:
            embed = discord.Embed(title="", decription="", color=discord.Color.green())
            embed.add_field(name=f'????', value="Pe cine pupi mă")
            await ctx.reply(embed=embed)
            return
        else:
            sansa = randint(0, 100)
            if sansa < 10:
                embed = discord.Embed(title="", description="", color=discord.Color.green())
                embed.add_field(name=f"Pfaiaiaia", value=f"{ctx.author.mention} ce-ti pute gura vere")
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/735155822736179201/831858603899486229/unknown.png')
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                await ctx.reply(embed=embed)
                return
            embed = discord.Embed(title="", description="", color=discord.Color.from_rgb(255, 182, 193))
            # embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/834101384504672347.png?v=1")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/726174197931573398/860244442479853608/809234952570011676.jpg")
            embed.add_field(name=f'Ce drăguț!!!', value=f"{ctx.author.mention} âi da un pupik lui {member.mention}")
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()

        voterandom = randint(1, 5)
        if voterandom == 3:
            #msg = await ctx.reply(embed=embed, components=[Button(style=5, label="Voteaza-ma pe top.gg!", url="https://top.gg/bot/790607817128017920",custom_id="vot")])
            msg = await ctx.reply(embed=embed, components=[
                Button(style=5, label="Voteaza-ma pe top.gg!",
                       url="https://top.gg/bot/885503634710884412", custom_id="vot")])
            while ctx.message != None:
                try:
                    interaction = await self.client.wait_for("button_click", check=lambda i: i.custom_id == "vot",
                                                             timeout=40)
                except:
                    await msg.edit(embed=embed, components=[])
                    return
        else:
            await ctx.reply(embed=embed)

    @commands.command(aliases=['penisfight'])
    async def ppfight(self, ctx, membru: discord.Member = None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()

        async def penisptppfight(ctx, membru: discord.Member = None):
            random = randint(0, 17)
            with open("pad/data/data.json", "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()
            with open("pad/data/data.json", "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()
            if f"ppfight{ctx.author.id}" not in data:
                data[f"ppfight{ctx.author.id}"] = 0
            if f"ppfight{membru.id}" not in data:
                data[f"ppfight{membru.id}"] = 0
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.set_footer(text="In caz de e mica, nu sunt stricat. Doar o ai mica .")
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/783472322022998016.png?v=1")
            embed.set_author(name="Măsurător", icon_url="https://cdn.discordapp.com/emojis/794221782596452423.gif?v=1")
            if random == 0:
                embed.add_field(name="Huh", value=f"N-am gasit nimic acolo jos , {membru}")
            else:
                ppp = "8"
                for i in range(random):
                    ppp = ppp + "="
                ppp = ppp + "D"
                embed.add_field(name=f"Penisul lui {membru}", value=f"{ppp}")
            await ctx.send(embed=embed)
            return random

        if membru == None:
            await ctx.send("Cu cine te bati?")
            return
        if membru.id == ctx.author.id:
            await ctx.send("Te bati singur?")
            return
        await ctx.send(
            f"{membru.mention}, esti provocat la duel de catre {ctx.author.mention}. Accepti acest pp fight? Ai 15 secunde sa raspunzi. (scrie DA sau NU)")

        def raspuns(m):
            return m.channel.id == ctx.channel.id and m.author.id == membru.id

        try:
            msg = await self.client.wait_for('message', check=raspuns, timeout=15)
        except asyncio.TimeoutError:
            await ctx.send(f"Bruh n-a raspuns {membru.mention} plebul")
            return
        if ("DA" not in msg.content.upper() and "YES" not in msg.content.upper()) and (
                "NU" not in msg.content.upper() and "NO" not in msg.content.upper()):
            await ctx.send(f"Raspuns gresit {membru.mention}, trebuia sa zici da sau nu")
            return
        if "DA" in msg.content.upper() or "YES" in msg.content.upper():
            random1 = await penisptppfight(ctx, membru)
            random2 = await penisptppfight(ctx, ctx.author)
            if random1 > random2:
                await ctx.send(f"CASTIGATOR: {membru.mention}")
                data[f"ppfight{membru.id}"] = int(data[f"ppfight{membru.id}"]) + 1
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
            elif random1 < random2:
                await ctx.send(f"CASTIGATOR: {ctx.author.mention}")
                data[f"ppfight{ctx.author.id}"] = int(data[f"ppfight{ctx.author.id}"]) + 1
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
            else:
                await ctx.send("Egalitéé")
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
        if "NU" in msg.content.upper() or "NO" in msg.content.upper():
            await ctx.send("Ce pleb")
            return

    @commands.command(aliases=['pptop'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def fighttop(self, ctx, nr: int = 1):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        match_keys = res = {key: val for key, val in data.items() if key.startswith("ppfight")}
        if len(match_keys) > 15:
            mesaj = await ctx.reply("stai asa, generez topul...")
        else:
            mesaj = None
        sort = sorted(match_keys, key=lambda x: data[x], reverse=True)

        i = (nr - 1) * 5
        j = nr * 5
        if len(sort) < j:
            j = len(sort)
        embed = discord.Embed(title="", description="", color=discord.Color.green())
        embed.set_author(name="Topul p*nisurilor in padure",
                         icon_url="https://cdn.discordapp.com/attachments/745384647885848594/864852166433570856/89a9a37af2f4387bc8293ae4dacfb4c4.jpg")
        # embed = discord.Embed(title="Top puncte ", description="in padurea Baneasa", color=discord.Color.green())
        if i >= j:
            ctx.eroare
        while i < j:
            key = sort[i]
            xp = int(data[key])
            if xp != 0:
                id = int(key[7:])
                try:
                    user = await self.client.get_user(id)
                    print(user.id)
                except:
                    user = await self.client.fetch_user(id)
                embed.add_field(name=f"#{i + 1}", value=f"**🌲 {user.display_name}** are {xp} castiguri")
                i = i + 1
        embed.set_footer(text=f"foloseste comanda .top {nr + 1} pentru a vede următoarea pagina",
                         icon_url="https://freepikpsd.com/media/2019/11/emoji-meme-png-4-Transparent-Images.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/781911253458354256.png?v=1&size=40")
        if mesaj is not None:
            await mesaj.delete()
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.cooldown(1, 7200, commands.BucketType.user)
    async def muie(self, ctx, member: discord.Member = None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if member == None:
            await ctx.send("Cui dai 😳😳😳?")
            ctx.command.reset_cooldown(ctx)
            return
        if member.id == ctx.author.id:
            await ctx.send("Asta e ciudat!")
            ctx.command.reset_cooldown(ctx)
            return
        if f"mue{member.id}" not in data:
            data[f"mue{member.id}"] = 1
        else:
            data[f"mue{member.id}"] = data[f"mue{member.id}"] + 1
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()
        embed = discord.Embed(title="", description="", color=discord.Color.green())
        embed.add_field(name=f'HAHA', value=f"Domnul {member.mention} a fost m*it de către {ctx.author.mention}")
        embed.set_footer(text="pentru a vedea cate mui are cineva foloseste comanda .mui")
        await ctx.send(embed=embed)

    @muie.error
    async def muie_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            timp = error.retry_after / 60
            em = discord.Embed(title=f"HOOOO DOMNULE",
                               description=f" Ai de asteptat {timp:.2f} minute pana poti mu* pe cnv iar",
                               color=discord.Color.green())
            await ctx.reply(embed=em)

    @commands.command()
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def mui(self, ctx, member: discord.Member = None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if member == None:
            member.id = ctx.author.id
        embed = discord.Embed(title="", description="", color=discord.Color.green())
        if f"mue{member.id}" not in data:
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/745384647885848594/864479690550542346/740295657117581372.jpg")
            if member.id == ctx.author.id:
                embed.add_field(name=f'Woah!', value=f"Domnule {member.mention}, n-ai primit nicio mu*e !")
            else:
                embed.add_field(name=f'Woah!', value=f"Domnul {member.mention} n-a primit nicio mu*e !")
        else:
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/745384647885848594/864479410811699200/825684334572339211-1.jpg")
            mue = data[f"mue{member.id}"]
            if member.id == ctx.author.id:
                embed.add_field(name=f'Haha!', value=f"Domnule {member.mention}, ai primit {mue} mui !")
            else:
                embed.add_field(name=f'Haha!', value=f"Domnul {member.mention} a primit {mue} mui !")
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)

    @mui.error
    async def mui_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"HOOOO DOMNULE",
                               description=f" Ai de asteptat {error.retry_after:.0f} minute pana poti vedea mu*le iar",
                               color=discord.Color.green())
            await ctx.reply(embed=em)

    @commands.command(aliases=['seggs', 'seggz', 'secs', 'fute', 'futai', 'dragoste'])
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def sex(self, ctx, member: discord.Member = None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        guild = ctx.guild
        if member.id == ctx.author.id:
            await ctx.reply("ba, fara l*ba ma")
            return
        if member == None:
            if f"Casatorit{ctx.author.id}" in data:
                sotid = data[f"Casatorit{ctx.author.id}"]
                member = guild.get_member(int(sotid))
            else:
                await ctx.reply("wtf faci sex singur?")
                return
        prob=randint(1,8)
        if f"Casatorit{ctx.author.id}" in data and int(data[f"Casatorit{ctx.author.id}"]) != 0 and int(data[f"Casatorit{ctx.author.id}"]) != member.id:
          if prob==4:
            if f"Casatorit{member.id}" in data and int(data[f"Casatorit{member.id}"]) != 0 and int(data[f"Casatorit{member.id}"]) != ctx.author.id:
              sot1 = int(data[f"Casatorit{ctx.author.id}"])
              sot2 = int(data[f"Casatorit{member.id}"])
              await ctx.send(
                    f"<@{sot1}>, <@{sot2}> vedeti ca partenerii vostri de viata au facut **sex IMPREUNA CEMAMAMEA**")
            else:
              sot1 = int(data[f"Casatorit{ctx.author.id}"])
              await ctx.send(f"<@{sot1}>, ai grija ca {ctx.author.mention} te inseala.")
        if f"Casatorit{member.id}" in data and int(data[f"Casatorit{member.id}"]) != 0 and int(
                data[f"Casatorit{member.id}"]) != ctx.author.id:
            if f"Casatorit{ctx.author.id}" not in data or int(data[f"Casatorit{ctx.author.id}"]) == 0:
                sot1 = int(data[f"Casatorit{member.id}"])
                await ctx.send(f"<@{sot1}>, ai grija ca {member.mention} te inseala.")
        situatie = randint(1, 10)
        if situatie == 1:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name="Wtf", value=f"Ai facut sex cu {member.mention} dar ai foot fetish", inline=True)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/874999910863364177.gif?v=1&size=40')
        elif situatie == 2:
            embed = discord.Embed(
                title="", description="", color=discord.Color.from_rgb(255, 182, 193))
            embed.add_field(name="Frumos", value=f"L-ai satisfacut pe {member.mention}", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/828260808608972801.gif?v=1&size=40')
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
        elif situatie == 3:
            embed = discord.Embed(
                title="", description="", color=discord.Color.from_rgb(255, 182, 193))
            embed.add_field(name="Mmmmmm", value=f"Ai facut seggs senzual cu {member.mention}", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/828282925102923806.gif?v=1&size=40')
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
        elif situatie == 4:
            embed = discord.Embed(
                title="", description="", color=discord.Color.from_rgb(255, 182, 193))
            embed.add_field(name="Sex...", value=f"...pe covor cu {member.mention}", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/792574177139621909.gif?v=1&size=40')
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
        elif situatie == 5:
            embed = discord.Embed(
                title="", description="", color=discord.Color.from_rgb(255, 182, 193))
            embed.add_field(name="Felicitari!", value=f"Ai procreat un copil cu {member.mention}", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/795275310349418497.gif?v=1&size=40')
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
        elif situatie == 6:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name="Uhhhh", value=f"Cred ca vei fi mamica {member.mention}", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/821053795726655518.png?v=1&size=40')
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
        elif situatie == 6:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name="Uhhhh", value=f"Cred ca vei fi tatic {member.mention}", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/821053795726655518.png?v=1&size=40')
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
        if situatie == 7:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name="Scuze",
                            value=f"{member.mention} ti-a refuzat cererea de sex, motiv: `o are mica da-l dracu`",
                            inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/825735245965950996.gif?v=1&size=40')
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
        if situatie == 8:
            embed = discord.Embed(
                title="", description="", color=discord.Color.green())
            embed.add_field(name="Scuze", value=f"{member.mention} ti-a refuzat cererea de sex, motiv: `sunt gay`",
                            inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/788522211161407498.gif?v=1&size=40')
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
        elif situatie == 9:
            embed = discord.Embed(
                title="", description="", color=discord.Color.from_rgb(255, 182, 193))
            embed.add_field(name="Woah woah be careful",
                            value=f"Ai procreat un copil cu {member.mention}, poti ramane bankrupt", inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/879375203040391169.gif?v=1&size=40')
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
        elif situatie == 10:
            embed = discord.Embed(
                title="", description="", color=discord.Color.from_rgb(255, 182, 193))
            timp = randint(2, 44)
            embed.add_field(name="Sunteti tari", value=f"Ai facut sex cu {member.mention} timp de {timp} ore",
                            inline=True)
            embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/736665975939792936.gif?v=1&size=40')
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
        voterandom = randint(1, 5)
        if voterandom == 3:
            #msg = await ctx.reply(embed=embed, components=[Button(style=5, label="Voteaza-ma pe top.gg!", url="https://top.gg/bot/790607817128017920",custom_id="vot1")])
            msg = await ctx.reply(embed=embed, components=[
                Button(style=5, label="Voteaza-ma pe top.gg!", url="https://top.gg/bot/885503634710884412",custom_id="vot1")])
            while ctx.message != None:
                try:
                    interaction = await self.client.wait_for("button_click", check=lambda i: i.custom_id == "vot1",
                                                             timeout=40)
                except:
                    await msg.edit(embed=embed, components=[])
                    return
        else:
            await ctx.reply(embed=embed)

    @sex.error
    async def sex_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"HOOOO DOMNULE",
                               description=f" Ai de asteptat {error.retry_after:.0f} secunde pana poti face seggs iar",
                               color=discord.Color.green())
            await ctx.reply(embed=em)

    @commands.command()
    async def cuddle(self, ctx, member: discord.Member = None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"Casatorit{ctx.author.id}" not in data or data[f"Casatorit{ctx.author.id}"] == 0:
            await ctx.reply("Poti sa teiubesti doar cu sotul/sotia")
            return
        id = data[f"Casatorit{ctx.author.id}"]
        sott = self.client.get_user(id)
        if member is not None:
            if member is not sott:
                await ctx.reply("Poti sa teiubesti doar cu sotul/sotia")
                return
        random = randint(1, 9)
        if random == 1:
            sot = data[f"Casatorit{ctx.author.id}"]
            data[f"Casatorit{ctx.author.id}"] = 0
            data[f"Casatorit{sot}"] = 0
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            embed = discord.Embed(title="", decription="", color=discord.Color.green())
            embed.add_field(name=f'Ce prost',
                            value="Ti-ai strans partenerul prea tare si a murit. Sunteti divorțați acum.")
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.reply(embed=embed)
        elif random == 2:
            id = data[f"Casatorit{ctx.author.id}"]
            sot = self.client.get_user(id)
            embed = discord.Embed(title="", decription="", color=discord.Color.green())
            embed.add_field(name=f'Ce prost', value=f"Ti s-a sculat unealta si {sot.mention} s-a speriat .")
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.reply(embed=embed)
        elif random == 3:
            id = data[f"Casatorit{ctx.author.id}"]
            sot = self.client.get_user(id)
            embed = discord.Embed(title="", decription="", color=discord.Color.green())
            embed.add_field(name=f'Ce dragut!!', value=f"Tu si {sot.mention} va iubiti probabil.")
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.reply(embed=embed)
        elif random == 4:
            id = data[f"Casatorit{ctx.author.id}"]
            sot = self.client.get_user(id)
            embed = discord.Embed(title="", decription="", color=discord.Color.green())
            embed.add_field(name=f'Bruh', value=f"Bruh")
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.reply(embed=embed)
        elif random == 5:
            id = data[f"Casatorit{ctx.author.id}"]
            sot = self.client.get_user(id)
            embed = discord.Embed(title="", decription="", color=discord.Color.green())
            embed.add_field(name=f'Ce dragut!!', value=f"Ti-ai imbratisat amanta, vezi sa nu stie {sot}")
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.reply(embed=embed)
        elif random == 6:
            id = data[f"Casatorit{ctx.author.id}"]
            sot = self.client.get_user(id)
            embed = discord.Embed(title="", decription="", color=discord.Color.green())
            embed.add_field(name=f'oh wow', value=f"e ariana grand")
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.reply(embed=embed)
        elif random == 7:
            id = data[f"Casatorit{ctx.author.id}"]
            sot = self.client.get_user(id)
            embed = discord.Embed(title="", decription="", color=discord.Color.green())
            embed.add_field(name=f'Misto', value=f"Tu si {sot} va iubiti reciproc.")
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.reply(embed=embed)
        elif random == 8:
            id = data[f"Casatorit{ctx.author.id}"]
            sot = self.client.get_user(id)
            embed = discord.Embed(title="", decription="", color=discord.Color.green())
            embed.add_field(name=f'Aaaah ghinion', value=f"Ti-ai pierdut v-cardul.")
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.reply(embed=embed)
        elif random == 9:
            id = data[f"Casatorit{ctx.author.id}"]
            sot = ctx.guild.get_member(id)
            await ctx.reply("Ati recurs la segss!")
            sex(self, ctx, sot)

    @commands.command(aliases=['casatorie', 'căsătorie', 'casatotie', 'căsatorie', 'casătorie'])
    # @commands.cooldown(1, 7200, commands.BucketType.user)

    async def marry(self, ctx, member: discord.Member = None, *, mesaj=None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if member == None:
            await ctx.reply("cu cn te casatoresti??")
            ctx.command.reset_cooldown(ctx)
            return
        if f"parinte{ctx.author.id}" in data and data[f"parinte{ctx.author.id}"] == member.id:
            await ctx.reply("sweet home alabama")
            ctx.command.reset_cooldown(ctx)
            return
        if f"copil{ctx.author.id}" in data and data[f"copil{ctx.author.id}"] == member.id:
            await ctx.reply("sweet home alabama")
            ctx.command.reset_cooldown(ctx)
            return
        guild = member.guild
        padurar = discord.utils.get(guild.roles, name='Padurar la Băneasa')
        gardian = discord.utils.get(guild.roles, name='Protectori')
        if padurar in member.roles:
            await ctx.reply("Am gagica bro.")
            return
        if gardian in member.roles:
            await ctx.reply("Are gagica bro.")
            ctx.command.reset_cooldown(ctx)
            return
        if member == ctx.author:
            await ctx.reply("wtf")
            ctx.command.reset_cooldown(ctx)
            return
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"Casatorit{member.id}" not in data:
            data[f"Casatorit{member.id}"] = 0
        if f"Casatorit{ctx.author.id}" not in data:
            data[f"Casatorit{ctx.author.id}"] = 0
        if f"Cer{member.id}" not in data:
            data[f"Cer{member.id}"] = 0
        if f"Cer{ctx.author.id}" not in data:
            data[f"Cer{ctx.author.id}"] = 0
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()
        if data[f"Casatorit{ctx.author.id}"] != 0:
            embed = discord.Embed(title="Calm ba playboy", description="Esti casatorit deja", color=discord.Color.green())
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.reply(embed=embed)
            ctx.command.reset_cooldown(ctx)
            return
        if data[f"Casatorit{member.id}"] != 0:
            embed = discord.Embed(title="Calm ba playboy", description="E casatorit deja", color=discord.Color.green())
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            await ctx.reply(embed=embed)
            ctx.command.reset_cooldown(ctx)
            return

        if data[f"Cer{ctx.author.id}"] == member.id:
            data[f"Casatorit{member.id}"] = ctx.author.id
            data[f"Casatorit{ctx.author.id}"] = member.id
            data[f"Cer{ctx.author.id}"] = 0
            data[f"Cer{member.id}"] = 0
            data[f"datacasatoriei{ctx.author.id}"]=str(datetime.now())
            data[f"datacasatoriei{member.id}"]=str(datetime.now())
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            embed = discord.Embed(title="FELICITARI", description="Sunteti casatoriti!!!!!!!", color=discord.Color.from_rgb(255, 182, 193))
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/745384647885848594/948598560180539432/916794662335950928.gif')
            await ctx.reply(embed=embed)
        else:
            data[f"Cer{member.id}"] = ctx.author.id
            embed = discord.Embed(title="Ai putina rabdare!", description="I-am trimis o cerere in casatorie.", color=discord.Color.from_rgb(255, 182, 193))
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/745384647885848594/948597675064954931/940192094981611521.gif')
            await ctx.reply(embed=embed)
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            if mesaj != None:
                await member.send(f"""**Domnul {ctx.author} te-a cerut in casatorie .**
Pentru a accepta cererea , scrie .casatorie @{ctx.author} pe serverul `{ctx.guild.name}`.

Mesajul lui: 
```
{mesaj}
```""")
            else:
                await member.send(f"""**Domnul {ctx.author} te-a cerut in casatorie .**
Pentru a accepta cererea , scrie .casatorie @{ctx.author} pe serverul `{ctx.guild.name}`.""")

    @marry.error
    async def marry_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"HOOOO DOMNULE",
                               description=f" Ai de asteptat {(error.retry_after / 60):.0f} minute pana te poti casatori iar!",
                               color=discord.Color.green())
            await ctx.reply(embed=em)

    @commands.command(aliases=['adoptie', 'adopție', 'adoptare'])
    async def adopt(self, ctx, member: discord.Member = None, *, mesaj=None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if member == None:
            await ctx.reply("pe cn adopti??")
            return
        if f"parinte{member.id}" in data and data[f"parinte{member.id}"] != 0:
            await ctx.reply("baiatu' are părinți.")
            return
        if f"parinte{ctx.author.id}" in data and data[f"parinte{ctx.author.id}"] == member.id:
            await ctx.reply("iti adopti parintii wtf.")
            return
        if member.id == ctx.author.id:
            await ctx.reply("te adopti singur wtf??")
            return
        if f"Casatorit{member.id}" in data and data[f"Casatorit{member.id}"] == ctx.author.id:
            await ctx.reply("bruh iti adopti soțul/sotia?.")
            return
        if f"nrcopii{ctx.author.id}" in data and data[f"nrcopii{ctx.author.id}"] == 1:
            await ctx.reply("ai copil patroane , mai lasa si la altii.")
            return
        data[f"cererepar{member.id}"] = ctx.author.id
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()

        await ctx.reply(
            f"Bn, {member.mention} nesilit de nimeni accepti cererea de adopție? (scrie .accept_adoptie daca da)")
        await member.send(
            f"Neata. **{ctx.author}** încearcă sa te adopte. Pentru a accepta cererea, spune .accept_adoptie pe  serverul {ctx.guild.name}")

    @commands.command(aliases=['accept_adopt'])
    async def accept_adoptie(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"cererepar{ctx.author.id}" not in data or data[f"cererepar{ctx.author.id}"] == 0:
            await ctx.reply("n-ai nicio cerere de adopție")
            return
        member = data[f"cererepar{ctx.author.id}"]
        if f"Casatorit{ctx.author.id}" in data and data[f"Casatorit{member}"] == ctx.author.id:
            await ctx.reply(f"bruh esti casatorit cu <@{member}>.")
            return
        if f"nrcopii{member}" in data and data[f"nrcopii{member}"] != 0:
            await ctx.reply("ti-a luat-o inainte alt copil, la cersit cu tine.")
            return
        data[f"parinte{ctx.author.id}"] = member
        data[f"cererepar{ctx.author.id}"] = 0
        data[f"nrcopii{member}"] = 1
        data[f"copil{member}"] = ctx.author.id
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()
        await ctx.reply("o sa iti ia alocatia. gg ai părinți!!!")

    @commands.command(aliases=['casadecopii'])
    async def orfelinat(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"nrcopii{ctx.author.id}" not in data or int(data[f"nrcopii{ctx.author.id}"]) == 0:
            await ctx.reply("n-ai copil")
            return
        member = data[f"copil{ctx.author.id}"]
        data[f"copil{ctx.author.id}"] = 0
        data[f"parinte{member}"] = 0
        data[f"nrcopii{ctx.author.id}"] = 0
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()
        await ctx.reply("ai scapat de plod")
        await ctx.reply(f"<@{member}> esti orfan")

    @commands.command(aliases=['familie'])
    async def familytree(self, ctx, member: discord.Member = None, ):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        familytre = Image.open("pad/fisiere/imagini/familytree.jpg")
        if member == None:
            member = ctx.author
        avatar1 = member.avatar_url_as(size=128)
        dataa = BytesIO(await avatar1.read())
        pfp = Image.open(dataa)
        pfp = pfp.resize((155, 155))
        familytre.paste(pfp, (470, 550))
        if f"parinte{member.id}" in data and int(data[f"parinte{member.id}"]) != 0:
            parinte = data[f"parinte{member.id}"]
            parinte1 = self.client.get_user(parinte)
            avatar1 = parinte1.avatar_url_as(size=128)
            dataa = BytesIO(await avatar1.read())
            pfp = Image.open(dataa)
            pfp = pfp.resize((155, 155))
            familytre.paste(pfp, (300, 380))
            if f"Casatorit{parinte1.id}" in data and int(data[f"Casatorit{parinte1.id}"]) != 0:
                parinte = data[f"Casatorit{parinte1.id}"]
                parinte2 = self.client.get_user(parinte)
                avatar1 = parinte2.avatar_url_as(size=128)
                dataa = BytesIO(await avatar1.read())
                pfp = Image.open(dataa)
                pfp = pfp.resize((155, 155))
                familytre.paste(pfp, (630, 380))
                if f"parinte{parinte2.id}" in data and int(data[f"parinte{parinte2.id}"]) != 0:
                    bunic = data[f"parinte{parinte2.id}"]
                    bunic1 = self.client.get_user(bunic)
                    avatar1 = bunic1.avatar_url_as(size=128)
                    dataa = BytesIO(await avatar1.read())
                    pfp = Image.open(dataa)
                    pfp = pfp.resize((140, 140))
                    familytre.paste(pfp, (560, 200))
                    if f"Casatorit{bunic1.id}" in data and int(data[f"Casatorit{bunic1.id}"]) != 0:
                        bunic = data[f"Casatorit{bunic1.id}"]
                        bunic2 = self.client.get_user(bunic)
                        avatar1 = bunic2.avatar_url_as(size=128)
                        dataa = BytesIO(await avatar1.read())
                        pfp = Image.open(dataa)
                        pfp = pfp.resize((140, 140))
                        familytre.paste(pfp, (715, 200))
            if f"parinte{parinte1.id}" in data and int(data[f"parinte{parinte1.id}"]) != 0:
                bunic = data[f"parinte{parinte1.id}"]
                bunic3 = self.client.get_user(bunic)
                avatar1 = bunic3.avatar_url_as(size=128)
                dataa = BytesIO(await avatar1.read())
                pfp = Image.open(dataa)
                pfp = pfp.resize((140, 140))
                familytre.paste(pfp, (240, 200))
                if f"Casatorit{bunic3.id}" in data and int(data[f"Casatorit{bunic3.id}"]) != 0:
                    bunic = data[f"Casatorit{bunic3.id}"]
                    bunic4 = self.client.get_user(bunic)
                    avatar1 = bunic4.avatar_url_as(size=128)
                    dataa = BytesIO(await avatar1.read())
                    pfp = Image.open(dataa)
                    pfp = pfp.resize((140, 140))
                    familytre.paste(pfp, (400, 200))
        familytre.save("profile.jpg")
        await ctx.reply(file=discord.File("profile.jpg"))
        os.remove("profile.jpg")

    @commands.command(aliases=['copii'])
    async def copil(self, ctx, membru: discord.Member = None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if membru == None:
            membru = ctx.author
        if f"nrcopii{membru.id}" not in data or int(data[f"nrcopii{membru.id}"]) == 0:
            if membru.id == ctx.author.id:
                await ctx.reply("n-ai copil")
            else:
                await ctx.reply("n-are copil")
            return
        member = data[f"copil{membru.id}"]
        if membru.id == ctx.author.id:
            await ctx.reply(f"L-ai adoptat pe <@{member}> acu ceva timp.")
        else:
            await ctx.reply(f"L-a adoptat pe <@{member}> acu ceva timp.")

    @commands.command(aliases=['parinte', 'tata', 'mama', 'parinti'])
    async def părinți(self, ctx, membru: discord.Member = None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if membru == None:
            membru = ctx.author
        if f"parinte{membru.id}" not in data or data[f"parinte{membru.id}"] == 0:
            await ctx.reply("n-ai parinti orfane")
            return
        member = data[f"parinte{membru.id}"]
        if f"Casatorit{member}" in data and data[f"Casatorit{member}"] != 0:
            member2 = data[f"Casatorit{member}"]
            if ctx.author.id == membru.id:
                await ctx.reply(f"Ești plodu' lui <@{member}> si a lui <@{member2}>.")
            else:
                await ctx.reply(f"E plodu' lui <@{member}> si a lui <@{member2}>.")
        else:
            if ctx.author.id == membru.id:
                await ctx.reply(f"Te-a adoptat <@{member}> acu ceva timp.")
            else:
                await ctx.reply(f"L-a adoptat <@{member}> acu ceva timp.")

    @commands.command(aliases=['checkmarry', 'checkmarriage', 'sotie','cuplu'])
    async def sot(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        guild = ctx.guild
        if ctx.author.bot:
            await ctx.reply("e gagica.")
            return
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"Casatorit{member.id}" not in data:
            data[f"Casatorit{member.id}"] = 0
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
        if (data[f"Casatorit{member.id}"] == 0):
            if member.id == ctx.author.id:
                embed = discord.Embed(title="Esti singur domnule", description="Nu esti casatorit", color=discord.Color.green())
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                embed.set_thumbnail(url='https://media.discordapp.net/attachments/745384647885848594/948597179033985114/924645878193586186.gif')
                await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="Este un domn singur", description=f"{member.mention} nu e casatorit", color=discord.Color.green())
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                embed.set_thumbnail(url='https://media.discordapp.net/attachments/745384647885848594/948597179033985114/924645878193586186.gif')
                await ctx.reply(embed=embed)
        else:
            datacass=data[f"datacasatoriei{member.id}"]
            datacas=datetime.strptime(datacass, '%Y-%m-%d %H:%M:%S.%f')
            datacurenta=datetime.now()
            timp=datacurenta-datacas
            if timp.seconds <60:
              timp=str(int(timp.seconds))+" secunde"
            elif timp.seconds/60 <60:
              timp=str(int(timp.seconds/60))+" minute"
            elif timp.seconds/3600 <24:
              timp=str(int(timp.seconds/3600))+" ore"
            elif timp.days <31:
              timp=str(int(timp.days))+" zile"
            elif timp.days/30 <12:
              timp=str(int(timp.days/30))+" luni"
            else:
              timp=str(int(timp.days/360))+" ani"
            try:
              persoana=await ctx.guild.fetch_member(data[f"Casatorit{member.id}"])
              persoana=f"<@{persoana.id}>"
            except:
              persoana = self.client.get_user(data[f"Casatorit{member.id}"])
            if member.id == ctx.author.id:
              embed = discord.Embed(title="Felicitari!", description=f"{member.mention}, esti intr-o relatie cu {persoana} de {timp}", color=discord.Color.from_rgb(255, 182, 193))
              embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
              embed.timestamp = datetime.utcnow()
              embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/zy5gZQOkf6fez6tOPeAtvZomGwlEPFt2PxTVfNWEBAM/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/784630478673936434.gif')
              await ctx.reply(embed=embed)
            else:
                embed = discord.Embed(title="Frumos!", description=f"{member.mention} e intr-o relatie cu {persoana} de {timp}", color=discord.Color.from_rgb(255, 182, 193))
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/zy5gZQOkf6fez6tOPeAtvZomGwlEPFt2PxTVfNWEBAM/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/784630478673936434.gif')
                await ctx.reply(embed=embed)

    @sot.error
    async def sot_error(self, ctx, error):
        print(error)
        await ctx.reply("Ceva n-a mers bine.")

    @commands.command(aliases=['divorț', 'divorce'])
    async def divort(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"Cer{ctx.author.id}" not in data:
            data[f"Cer{ctx.author.id}"] = 0
        if f"Casatorit{ctx.author.id}" not in data:
            data[f"Casatorit{ctx.author.id}"] = 0
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()
        if data[f"Casatorit{ctx.author.id}"] == 0:
            embed = discord.Embed(title="Uhmmmm", description=f"Nu esti casatorit.", color=discord.Color.green())
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            embed.set_thumbnail(url='https://www.freepnglogos.com/uploads/question-mark-png/file-red-question-mark-svg-wikimedia-commons-14.png')
            await ctx.reply(embed=embed)
        else:
            id = int(data[f"Casatorit{ctx.author.id}"])
            data[f"Casatorit{ctx.author.id}"] = 0
            data[f"Casatorit{id}"] = 0
            data[f"Cer{ctx.author.id}"] = 0
            data[f"Cer{id}"] = 0
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            embed = discord.Embed(title="Gata documentele", description=f"Nu mai esti casatorit!!", color=discord.Color.green())
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/xp1mvFwAseXgYV4UCIgZE4wteLIdvM5x3PuyEwMx0YE/%3Fv%3D1%26size%3D40/https/cdn.discordapp.com/emojis/903543737534283836.gif')
            await ctx.reply(embed=embed)
            member = self.client.get_user(id)
            await ctx.reply(f"Si tu esti single acum {member.mention}")
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()


def setup(client):
    client.add_cog(Fun(client))