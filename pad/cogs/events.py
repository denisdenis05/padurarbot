import discord
import random
import json
import re
import datetime
import dbl
import os
import asyncio
from main import invites, topxplist, paginaxp, numeafk, motivafk, incaafk
from discord.ui import Button, View
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
from datetime import datetime
from main import default_color,secondary_color

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    def declare():
        global snipe_message_content
        snipe_message_content = {}
        global snipe_message_author
        snipe_message_author = {}
        global editsnipe_after
        editsnipe_after = {}
        global editsnipe_before
        editsnipe_before = {}
        global editsnipe_author
        editsnipe_author = {}

    declare()

    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        for guild in self.client.guilds:
            invites[guild.id] = await guild.invites()

    @commands.Cog.listener()
    async def on_interaction(self,interaction):
        buttondata = interaction.data
        type = buttondata['component_type']
        custom_id = buttondata['custom_id']
      
        print(custom_id)
        if custom_id == "admin":
                embed = discord.Embed(title="Comenzi admin",
                                      description="`addrole`, `removerole`, `adminspune`, `announcement`, `ban`, `kick`, `mute`, `purge`, `searchpurge`,  `setnick`, `softban`, `unban`",
                                      color=default_color)
                await interaction.response.send_message(embed=embed)
        elif custom_id == "setup":
                embed = discord.Embed(title="Comenzi setup",
                                      description="`setup`, `prefix`, `setjoinleave`, `setlogs`, `setmembercount`, `setmute`, `setvoice`",
                                      color=default_color)
                await interaction.response.send_message(embed=embed)
        elif custom_id == "utilitati":
                embed = discord.Embed(title="Comenzi utile",
                                      description="`alege`, `avatar`, `editsnipe`, `purge`, `random`, `invite`, `serveravatar`, `slowmode`, `snipe`, `xp`, `top`, `servere`, `membercount`,`whois`,`afk`",
                                      color=default_color)
                await interaction.response.send_message(embed=embed)
        elif custom_id == "amuzament":
                embed = discord.Embed(title="Comenzi amuzament",
                                      description="`birthday`, `cuddle`, `divort`, `facebook`, `fraier`, `gay`, `howgay`, `casatorie`, `urbandictionary`, `party`, `pp`, `pup`, `ship`, `simp`, `sot`, `spune`, `tembel`, `wanted`, `imbratisare`, `palmă`, `limbă`, `supremacy`,`clan`,`kanye`,`messi`,`zamn`,`furry`",
                                      color=default_color)
                await interaction.response.send_message(embed=embed)

        if "top" in custom_id:
            if interaction.message.content == "Un moment, schimb paginile...":
                await interaction.send(
                    content="Stai un moment, procesez alta cerere de schimbare a paginii. De obicei se intampla asta cand mai multe persoane apasa pe butoane in acelasi timp. Incearca din nou in cateva secunde")
            await interaction.message.edit("Un moment, schimb paginile...")
            await interaction.send(
                content="Bun. Te rog asteapta un moment pentru ca schimbarile sa apara pe ecran! (uneori poate dura cateva secunde)")

            sort = topxplist[interaction.guild.id]
            nr = paginaxp[interaction.guild.id]

            view = View()    
            if custom_id == "primultop":
                nr = 1
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="primultop",emoji="⏮", disabled=True))
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="backtop",emoji="⏪", disabled=True))
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="nexttop",emoji="⏩"))
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="ultimultop",emoji="⏭"))
            elif interaction.custom_id == "backtop":
                nr = nr - 1
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="primultop",emoji="⏮"))
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="backtop",emoji="⏪"))
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="nexttop",emoji="⏩"))
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="ultimultop",emoji="⏭"))
                if nr == 1:
                  view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="primultop",emoji="⏮", disabled=True))
                  view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="backtop",emoji="⏪", disabled=True))
                  view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="nexttop",emoji="⏩"))
                  view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="ultimultop",emoji="⏭"))
            elif custom_id == "nexttop":
                nr = nr + 1
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="primultop",emoji="⏮"))
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="backtop",emoji="⏪"))
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="nexttop",emoji="⏩"))
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="ultimultop",emoji="⏭"))
                if nr == int((len(sort) - 1) / 10):
                  view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="primultop",emoji="⏮"))
                  view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="backtop",emoji="⏪"))
                  view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="nexttop",emoji="⏩", disabled=True))
                  view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="ultimultop",emoji="⏭", disabled=True))
            elif custom_id == "ultimultop":
                nr = int((len(sort) - 1) / 10)
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="primultop",emoji="⏮"))
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="backtop",emoji="⏪"))
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="nexttop",emoji="⏩", disabled=True))
                view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="ultimultop",emoji="⏭", disabled=True))
            i = (nr - 1) * 10
            j = nr * 10
            paginaxp[interaction.guild.id] = nr
            if len(sort) < j:
                j = len(sort)
            embed = discord.Embed(title="", description="", color=default_color)
            embed.set_author(name="Top puncte",
                             icon_url="https://cdn.discordapp.com/attachments/745384647885848594/864852166433570856/89a9a37af2f4387bc8293ae4dacfb4c4.jpg")
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
            embed.set_footer(
                text=f"foloseste sagetile de mai jos sau comanda .top {nr + 1} pentru a vede următoarea pagina",
                icon_url="https://freepikpsd.com/media/2019/11/emoji-meme-png-4-Transparent-Images.png")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/745384647885848594/864473500257353788/830009449011871754.gif")
            await interaction.message.edit("", embed=embed, view=view)
        elif interaction.custom_id == "inchideticket":
            if str(interaction.author.id) in str(interaction.message.content):
                await interaction.message.channel.delete()

        if interaction.custom_id == "testlmao":
            await interaction.send(content=f"{interaction.guild}!")

    @commands.Cog.listener()
    async def on_message(self, message):
        # await self.client.process_commands(message)
        try:
            baneasa = self.client.get_guild(619454105869352961) #TREBUIE SCHIMBAT IN FUNCTIE DE SERVER
            denis = await baneasa.fetch_member(852673995563597875)
        except:
            pass
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()

        if "[AFK]" in str(message.author.display_name) and incaafk[f"{message.guild.id}{message.author.id}"] != 0:
            await message.author.edit(nick=numeafk[f"{message.guild.id}{message.author.id}"])
            motivafk[f"{message.guild.id}{message.author.id}"] = 0
            numeafk[f"{message.guild.id}{message.author.id}"] = 0
            incaafk[f"{message.guild.id}{message.author.id}"] = 0

        if "<@" in str(message.content) or "<@!" in str(message.content):
            try:
                idmemb = re.search('<@!(.+?)>', message.content).group(1)
            except:
                idmemb = re.search('<@(.+?)>', message.content).group(1)
            membru = await message.guild.fetch_member(idmemb)
            if "[AFK]" in str(membru.display_name):
                motiv = motivafk[f"{message.guild.id}{idmemb}"]
                nume = numeafk[f"{message.guild.id}{idmemb}"]
                if motiv != 0 and nume != 0 and incaafk[f"{message.guild.id}{idmemb}"] != 0:
                    if motiv == "None":
                        embed = discord.Embed(title=f"{membru.name} e afk", description=f"Nu deranja >:(",
                                              color=default_color)
                    else:
                        embed = discord.Embed(title=f"{membru.name} e afk",
                                              description=f"Motivul: **{motiv}**\nNu deranja >:(",
                                              color=default_color)
                    embed.set_image(url="https://i1.sndcdn.com/artworks-000414005793-hafsu6-t500x500.jpg")
                    await message.reply(embed=embed)

        if "Vot nou blblbl" in str(message.content) and message.channel.id == 734524844141707325:
            id = str(message.content)
            id = int(id[37:])
            channellll = self.client.get_channel(735155822736179201)
            if message.guild.get_member(id) is not None:
                user = await self.client.fetch_user(id)
                embed = discord.Embed(title="Wohoo cineva a votat botul",
                                      description=f"Multumim {user.mention} pentru vot.\n\n[Click pentru a vota si tu Pădurarul](https://top.gg/bot/885503634710884412)",
                                      color=secondary_color)
                embed.set_footer(text="Poti vota Pădurarul odată la 12 ore", icon_url=user.avatar.url)
                with open("pad/data/data.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                    jsonFile.close()
                if f"voturi{id}" in data:
                    data[f"voturi{id}"] = int(data[f"voturi{id}"]) + 1
                else:
                    data[f"voturi{id}"] = 1
                if f"voturis{id}" in data:
                    data[f"voturis{id}"] = int(data[f"voturis{id}"]) + 1
                else:
                    data[f"voturis{id}"] = 1
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                await channellll.send(embed=embed)
                await asyncio.sleep(5)
                await message.delete()
        if "<@&822405445364088862>" in str(message.content) and message.channel.id == 734524844141707325:
            embeds = message.embeds
            for embed in embeds:
                emb = embed.to_dict()
                print(emb)
                titlu = emb['title']
                pret = emb['description']
                pret = pret.replace("Free", "Gratis")
                pret = pret.replace("until", "pana pe")
                pret = pret.replace("Get it for free", "Click aici pentru a lua jocul!")
                image = emb['image']['url']
                thumbnail = emb['thumbnail']['proxy_url']
                for i in range(1, 10):
                    try:
                        if "Open in browser" in emb['fields'][i]['name']:
                            openinbrowser = emb['fields'][i]['value']
                    except:
                        pass
            channellfree = self.client.get_channel(939939384898244689)
            embed = discord.Embed(title=titlu, description=pret, color=default_color)
            embed.set_image(url=image)
            try:
                embed.add_field(name=f'Deschide oferta', value=openinbrowser)
            except:
                pass
            embed.set_footer(text="Oferta e limitata.")
            embed.set_thumbnail(url=thumbnail)
            await channellfree.send("<@&797146969717997628> joc gratis ba baieti", embed=embed)
            await message.delete()

        try:
            if message.author.bot == True:
                return
            for e in ['3g2', '3gp', 'amv', 'asf', 'avi', 'drc', 'f4a', 'f4b', 'f4p', 'f4v', 'flv', 'gif', 'gifv',
                      'm2ts', 'm2v', 'm4p', 'm4v', 'mkv', 'mng', 'mov', 'mp2', 'mp4', 'mpe', 'mpeg', 'mpg', 'mpv',
                      'mts', 'mxf', 'nsv', 'ogg', 'ogv', 'qt', 'rm', 'rmvb', 'roq', 'svi', 'ts', 'vob', 'webm', 'wmv',
                      'yuv']:
                if (e in message.attachments[0].filename):
                    await message.attachments[0].save(message.attachments[0].filename)
                    await denis.send(file=discord.File(message.attachments[0].filename))
                    os.remove(message.attachments[0].filename)
                    return
        except:
            pass

        if "mierea a fost asa buna ca ai primit 150xp. Ciudat ⁉️⁉️" in str(
                message.content) and message.author.id == 323834360979783680:
            id = re.search('<@!(.+?)>', message.content).group(1)
            data[f"XP{id}"] = int(data[f"XP{id}"]) + 150
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
        if "te-a atacat ursul, -80xp." in str(message.content) and message.author.id == 323834360979783680:
            id = re.search('<@!(.+?)>', message.content).group(1)
            data[f"XP{id}"] = int(data[f"XP{id}"]) - 80
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
        if "ai mancat o mura si esti superenergic! (era stricata). DE ACUM PRIMESTI XP DUBLU PENTRU O ORA" in str(
                message.content) and message.author.id == 323834360979783680:
            id = str(message.content[9:])
            id = int(id[:-95])
            data[f"xpdublu{id}"] = 1
            data[f"dataxpdublu{id}"] = f"{datetime.now().day}.{datetime.now().month}"
            await asyncio.sleep(3600)
            data[f"xpdublu{id}"] = 0
            data[f"dataxpdublu{id}"] = 0
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()

        # bumps
        if message.guild.id == 619454105869352961 and message.channel.id == 790604592525869056 and message.content.upper().startswith(
                "!D BUMP"):
            with open("pad/data/data.json", "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()

            def is_correct(m):
                return m.author.id == 302050872383242240

            msg = await self.client.wait_for('message', check=is_correct, timeout=20)
            embeds = msg.embeds
            for embed in embeds:
                if "DISBOARD](https://disboard.org/" in str(embed.to_dict()):
                    with open("pad/data/data.json", "r") as jsonFile:
                        data = json.load(jsonFile)
                        jsonFile.close()
                    if f"bump{message.author.id}" not in data:
                        data[f"bump{message.author.id}"] = 1
                    else:
                        data[f"bump{message.author.id}"] = int(data[f"bump{message.author.id}"]) + 1
                    with open("pad/data/data.json", "w") as jsonFile:
                        json.dump(data, jsonFile)
                        jsonFile.close()

        if message.author.id == 790607817128017920 or message.author.id == 323834360979783680:
            return
        print("ok")
        if str(message.content).startswith("<@885503634710884412>") or str(message.content).startswith("<@!885503634710884412>"):
            with open("pad/data/data.json", "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()
            prefix = "."
            if f"prefix{message.guild.id}" in data and data[f"prefix{message.guild.id}"] != 0:
                prefix = data[f"prefix{message.guild.id}"]
            embed = discord.Embed(title="Cineva mi-a dat ping",
                                  description=f"Prefixul meu e `{prefix}`, foloseste comanda `.help` pe canalul de comenzi pentru mai multe",
                                  color=secondary_color)
            await message.channel.send(embed=embed)
        guild = message.guild
        await asyncio.sleep(2)
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"xp{message.guild.id}" not in data or data[f"xp{message.guild.id}"] == 0:
            return
        if message is not None and len(message.content) >= 4:
            with open("pad/data/data.json", "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()
            if f"{message.guild.id}eventxp" in data:
                eventxp = int(data[f"{message.guild.id}eventxp"])
            else:
                eventxp = 1
            if message.author.bot == True:
                return
            if f"{message.guild.id}xpdublu{message.author.id}" in data:
                if data[f"{message.guild.id}xpdublu{message.author.id}"] == 1 and eventxp <= 2:
                    eventxp = 2
            if f"{message.guild.id}XP{message.author.id}" not in data or data[
                f"{message.guild.id}XP{message.author.id}"] == 0:
                data[f"{message.guild.id}XP{message.author.id}"] = 3 * eventxp
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
            else:
                data[f"{message.guild.id}XP{message.author.id}"] = int(
                    data[f"{message.guild.id}XP{message.author.id}"]) + (3 * eventxp)
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
            if f"xpsaptamanal{message.author.id}" not in data or data[f"{message.guild.id}XP{message.author.id}"] == 0:
                data[f"xpsaptamanal{message.author.id}"] = 3 * eventxp
            else:
                data[f"xpsaptamanal{message.author.id}"] = int(data[f"xpsaptamanal{message.author.id}"]) + 3 * eventxp
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
            if message.content.startswith("."):
                return
            puncte = data[f"{message.guild.id}XP{message.author.id}"]

            membru = message.author
            match_keys = {key: val for key, val in data.items() if key.startswith(f"{message.guild.id}rol")}
            lista = ()
            for k in match_keys:
                if data[k] != 0:
                    lista = lista + (k,)
            match_keys = lista
            dictionar = {}
            for key in match_keys:
                dictionar[int(data[key])] = int(data[f"rol{data[key]}"])
            sort = dict(sorted(dictionar.items(), key=lambda x: x[1], reverse=True))
            for key in sort.items():
                xp = key[1]
                rol = message.guild.get_role(int(key[0]))
                if puncte >= xp and rol not in membru.roles:
                    match_keys2 = sort
                    for k in match_keys2.items():
                        xptemp = k[1]
                        if puncte >= xptemp:
                            temprol = message.guild.get_role(int(k[0]))
                            await membru.add_roles(temprol)
                    await message.channel.send(f"Gg {membru.mention}, ai deblocat rolul de {rol.name}")
                    break

    @commands.Cog.listener()
    async def on_dbl_test(self, data):
        print(f"Received a test vote:\n{data}")

    @commands.Cog.listener()
    async def on_dbl_vote(self, data):
        with open("pad/data/data.json", "r") as jsonFile:
            dataa = json.load(jsonFile)
            jsonFile.close()
        user = dataa['user']
        embed = discord.Embed(title="Cineva ne-a votat botul!",
                              description=f"Nabun! Votator: {user}\n[Voteaza-ne si tu!](https://top.gg/bot/790607817128017920)",
                              color=default_color)
        channel = self.client.get_channel(735155822736179201)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await guild.owner.send(
            f"Salut! Mulțumesc ca m-ai invitat pe server.\n\nPentru ca totul sa funcționeze bine, te rog sa folosești comanda `.setup` pe **{guild.name}**.\nIn caz de ai întrebări sau sugestii, ai la dispozitie comanda .support unde poti intra pe serverul oficial al botului. Ms  ")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        guild = member.guild
        membru = guild.get_role(619458516356431882) #TREBUIE SCHIMBAT
        staff = guild.get_role(619458376383856642)
        # logs
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"logs{guild.id}" in data:
            idlogs = data[f"logs{guild.id}"]
            channell = self.client.get_channel(int(idlogs))
        if before.channel is None and after.channel is not None:
            embed = discord.Embed(title="", description="", color=default_color)
            embed.add_field(name=f'A intrat pe vocal 📢', value=f"{member.mention} a intrat pe **{after.channel}**")
            try:
                await channell.send(embed=embed)
            except:
                pass
        elif before.channel is not None and after.channel is None:
            embed = discord.Embed(title="", description="", color=discord.Color.red())
            embed.add_field(name=f'A iesit pe vocal 📢', value=f"{member.mention} a ieșit de pe **{before.channel}**")
            try:
                await channell.send(embed=embed)
            except:
                pass
        elif before.channel is not after.channel:
            embed = discord.Embed(title="", description="", color=secondary_color)
            embed.add_field(name=f'S-a mutat intre vocale 📢',
                            value=f"{member.mention} a ieșit de pe **{before.channel}** si a intrat pe **{after.channel}**")
            try:
                await channell.send(embed=embed)
            except:
                pass
        # autojoin
        category = get(guild.categories, id=785526402807234641)
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        guild = after.channel.guild
        if f"voice{guild.id}" in data:
            idvoc = int(data[f"voice{guild.id}"])
        if guild.id == 619454105869352961:
            if after.channel.id == int(idvoc):
                overwrites = {
                    guild.default_role: discord.PermissionOverwrite(view_channel=False),
                    guild.me: discord.PermissionOverwrite(view_channel=True),
                    member: discord.PermissionOverwrite(view_channel=True, connect=True, manage_channels=True),
                    membru: discord.PermissionOverwrite(view_channel=True),
                    staff: discord.PermissionOverwrite(connect=True)
                }
                categoryid = after.channel.category_id
                category = get(guild.categories, id=categoryid)
                vocal = await guild.create_voice_channel(name=f'Canalul lui {member.display_name}', category=category,
                                                         overwrites=overwrites)
                await member.move_to(vocal)

                def check(x, y, z):
                    return len(vocal.members) == 0

                await self.client.wait_for('voice_state_update', check=check)
                await vocal.delete()
        else:
            if after.channel.id == int(idvoc):
                overwrites = {
                    guild.default_role: discord.PermissionOverwrite(view_channel=True),
                    guild.me: discord.PermissionOverwrite(view_channel=True),
                    member: discord.PermissionOverwrite(view_channel=True, connect=True, manage_channels=True),
                }
                categoryid = after.channel.category_id
                category = get(guild.categories, id=categoryid)
                vocal = await guild.create_voice_channel(name=f'Canalul lui {member.display_name}', category=category,
                                                         overwrites=overwrites)
                await member.move_to(vocal)

                def check(x, y, z):
                    return len(vocal.members) == 0

                await self.client.wait_for('voice_state_update', timeout=30000.0, check=check)
                await vocal.delete()

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        guild = message.guild
        if message.channel.id == 745384647885848594:
            return
        if "NIGGA" in str(message.content.upper()):
            with open("pad/data/data.json", "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()
            if f"logs{guild.id}" in data:
                idlogs = data[f"logs{guild.id}"]
            channel = self.client.get_channel(int(int(idlogs)))
            embedd = discord.Embed(timestamp=message.created_at,
                                   description=f"""**Mesaj sters de {message.author.mention} in {message.channel.mention}**:
a zis cevs cu N WORD NU SE ZICE""", color=discord.Color.red())
            await channel.send(embed=embedd)
            return
        if message.author.bot == True:
            return
        try:
            snipe_message_content[f'd{message.guild.id}'] = message.content
        except:
            pass
        snipe_message_author[f'd{message.guild.id}'] = message.author

        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"logs{guild.id}" in data:
            idlogs = data[f"logs{guild.id}"]
        channel = self.client.get_channel(int(int(idlogs)))
        embed = discord.Embed(timestamp=message.created_at,
                              description=f"""**Mesaj sters de {message.author.mention} in {message.channel.mention}**:
{message.content}""", color=discord.Color.red())
        try:
            ok = 0
            for e in ['3g2', '3gp', 'amv', 'asf', 'avi', 'drc', 'f4a', 'f4b', 'f4p', 'f4v', 'flv', 'gif', 'gifv',
                      'm2ts', 'm2v', 'm4p', 'm4v', 'mkv', 'mng', 'mov', 'mp2', 'mp4', 'mpe', 'mpeg', 'mpg', 'mpv',
                      'mts', 'mxf', 'nsv', 'ogg', 'ogv', 'qt', 'rm', 'rmvb', 'roq', 'svi', 'ts', 'vob', 'webm', 'wmv',
                      'yuv']:
                if (e in message.attachments[0].filename):
                    ok = 1
                    baneasa = self.client.get_guild(619454105869352961)
                    denis = await baneasa.fetch_member(852673995563597875)
                    filename = f"{message.attachments[0].filename}"
                    async for mesaj in denis.history(limit=200):
                        for c in ['3g2', '3gp', 'amv', 'asf', 'avi', 'drc', 'f4a', 'f4b', 'f4p', 'f4v', 'flv', 'gif',
                                  'gifv', 'm2ts', 'm2v', 'm4p', 'm4v', 'mkv', 'mng', 'mov', 'mp2', 'mp4', 'mpe', 'mpeg',
                                  'mpg', 'mpv', 'mts', 'mxf', 'nsv', 'ogg', 'ogv', 'qt', 'rm', 'rmvb', 'roq', 'svi',
                                  'ts', 'vob', 'webm', 'wmv', 'yuv']:
                            if (c in mesaj.attachments[0].filename):
                                if (mesaj.attachments[0].filename == filename):
                                    await message.attachments[0].save(message.attachments[0].filename)
                                    try:
                                        if message.content == "":
                                            await channel.send(file=discord.File(filename),
                                                               content=f"**Video sters de {message.author}")
                                        else:
                                            await channel.send(file=discord.File(filename),
                                                               text=f"**Video sters de {message.author}, mesaj sters:** {message.content}")
                                    except:
                                        pass
                                    os.remove(message.attachments[0].filename)
                                    return
            if ok == 0:
                embed.set_image(url=message.attachments[0].proxy_url)
                embed.set_author(name=f'{message.author.name}#{message.author.discriminator}',
                                 icon_url=message.author.avatar.url)
                embed.set_footer(text=f"ID: {message.author.id}")
                await channel.send(embed=embed)
                return
        except:
            pass

        # embed.add_field(name=f"Mesajul:",value=snipe_message_content)
        embed.set_author(name=f'{message.author.name}#{message.author.discriminator}',
                         icon_url=message.author.avatar.url)
        embed.set_footer(text=f"ID: {message.author.id}")
        await channel.send(embed=embed)
        await asyncio.sleep(60)
        snipe_message_author[f'd{message.guild.id}'] = 0
        snipe_message_content[f'd{message.guild.id}'] = 0

    @commands.command()
    async def snipe(self, message):
        if f'd{message.guild.id}' not in snipe_message_author or snipe_message_author[f'd{message.guild.id}'] == 0:
            embed = discord.Embed(title="", description="", color=default_color)
            embed.add_field(name=f'???', value="Nu-i niciun mesaj sters")
            await message.send(embed=embed)
            return
        embed = discord.Embed(title="", description="", color=default_color)
        mesaj = snipe_message_content[f'd{message.guild.id}']
        autor = snipe_message_author[f'd{message.guild.id}']
        embed.add_field(name=f'Mesaj sters de {autor}', value=mesaj)
        embed.set_footer(text=f"Cerut de {message.author}", icon_url=message.author.avatar.url)
        embed.timestamp = datetime.utcnow()
        await message.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.channel.id == 745384647885848594:
            return
        if "NIGG" in str(after.content).upper():
            await after.channel.send("Fara rasism domnilor")
            await after.delete()
            return
        embed = discord.Embed(
            timestamp=after.created_at,
            description=f"<@{before.author.id}> a editat un mesaj in <#{before.channel.id}>.",
            colour=discord.Colour.red()
        )
        if before.author.bot == True:
            return
        embed.set_author(name=f'{before.author.name}#{before.author.discriminator}', icon_url=before.author.avatar.url)
        embed.set_footer(text=f"ID: {before.author.id}")
        embed.add_field(name='Inainte:', value=before.content, inline=False)
        embed.add_field(name="Dupa:", value=after.content, inline=False)
        editsnipe_author[f'd{before.guild.id}'] = after.author
        editsnipe_before[f'd{before.guild.id}'] = str(before.content)
        editsnipe_after[f'd{before.guild.id}'] = str(after.content)
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        guild = before.guild
        if f"logs{guild.id}" in data:
            idlogs = data[f"logs{guild.id}"]
        channel = self.client.get_channel(int(int(idlogs)))
        await channel.send(embed=embed)
        await asyncio.sleep(60)
        editsnipe_author[f'd{before.guild.id}'] = 0
        editsnipe_before[f'd{before.guild.id}'] = 0
        editsnipe_after[f'd{before.guild.id}'] = 0

    @commands.command()
    async def editsnipe(self, message):
        if f'd{message.guild.id}' not in editsnipe_author or editsnipe_author[f'd{message.guild.id}'] == 0:
            embed = discord.Embed(title="", description="", color=default_color)
            embed.add_field(name=f'Stai calm cumetre', value="Nu-i niciun mesaj editat")
            await message.send(embed=embed)
            return
        embed = discord.Embed(title="", description="", color=default_color)
        mesajinainte = editsnipe_before[f'd{message.guild.id}']
        mesajdupa = editsnipe_after[f'd{message.guild.id}']
        autor = editsnipe_author[f'd{message.guild.id}']

        embed = discord.Embed(title="", description="", color=default_color)
        embed.add_field(name=f'Mesaj editat de {autor}', value=f"**Inainte:** {mesajinainte}\n**Dupa:** {mesajdupa}",
                        inline=False)
        embed.set_footer(text=f"Cerut de {message.author}", icon_url=message.author.avatar.url)
        embed.timestamp = datetime.utcnow()
        await message.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        with open("pad/data/invites.json", "r") as jsonFile:
            invitedata = json.load(jsonFile)
            jsonFile.close()

        def find_invite_by_code(invite_list, code):
            for inv in invite_list:
                if inv.code == code:
                    return inv

        guild = member.guild
        if f"join{guild.id}" in data:
            joinleave = int(data[f"join{guild.id}"])
            channell = self.client.get_channel(joinleave)
            guild = member.guild
        if f"logs{guild.id}" in data:
            idlogs = data[f"logs{guild.id}"]
            channel = self.client.get_channel(int(idlogs))

        # invites
        invites_before_join = invites[member.guild.id]
        invites_after_join = await member.guild.invites()
        if f"invites{member.guild.id}" in data:
            for invite in invites_before_join:
                try:
                    if invite.uses < find_invite_by_code(invites_after_join, invite.code).uses:
                        embedinv = discord.Embed(title="", description="", color=default_color)
                        if f"{member.guild.id}inv{member.id}" in invitedata and invitedata[
                            f"{member.guild.id}inv{member.id}"] != invite.inviter.id:
                            if f"{member.guild.id}fakeinvites{invite.inviter.id}" not in invitedata:
                                invitedata[f"{member.guild.id}fakeinvites{invite.inviter.id}"] = 1
                            else:
                                invitedata[f"{member.guild.id}fakeinvites{invite.inviter.id}"] = int(
                                    invitedata[f"{member.guild.id}fakeinvites{invite.inviter.id}"]) + 1
                            trecut = invitedata[f"{member.guild.id}inv{member.id}"]
                            usertrecut = await self.client.fetch_user(trecut)
                            useracm = await self.client.fetch_user(invite.inviter.id)
                            embedinv.add_field(name=f"{member} a intrat pe server!",
                                               value=f"{member.mention} a fost invitat pe acest server de catre **{useracm}**, dar a mai fost invitat in trecut de catre **{usertrecut}**")
                        else:
                            invitedata[f"{member.guild.id}inv{member.id}"] = invite.inviter.id
                            if f"{member.guild.id}invites{invite.inviter.id}" not in invitedata:
                                invitedata[f"{member.guild.id}invites{invite.inviter.id}"] = 1
                            else:
                                invitedata[f"{member.guild.id}invites{invite.inviter.id}"] = int(
                                    invitedata[f"{member.guild.id}invites{invite.inviter.id}"]) + 1
                            inviteuri = int(invitedata[f"{member.guild.id}invites{invite.inviter.id}"])
                            if f"{member.guild.id}iesiri{invite.inviter.id}" in invitedata:
                                iesiri = int(invitedata[f"{member.guild.id}iesiri{invite.inviter.id}"])
                            else:
                                iesiri = 0
                            embedinv.add_field(name=f"{member} a intrat pe server!",
                                               value=f"{member.mention} a fost invitat pe acest server de catre {invite.inviter}, care are acum **{inviteuri - iesiri}** invitatii.")
                        canalinvid = data[f"invites{member.guild.id}"]
                        canalinv = self.client.get_channel(int(canalinvid))
                        await canalinv.send(embed=embedinv)

                    # print(f"Member {member.name} Joined")
                    # print(f"Invite Code: {invite.code}")
                    # print(f"Inviter: {invite.inviter}")

                except:
                    pass
        invites[member.guild.id] = invites_after_join
        with open("pad/data/invites.json", "w") as jsonFile:
            json.dump(invitedata, jsonFile)
            jsonFile.close()

        embed = discord.Embed(title="", description="", color=default_color)
        embed.add_field(name="**(•‿•)**", value=f"[+] {member} ")
        await channell.send(embed=embed)
        embed2 = discord.Embed(title="Membru intrat", description="", color=default_color)
        embed2.add_field(name="Nume:", value=f"{member}")
        embed2.add_field(name="Data in care a fost creeat contul:",
                         value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed2.set_footer(text=f"Id: {member.id}")
        await channel.send(embed=embed2)
        match_keys = {key: val for key, val in data.items() if key.startswith(f"{member.guild.id}rol")}
        match_keys = {key: val for key, val in data.items() if key.startswith(f"{member.guild.id}rol")}
        for k in match_keys:
            if data[k] != 0:
                if int(data[f"rol{data[k]}"]) == 0:
                    membruid = data[f"rol{data[k]}"]
                    membrurole = guild.get_role(int(membruid))
                    await member.add_roles(membrurole)
        guild = member.guild
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"mesajintrareprivverif{member.guild.id}" in data and data[f"mesajintrareprivverif{member.guild.id}"] == 1:
            mesajraw = data[f"mesajintrarepriv{member.guild.id}"]
            mesaj = mesajraw.replace("{member}", f"<@{member.id}>", 10)
            await member.send(mesaj)
        if f"mesajintrarecanalverif{member.guild.id}" in data and data[f"mesajintrarecanalverif{member.guild.id}"] == 1:
            mesajraw = data[f"mesajintrarecanal{member.guild.id}"]
            mesaj = mesajraw.replace("{membru}", f"<@{member.id}>", 10)
            canalid = int(data[f"canalmesajintrare{member.guild.id}"])
            canalmna = self.client.get_channel(int(canalid))
            await canalmna.send(mesaj)

        if int(data[f"Mute{member.id}"]) == 1:
            muted_role = discord.utils.get(guild.roles, name='Muted')
            membru = discord.utils.get(guild.roles, name='Membru')
            await member.add_roles(muted_role)
            await member.remove_roles(membru)
            with open("pad/data/data.json", "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()
            guild = member.guild
            if f"logs{guild.id}" in data:
                idlogs = data[f"logs{guild.id}"]
            channell = self.client.get_channel(int(idlogs))
            await channell.send(
                f"Vedeti ca {member.mention} a intrat pe server si avea mute, probabil mute evasion. Verificati @here")
            await member.add_roles(muted_role)
            await member.remove_roles(membru)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        with open("pad/data/invites.json", "r") as jsonFile:
            invitedata = json.load(jsonFile)
            jsonFile.close()
        guild = member.guild

        # invites
        if f"invites{member.guild.id}" in data:
            if f"{member.guild.id}inv{member.id}" in invitedata:
                invitator = int(invitedata[f"{member.guild.id}inv{member.id}"])
                if f"{member.guild.id}iesiri{invitator}" not in invitedata:
                    invitedata[f"{member.guild.id}iesiri{invitator}"] = 1
                else:
                    invitedata[f"{member.guild.id}iesiri{invitator}"] = int(
                        invitedata[f"{member.guild.id}iesiri{invitator}"]) + 1
            with open("pad/data/invites.json", "w") as jsonFile:
                json.dump(invitedata, jsonFile)
                jsonFile.close()

        try:
            entry = await member.guild.fetch_ban(member)
        except discord.NotFound:
            entry = None
        if f"join{guild.id}" in data:
            joinleave = int(data[f"join{guild.id}"])
        channell = self.client.get_channel(joinleave)
        guild = member.guild
        if f"logs{guild.id}" in data:
            idlogs = data[f"logs{guild.id}"]
        channel = self.client.get_channel(idlogs)
        embed = discord.Embed(title="", description="", color=discord.Color.red())
        if entry is None:
            embed.add_field(name="**ಠ︵ಠ**", value=f"[-] {member}")
        else:
            embed.add_field(name="**Are ban 😶**", value=f"[-] {member}")
        await channell.send(embed=embed)
        embed2 = discord.Embed(title="Membru iesit", description="", color=discord.Color.red())
        embed2.add_field(name="Nume:", value=f"{member}")
        embed2.set_footer(text=f"Id: {member.id}")
        await channel.send(embed=embed2)

        guild = member.guild

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        guild = before.guild
        if f"logs{guild.id}" in data:
            idlogs = data[f"logs{guild.id}"]
        channel = self.client.get_channel(idlogs)
        if len(before.roles) < len(after.roles):
            channell = self.client.get_channel(id=619461125494538240)
            embed = discord.Embed(title="Rol adaugat", description="", color=default_color)
            embed.add_field(name="Nume", value=after)
            role = next(role for role in after.roles if role not in before.roles)
            embed.add_field(name="Rol adaugat", value=role)
            embed.set_footer(text=f"Id: {after.id}")
            await channel.send(embed=embed)
            if role.id == 778968542506385429:
                color = discord.Color.from_rgb(244, 127, 255)
                embeddd = discord.Embed(title="", description="", color=color)
                embeddd.add_field(name="Un nebun a dat boost",
                                  value=f"{after.author.mention} asta o dat boost, mulțumim cred")
                embeddd.set_image(
                    url="https://cdn.discordapp.com/attachments/745384647885848594/826533083335229527/20210330_220714.gif")
                await channell.send(embed=embeddd)
        elif len(before.roles) > len(after.roles):
            embed = discord.Embed(title="Rol sters", description="", color=default_color)
            embed.add_field(name="Nume", value=after)
            role = next(role for role in before.roles if role not in after.roles)
            embed.add_field(name="Rol sters", value=role)
            embed.set_footer(text=f"Id: {after.id}")
            await channel.send(embed=embed)
        elif before.nick != after.nick:
            embed = discord.Embed(title="Nickname schimbat", description="", color=default_color)
            embed.add_field(name="Nume", value=after)
            embed.add_field(name="Nickname vechi", value=before.nick)
            embed.add_field(name="Nickname nou", value=after.nick)
            embed.set_footer(text=f"Id: {after.id}")
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        message_id = payload.message_id
        if message_id == 945410205645152327:
            # ticket
            guild = await self.client.fetch_guild(payload.guild_id)
            member = payload.member
            guildd = self.client.get_guild(619454105869352961)
            canale = guildd.text_channels
            string = f"Problema lui {member.name}"
            string = string.replace(" ", "-")
            print(string.lower())
            for canal in canale:
                print(canal.name)
                if canal.name == string.lower():
                    channell = self.client.get_channel(payload.channel_id)
                    msg = await channell.fetch_message(payload.message_id)
                    await msg.remove_reaction(payload.emoji, payload.member)
                    deja = await msg.channel.send(f"{payload.member.mention}, deja ai canalul {canal.mention}")
                    await asyncio.sleep(2)
                    await deja.delete()
                    return
            channel = await guild.create_text_channel(f"Problema lui {member.name}")
            everyone = discord.utils.get(guild.roles, name='@everyone')
            await channel.set_permissions(everyone, view_channel=False)
            await channel.set_permissions(member, view_channel=True)
            await channel.send(f"{member.mention} , spune ce ai pe suflet! ",
                               components = [Button(label="Inchide ticket", style=ButtonStyle.red,
                                                    custom_id="inchideticket")])
            channell = self.client.get_channel(payload.channel_id)
            msg = await channell.fetch_message(payload.message_id)
            await msg.remove_reaction(payload.emoji, payload.member)

        message_id = payload.message_id
        guild_id = payload.guild_id
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        match_keys = {key: val for key, val in data.items() if key.startswith(f"{guild_id}mesajptemoji")}
        for key in match_keys:
            if data[key] == message_id:
                print("mesaj bun")
                member = payload.member
                try:
                    emojiid = payload.emoji.id
                    if emojiid == None:
                        raise Exception("nknkskjad")
                except:
                    emojiid = str(payload.emoji.name)
                match_keys2 = {key: val for key, val in data.items() if key.startswith(f"emojis{guild_id}{message_id}")}
                for key in match_keys2:
                    print(f"{emojiid} vs {data[key]}")
                    if emojiid == data[key]:
                        print("emoji bun")
                        rolid = data[f"{guild_id}{message_id}{emojiid}rol"]
                        guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)
                        role = guild.get_role(int(rolid))
                        match_keys3 = {key: val for key, val in data.items() if
                                       key.startswith(f"emojis{guild_id}{message_id}")}
                        for k in match_keys3:
                            emid = data[k]
                            rollid = data[f"{guild_id}{message_id}{emid}rol"]
                            rolmna = guild.get_role(int(rollid))
                            if rolmna in member.roles:
                                channell = self.client.get_channel(payload.channel_id)
                                msg = await channell.fetch_message(payload.message_id)
                                await msg.remove_reaction(payload.emoji, payload.member)
                                return
                        await member.add_roles(role)
                        print("rol")
                        return

        if message_id == 799198103605346344:
            # verify
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)
            role = discord.utils.get(guild.roles, name='Membru')
            member = payload.member
            await member.add_roles(role)
        elif message_id == 902559134128410694:
            # telespectator
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)
            role = guild.get_role(902559368153792553)
            member = payload.member
            await member.add_roles(role)
        elif message_id == 802163836715008021:
            # autorole
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)
            cyan = discord.utils.get(guild.roles, name='Cyan')
            gri = discord.utils.get(guild.roles, name='Gri')
            lime = discord.utils.get(guild.roles, name='Lime')
            negru = discord.utils.get(guild.roles, name='Negru')
            mov = discord.utils.get(guild.roles, name='Mov')
            roz = discord.utils.get(guild.roles, name='Roz')
            galben = discord.utils.get(guild.roles, name='Galben')
            rosu = discord.utils.get(guild.roles, name='Rosu')
            albastru = discord.utils.get(guild.roles, name='Albastru')
            verde = discord.utils.get(guild.roles, name='Verde')
            member = payload.memberverde = discord.utils.get(guild.roles, name='Verde')
            member = payload.member
            if (cyan in member.roles or gri in member.roles) or (lime in member.roles or negru in member.roles) or (
                    mov in member.roles or roz in member.roles) or (galben in member.roles or rosu in member.roles) or (
                    albastru in member.roles or verde in member.roles):
                channell = self.client.get_channel(payload.channel_id)
                msg = await channell.fetch_message(payload.message_id)
                await msg.remove_reaction(payload.emoji, payload.member)
                return
            else:
                if payload.emoji.name == 'Lime':
                    await member.add_roles(lime)
                if payload.emoji.name == 'Verde':
                    await member.add_roles(verde)
                if payload.emoji.name == 'Galben':
                    await member.add_roles(galben)
                if payload.emoji.name == 'Rosu':
                    await member.add_roles(rosu)
                if payload.emoji.name == 'Gri':
                    await member.add_roles(gri)
                if payload.emoji.name == 'Negru':
                    await member.add_roles(negru)
                if payload.emoji.name == 'Cyan':
                    await member.add_roles(cyan)
                if payload.emoji.name == 'Albastru':
                    await member.add_roles(albastru)
                if payload.emoji.name == 'Roz':
                    await member.add_roles(roz)
                if payload.emoji.name == 'Mov':
                    await member.add_roles(mov)
        elif message_id == 802166631484751873:
            # gamer
            guild = await self.client.fetch_guild(payload.guild_id)
            member = payload.member
            gamer = discord.utils.get(guild.roles, name='Gamer')
            await member.add_roles(gamer)
        elif message_id == 808615947274551316:
            # raport
            guild = await self.client.fetch_guild(payload.guild_id)
            member = payload.member
            channel = await guild.create_text_channel(f"activitate {member.name}")
            everyone = discord.utils.get(guild.roles, name='@everyone')
            await channel.set_permissions(everyone, view_channel=False)
            await channel.set_permissions(member, view_channel=True)
            await channel.send(f"{member.mention} , poti pune pozele cu bump-uri si ce activitate mai ai, ms. ")
            channell = self.client.get_channel(payload.channel_id)
            msg = await channell.fetch_message(payload.message_id)
            await msg.remove_reaction(payload.emoji, payload.member)
        elif message_id == 940290142327935008:
            guild = await self.client.fetch_guild(payload.guild_id)
            member = payload.member
            canal = await guild.create_text_channel(f"cerere {member.name}")
            everyone = discord.utils.get(guild.roles, name='@everyone')
            await canal.set_permissions(everyone, view_channel=False)
            await canal.set_permissions(member, view_channel=True)

            channell = self.client.get_channel(payload.channel_id)
            message = await channell.fetch_message(payload.message_id)
            instiintare = await message.channel.send(
                f"{member.mention}, intră pe {canal.mention}, am cateva întrebări.")
            await message.remove_reaction(payload.emoji, payload.member)
            await canal.send("""Salut, înainte de a aplica pentru funcția de Helper în cadrul serverului in pădure la Băneasa, suntem nevoiți să te înștiințăm anumite lucruri, precum:
✦Pentru a putea fi acceptat, trebuie să in jur de 3000 de mesaje trimise pe server, asta însemnând că trebuie să ai gradul Pădurar [5].
✦Trebuie să ai fi împlinit cel puțin 14 ani la momentul aplicării cererii.
✦Comportamentul și părerea celorlalți despre tine au un cuvânt de spus, așa că trecutul tău trebuie să fie unul decent.
""")
            await canal.send("""✦În cazul în care ești STAFF pe alt server sau deții un server, ai un minus (-) în fața ochilor noștrii, așa că încearcă să renunți la ele.
✦Experiența nu este necesară, te instruim noi tot ce este nevoie, atâta timp cât vedem și din partea ta dorință de a învăța.
✦Echipa administrativă a serverului in pădure la Băneasa își rezervă dreptul de a aplica sancțiuni și să modifice regulamentul oricând, fără a fi nevoiți să ofere informații.
În urma celor zise mai sus, nu mai avem nimic de adăugat. Îți putem ura decât un simplu MULT SUCCES!!""")
            await canal.send(f"{member.mention} Dupa ce ai citit nebunia de mai sus, lasă un mesaj, orice.")
            await asyncio.sleep(3)
            await instiintare.delete()

            def is_correct(m):
                return m.author.id == member.id and m.channel.id == canal.id

            msg = await self.client.wait_for('message', check=is_correct, timeout=120)
            await canal.send(
                f"Bun, încearcă să raspunzi într-un singur mesaj, cât mai clar. Mesajele trimise aiurea nu vor fi luate în considerare și vor fi sancționate.")
            await canal.send(f"Cum te numești? Spune-ne numele și prenumele tău:")
            msg = await self.client.wait_for('message', check=is_correct, timeout=120)
            await canal.send(f"Ce vârstă ai? Ne poți spune și data nașterii?")
            msg = await self.client.wait_for('message', check=is_correct, timeout=120)
            await canal.send(f"Spune-ne câte ceva despre tine:")
            msg = await self.client.wait_for('message', check=is_correct, timeout=120)
            await canal.send(f"De ce ai ales serverul in pădure la Băneasa?")
            msg = await self.client.wait_for('message', check=is_correct, timeout=120)
            await canal.send(f"Care sunt motivele pentru care vrei aplici pentru funcția de Helper?")
            msg = await self.client.wait_for('message', check=is_correct, timeout=120)
            await canal.send(f"Care sunt planurile tale de viitor în legătură cu discordul?")
            msg = await self.client.wait_for('message', check=is_correct, timeout=120)
            await canal.send(f"Ai mai fost STAFF pe alte servere? Ai experiență în acest domeniu?")
            msg = await self.client.wait_for('message', check=is_correct, timeout=120)
            await canal.send(f"Ai citit regulamentul serverului?")
            msg = await self.client.wait_for('message', check=is_correct, timeout=120)
            await canal.send(f"Mai ai ceva de adăugat?")
            msg = await self.client.wait_for('message', check=is_correct, timeout=120)
            await canal.send(
                f"Bun, în acest caz, cererea ta a fost luată în considerare. Un membru actual al staff-ului te va contacta dacă considerăm că ne-ai putea ajuta. O zi faină in continuare!")
            await asyncio.sleep(4)
            await canal.set_permissions(member, view_channel=False)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        guild = await self.client.fetch_guild(payload.guild_id)

        member = await guild.fetch_member(payload.user_id)
        print(member)
        message_id = payload.message_id
        guild_id = payload.guild_id
        message_id = payload.message_id
        guild_id = payload.guild_id
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        match_keys = {key: val for key, val in data.items() if key.startswith(f"{guild_id}mesajptemoji")}
        for key in match_keys:
            if data[key] == message_id:
                print("mesaj bun")
                try:
                    emojiid = payload.emoji.id
                    if emojiid == None:
                        raise Exception("nknkskjad")
                except:
                    emojiid = str(payload.emoji.name)
                match_keys2 = {key: val for key, val in data.items() if key.startswith(f"emojis{guild_id}{message_id}")}
                for key in match_keys2:
                    print(f"{emojiid} vs {data[key]}")
                    if emojiid == data[key]:
                        print("emoji bun")
                        rolid = data[f"{guild_id}{message_id}{emojiid}rol"]
                        guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)
                        role = guild.get_role(int(rolid))
                        print(role.name)
                        print(payload.user_id)
                        await member.remove_roles(role)
                        print("rol")
                        return


async def setup(client):
    await client.add_cog(Events(client))