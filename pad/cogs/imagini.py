import discord
import imageio
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
from main import default_color

class Imagini(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def furry(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        # 0
        wanted0 = Image.open("pad/fisiere/imagini/furry.png")
        wanted0.save("pad/temp/profile0.png")

        # 1
        wanted1 = Image.open("pad/fisiere/imagini/furry.png")
        avatar1 = member.avatar.replace(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((100, 100))
        wanted1.paste(pfp, (2, 20))
        wanted1.save("pad/temp/profile1.png")
        # await ctx.reply(file=discord.File("profile.png"))
        # os.remove("profile.png")
        print("ceva")
        # 2
        wanted2 = Image.open("pad/fisiere/imagini/furry.png")
        avatar1 = member.avatar.replace(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((100, 100))
        wanted2.paste(pfp, (60, 65))
        wanted2.save("pad/temp/profile2.png")
        # await ctx.reply(file=discord.File("profile.png"))
        # os.remove("profile.png")
        print("ceva")
        # 3
        wanted3 = Image.open("pad/fisiere/imagini/furry.png")
        avatar1 = member.avatar.replace(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((100, 100))
        wanted3.paste(pfp, (130, 110))
        wanted3.save("pad/temp/profile3.png")
        # await ctx.reply(file=discord.File("profile.png"))
        # os.remove("profile.png")
        print("ceva")
        # 4
        wanted4 = Image.open("pad/fisiere/imagini/furry.png")
        avatar1 = member.avatar.replace(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((100, 100))
        wanted4.paste(pfp, (200, 155))
        wanted4.save("pad/temp/profile4.png")
        # await ctx.reply(file=discord.File("profile.png"))
        # os.remove("pad/profile.png")
        print("ceva")
        # 5
        wanted5 = Image.open("pad/fisiere/imagini/furry.png")
        avatar1 = member.avatar.replace(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((100, 100))
        wanted5.paste(pfp, (270, 200))
        wanted5.save("pad/temp/profile5.png")
        # await ctx.reply(file=discord.File("profile.png"))
        # os.remove("profile.png")
        print("ceva")
        # 6
        wanted6 = Image.open("pad/fisiere/imagini/furry.png")
        avatar1 = member.avatar.replace(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((100, 100))
        wanted6.paste(pfp, (250, 250))
        wanted6.save("pad/temp/profile6.png")
        # await ctx.reply(file=discord.File("profile.png"))
        # os.remove("profile.png")
        print("ceva")
        # 7
        wanted7 = Image.open("pad/fisiere/imagini/furry.png")
        avatar1 = member.avatar.replace(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((100, 100))
        wanted7.paste(pfp, (230, 300))
        wanted7.save("pad/temp/profile7.png")
        # await ctx.reply(file=discord.File("profile.png"))
        # os.remove("profile.png")
        print("ceva")
        # 8
        wanted8 = Image.open("pad/fisiere/imagini/furry.png")
        avatar1 = member.avatar.replace(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((100, 100))
        wanted8.paste(pfp, (210, 350))
        wanted8.save("pad/temp/profile8.png")
        # await ctx.reply(file=discord.File("profile.png"))
        # os.remove("profile.png")
        print("ceva")
        # 9
        wanted9 = Image.open("pad/fisiere/imagini/furry.png")
        avatar1 = member.avatar.replace(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((100, 100))
        wanted9.paste(pfp, (190, 400))
        wanted9.save("pad/temp/profile9.png")
        # await ctx.reply(file=discord.File("profile.png"))
        # os.remove("profile.png")
        print("ceva")
        imgs = (wanted0, wanted1, wanted2, wanted3, wanted4, wanted5, wanted6, wanted7, wanted8, wanted9)
        wanted0.save('movie.gif', save_all=True, append_images=imgs, optimize=False, duration=60, loop=0)
        await ctx.reply(file=discord.File("movie.gif"))
        os.remove("movie.gif")
        os.remove("pad/temp/profile0.png")
        os.remove("pad/temp/profile1.png")
        os.remove("pad/temp/profile2.png")
        os.remove("pad/temp/profile3.png")
        os.remove("pad/temp/profile4.png")
        os.remove("pad/temp/profile5.png")
        os.remove("pad/temp/profile6.png")
        os.remove("pad/temp/profile7.png")
        os.remove("pad/temp/profile8.png")
        os.remove("pad/temp/profile9.png")

    @commands.command()
    async def wanted(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        wanted = Image.open("pad/fisiere/imagini/wanted.jpg")
        avatar1 = member.avatar.replace(size=128)
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
        embed = discord.Embed(title=f"Ben raspunde la intrebarea:", description=intrebare, color=default_color)
        if "BLACK" in str(intrebare).upper() or "NIGG" in str(intrebare).upper() or "BLM" in str(
                intrebare).upper() or "RACIST" in str(intrebare).upper() or "RASIST" in str(intrebare).upper():
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/920425074882904104/950081866554277929/blackben.png")
            await ctx.reply(embed=embed)
            return

        if "LEAN" in str(intrebare).upper():
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/920425074882904104/951223110101774446/artworks-KJ1dWrMtmKvrEDUi-mHUUdw-t240x240.jpg")
            await ctx.reply(embed=embed)
            return
        rand = randint(1, 4)
        if rand == 1:
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/920425074882904104/950081866252292186/yesben.png")
        elif rand == 2:
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/920425074882904104/950081865962889216/noben.png")
        elif rand == 3:
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/920425074882904104/950081865564434442/hohoben.png")
        elif rand == 4:
            embed.set_image(
                url="https://cdn.discordapp.com/attachments/920425074882904104/950081865140797440/blblben.png")
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
            wanted.paste(kanyemaini, (0, 0), kanyemaini)
            wanted.save("profile.png")
            await ctx.reply(file=discord.File("profile.png"))
            os.remove("profile.png")
            os.remove("avatar.jpg")
            print("ceva")
            return
        avatar1 = member.avatar.replace(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((300, 400))
        wanted.paste(pfp, (220, 370))
        wanted.paste(kanyemaini, (0, 0), kanyemaini)
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
        avatar1 = member.avatar.replace(size=128)
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
        avatar1 = member.avatar.replace(size=128)
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
        avatar1 = member.avatar.replace(size=128)
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
            avatar1 = member.avatar.replace(size=128)
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
        avatar1 = member.avatar.replace(size=128)
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
        avatar1 = member.avatar.replace(size=128)
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


async def setup(client):
    await client.add_cog(Imagini(client))