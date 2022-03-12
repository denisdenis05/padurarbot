import discord
import random
import json
import re
import os
import datetime
from random import randint
from discord.ext import commands
from datetime import datetime
from io import BytesIO
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Imagini(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def wanted(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        wanted = Image.open("pad/fisiere/imagini/wanted.jpg")
        avatar1 = member.avatar_url_as(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((100, 100))
        wanted.paste(pfp, (100, 150))
        wanted.save("profile.jpg")
        await ctx.reply(file=discord.File("profile.jpg"))
        os.remove("profile.jpg")
        print("ceva")


    @commands.command()
    async def ben(self, ctx, *, intrebare):
      embed = discord.Embed(title=f"Ben raspunde la intrebarea:",description=intrebare ,color=discord.Color.green())
      if "BLACK" in str(intrebare).upper() or "NIGG" in str(intrebare).upper() or "BLM" in str(intrebare).upper() or "RACIST" in str(intrebare).upper() or "RASIST" in str(intrebare).upper():
        embed.set_image(url="https://cdn.discordapp.com/attachments/920425074882904104/950081866554277929/blackben.png")
        await ctx.reply(embed=embed)
        return

      if "LEAN" in str(intrebare).upper():
        embed.set_image(url="https://cdn.discordapp.com/attachments/920425074882904104/951223110101774446/artworks-KJ1dWrMtmKvrEDUi-mHUUdw-t240x240.jpg")
        await ctx.reply(embed=embed)
        return
      rand=randint(1,4)
      if rand==1:
        embed.set_image(url="https://cdn.discordapp.com/attachments/920425074882904104/950081866252292186/yesben.png")
      elif rand==2:
        embed.set_image(url="https://cdn.discordapp.com/attachments/920425074882904104/950081865962889216/noben.png")
      elif rand==3:
        embed.set_image(url="https://cdn.discordapp.com/attachments/920425074882904104/950081865564434442/hohoben.png")
      elif rand==4:
        embed.set_image(url="https://cdn.discordapp.com/attachments/920425074882904104/950081865140797440/blblben.png")
      await ctx.reply(embed=embed)

    @commands.command()
    async def kanye(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        wanted = Image.open("pad/fisiere/imagini/kanye.png")
        kanyemaini = Image.open("pad/fisiere/imagini/kanyemaini.png")
        if ctx.message.attachments:
            imagesufix = [".png", ".jpg", ".jpeg", ".gif"]
            for sufix in imagesufix:
                if ctx.message.attachments[0].filename.lower().endswith(sufix):
                    await (ctx.message.attachments[0]).save(f"avatar{sufix}")
                    avatar1 = Image.open(f"avatar{sufix}")
            avatar1 = avatar1.resize((128, 128))
            pfp = avatar1
            pfp = pfp.resize((300, 400))
            wanted.paste(pfp, (220, 370))
            wanted.paste(kanyemaini, (0,0), kanyemaini)
            wanted.save("profile.png")
            await ctx.reply(file=discord.File("profile.png"))
            os.remove("profile.png")
            os.remove("avatar.jpg")
            print("ceva")
            return
        avatar1 = member.avatar_url_as(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((300, 400))
        wanted.paste(pfp, (220, 370))
        wanted.paste(kanyemaini, (0,0), kanyemaini)
        wanted.save("profile.png")
        await ctx.reply(file=discord.File("profile.png"))
        os.remove("profile.png")
        print("ceva")



    @commands.command(aliases=['mesi'])
    async def messi(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        wanted = Image.open("pad/fisiere/imagini/messi.jpg")
        if ctx.message.attachments:
            imagesufix = [".png", ".jpg", ".jpeg", ".gif"]
            for sufix in imagesufix:
                if ctx.message.attachments[0].filename.lower().endswith(sufix):
                    await (ctx.message.attachments[0]).save(f"avatar{sufix}")
                    avatar1 = Image.open(f"avatar{sufix}")
            avatar1 = avatar1.resize((128, 128))
            pfp = avatar1
            pfp = pfp.resize((300, 400))
            wanted.paste(pfp, (715, 30))
            wanted.save("profile.jpg")
            await ctx.reply(file=discord.File("profile.jpg"))
            os.remove("profile.jpg")
            os.remove("avatar.jpg")
            print("ceva")
            return
        avatar1 = member.avatar_url_as(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((300, 400))
        wanted.paste(pfp, (715, 30))
        wanted.save("profile.jpg")
        await ctx.reply(file=discord.File("profile.jpg"))
        os.remove("profile.jpg")
        print("ceva")
  
    @commands.command(aliases=['12'])
    async def zamn(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        wanted = Image.open("pad/fisiere/imagini/zamn.jpg")
        if ctx.message.attachments:
            imagesufix = [".png", ".jpg", ".jpeg", ".gif"]
            for sufix in imagesufix:
                if ctx.message.attachments[0].filename.lower().endswith(sufix):
                    await (ctx.message.attachments[0]).save(f"avatar{sufix}")
                    avatar1 = Image.open(f"avatar{sufix}")
            avatar1 = avatar1.resize((128, 128))
            pfp = avatar1
            pfp = pfp.resize((100, 150))
            wanted.paste(pfp, (95, 28))
            wanted.save("profile.jpg")
            await ctx.reply(file=discord.File("profile.jpg"))
            os.remove("profile.jpg")
            os.remove("avatar.jpg")
            print("ceva")
            return
        avatar1 = member.avatar_url_as(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((100, 150))
        wanted.paste(pfp, (95, 28))
        wanted.save("profile.jpg")
        await ctx.reply(file=discord.File("profile.jpg"))
        os.remove("profile.jpg")
        print("ceva")
      

    @commands.command()
    async def tembel(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        wanted = Image.open("pad/fisiere/imagini/tembel.jpg")
        if ctx.message.attachments:
            imagesufix = [".png", ".jpg", ".jpeg", ".gif"]
            for sufix in imagesufix:
                if ctx.message.attachments[0].filename.lower().endswith(sufix):
                    await (ctx.message.attachments[0]).save(f"avatar{sufix}")
                    avatar1 = Image.open(f"avatar{sufix}")
            avatar1 = avatar1.resize((128, 128))
            pfp = avatar1
            pfp = pfp.resize((220, 220))
            wanted.paste(pfp, (30, 15))
            wanted.save("profile.jpg")
            await ctx.reply(file=discord.File("profile.jpg"))
            os.remove("profile.jpg")
            os.remove("avatar.jpg")
            print("ceva")
            return
        avatar1 = member.avatar_url_as(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((220, 220))
        wanted.paste(pfp, (30, 15))
        wanted.save("profile.jpg")
        await ctx.reply(file=discord.File("profile.jpg"))
        os.remove("profile.jpg")
        print("ceva")

    @commands.command()
    async def gay(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        wanted = Image.open("pad/fisiere/imagini/gay.jpg")
        if ctx.message.attachments:
            imagesufix = [".png", ".jpg", ".jpeg", ".gif"]
            for sufix in imagesufix:
                if ctx.message.attachments[0].filename.lower().endswith(sufix):
                    await (ctx.message.attachments[0]).save(f"avatar{sufix}")
                    avatar1 = Image.open(f"avatar{sufix}")
            avatar1 = avatar1.resize((128, 128))
            pfp = avatar1
            pfp = pfp.resize((503, 503))
            wanted.paste(pfp, (0, 69))
            wanted.save("profile.jpg")
            await ctx.reply(file=discord.File("profile.jpg"))
            os.remove("profile.jpg")
            os.remove("avatar.jpg")
            print("ceva")
        else:
            avatar1 = member.avatar_url_as(size=128)
            data = BytesIO(await avatar1.read())
            pfp = Image.open(data)
            pfp = pfp.resize((503, 503))
            wanted.paste(pfp, (0, 69))
            wanted.save("profile.jpg")
            await ctx.reply(file=discord.File("profile.jpg"))
            os.remove("profile.jpg")
            os.remove("avatar.jpg")
            print("ceva")

    @commands.command(aliases=['suprematie', 'suprem'])
    async def supremacy(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        wanted = Image.open("pad/fisiere/imagini/supremacy.jpg")
        if ctx.message.attachments:
            imagesufix = [".png", ".jpg", ".jpeg", ".gif"]
            for sufix in imagesufix:
                if ctx.message.attachments[0].filename.lower().endswith(sufix):
                    await (ctx.message.attachments[0]).save(f"avatar{sufix}")
                    avatar1 = Image.open(f"avatar{sufix}")
            avatar1 = avatar1.resize((128, 128))
            pfp = avatar1
            pfp = pfp.resize((400, 400))
            wanted.paste(pfp, (30, 430))
            font = ImageFont.truetype('pad/fisiere/fonturi/Helvetica-Bold.ttf', 67)
            draw = ImageDraw.Draw(wanted)
            draw.text((390, 180), f"chestia aia din poza", (0, 0, 0), font=font)
            wanted.save("profile.jpg")
            await ctx.reply(file=discord.File("profile.jpg"))
            os.remove("profile.jpg")
            os.remove("avatar.jpg")
            print("ceva")
            return
        avatar1 = member.avatar_url_as(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((400, 400))
        wanted.paste(pfp, (30, 430))
        font = ImageFont.truetype('pad/fisiere/fonturi/Helvetica-Bold.ttf', 97)
        draw = ImageDraw.Draw(wanted)
        draw.text((390, 180), f"{member.display_name}", (0, 0, 0), font=font)
        wanted.save("profile.jpg")
        await ctx.reply(file=discord.File("profile.jpg"))
        os.remove("profile.jpg")
        print("ceva")

    @commands.command(aliases=['fb'])
    async def facebook(self, ctx, member: discord.Member = None, *, text):
        wanted = Image.open("pad/fisiere/imagini/facebook.jpg")
        avatar1 = member.avatar_url_as(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((42, 42))
        wanted.paste(pfp, (10, 8))
        font = ImageFont.truetype('pad/fisiere/fonturi/Helvetica.ttf', 17)
        draw = ImageDraw.Draw(wanted)
        draw.text((59, 13), f"{member.display_name}", (66, 103, 178), font=font)
        if int(len(text)) >= 30:
            await ctx.reply("prea mult scrii mă")
            return
        if int(len(text)) <= 2:
            font2 = ImageFont.truetype('pad/fisiere/fonturi/Helvetica.ttf', 40)
            draw.text((245, 200), f"{text}", (255, 255, 255), font=font2)
        elif int(len(text)) <= 5:
            font2 = ImageFont.truetype('pad/fisiere/fonturi/Helvetica.ttf', 40)
            draw.text((218, 200), f"{text}", (255, 255, 255), font=font2)
        elif int(len(text)) <= 10:
            font2 = ImageFont.truetype('pad/fisiere/fonturi/Helvetica.ttf', 38)
            draw.text((180, 200), f"{text}", (255, 255, 255), font=font2)
        elif int(len(text)) <= 15:
            font2 = ImageFont.truetype('pad/fisiere/fonturi/Helvetica.ttf', 32)
            draw.text((130, 200), f"{text}", (255, 255, 255), font=font2)
        elif int(len(text)) < 20:
            font2 = ImageFont.truetype('pad/fisiere/fonturi/Helvetica.ttf', 28)
            draw.text((145, 200), f"{text}", (255, 255, 255), font=font2)
        elif int(len(text)) < 25:
            font2 = ImageFont.truetype('pad/fisiere/fonturi/Helvetica.ttf', 24)
            draw.text((117, 200), f"{text}", (255, 255, 255), font=font2)
        elif int(len(text)) < 30:
            font2 = ImageFont.truetype('pad/fisiere/fonturi/Helvetica.ttf', 24)
            draw.text((100, 200), f"{text}", (255, 255, 255), font=font2)
        wanted.save("profile.jpg")
        await ctx.reply(file=discord.File("profile.jpg"))
        os.remove("profile.jpg")
        print("ceva")

    @facebook.error
    async def facebook_error(self, ctx, error):
        await ctx.reply("**.facebook @persoana text**, te rog.")


def setup(client):
    client.add_cog(Imagini(client))