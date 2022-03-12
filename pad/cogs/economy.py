import discord
import random
import json
import time
import datetime
from discord.ext import commands
from random import randint
from datetime import datetime

import discord_components
from discord_components import DiscordComponents, Button, ButtonStyle

#NOT YET USED

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['busteni','bușteni'])
    async def bustean(self,ctx,member:discord.Member=""):
      if member=="":
        member=ctx.author
      with open("pad/data/data.json", "r") as jsonFile:
          data = json.load(jsonFile)
          jsonFile.close()
      if f"busteni{member.id}" not in data or int(data[f"busteni{member.id}"])==0:
        embed = discord.Embed(title="", description="", color=discord.Color.green())
        embed.add_field(name=f'???',value=f"Domnule n-ai niciun buștean. Du-te strange cativa!")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/847006652313239582/1622012511135.jpg")
        await ctx.send(embed=embed)
      else:
        if member==ctx.author:
          nr=int(data[f"busteni{member.id}"])
          if nr!=1:
            embed = discord.Embed(title="", description="", color=discord.Color.green())
            embed.add_field(name="BINE domnule",value=f"Pana acum ai {nr} busteni")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/847006652313239582/1622012511135.jpg")
            await ctx.send(embed=embed)
          else:
            embed = discord.Embed(title="", description="", color=discord.Color.green())
            embed.add_field(name="BINE domnule",value=f"Pana acum ai un bustean")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/847006652313239582/1622012511135.jpg")
            await ctx.send(embed=embed)
        else:
          nr=int(data[f"busteni{member.id}"])
          if nr!=1:
            embed = discord.Embed(title="", description="", color=discord.Color.green())
            embed.add_field(name="BINE domnule",value=f"Pana acum {member.mention} are {nr} busteni")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/847006652313239582/1622012511135.jpg")
            await ctx.send(embed=embed)
          else:
            embed = discord.Embed(title="", description="", color=discord.Color.green())
            embed.add_field(name="BINE domnule",value=f"Pana acum {member.mention} are un bustean")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/847006652313239582/1622012511135.jpg")
            await ctx.send(embed=embed)



    @commands.command(aliases=['pietre','piatră'])
    async def piatra(self,ctx,member:discord.Member=""):
      if member=="":
        member=ctx.author
      with open("pad/data/data.json", "r") as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()
      if f"pietre{member.id}" not in data or int(data[f"pietre{member.id}"])==0:
        embed = discord.Embed(title="", description="", color=discord.Color.green())
        embed.add_field(name=f'????',value=f"Domnule n-ai nicio piatra, nu ești meserias")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/847008982963060756/1622013072745.jpg")
        await ctx.send(embed=embed)
      else:
        if member==ctx.author:
          nr=int(data[f"pietre{member.id}"])
          if nr!=1:
            embed = discord.Embed(title="", description="", color=discord.Color.green())
            embed.add_field(name="BINE DOMNULE",value=f"Pana acum ai {nr} pietre în Padurea Băneasa")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/847008982963060756/1622013072745.jpg")
            await ctx.send(embed=embed)
          else:
            embed = discord.Embed(title="", description="", color=discord.Color.green())
            embed.add_field(name="BINE DOMNULE",value=f"Pana acum ai o piatra în Padurea Băneasa")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/847008982963060756/1622013072745.jpg")
            await ctx.send(embed=embed)
        else:
          nr=int(data[f"pietre{member.id}"])
          if nr!=1:
            embed = discord.Embed(title="", description="", color=discord.Color.green())
            embed.add_field(name="BINE DOMNULE",value=f"Pana acum {member.mention} are {nr} pietre din Padurea Băneasa")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/847008982963060756/1622013072745.jpg")
            await ctx.send(embed=embed)
          else:
            embed = discord.Embed(title="", description="", color=discord.Color.green())
            embed.add_field(name="BINE DOMNULE",value=f"Pana acum {member.mention} are o piatra din Padurea Băneasa")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/847008982963060756/1622013072745.jpg")
            await ctx.send(embed=embed)



    @commands.command(aliases=['bat','bețe'])
    async def bete(self,ctx,member:discord.Member=""):
      if member=="":
        member=ctx.author
      with open("pad/data/data.json", "r") as jsonFile:
          data = json.load(jsonFile)
          jsonFile.close()
      if f"bete{member.id}" not in data or int(data[f"bete{member.id}"])==0:
        embed = discord.Embed(title="", description="", color=discord.Color.green())
        embed.add_field(name=f'????',value=f"Domnule n-ai niciun bat in Padurea Băneasa")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/847008579692134400/1622012974600.jpg")
        await ctx.send(embed=embed)   
      else:
        if member==ctx.author:
          nr=int(data[f"bete{member.id}"])
          embed = discord.Embed(title="", description="", color=discord.Color.green())
          embed.add_field(name=f"BINE DOMNULE",value=f"Pana acum ai furat {nr} bețe din Padurea Băneasa")
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/847008579692134400/1622012974600.jpg")
          await ctx.send(embed=embed)   
        else:
          nr=int(data[f"bete{member.id}"])
          embed = discord.Embed(title="", description="", color=discord.Color.green())
          embed.add_field(name=f"BINE DOMNULE",value=f"Pana acum {member.mention} a furat {nr} bețe din Padurea Băneasa")
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/847008579692134400/1622012974600.jpg")
          await ctx.send(embed=embed)   



    @commands.command()
    async def frunze(self,ctx,member:discord.Member=""):
      if member=="":
        member=ctx.author
      with open("pad/data/data.json", "r") as jsonFile:
          data = json.load(jsonFile)
          jsonFile.close()
      if f"frunze{member.id}" not in data or int(data[f"frunze{member.id}"])==0:
        embed = discord.Embed(title="", description="", color=discord.Color.green())
        embed.add_field(name=f'????',value=f"Domnule n-ai nicio frunza in Padurea Băneasa")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/868914417658638436/Screenshot_20210725-205533_Sketchbook.jpg")
        await ctx.send(embed=embed)   
      else:
        if member==ctx.author:
          nr=int(data[f"frunze{member.id}"])
          embed = discord.Embed(title="", description="", color=discord.Color.green())
          embed.add_field(name=f"BINE DOMNULE",value=f"Pana acum ai furat {nr} frunze din Padurea Băneasa")
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/868914417658638436/Screenshot_20210725-205533_Sketchbook.jpg")
          await ctx.send(embed=embed)   
        else:
          nr=int(data[f"frunze{member.id}"])
          embed = discord.Embed(title="", description="", color=discord.Color.green())
          embed.add_field(name=f"BINE DOMNULE",value=f"Pana acum {member.mention} a furat {nr} frunze din Padurea Băneasa")
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/868914417658638436/Screenshot_20210725-205533_Sketchbook.jpg")
          await ctx.send(embed=embed)   



    @commands.command(aliases=['daruieste'])
    async def give(ctx,member:discord.Member="",obiect="",nr:int=1):
      with open("pad/data/data.json", "r") as jsonFile:
          data = json.load(jsonFile)
          jsonFile.close()
      if member=="":
        await ctx.send("Cui daruiesti si ce? Ruleaza din nou comanda (exemplu: `.daruieste @Denis#2516 busteni 3`")
        return
      if member.id==ctx.author.id:
        await ctx.send("Nu-ti poti da singur ceva")
        return
      if obiect=="":
        await ctx.send("Ce daruiesti, bete, busteni sau pietre? Ruleaza din nou comanda (exemplu: `.daruieste @Denis#2516 busteni 3`")
        return
      if nr<0:
        await ctx.send("Nah fara obiecte pe minus")
        return
      embed = discord.Embed(title="", description="",color=discord.Color.green())
      embed.set_author(name="schimbator 2.0", icon_url="https://icon-library.com/images/icon-exchange/icon-exchange-8.jpg")
      if obiect.upper()=="BUSTEAN" or obiect.upper()=="BUSTENI" or obiect.upper()=="BUȘTEAN" or obiect.upper()=="BUȘTENI":
        if f"busteni{ctx.author.id}" not in data or data[f"busteni{ctx.author.id}"]==0:
          await ctx.send("Lmao n-ai niciun bustean")
          return
        elif data[f"busteni{ctx.author.id}"]<nr:
          await ctx.send("Lmao n-ai destui busteni")
          return
        if f"busteni{member.id}" not in data:
          data[f"busteni{ctx.author.id}"]=int(data[f"busteni{ctx.author.id}"])-nr
          data[f"busteni{member.id}"]=nr
          with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()
        else:
          data[f"busteni{ctx.author.id}"]=int(data[f"busteni{ctx.author.id}"])-nr
          data[f"busteni{member.id}"]=int(data[f"busteni{member.id}"])+nr
          with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()
        embed.add_field(name="Tranzactie incheiata",value=f'I-ai dat {nr} busteni lui {member.mention}',inline=True)
        await ctx.send(embed=embed)
      elif obiect.upper()=="PIATRĂ" or obiect.upper()=="PIATRA" or obiect.upper()=="PIETRE":
        if f"pietre{ctx.author.id}" not in data or data[f"pietre{ctx.author.id}"]==0:
          await ctx.send("Lmao n-ai nicio piatra")
          return
        elif data[f"pietre{ctx.author.id}"]<nr:
          await ctx.send("Lmao n-ai destule pietre")
          return
        if f"pietre{member.id}" not in data:
          data[f"pietre{ctx.author.id}"]=int(data[f"pietre{ctx.author.id}"])-nr
          data[f"pietre{member.id}"]=nr
          with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()
        else:
          data[f"pietre{ctx.author.id}"]=int(data[f"pietre{ctx.author.id}"])-nr
          data[f"pietre{member.id}"]=int(data[f"pietre{member.id}"])+nr
        embed.add_field(name="Tranzactie incheiata",value=f'I-ai dat {nr} pietre lui {member.mention}',inline=True)
        with open("pad/data/data.json", "w") as jsonFile:
          json.dump(data, jsonFile)
          jsonFile.close()
        await ctx.send(embed=embed)
      elif obiect.upper()=="BAT" or obiect.upper()=="BETE" or obiect.upper()=="BAȚ" or obiect.upper()=="BEȚE":
        if f"bete{ctx.author.id}" not in data or data[f"bete{ctx.author.id}"]==0:
          await ctx.send("Lmao n-ai niciun bat")
          return
        elif data[f"bete{ctx.author.id}"]<nr:
          await ctx.send("Lmao n-ai destule bete")
          return
        if f"bete{member.id}" not in data:
          data[f"bete{ctx.author.id}"]=int(data[f"bete{ctx.author.id}"])-nr
          data[f"bete{member.id}"]=nr
        else:
          data[f"bete{ctx.author.id}"]=int(data[f"bete{ctx.author.id}"])-nr
          data[f"bete{member.id}"]=int(data[f"bete{member.id}"])+nr
        with open("pad/data/data.json", "w") as jsonFile:
          json.dump(data, jsonFile)
          jsonFile.close()
        embed.add_field(name="Tranzactie incheiata",value=f'I-ai dat {nr} bete lui {member.mention}',inline=True)
        await ctx.send(embed=embed)
      elif obiect.upper()=="FRUNZA" or obiect.upper()=="FRUNZE" or obiect.upper()=="FRUNZĂ":
        if f"frunze{ctx.author.id}" not in data or data[f"frunze{ctx.author.id}"]==0:
          await ctx.send("Lmao n-ai nicio frunza")
          return
        elif data[f"frunze{ctx.author.id}"]<nr:
          await ctx.send("Lmao n-ai destule frunze")
          return
        if f"frunze{member.id}" not in data:
          data[f"frunze{ctx.author.id}"]=int(data[f"frunze{ctx.author.id}"])-nr
          data[f"frunze{member.id}"]=nr
        else:
          data[f"frunze{ctx.author.id}"]=int(data[f"frunze{ctx.author.id}"])-nr
          data[f"frunze{member.id}"]=int(data[f"frunze{member.id}"])+nr
        with open("pad/data/data.json", "w") as jsonFile:
          json.dump(data, jsonFile)
          jsonFile.close()
        embed.add_field(name="Tranzactie incheiata",value=f'I-ai dat {nr} frunze lui {member.mention}',inline=True)
        await ctx.send(embed=embed)


    @commands.command(aliases=['furt','fură'])
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def fura(self,ctx):
      with open("pad/data/data.json", "r") as jsonFile:
          data = json.load(jsonFile)
          jsonFile.close()
      await ctx.reply("Esti sigur ca vrei sa mergi la furat cu tiganii din padure?")
      def is_correct(m):
        return m.author.id == ctx.author.id and m.channel.id==ctx.channel.id
      msg = await self.client.wait_for('message', check=is_correct, timeout=20)
      while "NU" not in str(msg.content).upper() and "DA" not in str(msg.content).upper():
        await msg.reply("Ma prostule, zi da sau nu, ca sar tiganii pe tine indata ") 
        msg = await self.client.wait_for('message', check=is_correct, timeout=20)
      if "NU" in str(msg.content).upper():
        nrfrunze=randint(1,990)
        if f"frunze{ctx.author.id}" not in data:
          data[f"frunze{ctx.author.id}"]=0
        bal=int(data[f"frunze{ctx.author.id}"])
        data[f"frunze{ctx.author.id}"]=bal-nrfrunze
        with open("pad/data/data.json", "w") as jsonFile:
          json.dump(data, jsonFile)
          jsonFile.close()
        if bal==0:
          await ctx.reply(f"Ti-ai luat un pumn in gura de la tigani. Acum le esti dator tiganilor cu {nrfrunze} frunze.")
        elif nrfrunze<=bal:
          await ctx.reply(f"Ti-ai luat un pumn in gura de la tigani. Aveai {nrfrunze} frunze la tine si na, nu le mai ai.")
        else:
          await ctx.reply(f"Ti-ai luat un pumn in gura de la tigani. Aveai {bal} frunze la tine si na, nu le mai ai. Esti si dator cu {nrfrunze-bal} frunze. Ai grija cand mergi pe strasa.")
      elif "DA" in str(msg.content).upper():
        if f"frunze{ctx.author.id}" not in data:
          data[f"frunze{ctx.author.id}"]=0
        if f"bete{ctx.author.id}" not in data:
          data[f"bete{ctx.author.id}"]=0
        if f"busteni{ctx.author.id}" not in data:
          data[f"busteni{ctx.author.id}"]=0
        if f"m{ctx.author.id}" not in data:
          data[f"m{ctx.author.id}"]=0
        if f"M{ctx.author.id}" not in data:
          data[f"M{ctx.author.id}"]=0
        with open("pad/data/data.json", "w") as jsonFile:
          json.dump(data, jsonFile)
          jsonFile.close()
        ciuperci=randint(0,1)
        probmure=randint(0,100)
        if probmure<=30:
          mure=1
        else:
          mure=0
        if ciuperci==1:
          otravitoare=randint(0,1)
        probmiere=randint(0,100)
        miere=0
        if probmiere<=15:
          miere=1
        probbusteni=randint(0,100)
        if probbusteni<=30:
          busteni=randint(1,3)
          data[f"busteni{ctx.author.id}"]=int(data[f"busteni{ctx.author.id}"])+busteni
          with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()
        bete=randint(0,2639)
        frunze=randint(0,1230)
        if frunze==1230:
          frunze=4000
        data[f"frunze{ctx.author.id}"]=int(data[f"frunze{ctx.author.id}"])+frunze
        data[f"bete{ctx.author.id}"]=int(data[f"bete{ctx.author.id}"])+bete
        data[f"m{ctx.author.id}"]=int(data[f"m{ctx.author.id}"])+mure
        data[f"M{ctx.author.id}"]=int(data[f"M{ctx.author.id}"])+miere
        with open("pad/data/data.json", "w") as jsonFile:
          json.dump(data, jsonFile)
          jsonFile.close()
        embed = discord.Embed(title="", description="",color=discord.Color.green())
        embed.set_author(name="Furat", icon_url="https://pngvalor.com/files/preview/900x561/12016194727990pgyu7fdfzil2133ajfxfz7fjqpvvc6yktkr84bscytcfjgqshttoriz6c4eow5ke3xyfgwpzr8knxsd5ga1csrui69vfo56tdv7.png")
        text=""
        if mure==1:
          text=text+f"`{mure}` mure, "
        if miere==1:
          text=text+f"`{miere}` borcan cu miere, "
        if ciuperci==1:
          text=text+f"`{ciuperci}` ciuperci, "
        if probbusteni<=30:
          text=text+f"`{busteni}` busteni, "
        text=text+f"`{bete}` bete, "
        if frunze<4000:
          text=text+f"`{frunze}` frunze."
        else:
          text=text+f"`{frunze}` frunze(WOAH 4000???)."
        embed.add_field(name=f" Ai furat din padure:",value=text,inline=True)
        embed.set_footer(text=f"{ctx.author} | foloseste `.inv` pentru a vedea itemele",icon_url=ctx.author.avatar_url)
        await msg.reply(embed=embed)
        if ciuperci==1 and otravitoare==0:
          await ctx.send("Ai mancat ciuperca si ai energie pentru a fura iar. Poti rula comanda `.fura` iar!")
          fura.reset_cooldown(ctx)
        elif ciuperci==1 and otravitoare==1:
          await ctx.send("Ai mancat ciuperca si a **fost otravitoare**. Ti-ai pierdut betele furate pe drum.")
          data[f"bete{ctx.author.id}"]=int(data[f"bete{ctx.author.id}"])-bete
          with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()
    @fura.error
    async def fura_error(self,ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        timp=error.retry_after
        em = discord.Embed(title=f"HOOOO DOMNULE",description=f" Ai de asteptat {timp/60:.0f} minute pana poti fura iar. Nu stau domnii dupa tine.", color=discord.Color.green())
        await ctx.reply(embed=em)



    @commands.command(aliases=['inventar','inventory'])
    async def inv(self,ctx,member:discord.Member=""):
      if member=="":
        member=ctx.author
      with open("pad/data/data.json", "r") as jsonFile:
          data = json.load(jsonFile)
          jsonFile.close()
      if f"pietre{member.id}" not in data:
        pietre=0
      else:
        pietre=int(data[f"pietre{member.id}"])
      if f"busteni{member.id}" not in data:
        busteni=0
      else:
        busteni=int(data[f"busteni{member.id}"])
      if f"m{member.id}" not in data:
        mure=0
      else:
        mure=int(data[f"m{member.id}"])
      if f"M{member.id}" not in data:
        miere=0
      else:
        miere=int(data[f"M{member.id}"])
      if f"bete{member.id}" not in data:
        bete=0
      else:
        bete=int(data[f"bete{member.id}"])
      embed = discord.Embed(title="INVENTAR", description=f"Asta-i inventarul lui {member.mention}", color=discord.Color.green())
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745384647885848594/847016573478633532/1622014866015.jpg")
      embed.add_field(name=f"Bete",value=f"Numarul de bete detinute: {bete}")
      embed.add_field(name=f"Busteni",value=f"Numarul de busteni detinuti: {busteni}")
      embed.add_field(name=f"Pietre",value=f"Numarul de pietre detinute: {pietre}")
      txt=""
      #if mure>0:
        #txt="\nPoti mânca murele pentru xp dublu (cu comanda `.foloseste mure`)"
      embed.add_field(name=f"Mure",value=f"Numarul de mure detinute: {mure}"+txt)
      txt=""
      #if miere>0:
        #txt="\nPoti mânca mierea pentru un bonus xp (cu comanda `.foloseste miere`)"
      embed.add_field(name=f"Borcane cu miere",value=f"Numarul de borcane detinute: {miere}"+txt)
      await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Economy(client))