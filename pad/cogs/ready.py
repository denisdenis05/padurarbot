import discord
import random
import json
import datetime
import asyncio
import re
from main import invites
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
from datetime import datetime
from main import default_color

class Ready(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def resetbumps(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        match_keys = {key: val for key, val in data.items()
                      if key.startswith("bump")}
        for k in match_keys:
            data[k] = 0
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def resetxpdublu(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        match_keys = {key: val for key, val in data.items() if key.startswith("xpdublu")}
        for k in match_keys:
            data[k] = 0
        match_keys2 = {key: val for key, val in data.items()
                       if key.startswith("dataxpdublu")}
        for k in match_keys2:
            data[k] = 0
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rraport(self, ctx):
        print("da raport!")
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        guild = self.client.get_guild(619454105869352961)
        category = get(guild.categories, id=792354214449905714)
        channels = category.channels
        for canal in channels:
            if canal.id != 787332862902665237:
                print(canal.name)
                overwrite = canal.overwrites
                perm = str(overwrite)
                # print(perm)
                try:
                    start = perm.index("<Member id=") + len("<Member id=")
                    end = perm.index(" name=", start)
                    membruid = perm[start:end]
                    membru = self.client.get_user(int(membruid))
                    xp = int(data[f"{guild.id}XP{membru.id}"])
                    embed = discord.Embed(title="Raport", description=f"Domnul {membru.mention} are:",
                                          color=default_color)
                    embed.add_field(name=f'Xp', value=f"{xp} puncte.", inline=True)
                except:
                    await canal.send('<@852673995563597875> eroare probabil n-are permisiune baiatu')
                await asyncio.sleep(2)
        match_keys = {key: val for key, val in data.items()
                      if key.startswith("bump")}
        for k in match_keys:
            data[k] = 0
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()

    # db[f"xpdublu{id}"]=1 db[f"dataxpdublu{id}"]

    @tasks.loop(minutes=30)
    async def xpdubluverif(self):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        match_keys = {key: val for key, val in data.items()
                      if key.startswith("dataxpdublu")}
        for k in match_keys:
            if data[k] != 0:
                dataacum = datetime.now().day
                lunaacum = datetime.now().month
                data, luna = str(data[k]).split(".")
                if data != dataacum or luna != lunaacum:
                    id = int(str(k)[11:])
                    data[f"xpdublu{id}"] = 0
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()

    @tasks.loop(minutes=30)
    async def verificarevocal(self):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        for guild in self.client.guilds:
            if f"voice{guild.id}" in data and data[f"voice{guild.id}"] != 0:
                vocale = guild.voice_channels
                for vocal in vocale:
                    if "Canalul lui" in str(vocal.name):
                        if len(vocal.members) == 0:
                            await vocal.delete()

    @tasks.loop(minutes=60)
    async def verificaresarbatoriti(self):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if datetime.now().hour == 23:
            for guild in self.client.guilds:
                try:
                    if f"birthdayrol{guild.id}" in data and data[f"birthdayrol{guild.id}"] != 0:
                        rolid = int(data[f"birthdayrol{guild.id}"])
                        sarbatorit = guild.get_role(rolid)
                        for member in guild.members:
                            if sarbatorit in member.roles:
                                await membru.remove_roles(sarbatorit)
                                data[f"birthdaydate{member.id}"] = data[f"tempbirthdaydate{member.id}"]
                                with open("pad/data/data.json", "w") as jsonFile:
                                    json.dump(data, jsonFile)
                                    jsonFile.close()
                except:
                    pass

    @tasks.loop(minutes=60)
    async def verificareraport(self):
        if datetime.now().weekday() == 6:
            if datetime.now().hour == 15:
                with open("pad/data/data.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                    jsonFile.close()
                print("da raport!")
                guild = self.client.get_guild(619454105869352961)
                admin = guild.get_role(764430139198406666)
                mod = guild.get_role(619460445165584407)
                helper = guild.get_role(619460416661356544)
                category = get(guild.categories, id=792354214449905714)
                channels = category.channels
                for canal in channels:
                    if canal.id != 787332862902665237:
                        print(canal.name)
                        overwrite = canal.overwrites
                        perm = str(overwrite)
                        # print(perm)
                        try:
                            start = perm.index("<Member id=") + len("<Member id=")
                            end = perm.index(" name=", start)
                            membruid = perm[start:end]
                            membru = guild.get_member(int(membruid))
                            xp = int(data[f"{guild.id}XP{membru.id}"])
                            async for message in canal.history(limit=1):
                                msg = message
                            embeds = msg.embeds
                            for emb in embeds:
                                text = str(emb.to_dict())
                                xptrecut = ""
                                ok = 0
                                for litera in text:
                                    if litera.isdigit():
                                        xptrecut = xptrecut + litera
                                        ok = 1
                                    elif ok == 1:
                                        break
                            xptrecut = int(xptrecut)
                            if admin in membru.roles:
                                if xp - xptrecut < 3550:
                                    await canal.send(f"!!!!RAPORT NEFACUT!!! ({xp - xptrecut} xp saptamanal)")
                                else:
                                    await canal.send(f"Raport terminat, {xp - xptrecut} xp saptamanal")
                            elif mod in membru.roles:
                                if xp - xptrecut < 4000:
                                    await canal.send(f"!!!!RAPORT NEFACUT!!! ({xp - xptrecut} xp saptamanal)")
                                else:
                                    await canal.send(f"Raport terminat, {xp - xptrecut} xp saptamanal")
                            elif helper in membru.roles:
                                if xp - xptrecut < 5500:
                                    await canal.send(f"!!!!RAPORT NEFACUT!!! ({xp - xptrecut} xp saptamanal)")
                                else:
                                    await canal.send(f"Raport terminat, {xp - xptrecut} xp saptamanal")
                            embed = discord.Embed(title="Raport", description=f"Domnul {membru.mention} are ",
                                                  color=default_color)
                            embed.add_field(name=f'Xp ', value=f"{xp} puncte.", inline=True)
                            await canal.send(embed=embed)
                        except Exception as ex:
                            print(ex)
                            pass
                            # await canal.send('<@852673995563597875> eroare probabil n-are permisiune baiatu')
                        await asyncio.sleep(2)
                match_keys = {key: val for key, val in data.items()
                              if key.startswith("bump")}
                for k in match_keys:
                    data[k] = 0
                match_keys2 = {key: val for key, val in data.items()
                               if key.startswith("voturis")}
                for k in match_keys2:
                    data[k] = 0
                match_keys3 = {key: val for key, val in data.items()
                               if key.startswith("xpsaptamanal")}
                for k in match_keys3:
                    data[k] = 0
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()

    @tasks.loop(minutes=10)
    async def mcount(self):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        for guild in self.client.guilds:
            try:
                if f"count{guild.id}" in data:
                    memcount = int(data[f"count{guild.id}"])
                    count = self.client.get_channel(memcount)
                    if f"name{guild.id}" in data and data[f"name{guild.id}"] != 0:
                        nume = data[f"name{guild.id}"]
                        await count.edit(name=f"{nume} : {guild.member_count}")
                    else:
                        await count.edit(name=f"|🌲| Membrii : {guild.member_count}")
            except:
                print("eh")
            await asyncio.sleep(5)

    @tasks.loop(minutes=120)
    async def birth(self):
        # data[f"birthdaydate{member.id}"]

        if datetime.now().hour > 22:
            return
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        for guild in self.client.guilds:
            try:
                if f"birthdaycanal{guild.id}" in data and data[f"birthdaycanal{guild.id}"] != 0:
                    canalid = int(data[f"birthdaycanal{guild.id}"])
                    channell = self.client.get_channel(canalid)

                    match_keys = {key: val for key, val in data.items()
                                  if key.startswith("birthdaydate")}
                    day = datetime.now().day
                    month = datetime.now().month
                    year = datetime.now().year
                    for k in match_keys:
                        dayn, monthn, yearn = data[k].split(".")
                        if int(dayn) == int(day) and int(monthn) == int(month):
                            id = int(k.replace("birthdaydate", ""))
                            membru = await guild.fetch_member(id)
                            if yearn == 0:
                                await channell.send(f"LA MULTI ANI {membru.mention}!!!!!!!!!!!!!!",
                                                    file=discord.File("pad/fisiere/loco.mp4"))
                            else:
                                await channell.send(
                                    f"LA MULTI ANI {membru.mention}, azi faci {int(year) - int(yearn)} ani!!!!!!!!!!!!!!",
                                    file=discord.File("pad/fisiere/loco.mp4"))
            except:
                pass

            try:
                if f"birthdayrol{guild.id}" in data and data[f"birthdayrol{guild.id}"] != 0:
                    rolid = int(data[f"birthdayrol{guild.id}"])
                    sarbatorit = guild.get_role(rolid)
                    match_keys = {key: val for key, val in data.items()
                                  if key.startswith("birthdaydate")}
                    day = datetime.now().day
                    month = datetime.now().month
                    year = datetime.now().year
                    for k in match_keys:
                        dayn, monthn, yearn = data[k].split(".")
                        if int(dayn) == int(day) and int(monthn) == int(month):
                            id = int(k.replace("birthdaydate", ""))
                            membru = await guild.fetch_member(id)
                            await membru.add_roles(sarbatorit)
                            data[f"temp{k}"] = data[k]
                            data[k] = "temp"
                            with open("pad/data/data.json", "w") as jsonFile:
                                json.dump(data, jsonFile)
                                jsonFile.close()
            except:
                pass

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="xxxxxxxxxxxxxxxxxxxxxxxxx"))
        print("ready")
        global snipe_message_content
        global snipe_message_author
        global editsnipe_author
        for guild in self.client.guilds:
            try:
                invites[guild.id] = await guild.invites()
            except:
                pass
        editsnipe_author = None
        snipe_message_content = None
        snipe_message_author = None
        self.verificareraport.start()
        self.mcount.start()
        self.birth.start()
        self.verificaresarbatoriti.start()
        self.xpdubluverif.start()
        self.verificarevocal.start()


async def setup(client):
    await client.add_cog(Ready(client))