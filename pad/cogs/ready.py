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




class Ready(commands.Cog):

    def __init__(self, client):
        self.client = client


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
              if f"birthdayrol{guild.id}" in data and data[f"birthdayrol{guild.id}"]!=0:
                rolid=int(data[f"birthdayrol{guild.id}"])
                sarbatorit = guild.get_role(rolid)
                for member in guild.members:
                  if sarbatorit in member.roles:
                    await membru.remove_roles(sarbatorit)
                    data[f"birthdaydate{member.id}"]=data[f"tempbirthdaydate{member.id}"]
                    with open("pad/data/data.json", "w") as jsonFile:
                        json.dump(data, jsonFile)
                        jsonFile.close()    
            except:
              pass



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
      #data[f"birthdaydate{member.id}"]
        if datetime.now().hour > 22:
            return
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        for guild in self.client.guilds:
          try:
            if f"birthdaycanal{guild.id}" in data and data[f"birthdaycanal{guild.id}"]!=0:
              canalid=int(data[f"birthdaycanal{guild.id}"])
              channell = self.client.get_channel(canalid)
        
              match_keys = {key: val for key, val in data.items()
                      if key.startswith("birthdaydate")}
              day = datetime.now().day
              month = datetime.now().month
              year = datetime.now().year
              for k in match_keys:
                dayn,monthn,yearn=data[k].split(".")
                if int(dayn)==int(day) and int(monthn)==int(month):
                  id=int(k.replace("birthdaydate",""))
                  membru = await guild.fetch_member(id)
                  if yearn==0:
                    await channell.send(f"LA MULTI ANI {membru.mention}!!!!!!!!!!!!!!", file=discord.File("pad/fisiere/loco.mp4"))
                  else:
                    await channell.send(f"LA MULTI ANI {membru.mention}, azi faci {int(year)-int(yearn)} ani!!!!!!!!!!!!!!", file=discord.File("pad/fisiere/loco.mp4"))
          except:
            pass
          
          try:
            if f"birthdayrol{guild.id}" in data and data[f"birthdayrol{guild.id}"]!=0:
              rolid=int(data[f"birthdayrol{guild.id}"])
              sarbatorit = guild.get_role(rolid)
              match_keys = {key: val for key, val in data.items()
                      if key.startswith("birthdaydate")}
              day = datetime.now().day
              month = datetime.now().month
              year = datetime.now().year
              for k in match_keys:
                dayn,monthn,yearn=data[k].split(".")
                if int(dayn)==int(day) and int(monthn)==int(month):
                  id=int(k.replace("birthdaydate",""))
                  membru = await guild.fetch_member(id)
                  await membru.add_roles(sarbatorit)
                  data[f"temp{k}"]=data[k]
                  data[k]="temp"
                  with open("pad/data/data.json", "w") as jsonFile:
                        json.dump(data, jsonFile)
                        jsonFile.close()          
          except:
            pass

                    


    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="Pădurea Baneasa"))
        print("ready")
        print(datetime.now())
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
        self.mcount.start() #updates member count
        self.birth.start() #checks if today is someone's birthday
        self.verificaresarbatoriti.start() #check if the birthday has passed
        self.xpdubluverif.start() #check if double/triple xp is still enabled on servers
        self.verificarevocal.start() #check if there still exist temp vocal channels (kinda unstable)



def setup(client):
    client.add_cog(Ready(client))