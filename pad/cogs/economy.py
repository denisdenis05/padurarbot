import discord
import random
import json
import os
import re
import time
import datetime
import asyncio
from discord.ext import commands
from discord.ui import Button, View
from random import randint
from datetime import datetime
import main
from io import BytesIO
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def plm(self, ctx):
        await ctx.reply("+10 social credits")

    @commands.command(aliases=['frunze', 'frunz', 'leafs', 'balance', 'balanta', 'portofel', 'visa', 'bal'])
    async def frunza(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"frunze{member.id}" not in data or int(data[f"frunze{member.id}"]) == 0:
            embed = discord.Embed(title="Omg nu ai un cont bancar!",
                                  description="Nu ai nicio frunza in contul tau bancar, dar asta se rezolva usor! Foloseste orice comanda din cadrul celor de economie, castiga frunze si intoarce-te inapoi!",
                                  color=discord.Color.green())
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/860172893816094771/1005179959389720606/PngItem_5308600.png")
            embed.set_footer(text=f"Foloseste comanda `help` pentru a afla cum poti castiga frunze")
            await ctx.reply(embed=embed)
            return

        nr = data[f"frunze{member.id}"]
        if nr < 1000:
            nr = int(nr)
        elif nr < 1000000:
            nr = str("{:.2f}".format(nr / 1000)) + "k"
        elif nr < 1000000000:
            nr = str("{:.3f}".format(nr / 1000000)) + "M"
        elif nr < 1000000000000:
            nr = str("{:.4f}".format(nr / 1000000000)) + "B"
        else:
            nr = str("{:.5f}".format(nr / 1000000000000)) + "T"
        wanted = Image.open("pad/fisiere/imagini/card.png")
        avatar1 = member.avatar.replace(size=128)
        data = BytesIO(await avatar1.read())
        pfp = Image.open(data)
        pfp = pfp.resize((80, 80))
        wanted.paste(pfp, (95, 264))
        font = ImageFont.truetype('pad/fisiere/fonturi/Myriad.ttf', 40)
        draw = ImageDraw.Draw(wanted)
        draw.text((100, 623), f"Sold curent:", (47, 98, 193), font=font)
        draw.text((100, 693), f"{nr} frunze", (47, 98, 153), font=font)
        wanted.save("pad/temp/balance.png")
        await ctx.reply(file=discord.File("pad/temp/balance.png"))
        os.remove("pad/temp/balance.png")

    @commands.command(aliases=['inv', 'inventory', 'ghiozdan', 'geanta'])
    async def inventar(self, ctx, member: discord.Member = None):
        if ctx.author.id != 852673995563597875 and member != None and member.id != ctx.author.id:
            embed = discord.Embed(title=f"Nu poti vedea ce detine {member}",
                                  description="Continutul ghiozdanului este ascuns", color=discord.Color.green())
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/920425074882904104/1005441465637408860/1659786314913.png")
            embed.set_footer(text=f"Cere-i personal lui {member} sa foloseasca comanda `inventar`")
            await ctx.reply(embed=embed)
            return
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"inventar{ctx.author.id}" not in data:
            embed = discord.Embed(title=f"Continutul ghiozdanului tau", description="Se pare ca e gol????",
                                  color=discord.Color.green())
            embed.set_thumbnail(url="https://www.pngall.com/wp-content/uploads/2016/04/Backpack-Download-PNG.png")
            embed.set_footer(text=f"Foloseste comanda `help` pentru a gasi comenzi care te vor ajuta sa castigi iteme")
            await ctx.reply(embed=embed)
            return
        text = ""
        with open("pad/data/iteme.json", "r") as jsonFile:
            itemdata = json.load(jsonFile)
            jsonFile.close()
        inv = data[f"inventar{ctx.author.id}"]
        main.inventar[str(ctx.author.id)] = {}
        i = 1
        for k in inv:
            print(k)
            if int(inv[k]) > 0:
                itemdata[k]["nr"] = inv[k]
                main.inventar[str(ctx.author.id)][str(i)] = itemdata[k]
                i = i + 1
                if i < 12:
                    if text == "":
                        text = "Ai in ghiozdan:\n\n"
                    text = text + "**" + itemdata[k]["nume"] + "** " + itemdata[k]["emoji"] + " :" + str(inv[k]) + '\n'

        if text == "":
            text = "Se pare ca e gol????"
            embed = discord.Embed(title=f"Continutul ghiozdanului tau", description=text, color=discord.Color.green())
            embed.set_footer(text=f"Foloseste comanda `help` pentru a gasi comenzi care te vor ajuta sa castigi iteme")
        else:
            view = View()
            if i > 11:
                embed = discord.Embed(title=f"Continutul ghiozdanului tau | 1", description=text,
                                      color=discord.Color.green())
                buton1 = Button(style=discord.ButtonStyle.primary, emoji="⏪", disabled=True, custom_id="invback")
                buton2 = Button(style=discord.ButtonStyle.primary, emoji="⏩", custom_id="invnext")
                view.add_item(buton1)
                view.add_item(buton2)
            else:
                embed = discord.Embed(title=f"Continutul ghiozdanului tau", description=text,
                                      color=discord.Color.green())
            embed.set_footer(text=f"Foloseste itemele intelept!!!\n| {ctx.author.id} |")
        embed.set_thumbnail(url="https://www.pngall.com/wp-content/uploads/2016/04/Backpack-Download-PNG.png")
        mesaj = await ctx.reply(embed=embed, view=view)
        timeout = 0
        while True:
            timeout = timeout + 1
            await asyncio.sleep(1)
            if timeout == 30:
                main.inventar[str(ctx.author.id)] = {}
                view = View()
                buton1 = Button(style=discord.ButtonStyle.primary, emoji="⏪", custom_id="invback", disabled=True)
                buton2 = Button(style=discord.ButtonStyle.primary, emoji="⏩", custom_id="invnext", disabled=True)
                view.add_item(buton1)
                view.add_item(buton2)
                await mesaj.edit(embed=embed, view=view)
                return

    @inventar.error
    async def inventar_error(self, ctx, error):
        print(error)

    @commands.command(aliases=['steal', 'rob', 'furt', 'thief', 'fură'])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def fura(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        broom = 0
        if f"inventar{ctx.author.id}" in data:
            inv = data[f"inventar{ctx.author.id}"]
            if "item5" in inv and inv["item5"] > 0:
                view = View()
                broom = -1

                async def evident(interaction: discord.Interaction):
                    if interaction.user.id != ctx.author.id:
                        await interaction.response.defer()
                        return
                    view2 = View()
                    buton1 = Button(style=discord.ButtonStyle.primary, label="Evident!", emoji="😊", disabled=True)
                    buton2 = Button(style=discord.ButtonStyle.danger, label="Nu.", emoji="😠", disabled=True)
                    view2.add_item(buton1)
                    view2.add_item(buton2)
                    await interaction.response.edit_message(content="Raspuns: da", view=view2)
                    await interaction.response.defer()

                async def nuevident(interaction: discord.Interaction):
                    if interaction.user.id != ctx.author.id:
                        await interaction.response.defer()
                        return
                    view2 = View()
                    buton1 = Button(style=discord.ButtonStyle.primary, label="Evident!", emoji="😊", disabled=True)
                    buton2 = Button(style=discord.ButtonStyle.danger, label="Nu.", emoji="😠", disabled=True)
                    view2.add_item(buton1)
                    view2.add_item(buton2)
                    await interaction.response.edit_message(content="Raspuns: nu", view=view2)
                    await interaction.response.defer()

                buton1 = Button(style=discord.ButtonStyle.primary, label="Evident!", emoji="😊")
                buton2 = Button(style=discord.ButtonStyle.danger, label="Nu.", emoji="😠")
                buton1.callback = evident
                buton2.callback = nuevident
                view.add_item(buton1)
                view.add_item(buton2)
                embed = discord.Embed(title=f"Ai o matura in inventar", description="Vrei sa o folosesti?",
                                      color=discord.Color.green())
                mesaj1 = await ctx.reply(embed=embed, view=view)
                timeout = 0
                while True:
                    if timeout == 20:
                        view2 = View()
                        buton1 = Button(style=discord.ButtonStyle.primary, label="Evident!", emoji="😊", disabled=True)
                        buton2 = Button(style=discord.ButtonStyle.danger, label="Nu.", emoji="😠", disabled=True)
                        view2.add_item(buton1)
                        view2.add_item(buton2)
                        await mesaj1.edit(view=view2)
                        return
                    await asyncio.sleep(1)
                    msg = await ctx.fetch_message(mesaj1.id)
                    print(str(msg.content))
                    if "Raspuns: da" in str(msg.content):
                        broom = 1
                        break
                    elif "Raspuns: nu" in str(msg.content):
                        broom = 0
                        break
                    timeout = timeout + 1
        else:
            data[f"inventar{ctx.author.id}"] = {}
            inv = {}
        breakrate = 0
        if broom == 1:
            sansa = randint(1, 4)
            if (sansa == 1):
                frunze = randint(1, 4)
            else:
                frunze = randint(1, 3)
            if frunze == 1:
                frunze = randint(300, 900)
            elif frunze == 2:
                frunze = randint(900, 2000)
            elif frunze == 3:
                frunze = randint(2000, 5000)
            else:
                frunze = randint(5000, 9000)
            breakrate = randint(1, 3)
        else:
            frunze = randint(2, 400)
        sansabustean = randint(1, 4)
        if sansabustean == 2:
            busteni = randint(1, 3)
        else:
            busteni = 0
        politie = randint(1, 4)
        if politie > 1:
            text = f"Ia sa vedem ce ai gasit in padure:\n\n<:frunza:1005499341210927255> **Frunze**: {frunze}\n\n"
            if busteni != 0:
                text = text + f"<:busteni:1005444832895959180> **Busteni**: {busteni}"
            if frunze > 2000:
                embed = discord.Embed(title=f"Ai furat din padure (nerespectuos)", description=text,
                                      color=discord.Color.green())
            else:
                embed = discord.Embed(title=f"Ai furat din padure", description=text, color=discord.Color.green())
            embed.set_thumbnail(url="https://www.picng.com/upload/thief/png_thief_40046.png")
            if breakrate == 2:
                embed.add_field(name=f"❗❗TI-AI RUPT MATURA❗❗",
                                value=f"Daca nu mai ai maturi in inventar, e vai de tine.")
            embed.set_footer(text=f"Buna prada.")
            await ctx.reply(embed=embed)

            if f"frunze{ctx.author.id}" not in data:
                datafrunze = 0
            else:
                datafrunze = data[f"frunze{ctx.author.id}"]
            if f"inventar{ctx.author.id}" not in data:
                data[f"inventar{ctx.author.id}"] = {}
            if f"item1" not in data[f"inventar{ctx.author.id}"]:
                databusteni = 0
            else:
                databusteni = data[f"inventar{ctx.author.id}"][f"item1"]
            datafrunze = int(datafrunze + frunze)
            databusteni = int(databusteni + busteni)
            data[f"frunze{ctx.author.id}"] = datafrunze
            data[f"inventar{ctx.author.id}"][f"item1"] = databusteni
        else:
            text = f"Ia sa vedem ce a capturat politia:\n\n<:frunza:1005499341210927255> **Frunze**: {frunze}\n\n"
            if busteni != 0:
                text = text + f"<:busteni:1005444832895959180> **Busteni**: {busteni}"
            embed = discord.Embed(title=f"TE-A PRINS POLITIA", description=text, color=discord.Color.red())
            embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2561/2561978.png")
            if breakrate == 2:
                embed.add_field(name=f"❗❗TI-AI RUPT MATURA❗❗",
                                value=f"Daca nu mai ai maturi in inventar, e vai de tine.")
            embed.set_footer(text=f"Naspa. Politia ti-a confiscat tot ce ai furat")
            await ctx.reply(embed=embed)
        if f"inventar{ctx.author.id}" not in data:
            data[f"inventar{ctx.author.id}"] = {}
        if f"item5" not in data[f"inventar{ctx.author.id}"]:
            maturi = 0
        else:
            maturi = data[f"inventar{ctx.author.id}"]["item5"]
        if breakrate == 2:
            data[f"inventar{ctx.author.id}"][f"item5"] = int(maturi - 1)
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()

    @fura.error
    async def fura_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            timp = error.retry_after
            em = discord.Embed(title=f"Usor domnule.",
                               description=f"Ai de asteptat {timp:.0f} secunde pentru a fura iar",
                               color=discord.Color.green())
            await ctx.reply(embed=em)

    @commands.command(aliases=['bet', 'zaruri', 'gamble'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def barbut(self, ctx, amount=""):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"frunze{ctx.author.id}" not in data or data[f"frunze{ctx.author.id}"] == 0:
            frunze = 0
        else:
            frunze = data[f"frunze{ctx.author.id}"]
        if amount == "":
            em = discord.Embed(title=f"Pariul minim e de 200 de frunze",
                               description=f"Foloseste comanda sub forma `.barbut 200`", color=discord.Color.green())
            await ctx.reply(embed=em)
            return
        if "ALL" in amount.upper() or "TOT" in amount.upper():
            amount = frunze
        else:
            amount = int(amount)
        if int(amount) < 200:
            em = discord.Embed(title=f"Pariul minim e de 200 de frunze",
                               description=f"Nu poti paria {amount} frunze. Mai adauga {200 - int(amount)}.",
                               color=discord.Color.green())
            await ctx.reply(embed=em)
            return
        if frunze < int(amount):
            em = discord.Embed(title=f"Nu ai destule frunze",
                               description=f"Mai ai de castigat {int(amount) - frunze} pentru a putea paria atat.",
                               color=discord.Color.green())
            await ctx.reply(embed=em)
            return
        if int(amount) > 20000:
            em = discord.Embed(title=f"Nu poti paria atat de mult",
                               description=f"Inteleg ca esti bogat da las-o mai moale.", color=discord.Color.green())
            await ctx.reply(embed=em)
            return

        async def singur(interaction: discord.Interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.defer()
                return
            view2 = View()
            buton1 = Button(style=discord.ButtonStyle.success, label="Singur", emoji="🤖", disabled=True)
            buton2 = Button(style=discord.ButtonStyle.primary, label="Cu un prieten", emoji="🧍‍♂️", disabled=True)
            view2.add_item(buton1)
            view2.add_item(buton2)
            await interaction.response.edit_message(content="Raspuns: singur", view=view2)
            await interaction.response.defer()

        async def prieten(interaction: discord.Interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.defer()
                return
            view2 = View()
            buton1 = Button(style=discord.ButtonStyle.success, label="Singur", emoji="🤖", disabled=True)
            buton2 = Button(style=discord.ButtonStyle.primary, label="Cu un prieten", emoji="🧍‍♂️", disabled=True)
            view2.add_item(buton1)
            view2.add_item(buton2)
            await interaction.response.edit_message(content="Raspuns: prieten", view=view2)
            await interaction.response.defer()

        view = View()
        buton1 = Button(style=discord.ButtonStyle.success, label="Singur", emoji="🤖")
        buton2 = Button(style=discord.ButtonStyle.primary, label="Cu un prieten", emoji="🧍‍♂️")
        buton1.callback = singur
        buton2.callback = prieten
        view.add_item(buton1)
        view.add_item(buton2)
        embed = discord.Embed(title=f"Cum vrei sa te joci, singur sau cu un prieten?",
                              description="•Singur: te vei juca cu botul la umbra unui copac, 0 taxe\n•Cu un prieten: te vei juca cu un prieten intr-un cazino autorizat, 20% taxe",
                              color=discord.Color.green())
        mesaj1 = await ctx.reply(embed=embed, view=view)
        coechipier = ""
        timeout = 0
        while True:
            if timeout == 20:
                view2 = View()
                buton1 = Button(style=discord.ButtonStyle.success, label="Singur", emoji="🤖", disabled=True)
                buton2 = Button(style=discord.ButtonStyle.primary, label="Cu un prieten", emoji="🧍‍♂️", disabled=True)
                view2.add_item(buton1)
                view2.add_item(buton2)
                await mesaj1.edit(view=view2)
                return
            await asyncio.sleep(1)
            msg = await ctx.fetch_message(mesaj1.id)
            print(str(msg.content))
            if "Raspuns: singur" in str(msg.content):
                coechipier = "singur"
                break
            elif "Raspuns: prieten" in str(msg.content):
                coechipier = "prieten"
                break
            timeout = timeout + 1

        if coechipier == "singur":
            castigpierdere = randint(1, 10)
            if castigpierdere <= 3:
                random1 = 1
                random2 = 0
                while random1 >= random2:
                    random1 = randint(1, 6)
                    random2 = randint(1, 6)
            elif castigpierdere == 4:
                random1 = randint(1, 6)
                random2 = random1
            if castigpierdere >= 5:
                random1 = 0
                random2 = 1
                while random1 <= random2:
                    random1 = randint(1, 6)
                    random2 = randint(1, 6)
            if random1 < random2:
                procent = randint(30, 60)
                embed = discord.Embed(title="", description="", color=discord.Color.green())
                embed.add_field(name="Padurar la Baneasa", value=f'A dat cu zarul: {random1}', inline=True)
                embed.set_author(name="Barbut la umbra unui copac",
                                 icon_url="https://pngimg.com/uploads/dice/dice_PNG113.png")
                embed.set_thumbnail(url="https://cdn.britannica.com/95/156695-131-FF89C9FA/oak-tree.jpg")
                embed.add_field(name=f"{ctx.author.name}", value=f'A dat cu zarul: {random2}', inline=True)
                embed.set_footer(text=f"{ctx.author} | Procent câștigat: {procent}%", icon_url=ctx.author.avatar.url)
                floatt = float(procent / 100)
                embed.add_field(name="Felicitari!!!", value=f"Ai castigat `{int(amount + (amount * floatt))}` frunze",
                                inline=False)
                data[f"frunze{ctx.author.id}"] = int(data[f"frunze{ctx.author.id}"]) + int(amount * floatt)

            elif random1 > random2:
                embed = discord.Embed(title="", description="", color=discord.Color.red())
                embed.add_field(name="Padurar la Baneasa", value=f'A dat cu zarul: {random1}', inline=True)
                embed.set_author(name="Barbut la umbra unui copac",
                                 icon_url="https://pngimg.com/uploads/dice/dice_PNG113.png")
                embed.set_thumbnail(url="https://cdn.britannica.com/95/156695-131-FF89C9FA/oak-tree.jpg")
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.add_field(name=f"{ctx.author.name}", value=f'A dat cu zarul: {random2}', inline=True)
                embed.add_field(name="Ghinion!!!", value=f"Ai pierdut `{int(amount)}` frunze", inline=False)
                data[f"frunze{ctx.author.id}"] = int(data[f"frunze{ctx.author.id}"]) - int(amount)
            else:
                embed = discord.Embed(title="", description="", color=discord.Color.gold())
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.add_field(name="Padurar la Baneasa", value=f'A dat cu zarul: {random1}', inline=True)
                embed.set_author(name="Barbut la umbra unui copac",
                                 icon_url="https://pngimg.com/uploads/dice/dice_PNG113.png")
                embed.set_thumbnail(url="https://cdn.britannica.com/95/156695-131-FF89C9FA/oak-tree.jpg")
                embed.add_field(name=f"{ctx.author.name}", value=f'A dat cu zarul: {random2}', inline=True)
                embed.add_field(name="Asta este", value=f"E egalitate, n-ai pierdut nimic.", inline=False)
            await ctx.send(embed=embed)
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            return
        elif coechipier == "prieten":
            def is_correct(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

            msgl1 = await ctx.send("Care-i prietenul cu care vrei sa te joci? (da-i ping)")
            msgl2 = await self.client.wait_for('message', check=is_correct, timeout=20)
            print("OK")
            if "<@" in str(msgl2.content):
                if "<@!" in str(msgl2.content):
                    id = re.search('<@!(.*?)>', str(msgl2.content)).group(1)
                else:
                    id = re.search('<@(.*?)>', str(msgl2.content)).group(1)
            await msgl1.delete()
            await msgl2.delete()
            id = int(id)
            if ctx.author.id == id:
                em = discord.Embed(title=f"??????",
                                   description=f"Nu te poti juca cu tine insuti.\n\nRuleaza comanda din nou",
                                   color=discord.Color.green())
                await ctx.reply(embed=em)
                return
            if f"frunze{id}" not in data or data[f"frunze{id}"] < amount:
                em = discord.Embed(title=f"Oponentul n-are destule frunze",
                                   description=f"Suma de {amount} frunze este prea mare pentru <@{id}>",
                                   color=discord.Color.green())
                await ctx.reply(embed=em)
                return
            else:
                frunze2 = data[f"frunze{id}"]
            oponent = ctx.guild.get_member(int(id))

            async def da(interaction: discord.Interaction):
                if interaction.user.id != id:
                    await interaction.response.defer()
                    return
                view2 = View()
                buton1 = Button(style=discord.ButtonStyle.success, label="Da", disabled=True)
                buton2 = Button(style=discord.ButtonStyle.danger, label="Nu", disabled=True)
                view2.add_item(buton1)
                view2.add_item(buton2)
                await interaction.response.edit_message(content="Raspuns: da", view=view2)
                await interaction.response.defer()

            async def nu(interaction: discord.Interaction):
                if interaction.user.id != id:
                    await interaction.response.defer()
                    return
                view2 = View()
                buton1 = Button(style=discord.ButtonStyle.success, label="Da", disabled=True)
                buton2 = Button(style=discord.ButtonStyle.danger, label="Nu", disabled=True)
                view2.add_item(buton1)
                view2.add_item(buton2)
                await interaction.response.edit_message(content="Raspuns: nu", view=view2)
                await interaction.response.defer()

            view = View()
            buton1 = Button(style=discord.ButtonStyle.success, label="Da")
            buton2 = Button(style=discord.ButtonStyle.danger, label="Nu")
            buton1.callback = da
            buton2.callback = nu
            view.add_item(buton1)
            view.add_item(buton2)
            embed = discord.Embed(title=f"Provocare extrema",
                                  description=f"<@{id}>, ii accepti provocarea lui {ctx.author}?",
                                  color=discord.Color.green())
            mesaj1 = await ctx.reply(embed=embed, view=view)
            da = 0
            timeout = 0
            while True:
                if timeout == 40:
                    view2 = View()
                    buton1 = Button(style=discord.ButtonStyle.success, label="Da", disabled=True)
                    buton2 = Button(style=discord.ButtonStyle.danger, label="Nu", disabled=True)
                    view2.add_item(buton1)
                    view2.add_item(buton2)
                    await mesaj1.edit(view=view2)
                    return
                await asyncio.sleep(1)
                msg = await ctx.fetch_message(mesaj1.id)
                print(str(msg.content))
                if "Raspuns: da" in str(msg.content):
                    break
                elif "Raspuns: nu" in str(msg.content):
                    return
                timeout = timeout + 1
            random1 = randint(1, 6)
            random2 = randint(1, 6)
            if random1 < random2:
                floatt = 0.2
                embed = discord.Embed(title="", description="", color=discord.Color.green())
                embed.add_field(name=oponent.name, value=f'A dat cu zarul: {random1}', inline=True)
                embed.set_author(name="Cazino autorizat 'Marian Casino'",
                                 icon_url="https://pngimg.com/uploads/dice/dice_PNG113.png")
                embed.set_thumbnail(
                    url="https://img.traveltriangle.com/blog/wp-content/uploads/2018/09/hong-kong-casinos-cover.jpg")
                embed.add_field(name=ctx.author.name, value=f'A dat cu zarul: {random2}', inline=True)
                embed.set_footer(text=f"Taxa perceputa: 20%")
                embed.add_field(name=f"CASTIGATOR: {ctx.author.name}",
                                value=f"Castig `{int(amount - (amount * floatt))}` frunze", inline=False)
                data[f"frunze{ctx.author.id}"] = int(data[f"frunze{ctx.author.id}"]) + int(amount - (amount * floatt))
                data[f"frunze{oponent.id}"] = int(data[f"frunze{oponent.id}"]) - int(amount)

            elif random1 > random2:
                floatt = 0.2
                embed = discord.Embed(title="", description="", color=discord.Color.green())
                embed.add_field(name=oponent.name, value=f'A dat cu zarul: {random1}', inline=True)
                embed.set_author(name="Cazino autorizat 'Marian Casino'",
                                 icon_url="https://pngimg.com/uploads/dice/dice_PNG113.png")
                embed.set_thumbnail(
                    url="https://img.traveltriangle.com/blog/wp-content/uploads/2018/09/hong-kong-casinos-cover.jpg")
                embed.set_footer(text=f"Taxa perceputa: 20%")
                embed.add_field(name=ctx.author.name, value=f'A dat cu zarul: {random2}', inline=True)
                embed.add_field(name=f"CASTIGATOR: {oponent.name}",
                                value=f"Castig `{int(amount - (amount * floatt))}` frunze", inline=False)
                data[f"frunze{oponent.id}"] = int(data[f"frunze{oponent.id}"]) + int(amount - (amount * floatt))
                data[f"frunze{ctx.author.id}"] = int(data[f"frunze{ctx.author.id}"]) - int(amount)
            else:
                embed = discord.Embed(title="", description="", color=discord.Color.gold())
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.add_field(name=oponent.name, value=f'A dat cu zarul: {random1}', inline=True)
                embed.set_author(name="Cazino autorizat 'Marian Casino'",
                                 icon_url="https://pngimg.com/uploads/dice/dice_PNG113.png")
                embed.set_thumbnail(
                    url="https://img.traveltriangle.com/blog/wp-content/uploads/2018/09/hong-kong-casinos-cover.jpg")
                embed.add_field(name=f"{ctx.author.name}", value=f'A dat cu zarul: {random2}', inline=True)
                embed.add_field(name="Asta este", value=f"E egalitate, nu sunt pierderi.", inline=False)
            await ctx.send(embed=embed)
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            return

    @barbut.error
    async def barbur_error(self, ctx, error):
        print(error)

        if isinstance(error, commands.CommandOnCooldown):
            timp = error.retry_after
            em = discord.Embed(title=f"Usor domnule.",
                               description=f"Ai de asteptat {timp:.0f} secunde pentru a paria iar",
                               color=discord.Color.green())
            await ctx.reply(embed=em)
        else:
            em = discord.Embed(title=f"Ceva nu a mers bine :(",
                               description=f"Verifica daca ai folosit bine comanda si incearca din nou",
                               color=discord.Color.green())
            await ctx.reply(embed=em)

    @commands.command(aliases=['bj', 'twentyone', '21', 'pontoon'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def blackjack(self, ctx, amount=""):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"frunze{ctx.author.id}" not in data or data[f"frunze{ctx.author.id}"] == 0:
            frunze = 0
        else:
            frunze = data[f"frunze{ctx.author.id}"]
        if amount == "":
            em = discord.Embed(title=f"Pariul minim e de 200 de frunze",
                               description=f"Foloseste comanda sub forma `.blackjack 200`", color=discord.Color.green())
            await ctx.reply(embed=em)
            return
        if "ALL" in amount.upper() or "TOT" in amount.upper():
            amount = frunze
        else:
            amount = int(amount)
        if int(amount) < 200:
            em = discord.Embed(title=f"Pariul minim e de 200 de frunze",
                               description=f"Nu poti paria {amount} frunze. Mai adauga {200 - int(amount)}.",
                               color=discord.Color.green())
            await ctx.reply(embed=em)
            return
        if frunze < int(amount):
            em = discord.Embed(title=f"Nu ai destule frunze",
                               description=f"Mai ai de castigat {int(amount) - frunze} pentru a putea paria atat.",
                               color=discord.Color.green())
            await ctx.reply(embed=em)
            return
        if int(amount) > 7000:
            em = discord.Embed(title=f"Nu poti paria atat de mult",
                               description=f"Inteleg ca esti bogat da las-o mai moale.", color=discord.Color.green())
            await ctx.reply(embed=em)
            return
        nr = int(amount)

        baniii = data[f"frunze{ctx.author.id}"]
        castig = discord.Embed(title="GG ai câștigat", color=discord.Color.green())
        procent = randint(30, 70)
        floatt = float(procent / 100)
        sumacastigata = int(nr + (nr * floatt))
        castig.set_footer(text=f"{ctx.author} | Suma câștigată: {sumacastigata} frunze", icon_url=ctx.author.avatar.url)
        castig.set_thumbnail(
            url="https://img.traveltriangle.com/blog/wp-content/uploads/2018/09/hong-kong-casinos-cover.jpg")
        castig.set_author(name="Cazino autorizat 'Marian Casino'",
                          icon_url="https://cdn.discordapp.com/attachments/745384647885848594/866669346675359764/580b585b2edbce24c47b27a6.jpg")
        egal = discord.Embed(title="Egalitate", color=discord.Color.gold())
        egal.set_footer(text=f"{ctx.author} | Suma câștigată: 0 frunze", icon_url=ctx.author.avatar.url)
        egal.set_thumbnail(
            url="https://img.traveltriangle.com/blog/wp-content/uploads/2018/09/hong-kong-casinos-cover.jpg")
        egal.set_author(name="Cazino autorizat 'Marian Casino'",
                        icon_url="https://cdn.discordapp.com/attachments/745384647885848594/866669346675359764/580b585b2edbce24c47b27a6.jpg")
        pierdere = discord.Embed(title="Fara gg, ai pierdut.", color=discord.Color.red())
        pierdere.set_footer(text=f"{ctx.author} | Suma pierduta: {nr}", icon_url=ctx.author.avatar.url)
        pierdere.set_thumbnail(
            url="https://img.traveltriangle.com/blog/wp-content/uploads/2018/09/hong-kong-casinos-cover.jpg")
        pierdere.set_author(name="Cazino autorizat 'Marian Casino'",
                            icon_url="https://cdn.discordapp.com/attachments/745384647885848594/866669346675359764/580b585b2edbce24c47b27a6.jpg")

        # initializare
        cartea1 = randint(2, 13)
        cartea2 = randint(2, 13)
        if baniii > 30000:
            cartea1 = randint(5, 13)
            cartea2 = randint(6, 13)
        if cartea1 + cartea2 == 21:
            cartea1 = randint(5, 13)
            cartea2 = randint(6, 13)
        scor = cartea1 + cartea2
        if cartea1 == 11:
            cartea1 = "J"
        elif cartea1 == 12:
            cartea1 = "Q"
        elif cartea1 == 13:
            cartea1 = "K"
        if cartea2 == 11:
            cartea2 = "J"
        elif cartea2 == 12:
            cartea2 = "Q"
        elif cartea2 == 13:
            cartea2 = "K"
        carti = str(cartea1) + ", " + str(cartea2)
        scorbot = randint(2, 13) + randint(2, 13)
        if scor == 21 and scorbot != 21:
            castig.add_field(name=f"Scor Padurar:", value=f"Botul are un scor adunat de {scorbot}")
            castig.add_field(name=f"Scorul tau: {scor}", value=f"Carti: {carti}")
            await ctx.send(embed=castig)
            data[f"frunze{ctx.author.id}"] = data[f"frunze{ctx.author.id}"] + (sumacastigata - int(nr))
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            return
        elif scor >= 21 and scor == scorbot:
            egal.add_field(name=f"Scor Padurar:", value=f"Botul are un scor adunat de {scorbot}")
            egal.add_field(name=f"Scorul tau: {scor}", value=f"Carti: {carti}")
            await ctx.send(embed=egal)
            return
        elif scorbot == 21 and scor != 21:
            pierdere.add_field(name=f"Scor Padurar:", value=f"Botul are un scor adunat de {scorbot}")
            pierdere.add_field(name=f"Scorul tau: {scor}", value=f"Carti: {carti}")
            await ctx.send(embed=pierdere)
            data[f"frunze{ctx.author.id}"] = data[f"frunze{ctx.author.id}"] - nr
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            return
        elif scorbot > 21 and scorbot > scor:
            castig.add_field(name=f"Scor Padurar:", value=f"Botul are un scor adunat de {scorbot}")
            castig.add_field(name=f"Scorul tau: {scor}", value=f"Carti: {carti}")
            await ctx.send(embed=castig)
            data[f"frunze{ctx.author.id}"] = data[f"frunze{ctx.author.id}"] + (sumacastigata - int(nr))
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            return
        elif scor > 21 and scorbot < scor:
            pierdere.add_field(name=f"Scor bot:", value=f"Botul are un scor adunat de {scorbot}")
            pierdere.add_field(name=f"Scor: {scor}", value=f"Carti: {carti}")
            await ctx.send(embed=pierdere)
            data[f"frunze{ctx.author.id}"] = data[f"frunze{ctx.author.id}"] - nr
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            return
        info = discord.Embed(title=f"Blackjack: {scor}", description=f"Carti: {carti}\nScorul tau:{scor}",
                             color=discord.Color.green())
        info.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
        info.set_author(name="Cazino autorizat 'Marian Casino'",
                        icon_url="https://cdn.discordapp.com/attachments/745384647885848594/866669346675359764/580b585b2edbce24c47b27a6.jpg")
        info.set_thumbnail(
            url="https://img.traveltriangle.com/blog/wp-content/uploads/2018/09/hong-kong-casinos-cover.jpg")
        await ctx.send(embed=info)

        # ebun

        while scor < 21 or scorbot < 21:
            async def da(interaction: discord.Interaction):
                if interaction.user.id != ctx.author.id:
                    await interaction.response.defer()
                    return
                view2 = View()
                buton1 = Button(style=discord.ButtonStyle.success, label="Da", disabled=True)
                buton2 = Button(style=discord.ButtonStyle.danger, label="Nu", disabled=True)
                view2.add_item(buton1)
                view2.add_item(buton2)
                await interaction.response.edit_message(content="Raspuns: da", view=view2)
                await interaction.response.defer()

            async def nu(interaction: discord.Interaction):
                if interaction.user.id != ctx.author.id:
                    await interaction.response.defer()
                    return
                view2 = View()
                buton1 = Button(style=discord.ButtonStyle.success, label="Da", disabled=True)
                buton2 = Button(style=discord.ButtonStyle.danger, label="Nu", disabled=True)
                view2.add_item(buton1)
                view2.add_item(buton2)
                await interaction.response.edit_message(content="Raspuns: nu", view=view2)
                await interaction.response.defer()

            view = View()
            buton1 = Button(style=discord.ButtonStyle.success, label="Da")
            buton2 = Button(style=discord.ButtonStyle.danger, label="Nu")
            buton1.callback = da
            buton2.callback = nu
            view.add_item(buton1)
            view.add_item(buton2)
            embed = discord.Embed(title=f"Doresti sa mai tragi o carte?",
                                  description=f"{ctx.author.mention}, mai tragi o carte?", color=discord.Color.green())
            mesaj1 = await ctx.reply(embed=embed, view=view)
            da = 0
            timeout = 0
            while True:
                if timeout == 40:
                    view2 = View()
                    buton1 = Button(style=discord.ButtonStyle.success, label="Da", disabled=True)
                    buton2 = Button(style=discord.ButtonStyle.danger, label="Nu", disabled=True)
                    view2.add_item(buton1)
                    view2.add_item(buton2)
                    await mesaj1.edit(view=view2)
                    return
                await asyncio.sleep(1)
                msg = await ctx.fetch_message(mesaj1.id)
                print(str(msg.content))
                if "Raspuns: da" in str(msg.content):
                    da = 1
                    break
                elif "Raspuns: nu" in str(msg.content):
                    da = 0
                    break

            if da == 1:
                cartea1 = randint(2, 13)
                scorbot = scorbot + randint(2, 13)
                scor = scor + cartea1
                if cartea1 == 11:
                    cartea1 = "J"
                elif cartea1 == 12:
                    cartea1 = "Q"
                elif cartea1 == 13:
                    cartea1 = "K"
                carti = str(carti) + ", " + str(cartea1)
                if scor == 21 and scorbot != 21:
                    castig.add_field(name=f"Scor bot:", value=f"Botul are un scor adunat de {scorbot}")
                    castig.add_field(name=f"Scor: {scor}", value=f"Carti: {carti}")
                    await ctx.send(embed=castig)
                    data[f"frunze{ctx.author.id}"] = data[f"frunze{ctx.author.id}"] + (sumacastigata - int(nr))
                    with open("pad/data/data.json", "w") as jsonFile:
                        json.dump(data, jsonFile)
                        jsonFile.close()
                    return
                elif scor >= 21 and scor == scorbot:
                    egal.add_field(name=f"Scor bot:", value=f"Botul are un scor adunat de {scorbot}")
                    egal.add_field(name=f"Scor: {scor}", value=f"Carti: {carti}")
                    await ctx.send(embed=egal)
                    return
                elif scorbot == 21 and scor != 21:
                    pierdere.add_field(name=f"Scor bot:", value=f"Botul are un scor adunat de {scorbot}")
                    pierdere.add_field(name=f"Scor: {scor}", value=f"Carti: {carti}")
                    await ctx.send(embed=pierdere)
                    data[f"frunze{ctx.author.id}"] = data[f"frunze{ctx.author.id}"] - nr
                    with open("pad/data/data.json", "w") as jsonFile:
                        json.dump(data, jsonFile)
                        jsonFile.close()
                    return
                elif scorbot > 21 and scorbot > scor:
                    castig.add_field(name=f"Scor bot:", value=f"Botul are un scor adunat de {scorbot}")
                    castig.add_field(name=f"Scor: {scor}", value=f"Carti: {carti}")
                    await ctx.send(embed=castig)
                    data[f"frunze{ctx.author.id}"] = data[f"frunze{ctx.author.id}"] + (sumacastigata - int(nr))
                    with open("pad/data/data.json", "w") as jsonFile:
                        json.dump(data, jsonFile)
                        jsonFile.close()
                    return
                elif scor > 21 and scorbot < scor:
                    pierdere.add_field(name=f"Scor bot:", value=f"Botul are un scor adunat de {scorbot}")
                    pierdere.add_field(name=f"Scor: {scor}", value=f"Carti: {carti}")
                    await ctx.send(embed=pierdere)
                    data[f"frunze{ctx.author.id}"] = data[f"frunze{ctx.author.id}"] - nr
                    with open("pad/data/data.json", "w") as jsonFile:
                        json.dump(data, jsonFile)
                        jsonFile.close()
                    return
                info = discord.Embed(title=f"Blackjack:", description=f"Carti: {carti}\nScorul tau:{scor}",
                                     color=discord.Color.green())
                info.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                info.set_thumbnail(
                    url="https://img.traveltriangle.com/blog/wp-content/uploads/2018/09/hong-kong-casinos-cover.jpg")
                info.set_author(name="Cazino autorizat 'Marian Casino'",
                                icon_url="https://cdn.discordapp.com/attachments/745384647885848594/866669346675359764/580b585b2edbce24c47b27a6.jpg")
                await ctx.send(embed=info)

            elif da == 0:
                if scorbot == 21 and scor != 21:
                    pierdere.add_field(name=f"Scor bot:", value=f"Botul are un scor adunat de {scorbot}")
                    pierdere.add_field(name=f"Scor: {scor}", value=f"Carti: {carti}")
                    await ctx.send(embed=pierdere)
                    data[f"frunze{ctx.author.id}"] = data[f"frunze{ctx.author.id}"] - nr
                    with open("pad/data/data.json", "w") as jsonFile:
                        json.dump(data, jsonFile)
                        jsonFile.close()
                    return
                elif scorbot > 21 and scorbot > scor:
                    castig.add_field(name=f"Scor bot:", value=f"Botul are un scor adunat de {scorbot}")
                    castig.add_field(name=f"Scor: {scor}", value=f"Carti: {carti}")
                    await ctx.send(embed=castig)
                    data[f"frunze{ctx.author.id}"] = data[f"frunze{ctx.author.id}"] + (sumacastigata - int(nr))
                    with open("pad/data/data.json", "w") as jsonFile:
                        json.dump(data, jsonFile)
                        jsonFile.close()
                    return
                elif scorbot > scor:
                    pierdere.add_field(name=f"Scor bot:", value=f"Botul are un scor adunat de {scorbot}")
                    pierdere.add_field(name=f"Scor: {scor}", value=f"Carti: {carti}")
                    await ctx.send(embed=pierdere)
                    data[f"frunze{ctx.author.id}"] = data[f"frunze{ctx.author.id}"] - nr
                    with open("pad/data/data.json", "w") as jsonFile:
                        json.dump(data, jsonFile)
                        jsonFile.close()
                    return
                elif scor > scorbot:
                    castig.add_field(name=f"Scor bot:", value=f"Botul are un scor adunat de {scorbot}")
                    castig.add_field(name=f"Scor: {scor}", value=f"Carti: {carti}")
                    await ctx.send(embed=castig)
                    data[f"frunze{ctx.author.id}"] = data[f"frunze{ctx.author.id}"] + (sumacastigata - int(nr))
                    with open("pad/data/data.json", "w") as jsonFile:
                        json.dump(data, jsonFile)
                        jsonFile.close()
                    return
                elif scor == scorbot:
                    egal.add_field(name=f"Scor bot:", value=f"Botul are un scor adunat de {scorbot}")
                    egal.add_field(name=f"Scor: {scor}", value=f"Carti: {carti}")
                    await ctx.send(embed=egal)
                    return

    @blackjack.error
    async def blackjack_error(self, ctx, error):
        print(error)

        if isinstance(error, commands.CommandOnCooldown):
            timp = error.retry_after
            em = discord.Embed(title=f"Usor domnule.",
                               description=f"Ai de asteptat {timp:.0f} secunde pentru a paria iar",
                               color=discord.Color.green())
            await ctx.reply(embed=em)
        else:
            em = discord.Embed(title=f"Ceva nu a mers bine :(",
                               description=f"Verifica daca ai folosit bine comanda si incearca din nou",
                               color=discord.Color.green())
            await ctx.reply(embed=em)

    @commands.command(aliases=['orar'])
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def hourly(self, ctx):
        em = discord.Embed(title=f"Felicitari! ",
                           description=f"Ai primit 0 frunze. Ruleaza comanda din nou peste o ora pentru a primi alte 0 frunze",
                           color=discord.Color.green())
        await ctx.reply(embed=em)

    @hourly.error
    async def hourly_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            timp = error.retry_after
            em = discord.Embed(title=f"Inca n-a trecut o ora de la ultima recompensa.",
                               description=f"Mai ai de asteptat {(timp * 1000):.0f} milisecunde",
                               color=discord.Color.green())
            await ctx.reply(embed=em)

    @commands.command(aliases=['zilnic'])
    async def daily(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"dailytimeout{ctx.author.id}" in data:
            data1 = datetime.strptime(data[f"dailytimeout{ctx.author.id}"], "%Y-%m-%d %H:%M:%S.%f")
            data2 = datetime.now()
            if int((data2 - data1).days) == 0:
                if int(((data2 - data1).seconds) / 3600) == 23:
                    em = discord.Embed(title=f"Inca n-a trecut o zi de la ultima recompensa!",
                                       description=f"Mai ai de asteptat {int(60 - ((data2 - data1).seconds) / 60)} minute",
                                       color=discord.Color.green())
                    await ctx.reply(embed=em)
                    return
                else:
                    em = discord.Embed(title=f"Inca n-a trecut o zi de la ultima recompensa!",
                                       description=f"Mai ai de asteptat {int(24 - ((data2 - data1).seconds) / 3600)} ore",
                                       color=discord.Color.green())
                    await ctx.reply(embed=em)
                    return
        data[f"dailytimeout{ctx.author.id}"] = str(datetime.now())
        em = discord.Embed(title=f"Felicitari!!!!!!!!",
                           description=f"Ai castigat 200 frunze. Foloseste comanda si maine pentru a castiga alte 200 frunze!",
                           color=discord.Color.green())
        em.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
        em.set_thumbnail(url="https://c.tenor.com/VgCDirag6VcAAAAi/party-popper-joypixels.gif")
        await ctx.reply(embed=em)
        if f"frunze{ctx.author.id}" not in data:
            data[f"frunze{ctx.author.id}"] = 200
        else:
            data[f"frunze{ctx.author.id}"] = data[f"frunze{ctx.author.id}"] + 200
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()

    @commands.command(aliases=['saptamanal'])
    async def weekly(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"weeklytimeout{ctx.author.id}" in data:
            data1 = datetime.strptime(data[f"weeklytimeout{ctx.author.id}"], "%Y-%m-%d %H:%M:%S.%f")
            data2 = datetime.now()
            if (data2 - data1).days < 7:
                if (data2 - data1).days == 7 and int(((data2 - data1).seconds) / 3600) == 23:
                    em = discord.Embed(title=f"Inca n-a trecut o saptamana de la ultima recompensa!",
                                       description=f"Mai ai de asteptat {int(60 - (data2 - data1).seconds / 60)} minute",
                                       color=discord.Color.green())
                    await ctx.reply(embed=em)
                    return
                else:
                    em = discord.Embed(title=f"Inca n-a trecut o saptamana de la ultima recompensa!",
                                       description=f"Mai ai de asteptat {int(168 - (data2 - data1).seconds / 3600)} ore",
                                       color=discord.Color.green())
                    await ctx.reply(embed=em)
                    return
        data[f"weeklytimeout{ctx.author.id}"] = str(datetime.now())
        em = discord.Embed(title=f"Felicitari!!!!!!!!",
                           description=f"Ai castigat 1 frunza. Foloseste comanda si saptamana viitoare pentru a castiga alte frunza!",
                           color=discord.Color.green())
        em.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
        em.set_thumbnail(url="https://c.tenor.com/VgCDirag6VcAAAAi/party-popper-joypixels.gif")
        await ctx.reply(embed=em)
        if f"frunze{ctx.author.id}" not in data:
            data[f"frunze{ctx.author.id}"] = 1
        else:
            data[f"frunze{ctx.author.id}"] = data[f"frunze{ctx.author.id}"] + 1
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()

    @commands.command(aliases=['magazin'])
    async def shop(self, ctx, member: discord.Member = None):
        with open("pad/data/iteme.json", "r") as jsonFile:
            itemdata = json.load(jsonFile)
            jsonFile.close()
        main.obiecte = {}
        i = 1
        itemdata = dict(sorted(itemdata.items(), key=lambda item: item[1]["buy"]))
        for k in itemdata:
            if itemdata[k]["buy"] > 0:
                main.obiecte[str(i)] = itemdata[k]
                i = i + 1
        text = ""

        if len(main.obiecte) <= 5:
            j = 1
            while j < i:
                text = text + "•[" + main.obiecte[str(j)]["emoji"] + "] " + main.obiecte[str(j)][
                    "nume"] + " | Pret: " + str(main.obiecte[str(j)]["buy"]) + " frunze\n\n"
                j = j + 1
            embed = discord.Embed(title="", description=text, color=discord.Color.green())
            embed.set_author(name="Magazinul Padurarului",
                             icon_url="https://cdn.discordapp.com/attachments/920425074882904104/1006147311283490876/1659954604529.png")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/920425074882904104/1006146875063287808/kindpng_212280.png")
            embed.set_footer(
                text=f"•Foloseste comanda `cumpara` alaturi de numele obiectului pentru a-l cumpara\n•Exemplu: `cumpara steag`")
            await ctx.reply(embed=embed)

        else:
            j = 1
            while j <= 5:
                text = text + "•[" + main.obiecte[str(j)]["emoji"] + "] " + main.obiecte[str(j)][
                    "nume"] + " | Pret: " + str(main.obiecte[str(j)]["buy"]) + " frunze\n"
                if "piataneagra" in main.obiecte[str(j)]:
                    if main.obiecte[str(j)]["piataneagra"] == 1:
                        text = text + "[obiect de pe piata neagra]\n\n"
                else:
                    text = text + '\n'

                j = j + 1
            embed = discord.Embed(title="Pagina 1", description=text, color=discord.Color.green())
            embed.set_author(name="Magazinul Padurarului",
                             icon_url="https://cdn.discordapp.com/attachments/920425074882904104/1006147311283490876/1659954604529.png")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/920425074882904104/1006146875063287808/kindpng_212280.png")
            embed.set_footer(
                text=f"•Foloseste comanda `cumpara` alaturi de numele obiectului pentru a-l cumpara\n•Exemplu: `cumpara steag`")
            view = View()
            buton1 = Button(style=discord.ButtonStyle.primary, emoji="⏪", disabled=True, custom_id="shopback")
            buton2 = Button(style=discord.ButtonStyle.primary, emoji="⏩", custom_id="shopnext")
            view.add_item(buton1)
            view.add_item(buton2)
            mesaj = await ctx.reply(embed=embed, view=view)
            timeout = 0
            while True:
                timeout = timeout + 1
                await asyncio.sleep(1)
                if timeout == 40:
                    main.obiecte = {}
                    view = View()
                    buton1 = Button(style=discord.ButtonStyle.primary, emoji="⏪", disabled=True)
                    buton2 = Button(style=discord.ButtonStyle.primary, emoji="⏩", disabled=True)
                    view.add_item(buton1)
                    view.add_item(buton2)
                    await mesaj.edit(embed=embed, view=view)
                    return

    @shop.error
    async def shop_error(self, ctx, error):
        print(error)

    @commands.command(aliases=['informatii'])
    async def info(self, ctx, *, item=""):
        with open("pad/data/iteme.json", "r") as jsonFile:
            itemdata = json.load(jsonFile)
            jsonFile.close()
        if item == "":
            embed = discord.Embed(title="Despre ce item vrei sa aflii informatii?",
                                  description="Foloseste comanda sub forma `info obiect`. Exemplu: `.info steag`",
                                  color=discord.Color.green())
            await ctx.reply(embed=embed)
            return
        ok = 0
        for k in itemdata:
            nume = (itemdata[k]["nume"]).upper()
            if item.upper() in nume or nume in item.upper():
                embed = discord.Embed(title=itemdata[k]["nume"], description=itemdata[k]["descriere"],
                                      color=discord.Color.green())
                embed.set_author(name="Informatii obiect",
                                 icon_url="https://cdn.discordapp.com/attachments/920425074882904104/1006193511160348712/toppng.com-red-question-mark-png-396x597.png")
                embed.set_thumbnail(url=itemdata[k]["poza"])
                if itemdata[k]["buy"] > 0:
                    embed.add_field(name=f"Pret cumparare", value=str(itemdata[k]["buy"]) + " frunze")
                else:
                    embed.add_field(name=f"Pret cumparare", value="Nu exista")
                if itemdata[k]["sell"] >= 0:
                    embed.add_field(name=f"Pret vanzare", value=str(itemdata[k]["sell"]) + " frunze")
                else:
                    embed.add_field(name=f"Pret vanzare", value="Nu exista")
                if "colectabil" in itemdata[k]:
                    embed.add_field(name=f"❗❗Obiect colectibil❗❗", value="Ar fi bine sa nu-l vinzi")
                if "piataneagra" in itemdata[k] and itemdata[k]["piataneagra"] == 1:
                    embed.add_field(name=f"❗❗OBIECT PERICULOS❗❗",
                                    value="Ai grija cand il cumperi/vinzi, se poate face doar pe piata neagra")
                embed.set_footer(text=f"•Suna bine?")
                await ctx.reply(embed=embed)
                return
        if ok == 0:
            embed = discord.Embed(title="Nu am gasit item-ul dorit",
                                  description="Incearca sa folosesti comanda din nou, insa foloseste alta denumire pentru obiect (de preferat denumirea corecta)",
                                  color=discord.Color.green())
            await ctx.reply(embed=embed)

    @info.error
    async def info_error(self, ctx, error):
        print(error)

    @commands.command(aliases=['pescuieste', 'pescuit'])
    @commands.cooldown(1, 50, commands.BucketType.user)
    async def fish(self, ctx, *, item=""):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"inventar{ctx.author.id}" not in data:
            embed = discord.Embed(title="Tinere, nu ai o undita",
                                  description="Ai nevoie de o <:undita:1006201138040811650> undita pentru a merge la pescuit",
                                  color=discord.Color.green())
            await ctx.reply(embed=embed)
            return
        else:
            inv = data[f"inventar{ctx.author.id}"]
        if "item6" not in inv or inv["item6"] == 0:
            embed = discord.Embed(title="Tinere, nu ai o undita",
                                  description="Ai nevoie de o <:undita:1006201138040811650> undita pentru a merge la pescuit",
                                  color=discord.Color.green())
            await ctx.reply(embed=embed)
            return

        async def lac(interaction: discord.Interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.defer()
                return
            view2 = View()
            buton1 = Button(style=discord.ButtonStyle.primary, emoji="⛵", label="In lacul Herastrau", disabled=True)
            buton2 = Button(style=discord.ButtonStyle.primary, emoji="🏞️", label="Pe raul Dambovita", disabled=True)
            buton3 = Button(style=discord.ButtonStyle.primary, emoji="🌇", label="Pe un bloc din apropiere",
                            disabled=True)
            view2.add_item(buton1)
            view2.add_item(buton2)
            view2.add_item(buton3)
            await interaction.response.edit_message(content="Alegere: lac", view=view2)
            await interaction.response.defer()

        async def rau(interaction: discord.Interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.defer()
                return
            view2 = View()
            buton1 = Button(style=discord.ButtonStyle.primary, emoji="⛵", label="In lacul Herastrau", disabled=True)
            buton2 = Button(style=discord.ButtonStyle.primary, emoji="🏞️", label="Pe raul Dambovita", disabled=True)
            buton3 = Button(style=discord.ButtonStyle.primary, emoji="🌇", label="Pe un bloc din apropiere",
                            disabled=True)
            view2.add_item(buton1)
            view2.add_item(buton2)
            view2.add_item(buton3)
            await interaction.response.edit_message(content="Alegere: rau", view=view2)
            await interaction.response.defer()

        async def bloc(interaction: discord.Interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.defer()
                return
            view2 = View()
            buton1 = Button(style=discord.ButtonStyle.primary, emoji="⛵", label="In lacul Herastrau", disabled=True)
            buton2 = Button(style=discord.ButtonStyle.primary, emoji="🏞️", label="Pe raul Dambovita", disabled=True)
            buton3 = Button(style=discord.ButtonStyle.primary, emoji="🌇", label="Pe un bloc din apropiere",
                            disabled=True)
            view2.add_item(buton1)
            view2.add_item(buton2)
            view2.add_item(buton3)
            await interaction.response.edit_message(content="Alegere: bloc", view=view2)
            await interaction.response.defer()

        embed = discord.Embed(title="Hai sa ne gasim un loc de pescuit", description="Ai optiunile urmatoare in zona!",
                              color=discord.Color.green())
        embed.set_footer(text=f"•Alege intelept")
        view = View()
        buton1 = Button(style=discord.ButtonStyle.primary, emoji="⛵", label="In lacul Herastrau")
        buton2 = Button(style=discord.ButtonStyle.primary, emoji="🏞️", label="Pe raul Dambovita")
        buton3 = Button(style=discord.ButtonStyle.primary, emoji="🌇", label="Pe un bloc din apropiere")
        buton1.callback = lac
        buton2.callback = rau
        buton3.callback = bloc
        view.add_item(buton1)
        view.add_item(buton2)
        view.add_item(buton3)
        mesaj1 = await ctx.reply(embed=embed, view=view)
        raspuns = ""
        timeout = 0
        while True:
            if timeout == 30:
                view2 = View()
                buton1 = Button(style=discord.ButtonStyle.primary, emoji="⛵", label="In lacul Herastrau", disabled=True)
                buton2 = Button(style=discord.ButtonStyle.primary, emoji="🏞️", label="Pe raul Dambovita",
                                disabled=True)
                buton3 = Button(style=discord.ButtonStyle.primary, emoji="🌇", label="Pe un bloc din apropiere",
                                disabled=True)
                view2.add_item(buton1)
                view2.add_item(buton2)
                view2.add_item(buton3)
                await mesaj1.edit(view=view2)
                return
            await asyncio.sleep(1)
            msg = await ctx.fetch_message(mesaj1.id)
            print(str(msg.content))
            if "Alegere: lac" in str(msg.content):
                raspuns = "lac"
                break
            elif "Alegere: rau" in str(msg.content):
                raspuns = "rau"
                break
            elif "Alegere: bloc" in str(msg.content):
                raspuns = "bloc"
                break
            timeout = timeout + 1

        if raspuns == "lac":  #
            breakrate = randint(1, 15)
            if breakrate == 2:
                broken = 1
            else:
                broken = 0
            sansapeste = randint(1, 20)
            if sansapeste < 5:
                peste = -1
            elif sansapeste < 12:
                peste = 0
            elif sansapeste < 16:
                peste = 1
            elif sansapeste < 17:
                peste = 3
            else:
                peste = 2
            if peste == -1:
                text = "Uhhhh\n\nSe pare ca n-ai prins nimic astazi.\n\n"
            elif peste == 0:
                text = "ok\n\nSe pare ca ai prins un <:bat:1006203516576083978> bat.\n\n"
                if "item9" not in inv:
                    inv["item9"] = 1
                else:
                    inv["item9"] = inv["item9"] + 1
            elif peste == 1:
                text = "Bunbun\n\Ai prins un <:peste:1006202388006326362> peste! Nice.\n\n"
                if "item7" not in inv:
                    inv["item7"] = 1
                else:
                    inv["item7"] = inv["item7"] + 1
            elif peste == 3:
                text = "Omg cine a lasat asta aici\n\Ai prins un <:colac:1006531577020432455> colac!\n\n"
                if "item13" not in inv:
                    inv["item13"] = 1
                else:
                    inv["item13"] = inv["item13"] + 1
            else:
                text = "WOAH WTF\n\nAi prins un <:dubios:1006202488652824677> peste dubios! Cat de urat e pfaiaia\n\n"
                if "item8" not in inv:
                    inv["item8"] = 1
                else:
                    inv["item8"] = inv["item8"] + 1
            if broken == 1:
                text = text + "❗❗TI S-A RUPT UNDITA❗❗ (ghinion)\n"
                inv["item6"] = inv["item6"] - 1

        elif raspuns == "rau":
            breakrate = randint(1, 15)
            if breakrate == 2:
                broken = 1
            else:
                broken = 0
            sansapeste = randint(1, 20)
            if sansapeste < 5:
                peste = -1
            elif sansapeste < 12:
                peste = 0
            elif sansapeste < 15:
                peste = 1
            elif sansapeste < 18:
                peste = 3
            else:
                peste = 2
            if peste == -1:
                text = "Uhhhh\n\nSe pare ca n-ai prins nimic astazi.\n\n"
            elif peste == 0:
                text = "ok\n\nSe pare ca ai prins un <:bat:1006203516576083978> bat.\n\n"
                if "item9" not in inv:
                    inv["item9"] = 1
                else:
                    inv["item9"] = inv["item9"] + 1
            elif peste == 1:
                text = "Bunbun\n\Ai prins un <:peste:1006202388006326362> peste! Nice.\n\n"
                if "item7" not in inv:
                    inv["item7"] = 1
                else:
                    inv["item7"] = inv["item7"] + 1

            else:
                text = "WOAH WTF\n\nAi prins un <:dubios:1006202488652824677> peste dubios! Cat de urat e pfaiaia\n\n"
                if "item8" not in inv:
                    inv["item8"] = 1
                else:
                    inv["item8"] = inv["item8"] + 1
            if broken == 1:
                text = text + "❗❗TI S-A RUPT UNDITA❗❗ (ghinion)\n"
                inv["item6"] = inv["item6"] - 1
        elif raspuns == "bloc":
            breakrate = randint(1, 6)
            if breakrate == 2:
                broken = 1
            sansapeste = randint(1, 20)
            if sansapeste < 10:
                text = "Uhhhh\n\nSe pare ca n-ai prins nimic astazi.\n\n"
            elif sansapeste < 13:
                text = "S-a cam comis furt\n\nAi prins un <:portofle:1006530951066689547> portofel! (???)\n\n"
                if "item10" not in inv:
                    inv["item10"] = 1
                else:
                    inv["item10"] = inv["item10"] + 1
            elif sansapeste < 14:
                text = "S-a cam comis furt\n\nAi prins un <:telefon:1006531415095136287> telefon! (???)\n\n"
                if "item12" not in inv:
                    inv["item12"] = 1
                else:
                    inv["item12"] = inv["item12"] + 1
            else:
                bete = randint(1, 10)
                if bete == 1:
                    text = "ok\n\nSe pare ca ai prins un <:bat:1006203516576083978> bat.\n\n"
                else:
                    text = f"ok\n\nSe pare ca ai prins {bete} <:bat:1006203516576083978> bete.\n\n"
                if "item9" not in inv:
                    inv["item9"] = bete
                else:
                    inv["item9"] = inv["item9"] + bete
        embed = discord.Embed(title="", description=text, color=discord.Color.green())
        embed.set_author(name="O zi frumoasa de pescuit",
                         icon_url="https://cdn.discordapp.com/attachments/920425074882904104/1006211622483787876/kindpng_1970443.png")
        embed.set_thumbnail(url="https://www.nicepng.com/png/full/846-8464760_-man-fishing-png.png")
        embed.set_footer(text=f"•Poti folosi comanda `inventar` pentru a vedea ce obiecte ai")
        await ctx.send(embed=embed)
        data[f"inventar{ctx.author.id}"] = inv
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()

    @fish.error
    async def fish_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            timp = error.retry_after
            em = discord.Embed(title=f"Usor domnule.",
                               description=f"Ai de asteptat {timp:.0f} secunde pentru a pescui iar",
                               color=discord.Color.green())
            await ctx.reply(embed=em)

    @commands.command(aliases=['crime', 'crim', 'crimă'])
    @commands.cooldown(1, 50, commands.BucketType.user)
    async def crima(self, ctx, *, item=""):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"inventar{ctx.author.id}" not in data:
            inv = {"item1": 0}
        else:
            inv = data[f"inventar{ctx.author.id}"]

        if "item16" not in inv or inv["item16"] == 0:
            pistol = 0
            embed = discord.Embed(title="Se pare ca nu ai un pistol", description="Nu-i problema, folosesti pumnii.",
                                  color=discord.Color.green())
            await ctx.send(embed=embed)
        else:
            pistol = 1
            embed = discord.Embed(title="Detii un pistol", description="Te va ajuta.", color=discord.Color.green())
            await ctx.send(embed=embed)

        async def lac(interaction: discord.Interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.defer()
                return
            view2 = View()
            buton1 = Button(style=discord.ButtonStyle.primary, emoji="🏦", label="Banca", disabled=True)
            buton2 = Button(style=discord.ButtonStyle.primary, emoji="🏫", label="Scoala (??)", disabled=True)
            buton3 = Button(style=discord.ButtonStyle.primary, emoji="🛒", label="Mall", disabled=True)
            view2.add_item(buton1)
            view2.add_item(buton2)
            view2.add_item(buton3)
            await interaction.response.edit_message(content="Alegere: banca", view=view2)
            await interaction.response.defer()

        async def rau(interaction: discord.Interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.defer()
                return
            view2 = View()
            buton1 = Button(style=discord.ButtonStyle.primary, emoji="🏦", label="Banca", disabled=True)
            buton2 = Button(style=discord.ButtonStyle.primary, emoji="🏫", label="Scoala (??)", disabled=True)
            buton3 = Button(style=discord.ButtonStyle.primary, emoji="🛒", label="Mall", disabled=True)
            view2.add_item(buton1)
            view2.add_item(buton2)
            view2.add_item(buton3)
            await interaction.response.edit_message(content="Alegere: scoala", view=view2)
            await interaction.response.defer()

        async def bloc(interaction: discord.Interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.defer()
                return
            view2 = View()
            buton1 = Button(style=discord.ButtonStyle.primary, emoji="🏦", label="Banca", disabled=True)
            buton2 = Button(style=discord.ButtonStyle.primary, emoji="🏫", label="Scoala (??)", disabled=True)
            buton3 = Button(style=discord.ButtonStyle.primary, emoji="🛒", label="Mall", disabled=True)
            view2.add_item(buton1)
            view2.add_item(buton2)
            view2.add_item(buton3)
            await interaction.response.edit_message(content="Alegere: mall", view=view2)
            await interaction.response.defer()

        embed = discord.Embed(title="Hai sa ne gasim un loc de pescuit", description="Ai optiunile urmatoare in zona!",
                              color=discord.Color.green())
        embed.set_footer(text=f"•Alege intelept")
        view = View()
        buton1 = Button(style=discord.ButtonStyle.primary, emoji="🏦", label="Banca", disabled=False)
        buton2 = Button(style=discord.ButtonStyle.primary, emoji="🏫", label="Scoala (??)", disabled=False)
        buton3 = Button(style=discord.ButtonStyle.primary, emoji="🛒", label="Mall", disabled=False)
        buton1.callback = lac
        buton2.callback = rau
        buton3.callback = bloc
        view.add_item(buton1)
        view.add_item(buton2)
        view.add_item(buton3)
        mesaj1 = await ctx.reply(embed=embed, view=view)
        raspuns = ""
        timeout = 0
        while True:
            if timeout == 30:
                view2 = View()
                buton1 = Button(style=discord.ButtonStyle.primary, emoji="🏦", label="Banca", disabled=True)
                buton2 = Button(style=discord.ButtonStyle.primary, emoji="🏫", label="Scoala (??)", disabled=True)
                buton3 = Button(style=discord.ButtonStyle.primary, emoji="🛒", label="Mall", disabled=True)
                view2.add_item(buton1)
                view2.add_item(buton2)
                view2.add_item(buton3)
                await mesaj1.edit(view=view2)
                return
            await asyncio.sleep(1)
            msg = await ctx.fetch_message(mesaj1.id)
            print(str(msg.content))
            if "Alegere: banca" in str(msg.content):
                raspuns = "banca"
                break
            elif "Alegere: scoala" in str(msg.content):
                raspuns = "scoala"
                break
            elif "Alegere: mall" in str(msg.content):
                raspuns = "mall"
                break
            timeout = timeout + 1

        if raspuns == "banca":  #
            politie = randint(1, 2)
            if politie == 1:
                if pistol == 1:  # armat
                    sansascapare = randint(1, 5)
                    if sansascapare <= 2:
                        embed = discord.Embed(title=f"Update crima:",
                                              description="**TE-A PRINS POLITIA**\n\nFurt armat.\n\n Te-a lasat politia sa pleci dupa ce ai platit 1500 frunze si pistolul",
                                              color=discord.Color.red())
                        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2561/2561978.png")
                        embed.set_footer(text=f"Wtf ce justitie e asta")
                        await ctx.reply(embed=embed)
                        inv["item16"] = inv["item16"] - 1
                        data[f"inventar{ctx.author.id}"] = inv
                        if f"frunze{ctx.author.id}" not in data:
                            frunze = 0
                        else:
                            frunze = data[f"frunze{ctx.author.id}"]
                        frunze = int(frunze) - 1500
                        data[f"frunze{ctx.author.id}"] = frunze
                        with open("pad/data/data.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                            jsonFile.close()
                        return
                    else:
                        pol = randint(1, 7)
                        embed = discord.Embed(title=f"Update crima:",
                                              description=f"**A venit politia**\n\nAi impuscat {pol} politisti\n\nA escaladat rapid dar ai scapat",
                                              color=discord.Color.green())
                        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2561/2561978.png")
                        embed.set_footer(text=f"Ai impuscat si camerele de luat vedere, cred ca vei scapa")
                        await ctx.reply(embed=embed)
                else:  # dezarmat
                    sansascapare = randint(1, 5)
                    if sansascapare <= 4:
                        embed = discord.Embed(title=f"Update crima:",
                                              description="**TE-A PRINS POLITIA**\n\nFurt.\n\n Te-a lasat politia sa pleci dupa ce ai platit 300 frunze",
                                              color=discord.Color.red())
                        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2561/2561978.png")
                        embed.set_footer(text=f"Wtf ce justitie e asta")
                        await ctx.reply(embed=embed)
                        if f"frunze{ctx.author.id}" not in data:
                            frunze = 0
                        else:
                            frunze = data[f"frunze{ctx.author.id}"]
                        frunze = int(frunze) - 300
                        data[f"frunze{ctx.author.id}"] = frunze
                        with open("pad/data/data.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                            jsonFile.close()
                        return
                    else:
                        pol = randint(1, 5)
                        embed = discord.Embed(title=f"Update crima:",
                                              description=f"**A venit politia**\n\nAi batut {pol} politisti\n\nAi noroc ca esti bine facut",
                                              color=discord.Color.green())
                        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2561/2561978.png")
                        embed.set_footer(text=f"FUGI")
                        await ctx.reply(embed=embed)
            if pistol == 0:
                frunzefurate = randint(200, 1800)
            else:
                frunzefurate = randint(1000, 3000)
            embed = discord.Embed(title=f"Crima incheiata", description=f"**Ai furat {frunzefurate} frunze din banca**",
                                  color=discord.Color.green())
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/920425074882904104/1014123075039666186/kindpng_1338589.png")
            embed.set_footer(text=f"Riscant dar wow")
            await ctx.reply(embed=embed)
            if f"frunze{ctx.author.id}" not in data:
                frunze = 0
            else:
                frunze = data[f"frunze{ctx.author.id}"]
            frunze = int(frunze) + int(frunzefurate)
            data[f"frunze{ctx.author.id}"] = frunze
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            return




        elif raspuns == "scoala":
            politie = randint(1, 3)
            pol = 0
            if politie == 1:
                if pistol == 1:  # armat
                    sansascapare = randint(1, 5)
                    if sansascapare <= 4:
                        embed = discord.Embed(title=f"Update crima:",
                                              description="**TE-A PRINS POLITIA**\n\n Asalt(??).\n\n Te-a lasat politia sa pleci dupa ce ai platit 900 frunze si pistolul",
                                              color=discord.Color.red())
                        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2561/2561978.png")
                        embed.set_footer(text=f"Ce-i ba asta, America???")
                        await ctx.reply(embed=embed)
                        inv["item16"] = inv["item16"] - 1
                        data[f"inventar{ctx.author.id}"] = inv
                        if f"frunze{ctx.author.id}" not in data:
                            frunze = 0
                        else:
                            frunze = data[f"frunze{ctx.author.id}"]
                        frunze = int(frunze) - 900
                        data[f"frunze{ctx.author.id}"] = frunze
                        with open("pad/data/data.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                            jsonFile.close()
                        return
                    else:
                        pol = randint(1, 7)
                        embed = discord.Embed(title=f"Update crima:",
                                              description=f"**A venit politia**\n\nAi impuscat {pol} politisti\n\nA escaladat rapid dar ai scapat",
                                              color=discord.Color.green())
                        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2561/2561978.png")
                        embed.set_footer(text=f"Ce-i asta ba, America???")
                        await ctx.reply(embed=embed)
                else:  # dezarmat
                    sansascapare = randint(1, 5)
                    if sansascapare <= 4:
                        embed = discord.Embed(title=f"Update crima:",
                                              description="**TE-A PRINS POLITIA**\n\n Asalt(??).\n\n Te-a lasat politia sa pleci dupa ce ai platit 300 frunze",
                                              color=discord.Color.red())
                        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2561/2561978.png")
                        embed.set_footer(text=f"Wtf ce justitie e asta")
                        await ctx.reply(embed=embed)
                        if f"frunze{ctx.author.id}" not in data:
                            frunze = 0
                        else:
                            frunze = data[f"frunze{ctx.author.id}"]
                        frunze = int(frunze) - 300
                        data[f"frunze{ctx.author.id}"] = frunze
                        with open("pad/data/data.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                            jsonFile.close()
                        return
                    else:
                        pol = randint(1, 5)
                        embed = discord.Embed(title=f"Update crima:",
                                              description=f"**A venit politia**\n\nAi batut {pol} politisti\n\nAi noroc ca esti bine facut",
                                              color=discord.Color.green())
                        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2561/2561978.png")
                        embed.set_footer(text=f"FUGI")
                        await ctx.reply(embed=embed)
            if pistol == 0:
                frunzefurate = randint(20, 100)
            else:
                frunzefurate = randint(200, 600)
            if pistol == 0:
                embed = discord.Embed(title=f"Crima incheiata",
                                      description=f"**Ai fost batut de copii dar ai fugit**\n\nAi furat totusi {frunzefurate} frunze",
                                      color=discord.Color.red())
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/920425074882904104/1014123075039666186/kindpng_1338589.png")
                embed.set_footer(text=f"De ce scoala ma psihopatule")
                await ctx.reply(embed=embed)
            else:
                persoane = randint(1, 36)
                if pol > 0:
                    text = f"{pol} politisti si "
                else:
                    text = ""
                embed = discord.Embed(title=f"Crima incheiata",
                                      description=f"**Ai impuscat {text}{persoane} persoane**\n\nAi furat si {frunzefurate} frunze",
                                      color=discord.Color.green())
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/920425074882904104/1014123075039666186/kindpng_1338589.png")
                embed.set_footer(text=f"De ce scoala ma psihopatule")
                await ctx.reply(embed=embed)
            if f"frunze{ctx.author.id}" not in data:
                frunze = 0
            else:
                frunze = data[f"frunze{ctx.author.id}"]
            frunze = int(frunze) + int(frunzefurate)
            data[f"frunze{ctx.author.id}"] = frunze
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            return

        elif raspuns == "mall":
            politie = randint(1, 2)
            if politie == 1:
                if pistol == 1:  # armat
                    sansascapare = randint(1, 5)
                    if sansascapare <= 2:
                        embed = discord.Embed(title=f"Update crima:",
                                              description="**TE-A PRINS POLITIA**\n\nFurt armat.\n\n Te-a lasat politia sa pleci dupa ce ai platit 1500 frunze si pistolul",
                                              color=discord.Color.red())
                        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2561/2561978.png")
                        embed.set_footer(text=f"Wtf ce justitie e asta")
                        await ctx.reply(embed=embed)
                        inv["item16"] = inv["item16"] - 1
                        data[f"inventar{ctx.author.id}"] = inv
                        if f"frunze{ctx.author.id}" not in data:
                            frunze = 0
                        else:
                            frunze = data[f"frunze{ctx.author.id}"]
                        frunze = int(frunze) - 1500
                        data[f"frunze{ctx.author.id}"] = frunze
                        with open("pad/data/data.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                            jsonFile.close()
                        return
                    else:
                        pol = randint(1, 7)
                        embed = discord.Embed(title=f"Update crima:",
                                              description=f"**A venit politia**\n\nAi impuscat {pol} politisti\n\nA escaladat rapid dar ai scapat",
                                              color=discord.Color.green())
                        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2561/2561978.png")
                        embed.set_footer(text=f"Ai impuscat si camerele de luat vedere, cred ca vei scapa")
                        await ctx.reply(embed=embed)
                else:  # dezarmat
                    sansascapare = randint(1, 5)
                    if sansascapare <= 4:
                        embed = discord.Embed(title=f"Update crima:",
                                              description="**TE-A PRINS POLITIA**\n\nFurt.\n\n Te-a lasat politia sa pleci dupa ce ai platit 300 frunze",
                                              color=discord.Color.red())
                        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2561/2561978.png")
                        embed.set_footer(text=f"Wtf ce justitie e asta")
                        await ctx.reply(embed=embed)
                        if f"frunze{ctx.author.id}" not in data:
                            frunze = 0
                        else:
                            frunze = data[f"frunze{ctx.author.id}"]
                        frunze = int(frunze) - 300
                        data[f"frunze{ctx.author.id}"] = frunze
                        with open("pad/data/data.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                            jsonFile.close()
                        return
                    else:
                        pol = randint(1, 5)
                        embed = discord.Embed(title=f"Update crima:",
                                              description=f"**A venit politia**\n\nAi batut {pol} politisti\n\nAi noroc ca esti bine facut",
                                              color=discord.Color.green())
                        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2561/2561978.png")
                        embed.set_footer(text=f"FUGI")
                        await ctx.reply(embed=embed)
            if pistol == 0:
                frunzefurate = randint(200, 1800)
            else:
                frunzefurate = randint(1000, 3000)
            embed = discord.Embed(title=f"Crima incheiata", description=f"**Ai furat {frunzefurate} frunze din mall**",
                                  color=discord.Color.green())
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/920425074882904104/1014123075039666186/kindpng_1338589.png")
            embed.set_footer(text=f"Riscant dar wow")
            await ctx.reply(embed=embed)
            if f"frunze{ctx.author.id}" not in data:
                frunze = 0
            else:
                frunze = data[f"frunze{ctx.author.id}"]
            frunze = int(frunze) + int(frunzefurate)
            data[f"frunze{ctx.author.id}"] = frunze
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            return

    @crima.error
    async def crima_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            timp = error.retry_after
            em = discord.Embed(title=f"Usor domnule.",
                               description=f"Ai de asteptat {timp:.0f} secunde pentru a comite crime iar",
                               color=discord.Color.green())
            await ctx.reply(embed=em)
        else:
            print(error)

    @commands.command(aliases=['cumpara', 'cumpără'])
    async def buy(self, ctx, *, item=""):
        with open("pad/data/iteme.json", "r") as jsonFile:
            itemdata = json.load(jsonFile)
            jsonFile.close()
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if item == "":
            embed = discord.Embed(title="Ce obiect vrei sa cumperi?",
                                  description="Foloseste comanda sub forma `cumpara obiect`. Exemplu: `.cumpara steag`",
                                  color=discord.Color.green())
            await ctx.reply(embed=embed)
            return
        ok = 0
        for k in itemdata:
            nume = (itemdata[k]["nume"]).upper()
            if item.upper() in nume or nume in item.upper():
                if itemdata[k]["buy"] <= 0:
                    embed = discord.Embed(title="Scuze bro",
                                          description=f"Obiectul `{itemdata[k]['nume']}` nu este de vanzare",
                                          color=discord.Color.green())
                    await ctx.reply(embed=embed)
                    return
                if "piataneagra" in itemdata[k] and itemdata[k]["piataneagra"] == 1:
                    view = View()
                    broom = -1

                    async def evident(interaction: discord.Interaction):
                        if interaction.user.id != ctx.author.id:
                            await interaction.response.defer()
                            return
                        view2 = View()
                        buton1 = Button(style=discord.ButtonStyle.primary, label="Evident!", emoji="😊", disabled=True)
                        buton2 = Button(style=discord.ButtonStyle.danger, label="Nu.", emoji="😠", disabled=True)
                        view2.add_item(buton1)
                        view2.add_item(buton2)
                        await interaction.response.edit_message(content="Raspuns: da", view=view2)
                        await interaction.response.defer()

                    async def nuevident(interaction: discord.Interaction):
                        if interaction.user.id != ctx.author.id:
                            await interaction.response.defer()
                            return
                        view2 = View()
                        buton1 = Button(style=discord.ButtonStyle.primary, label="Evident!", emoji="😊", disabled=True)
                        buton2 = Button(style=discord.ButtonStyle.danger, label="Nu.", emoji="😠", disabled=True)
                        view2.add_item(buton1)
                        view2.add_item(buton2)
                        await interaction.response.edit_message(content="Raspuns: nu", view=view2)
                        await interaction.response.defer()

                    buton1 = Button(style=discord.ButtonStyle.primary, label="Evident!", emoji="😊")
                    buton2 = Button(style=discord.ButtonStyle.danger, label="Nu.", emoji="😠")
                    buton1.callback = evident
                    buton2.callback = nuevident
                    view.add_item(buton1)
                    view.add_item(buton2)
                    embed = discord.Embed(title=f"!!!!!ESTI PE CALE SA CUMPERI DE PE PIATA NEAGRA!!!!!",
                                          description="Te supui riscului?", color=discord.Color.green())
                    mesaj1 = await ctx.reply(embed=embed, view=view)
                    timeout = 0
                    while True:
                        if timeout == 20:
                            view2 = View()
                            buton1 = Button(style=discord.ButtonStyle.primary, label="Evident!", emoji="😊",
                                            disabled=True)
                            buton2 = Button(style=discord.ButtonStyle.danger, label="Nu.", emoji="😠", disabled=True)
                            view2.add_item(buton1)
                            view2.add_item(buton2)
                            await mesaj1.edit(view=view2)
                            return
                        await asyncio.sleep(1)
                        msg = await ctx.fetch_message(mesaj1.id)
                        print(str(msg.content))
                        if "Raspuns: da" in str(msg.content):
                            broom = 1
                            break
                        elif "Raspuns: nu" in str(msg.content):
                            return
                        timeout = timeout + 1
                    sansapolitie = randint(1, 5)
                    if sansapolitie == 4:
                        embed = discord.Embed(title=f"TE-A PRINS POLITIA",
                                              description="Ai incercat sa cumperi un obiect de pe piata neagra si ai fost prins de politie. Ai scapat dar ai platit o amenda de 2000 frunze",
                                              color=discord.Color.red())
                        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2561/2561978.png")
                        embed.set_footer(text=f"Data viitoare fii mai vigilent.")
                        await ctx.reply(embed=embed)
                        if f"frunze{ctx.author.id}" not in data:
                            frunze = 0
                        else:
                            frunze = data[f"frunze{ctx.author.id}"]
                        frunze = int(frunze) - 2000
                        data[f"frunze{ctx.author.id}"] = frunze
                        with open("pad/data/data.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                            jsonFile.close()
                        return

                if f"frunze{ctx.author.id}" not in data:
                    frunze = 0
                else:
                    frunze = data[f"frunze{ctx.author.id}"]
                if frunze < itemdata[k]["buy"]:
                    embed = discord.Embed(title="Nu ai destule frunze",
                                          description=f"Obiectul `{itemdata[k]['nume']}` costa `{itemdata[k]['buy']}` frunze",
                                          color=discord.Color.green())
                    await ctx.reply(embed=embed)
                    return
                frunze = frunze - itemdata[k]["buy"]
                data[f"frunze{ctx.author.id}"] = frunze
                if f"inventar{ctx.author.id}" not in data:
                    data[f"inventar{ctx.author.id}"] = {"item1": 0}
                inv = data[f"inventar{ctx.author.id}"]
                if k not in inv:
                    inv[k] = 1
                else:
                    inv[k] = inv[k] + 1
                data[f"inventar{ctx.author.id}"] = inv
                embed = discord.Embed(title="Obiect cumparat cu succes",
                                      description=f"Ai cumparat un {itemdata[k]['emoji']} `{itemdata[k]['nume']}` pentru {itemdata[k]['buy']} frunze.",
                                      color=discord.Color.green())
                embed.set_thumbnail(url=itemdata[k]["poza"])
                embed.set_footer(text=f"•Ai grija unde il bagi")
                await ctx.send(embed=embed)
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                return
        if ok == 0:
            embed = discord.Embed(title="Nu am gasit item-ul dorit",
                                  description="Incearca sa folosesti comanda din nou, insa foloseste alta denumire pentru obiect (de preferat denumirea corecta)",
                                  color=discord.Color.green())
            await ctx.reply(embed=embed)

    @commands.command(aliases=['vinde', 'vanzare'])
    async def sell(self, ctx, *, item=""):
        with open("pad/data/iteme.json", "r") as jsonFile:
            itemdata = json.load(jsonFile)
            jsonFile.close()
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if item == "":
            embed = discord.Embed(title="Ce obiect vrei sa vinzi?",
                                  description="Foloseste comanda sub forma `vinde obiect`. Exemplu: `.vinde steag`",
                                  color=discord.Color.green())
            await ctx.reply(embed=embed)
            return
        ok = 0
        for k in itemdata:
            nume = (itemdata[k]["nume"]).upper()
            if item.upper() in nume or nume in item.upper():
                if itemdata[k]["sell"] < 0:
                    embed = discord.Embed(title="Scuze bro",
                                          description=f"Nu poti vinde obiectul `{itemdata[k]['nume']}`. Poti folosi comanda `info obiect` (exemplu: `.info {itemdata[k]['nume']}`) pentru a afla detalii si preturi pentru obiectul respectiv",
                                          color=discord.Color.green())
                    await ctx.reply(embed=embed)
                    return
                if f"inventar{ctx.author.id}" not in data:
                    data[f"inventar{ctx.author.id}"] = {"item1": 0}
                inv = data[f"inventar{ctx.author.id}"]
                if k not in inv or inv[k] == 0:
                    embed = discord.Embed(title="???Nu detii obiectul",
                                          description=f"Nu poti vinde obiectul `{itemdata[k]['nume']}` pentru ca nu ai asa ceva. Foloseste comanda `inventar` pentru a afla ce obiecte detii",
                                          color=discord.Color.green())
                    await ctx.reply(embed=embed)
                    return
                else:
                    inv[k] = inv[k] - 1
                data[f"inventar{ctx.author.id}"] = inv
                if "piataneagra" in itemdata[k] and itemdata[k]["piataneagra"] == 1:
                    view = View()
                    broom = -1

                    async def evident(interaction: discord.Interaction):
                        if interaction.user.id != ctx.author.id:
                            await interaction.response.defer()
                            return
                        view2 = View()
                        buton1 = Button(style=discord.ButtonStyle.primary, label="Evident!", emoji="😊", disabled=True)
                        buton2 = Button(style=discord.ButtonStyle.danger, label="Nu.", emoji="😠", disabled=True)
                        view2.add_item(buton1)
                        view2.add_item(buton2)
                        await interaction.response.edit_message(content="Raspuns: da", view=view2)
                        await interaction.response.defer()

                    async def nuevident(interaction: discord.Interaction):
                        if interaction.user.id != ctx.author.id:
                            await interaction.response.defer()
                            return
                        view2 = View()
                        buton1 = Button(style=discord.ButtonStyle.primary, label="Evident!", emoji="😊", disabled=True)
                        buton2 = Button(style=discord.ButtonStyle.danger, label="Nu.", emoji="😠", disabled=True)
                        view2.add_item(buton1)
                        view2.add_item(buton2)
                        await interaction.response.edit_message(content="Raspuns: nu", view=view2)
                        await interaction.response.defer()

                    buton1 = Button(style=discord.ButtonStyle.primary, label="Evident!", emoji="😊")
                    buton2 = Button(style=discord.ButtonStyle.danger, label="Nu.", emoji="😠")
                    buton1.callback = evident
                    buton2.callback = nuevident
                    view.add_item(buton1)
                    view.add_item(buton2)
                    embed = discord.Embed(title=f"!!!!!ESTI PE CALE SA VINZI PE PIATA NEAGRA!!!!!",
                                          description="Te supui riscului?", color=discord.Color.green())
                    mesaj1 = await ctx.reply(embed=embed, view=view)
                    timeout = 0
                    while True:
                        if timeout == 20:
                            view2 = View()
                            buton1 = Button(style=discord.ButtonStyle.primary, label="Evident!", emoji="😊",
                                            disabled=True)
                            buton2 = Button(style=discord.ButtonStyle.danger, label="Nu.", emoji="😠", disabled=True)
                            view2.add_item(buton1)
                            view2.add_item(buton2)
                            await mesaj1.edit(view=view2)
                            return
                        await asyncio.sleep(1)
                        msg = await ctx.fetch_message(mesaj1.id)
                        print(str(msg.content))
                        if "Raspuns: da" in str(msg.content):
                            broom = 1
                            break
                        elif "Raspuns: nu" in str(msg.content):
                            return
                        timeout = timeout + 1
                    sansapolitie = randint(1, 5)
                    if sansapolitie == 4:
                        embed = discord.Embed(title=f"TE-A PRINS POLITIA",
                                              description="Ai incercat sa vinzi un obiect pe piata neagra si ai fost prins de politie. Ai ramas fara el si ai platit o amenda de 5000 frunze",
                                              color=discord.Color.red())
                        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2561/2561978.png")
                        embed.set_footer(text=f"Data viitoare fii mai vigilent.")
                        await ctx.reply(embed=embed)
                        if f"frunze{ctx.author.id}" not in data:
                            frunze = 0
                        else:
                            frunze = data[f"frunze{ctx.author.id}"]
                        frunze = int(frunze) - 5000
                        data[f"frunze{ctx.author.id}"] = frunze
                        with open("pad/data/data.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                            jsonFile.close()
                        return

                if f"frunze{ctx.author.id}" not in data:
                    frunze = 0
                else:
                    frunze = data[f"frunze{ctx.author.id}"]
                frunze = frunze + itemdata[k]["sell"]
                data[f"frunze{ctx.author.id}"] = frunze
                embed = discord.Embed(title="Obiect vandut cu succes",
                                      description=f"Ai vandut un {itemdata[k]['emoji']} `{itemdata[k]['nume']}` pentru {itemdata[k]['sell']} frunze.",
                                      color=discord.Color.green())
                embed.set_thumbnail(url=itemdata[k]["poza"])
                embed.set_footer(text=f"•Ai ramas fara el")
                await ctx.send(embed=embed)
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                return
        if ok == 0:
            embed = discord.Embed(title="Nu am gasit item-ul dorit",
                                  description="Incearca sa folosesti comanda din nou, insa foloseste alta denumire pentru obiect (de preferat denumirea corecta)",
                                  color=discord.Color.green())
            await ctx.reply(embed=embed)

    @commands.command()
    async def addfrunze(self, ctx, member: discord.Member = None, nr=0):
        if ctx.author.id == 852673995563597875:
            with open("pad/data/data.json", "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()
            if f"frunze{member.id}" not in data:
                data[f"frunze{member.id}"] = nr
            else:
                data[f"frunze{member.id}"] = data[f"frunze{member.id}"] + nr
            await ctx.reply("okk")
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()

    @commands.command(aliases=['telefon', 'phone', 'smartphone', 'donatii', 'gofundme'])
    @commands.cooldown(1, 80, commands.BucketType.user)
    async def donatie(self, ctx, *, item=""):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"inventar{ctx.author.id}" not in data:
            embed = discord.Embed(title="Tinere, nu ai un telefon",
                                  description="Ai nevoie de un <:telefon:1006531415095136287> telefon pentru a cere donatii",
                                  color=discord.Color.green())
            await ctx.reply(embed=embed)
            return
        else:
            inv = data[f"inventar{ctx.author.id}"]
        if "item12" not in inv or inv["item12"] == 0:
            embed = discord.Embed(title="Tinere, nu ai un telefon",
                                  description="Ai nevoie de un <:telefon:1006531415095136287> telefon pentru a cere donatii",
                                  color=discord.Color.green())
            await ctx.reply(embed=embed)
            return

        async def bani(interaction: discord.Interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.defer()
                return
            view2 = View()
            buton1 = Button(style=discord.ButtonStyle.success, emoji="✋", label="''Am ramas fara bani''", disabled=True)
            buton2 = Button(style=discord.ButtonStyle.primary, emoji="💀", label="''Am cancer''", disabled=True)
            buton3 = Button(style=discord.ButtonStyle.primary, emoji="🚗", label="''N-am bani sa ajung acasa''",
                            disabled=True)
            buton4 = Button(style=discord.ButtonStyle.primary, emoji="🐕", label="''Scop caritabil''", disabled=True)
            view2.add_item(buton1)
            view2.add_item(buton2)
            view2.add_item(buton3)
            view2.add_item(buton4)
            await interaction.response.edit_message(content="Motiv: bani", view=view2)
            await interaction.response.defer()

        async def cancer(interaction: discord.Interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.defer()
                return
            view2 = View()
            buton1 = Button(style=discord.ButtonStyle.primary, emoji="✋", label="''Am ramas fara bani''", disabled=True)
            buton2 = Button(style=discord.ButtonStyle.success, emoji="💀", label="''Am cancer''", disabled=True)
            buton3 = Button(style=discord.ButtonStyle.primary, emoji="🚗", label="''N-am bani sa ajung acasa''",
                            disabled=True)
            buton4 = Button(style=discord.ButtonStyle.primary, emoji="🐕", label="''Scop caritabil''", disabled=True)
            view2.add_item(buton1)
            view2.add_item(buton2)
            view2.add_item(buton3)
            view2.add_item(buton4)
            await interaction.response.edit_message(content="Motiv: cancer", view=view2)
            await interaction.response.defer()

        async def acasa(interaction: discord.Interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.defer()
                return
            view2 = View()
            buton1 = Button(style=discord.ButtonStyle.primary, emoji="✋", label="''Am ramas fara bani''", disabled=True)
            buton2 = Button(style=discord.ButtonStyle.primary, emoji="💀", label="''Am cancer''", disabled=True)
            buton3 = Button(style=discord.ButtonStyle.success, emoji="🚗", label="''N-am bani sa ajung acasa''",
                            disabled=True)
            buton4 = Button(style=discord.ButtonStyle.primary, emoji="🐕", label="''Scop caritabil''", disabled=True)
            view2.add_item(buton1)
            view2.add_item(buton2)
            view2.add_item(buton3)
            view2.add_item(buton4)
            await interaction.response.edit_message(content="Motiv: acasa", view=view2)
            await interaction.response.defer()

        async def caritate(interaction: discord.Interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.defer()
                return
            view2 = View()
            buton1 = Button(style=discord.ButtonStyle.primary, emoji="✋", label="''Am ramas fara bani''", disabled=True)
            buton2 = Button(style=discord.ButtonStyle.primary, emoji="💀", label="''Am cancer''", disabled=True)
            buton3 = Button(style=discord.ButtonStyle.primary, emoji="🚗", label="''N-am bani sa ajung acasa''",
                            disabled=True)
            buton4 = Button(style=discord.ButtonStyle.success, emoji="🐕", label="''Scop caritabil''", disabled=True)
            view2.add_item(buton1)
            view2.add_item(buton2)
            view2.add_item(buton3)
            view2.add_item(buton4)
            await interaction.response.edit_message(content="Motiv: caritate", view=view2)
            await interaction.response.defer()

        embed = discord.Embed(title="Ce motiv ai pentru a cere bani?",
                              description="Alege un motiv inventat din cele de jos:", color=discord.Color.green())
        embed.set_footer(text=f"•Alege intelept")
        view = View()
        buton1 = Button(style=discord.ButtonStyle.primary, emoji="✋", label="''Am ramas fara bani''")
        buton2 = Button(style=discord.ButtonStyle.primary, emoji="💀", label="''Am cancer''")
        buton3 = Button(style=discord.ButtonStyle.primary, emoji="🚗", label="''N-am bani sa ajung acasa''")
        buton4 = Button(style=discord.ButtonStyle.primary, emoji="🐕", label="''Scop caritabil''")
        buton1.callback = bani
        buton2.callback = cancer
        buton3.callback = acasa
        buton4.callback = caritate
        view.add_item(buton1)
        view.add_item(buton2)
        view.add_item(buton3)
        view.add_item(buton4)
        mesaj1 = await ctx.reply(embed=embed, view=view)
        raspuns = ""
        timeout = 0
        while True:
            if timeout == 25:
                view2 = View()
                buton1 = Button(style=discord.ButtonStyle.primary, emoji="✋", label="''Am ramas fara bani''",
                                disabled=True)
                buton2 = Button(style=discord.ButtonStyle.primary, emoji="💀", label="''Am cancer''", disabled=True)
                buton3 = Button(style=discord.ButtonStyle.primary, emoji="🚗", label="''N-am bani sa ajung acasa''",
                                disabled=True)
                buton4 = Button(style=discord.ButtonStyle.primary, emoji="🐕", label="''Scop caritabil''",
                                disabled=True)
                view2.add_item(buton1)
                view2.add_item(buton2)
                view2.add_item(buton3)
                view2.add_item(buton4)
                await mesaj1.edit(view=view2)
                return
            await asyncio.sleep(1)
            msg = await ctx.fetch_message(mesaj1.id)
            print(str(msg.content))
            if "Motiv: bani" in str(msg.content):
                raspuns = "Nu mai am bani, hai ba :("
                break
            elif "Motiv: cancer" in str(msg.content):
                raspuns = "Am facut cancer, am nevoie de tratament"
                break
            elif "Motiv: acasa" in str(msg.content):
                raspuns = "Am nevoie de bani sa ajunga casa"
                break
            elif "Motiv: caritate" in str(msg.content):
                raspuns = "Donez banii stransi la caritate"
                break
            timeout = timeout + 1

        if raspuns == "":
            return  #
        else:
            breakrate = randint(1, 15)
            if breakrate == 2:
                broke = 1
            else:
                broke = 0
            sansasucces = randint(1, 21)
            if sansasucces < 6:
                frunze = randint(0, 200)
                if broke == 1:
                    oameni = randint(2, 5)
                    embed = discord.Embed(title="Ai fost prins cu minciuna.",
                                          description=f"{oameni} oameni ti-au dat debunk la minciuna. Auzi ba, `{raspuns}`, cine te crezi\n\nAi reusit totusi sa stragi exact **{frunze} frunze**, se putea si mai bine.\n\n❗❗Ti s-a stricat telefonul❗❗",
                                          color=discord.Color.green())
                else:
                    oameni = randint(2, 5)
                    embed = discord.Embed(title="Ai fost prins cu minciuna.",
                                          description=f"{oameni} oameni ti-au dat debunk la minciuna. Auzi ba, `{raspuns}`, cine te crezi\n\nAi reusit totusi sa stragi exact **{frunze} frunze**, se putea si mai bine.",
                                          color=discord.Color.green())
            elif sansasucces < 15:
                frunze = randint(200, 1000)
                if broke == 1:
                    embed = discord.Embed(title="Ai strans o suma frumusica.",
                                          description=f"A mers bine minciuna, ai noroc\n\nAi reusit sa stragi exact **{frunze} frunze**, se putea si mai bine.\n\n❗❗Ti s-a stricat telefonul❗❗",
                                          color=discord.Color.green())
                else:
                    embed = discord.Embed(title="Ai strans o suma frumusica.",
                                          description=f"A mers bine minciuna, ai noroc\n\nAi reusit sa stragi exact **{frunze} frunze**, se putea si mai bine.",
                                          color=discord.Color.green())
            elif sansasucces < 19:
                frunze = randint(1000, 4000)
                if broke == 1:
                    oameni = randint(20, 500)
                    embed = discord.Embed(title="Ai cam devenit viral!.",
                                          description=f"{oameni} de oameni ti-au dat share la initiativa `{raspuns}`\n\nAi strans exact **{frunze} frunze**, bravo!\n\n❗❗Ti s-a stricat telefonul❗❗",
                                          color=discord.Color.green())
                else:
                    oameni = randint(2, 5)
                    embed = discord.Embed(title="Ai cam devenit viral!.",
                                          description=f"{oameni} de oameni ti-au dat share la initiativa `{raspuns}`\n\nAi strans exact **{frunze} frunze**, bravo!",
                                          color=discord.Color.green())
            elif sansasucces < 21:
                frunze = randint(5000, 7000)
                if broke == 1:
                    oameni = randint(8000, 14000)
                    embed = discord.Embed(title="WOAH BA AI NOROC!.",
                                          description=f"{oameni} de oameni ti-au dat share la initiativa `{raspuns}`\n\nAi strans **{frunze} frunze**, insane!\n\n❗❗Ti s-a stricat telefonul❗❗",
                                          color=discord.Color.green())
                else:
                    oameni = randint(2, 5)
                    embed = discord.Embed(title="WOAH BA AI NOROC!.",
                                          description=f"{oameni} de oameni ti-au dat share la initiativa `{raspuns}`\n\nAi strans exact **{frunze} frunze**, insane!",
                                          color=discord.Color.green())
            else:
                frunze = randint(14000, 18000)
                if broke == 1:
                    oameni = randint(50000, 100000)
                    embed = discord.Embed(title="WOAH BA AI NOROC!.",
                                          description=f"{oameni} de oameni ti-au dat share la initiativa `{raspuns}`. Iohannis ti-a donat personal o suma mare\n\nAi strans **{frunze} frunze**, insane!\n\n❗❗Ti s-a stricat telefonul❗❗",
                                          color=discord.Color.green())
                else:
                    oameni = randint(2, 5)
                    embed = discord.Embed(title="WOAH BA AI NOROC!.",
                                          description=f"{oameni} de oameni ti-au dat share la initiativa `{raspuns}`. Iohannis ti-a donat personal o suma mare \n\nAi strans exact **{frunze} frunze**, insane!",
                                          color=discord.Color.green())
            embed.set_thumbnail(url="https://logos-world.net/wp-content/uploads/2021/03/GoFundMe-Logo.png")
            embed.set_footer(text="Ar trebui sa iti fie rusine, furi frunze de la oameni.")
            if f"frunze{ctx.author.id}" not in data:
                data[f"frunze{ctx.author.id}"] = frunze
            else:
                data[f"frunze{ctx.author.id}"] = data[f"frunze{ctx.author.id}"] + frunze
            if broke == 1:
                data[f"inventar{ctx.author.id}"]["item12"] = data[f"inventar{ctx.author.id}"]["item12"] - 1
            await ctx.send(embed=embed)
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()

    @donatie.error
    async def donatie_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            timp = error.retry_after
            em = discord.Embed(title=f"Usor domnule.",
                               description=f"Ai de asteptat {timp:.0f} secunde pentru a cere bani iar",
                               color=discord.Color.green())
            await ctx.reply(embed=em)

    @commands.command(aliases=['gather', 'strânge'])
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def strange(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        broom = 0
        if f"inventar{ctx.author.id}" in data:
            inv = data[f"inventar{ctx.author.id}"]
            if "item5" in inv and inv["item5"] > 0:
                view = View()
                broom = -1

                async def evident(interaction: discord.Interaction):
                    if interaction.user.id != ctx.author.id:
                        await interaction.response.defer()
                        return
                    view2 = View()
                    buton1 = Button(style=discord.ButtonStyle.primary, label="Evident!", emoji="😊", disabled=True)
                    buton2 = Button(style=discord.ButtonStyle.danger, label="Nu.", emoji="😠", disabled=True)
                    view2.add_item(buton1)
                    view2.add_item(buton2)
                    await interaction.response.edit_message(content="Raspuns: da", view=view2)
                    await interaction.response.defer()

                async def nuevident(interaction: discord.Interaction):
                    if interaction.user.id != ctx.author.id:
                        await interaction.response.defer()
                        return
                    view2 = View()
                    buton1 = Button(style=discord.ButtonStyle.primary, label="Evident!", emoji="😊", disabled=True)
                    buton2 = Button(style=discord.ButtonStyle.danger, label="Nu.", emoji="😠", disabled=True)
                    view2.add_item(buton1)
                    view2.add_item(buton2)
                    await interaction.response.edit_message(content="Raspuns: nu", view=view2)
                    await interaction.response.defer()

                buton1 = Button(style=discord.ButtonStyle.primary, label="Evident!", emoji="😊")
                buton2 = Button(style=discord.ButtonStyle.danger, label="Nu.", emoji="😠")
                buton1.callback = evident
                buton2.callback = nuevident
                view.add_item(buton1)
                view.add_item(buton2)
                embed = discord.Embed(title=f"Ai o matura in inventar", description="Vrei sa o folosesti?",
                                      color=discord.Color.green())
                mesaj1 = await ctx.reply(embed=embed, view=view)
                timeout = 0
                while True:
                    if timeout == 20:
                        view2 = View()
                        buton1 = Button(style=discord.ButtonStyle.primary, label="Evident!", emoji="😊", disabled=True)
                        buton2 = Button(style=discord.ButtonStyle.danger, label="Nu.", emoji="😠", disabled=True)
                        view2.add_item(buton1)
                        view2.add_item(buton2)
                        await mesaj1.edit(view=view2)
                        return
                    await asyncio.sleep(1)
                    msg = await ctx.fetch_message(mesaj1.id)
                    print(str(msg.content))
                    if "Raspuns: da" in str(msg.content):
                        broom = 1
                        break
                    elif "Raspuns: nu" in str(msg.content):
                        broom = 0
                        break
                    timeout = timeout + 1
        else:
            data[f"inventar{ctx.author.id}"] = {}
            inv = {}
        breakrate = 0
        if broom == 1:
            sansa = randint(1, 4)
            if (sansa == 1):
                frunze = randint(1, 4)
            else:
                frunze = randint(1, 3)
            if frunze <= 2:
                frunze = randint(900, 2000)
            elif frunze == 3:
                frunze = randint(2000, 5000)
            else:
                frunze = randint(5000, 9000)
            breakrate = randint(1, 3)
        else:
            frunze = randint(200, 1000)
        sansabustean = randint(1, 4)
        busteni = 0
        politie = randint(1, 4)
        if politie > 1:
            text = f"Ia sa vedem ce ai strans in Parcul Regina Maria:\n\n<:frunza:1005499341210927255> **Frunze**: {frunze}\n\n"
            if busteni != 0:
                text = text + f"<:busteni:1005444832895959180> **Busteni**: {busteni}"
            if frunze > 2000:
                embed = discord.Embed(title=f"Ai strans din parc (wtf wtf)", description=text,
                                      color=discord.Color.green())
            else:
                embed = discord.Embed(title=f"Ai strans din parc", description=text, color=discord.Color.green())
            embed.set_thumbnail(
                url="https://ak.jogurucdn.com/media/image/p25/place-2014-10-30-12-Greenpark9e7cb95e917f577d6012d82c72f492c0.jpg")
            if breakrate == 2:
                embed.add_field(name=f"❗❗TI-AI RUPT MATURA❗❗",
                                value=f"Daca nu mai ai maturi in inventar, e vai de tine.")
            embed.set_footer(text=f"Bravo.")
            await ctx.reply(embed=embed)

            if f"frunze{ctx.author.id}" not in data:
                datafrunze = 0
            else:
                datafrunze = data[f"frunze{ctx.author.id}"]
            if f"inventar{ctx.author.id}" not in data:
                data[f"inventar{ctx.author.id}"] = {}
            if f"item1" not in data[f"inventar{ctx.author.id}"]:
                databusteni = 0
            else:
                databusteni = data[f"inventar{ctx.author.id}"][f"item1"]
            datafrunze = int(datafrunze + frunze)
            databusteni = int(databusteni + busteni)
            data[f"frunze{ctx.author.id}"] = datafrunze
            data[f"inventar{ctx.author.id}"][f"item1"] = databusteni
        if f"inventar{ctx.author.id}" not in data:
            data[f"inventar{ctx.author.id}"] = {}
        if f"item5" not in data[f"inventar{ctx.author.id}"]:
            maturi = 0
        else:
            maturi = data[f"inventar{ctx.author.id}"]["item5"]
        if breakrate == 2:
            data[f"inventar{ctx.author.id}"][f"item5"] = int(maturi - 1)
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()

    @strange.error
    async def strange_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            timp = error.retry_after
            em = discord.Embed(title=f"Usor domnule.",
                               description=f"Ai de asteptat {timp:.0f} secunde pentru strange frunze iar",
                               color=discord.Color.green())
            await ctx.reply(embed=em)


async def setup(client):
    await client.add_cog(Economy(client)) 
