import discord
import random
import json
import re
from discord.ext import commands
from main import default_color

class Setup(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['setprefix'])
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def prefix(self, ctx, *, prefixes=None):
        if prefixes is not None:
            with open("pad/data/data.json", "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()
            data[f"prefix{ctx.guild.id}"] = prefixes
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            embed = discord.Embed(title=f"Ok! Prefixul pe acest server e {prefixes}",
                                  description=f"Pentru a reseta prefixul utilizeaza comanda {prefixes}resetprefix",
                                  color=discord.Color.from_rgb(105, 105, 105))
            await ctx.reply(embed=embed)
        else:
            with open("pad/data/data.json", "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()
            if f"prefix{ctx.guild.id}" in data and data[f"prefix{ctx.guild.id}"] != 0:
                aprefix = data[f"prefix{ctx.guild.id}"]
            else:
                aprefix = "."
            embed = discord.Embed(title=f"Neața! Prefixul actual e `{aprefix}`", description=f"Vrei sa îl schimbi?",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.reply(embed=embed)
            # da = self.client.get_emoji('✅')
            # nu = self.client.get_emoji('⛔')
            nu = '⛔'
            da = '✅'
            await mesaj.add_reaction(da)
            await mesaj.add_reaction(nu)

            def check1(reaction, user):
                return reaction.message.id == mesaj.id and user.id == ctx.author.id and (
                        str(reaction.emoji) == nu or str(reaction.emoji) == da)

            def check2(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
                if str(reaction.emoji) == nu:
                    raise Exception("nu")
                await mesaj.delete()
                embed = discord.Embed(title=f"Ce prefix vrei sa am?",
                                      description=f"Trimite un mesaj doar cu prefixul. Exemplu: `!`",
                                      color=discord.Color.from_rgb(105, 105, 105))
                mesaj = await ctx.reply(embed=embed)
                msg = await self.client.wait_for('message', check=check2, timeout=30)
                await mesaj.delete()
                pref = msg.content
                embed = discord.Embed(title=f"Esti sigur ca vrei sa am prefixul `{pref}` ?",
                                      description=f"Vei folosi comenzile in felul urmator: {pref}pwp @fata",
                                      color=discord.Color.from_rgb(105, 105, 105))
                mesaj = await msg.reply(embed=embed)
                await mesaj.add_reaction(da)
                await mesaj.add_reaction(nu)
                try:
                    reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
                    if str(reaction.emoji) == nu:
                        raise Exception("nu")
                    await mesaj.delete()
                    await msg.delete()
                    data[f"prefix{ctx.guild.id}"] = pref
                    with open("pad/data/data.json", "w") as jsonFile:
                        json.dump(data, jsonFile)
                        jsonFile.close()
                    embed = discord.Embed(title=f"Prefixul tau este schimbat!",
                                          description=f"Pentru a reseta prefixul utilizeaza comanda {pref}resetprefix",
                                          color=discord.Color.from_rgb(105, 105, 105))
                    await ctx.send(embed=embed)
                except:
                    await msg.delete()
                    await mesaj.delete()
                    embed = discord.Embed(title=f"Nu am facut nicio modificare",
                                          description=f"Daca vrei sa schimbi prefixul, ruleaza iar comanda.",
                                          color=discord.Color.from_rgb(105, 105, 105))
                    await ctx.send(embed=embed)
                    return
            except:
                await mesaj.delete()
                return

    @commands.command(
        aliases=['set_reaction_rol', 'set_reaction_role', 'setreactie', 'setemoji', 'autorole', 'selfrole',
                 'setreaction'])
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def setreactionrole(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        embed = discord.Embed(title=f"Cum vrei sa setezi reaction-roles?",
                              description=f"🇦(automat)- Mesaj trimis de catre mine pe un canal ales\n\n🇲(manual) - Alt mesaj (voi avea nevoie de id-ul mesajului)\n\n⛔-Renunta\n\n\n*Exemplu: puteti seta mesajul `Apasa pe emoji pentru a primi rolul de membru`, toate persoanele care vor reactiona cu un anumit emoji vor primi rolul de membru.*",
                              color=discord.Color.from_rgb(105, 105, 105))
        mesaj = await ctx.reply(embed=embed)
        nu = '⛔'
        da = '✅'
        m = '🇲'
        e = '🇪'
        a = '🇦'
        await mesaj.add_reaction(a)
        await mesaj.add_reaction(m)
        await mesaj.add_reaction(nu)

        def check1(reaction, user):
            return reaction.message.id == mesaj.id and user.id == ctx.author.id and (
                    str(reaction.emoji) == nu or str(reaction.emoji) == a or str(reaction.emoji) == m or str(
                reaction.emoji) == da or str(reaction.emoji) == e)

        def check2(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=65, check=check1)
            if str(reaction.emoji) == nu:
                await mesaj.delete()
                return
            if str(reaction.emoji) == a:
                await mesaj.delete()
                situatie = 1
            elif str(reaction.emoji) == m:
                await mesaj.delete()
                situatie = 2
        except:
            await mesaj.delete()
            return
        if situatie == 1:
            embed = discord.Embed(title=f"Ai vrea sa trimit mesajul in format embed sau ca mesaj normal?",
                                  description=f"Embed-ul (🇪) e un mesaj ceva mai frumos, asa cum este asta. Mesajul (🇲) normal e ce trimiti tu in general.",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.send(embed=embed)
            await mesaj.add_reaction(e)
            await mesaj.add_reaction(m)
            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=65, check=check1)
                if str(reaction.emoji) == e:
                    await mesaj.delete()
                    embed = discord.Embed(title=f"Care ai vrea sa fie titlul embedului?",
                                          description=f"Titlul apare in partea de sus.\n\nRecomandam sa alegeti ceva generic, gen `Alegeti-va un rol!`",
                                          color=discord.Color.from_rgb(105, 105, 105))
                    mesaj = await ctx.send(embed=embed)
                    try:
                        msg = await self.client.wait_for('message', check=check2, timeout=120)
                        titlu = msg.content
                        await mesaj.delete()
                        await msg.delete()
                        embed = discord.Embed(title=f"Care ai vrea sa fie textul propriu-zis?",
                                              description=f"Textul apare in zona de jos.\n\nRecomandam sa alegeti un text potrivit, gen `Apasati mai jos pe emoji pentru a primii rolul de...`",
                                              color=discord.Color.from_rgb(105, 105, 105))
                        mesaj = await ctx.send(embed=embed)
                        try:
                            msg = await self.client.wait_for('message', check=check2, timeout=120)
                            text = msg.content
                            emb = 1
                            await mesaj.delete()
                            await msg.delete()
                        except:
                            await mesaj.delete()
                    except:
                        await mesaj.delete()
                        return
                elif str(reaction.emoji) == m:
                    await mesaj.delete()
                    emb = 0
                    embed = discord.Embed(title=f"Care ai vrea sa fie textul mesajului?",
                                          description=f"Recomandam sa alegeti ceva generic, gen `Alegeti-va un rol! Apasati mai jos pe emoji pentru a primii rolul de...`",
                                          color=discord.Color.from_rgb(105, 105, 105))
                    mesaj = await ctx.send(embed=embed)
                    try:
                        msg = await self.client.wait_for('message', check=check2, timeout=120)
                        text = msg.content
                        await mesaj.delete()
                        await msg.delete()
                    except:
                        await mesaj.delete()
            except:
                await mesaj.delete()
                return
            embed = discord.Embed(title=f"Unde vrei sa trimit mesajul?",
                                  description=f"Trimite un mesaj continand **doar** canalul pe care vrei sa setezi mesajul.",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.send(embed=embed)
            try:
                msg = await self.client.wait_for('message', check=check2, timeout=120)
                pref = str(msg.content)
                await mesaj.delete()
                try:
                    canal = re.search('<#(.+?)>', pref).group(1)
                except AttributeError:
                    canal = int(pref)
                await msg.delete()
            except:
                await mesaj.delete()
                return
            channell = self.client.get_channel(int(canal))
            if emb == 1:
                embed = discord.Embed(title=titlu, description=text, color=discord.Color.from_rgb(105, 105, 105))
                mesajj = await channell.send(embed=embed)
            else:
                mesajj = await channell.send(text)
            ok = 0
            while ok == 0:
                embed = discord.Embed(title=f"Ce emoji folosesti pentru rol?",
                                      description=f"Te rog reactioneaza cu doar **un** emoji la acest mesaj",
                                      color=discord.Color.from_rgb(105, 105, 105))
                mesaj = await ctx.send(embed=embed)

                def check3(reaction, user):
                    return reaction.message.id == mesaj.id

                try:
                    reaction, user = await self.client.wait_for('reaction_add', timeout=65, check=check3)
                    emoji = reaction
                except:
                    await mesaj.delete()
                embed = discord.Embed(title=f"Ce rol asociezi emoji-ului??",
                                      description=f"Te rog trimite un mesaj **doar cu** rolul pe care il asociezi emoji-ului {reaction}",
                                      color=discord.Color.from_rgb(105, 105, 105))
                mesaj = await ctx.send(embed=embed)
                try:
                    msg = await self.client.wait_for('message', check=check2, timeout=120)
                    pref = str(msg.content)
                    await mesaj.delete()
                    try:
                        rol = re.search('<@&(.+?)>', pref).group(1)
                    except AttributeError:
                        rol = int(pref)
                    await msg.delete()
                except:
                    await mesaj.delete()
                    return
                with open("pad/data/data.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                    jsonFile.close()
                await mesajj.add_reaction(emoji)
                match_keys2 = {key: val for key, val in data.items() if
                               key.startswith(f"emojis{ctx.guild.id}{mesajj.id}")}
                i = len(match_keys2) + 1
                try:
                    emojiid = reaction.emoji.id
                except:
                    emojiid = str(reaction.emoji)
                data[f"emojis{ctx.guild.id}{mesajj.id}{i}"] = emojiid
                data[f"{ctx.guild.id}{mesajj.id}{emojiid}rol"] = int(rol)
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                embed = discord.Embed(title=f"Vrei sa mai setezi alte emoji-uri (roluri)?",
                                      description=f"Da sau nu domnule :O", color=discord.Color.from_rgb(105, 105, 105))
                mesaj = await ctx.send(embed=embed)
                await mesaj.add_reaction(da)
                await mesaj.add_reaction(nu)
                try:
                    reaction, user = await self.client.wait_for('reaction_add', timeout=65, check=check1)
                    if str(reaction.emoji) == nu:
                        await mesaj.delete()
                        ok = 1
                    if str(reaction.emoji) == da:
                        await mesaj.delete()
                except:
                    await mesaj.delete()
                    return
            with open("pad/data/data.json", "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()

            match_keys = {key: val for key, val in data.items() if key.startswith(f"{ctx.guild.id}mesajptemoji")}
            i = len(match_keys) + 1
            data[f"{ctx.guild.id}mesajptemoji{i}"] = mesajj.id
            match_keys2 = {key: val for key, val in data.items() if key.startswith(f"emojis{ctx.guild.id}{mesajj.id}")}
            i = len(match_keys2) + 1
            data[f"emojis{ctx.guild.id}{mesajj.id}{i}"] = emojiid
            match_keys3 = {key: val for key, val in data.items() if key.startswith(f"canalemojis{ctx.guild.id}")}
            i = len(match_keys3) + 1
            data[f"canalemojis{ctx.guild.id}{i}"] = int(mesajj.channel.id)
            data[f"{ctx.guild.id}{mesajj.id}{emojiid}rol"] = int(rol)
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            embed = discord.Embed(title=f"Gata domnule.",
                                  description=f"Daca doresti sa mai adaugi roluri la mesaj, ruleaza iar comanda si utilizeaza optiunea manual.",
                                  color=discord.Color.from_rgb(105, 105, 105))
            await ctx.send(embed=embed)

        elif situatie == 2:
            embed = discord.Embed(title=f"Pe ce canal e mesajul?",
                                  description=f"Trimite un mesaj continand **doar** canalul pe care e mesajul.",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.send(embed=embed)
            try:
                msg = await self.client.wait_for('message', check=check2, timeout=120)
                pref = str(msg.content)
                await mesaj.delete()
                try:
                    canal = re.search('<#(.+?)>', pref).group(1)
                except AttributeError:
                    canal = int(pref)
                await msg.delete()
            except:
                await mesaj.delete()
                return
            channell = self.client.get_channel(int(canal))
            embed = discord.Embed(title=f"Care este id-ul mesajului?",
                                  description=f"Te rog trimite **doar** id-ul. Daca nu stii cum sa il aflii, foloseste comanda `.id` (+ reply la mesaj), apoi rulezi iar comanda daca e necesar.",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.send(embed=embed)
            try:
                msg = await self.client.wait_for('message', check=check2, timeout=240)
                mesajid = int(msg.content)
                mesajj = None
                mesajjee = await channell.history(limit=200).flatten()
                for mesajt in mesajjee:
                    if mesajt.id == mesajid:
                        mesajj = mesajt
                if mesajj == None:
                    await ctx.send("n-am putut gasi mesajul, posibil sa fie prea vechi.")
                    raise Exception("lmao")
            except:
                await mesaj.delete()
                return
            ok = 0
            while ok == 0:
                embed = discord.Embed(title=f"Ce emoji folosesti pentru rol?",
                                      description=f"Te rog reactioneaza cu doar **un** emoji la acest mesaj",
                                      color=discord.Color.from_rgb(105, 105, 105))
                mesaj = await ctx.send(embed=embed)

                def check3(reaction, user):
                    return reaction.message.id == mesaj.id

                try:
                    reaction, user = await self.client.wait_for('reaction_add', timeout=65, check=check3)
                    emoji = reaction
                except:
                    await mesaj.delete()
                embed = discord.Embed(title=f"Ce rol asociezi emoji-ului??",
                                      description=f"Te rog trimite un mesaj **doar cu** rolul pe care il asociezi emoji-ului {reaction}",
                                      color=discord.Color.from_rgb(105, 105, 105))
                mesaj = await ctx.send(embed=embed)
                try:
                    msg = await self.client.wait_for('message', check=check2, timeout=120)
                    pref = str(msg.content)
                    await mesaj.delete()
                    try:
                        rol = re.search('<@&(.+?)>', pref).group(1)
                    except AttributeError:
                        rol = int(pref)
                    await msg.delete()
                except:
                    await mesaj.delete()
                    return
                with open("pad/data/data.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                    jsonFile.close()
                await mesajj.add_reaction(emoji)
                match_keys2 = {key: val for key, val in data.items() if
                               key.startswith(f"emojis{ctx.guild.id}{mesajid}")}
                i = len(match_keys2) + 1
                try:
                    emojiid = reaction.emoji.id
                except:
                    emojiid = str(reaction.emoji)
                data[f"emojis{ctx.guild.id}{mesajid}{i}"] = emojiid
                data[f"{ctx.guild.id}{mesajid}{emojiid}rol"] = int(rol)
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                embed = discord.Embed(title=f"Vrei sa mai setezi alte emoji-uri (roluri)?",
                                      description=f"Da sau nu domnule :O", color=discord.Color.from_rgb(105, 105, 105))
                mesaj = await ctx.send(embed=embed)
                await mesaj.add_reaction(da)
                await mesaj.add_reaction(nu)
                try:
                    reaction, user = await self.client.wait_for('reaction_add', timeout=65, check=check1)
                    if str(reaction.emoji) == nu:
                        await mesaj.delete()
                        ok = 1
                    if str(reaction.emoji) == da:
                        await mesaj.delete()
                except:
                    await mesaj.delete()
                    return
            with open("pad/data/data.json", "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()

            match_keys = {key: val for key, val in data.items() if key.startswith(f"{ctx.guild.id}mesajptemoji")}
            i = len(match_keys) + 1
            data[f"{ctx.guild.id}mesajptemoji{i}"] = mesajid
            match_keys2 = {key: val for key, val in data.items() if key.startswith(f"emojis{ctx.guild.id}{mesajid}")}
            i = len(match_keys2) + 1
            data[f"emojis{ctx.guild.id}{mesajid}{i}"] = emojiid
            match_keys3 = {key: val for key, val in data.items() if key.startswith(f"canalemojis{ctx.guild.id}")}
            i = len(match_keys3) + 1
            data[f"canalemojis{ctx.guild.id}{i}"] = int(channell.id)
            data[f"{ctx.guild.id}{mesajid}{emojiid}rol"] = int(rol)
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            embed = discord.Embed(title=f"Gata domnule.",
                                  description=f"Daca doresti sa mai adaugi roluri la mesaj, ruleaza iar comanda si utilizeaza optiunea manual.",
                                  color=discord.Color.from_rgb(105, 105, 105))
            await ctx.send(embed=embed)

    @commands.command(aliases=['setroluri', 'setroles', 'setrol'])
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def setrole(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"xp{ctx.guild.id}" not in data or data[f"xp{ctx.guild.id}"] == 0:
            xp = 0
        else:
            xp = 1
        if xp == 0:
            embed = discord.Embed(title=f"Xp-ul este dezactivat pe acest server.",
                                  description=f"Daca vrei sa il activezi foloseste comanda `.setxp`.",
                                  color=discord.Color.from_rgb(105, 105, 105))
            await ctx.reply(embed=embed)
            return
        embed = discord.Embed(title=f"Vrei sa setezi un rol xp?",
                              description=f"✅-Da\n\n⛔-Nu\n\n👍-Arata rolurile deja setate\n\n🚮-Sterge rolurile deja setate\n\n*Pro tip: daca vrei sa dau automat un rol membrilor nou-intrati, puteti seta un rol pentru 0xp.*",
                              color=discord.Color.from_rgb(105, 105, 105))
        mesaj = await ctx.reply(embed=embed)
        nu = '⛔'
        da = '✅'
        arata = '👍'
        sterge = '🚮'
        await mesaj.add_reaction(da)
        await mesaj.add_reaction(nu)
        await mesaj.add_reaction(arata)
        await mesaj.add_reaction(sterge)

        def check1(reaction, user):
            return reaction.message.id == mesaj.id and user.id == ctx.author.id and (
                    str(reaction.emoji) == nu or str(reaction.emoji) == da or str(reaction.emoji) == arata or str(
                reaction.emoji) == sterge)

        def check2(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
            if str(reaction.emoji) == nu:
                await mesaj.delete()
                return
            if str(reaction.emoji) == arata:
                await mesaj.delete()
                match_keys = {key: val for key, val in data.items() if key.startswith(f"{ctx.guild.id}rol")}
                text = ""
                for key in match_keys:
                    if int(data[key]) != 0:
                        k = f"rol{data[key]}"
                        text = text + f"<@&{int(data[key])}>: {int(data[k])}xp\n"
                embed = discord.Embed(title=f"Roluri setate", description=text,
                                      color=discord.Color.from_rgb(105, 105, 105))
                mesaj = await ctx.send(embed=embed)
                return
            if str(reaction.emoji) == sterge:
                await mesaj.delete()
                match_keys = {key: val for key, val in data.items() if key.startswith(f"{ctx.guild.id}rol")}
                text = "Roluri setate:\n"
                for key in match_keys:
                    if int(data[key]) != 0:
                        k = f"rol{data[key]}"
                        text = text + f"<@&{int(data[key])}>: {int(data[k])}xp\n"
                text = text + f"\n**Spune doar rolul (exemplU: @Rol)**"
                embed = discord.Embed(title=f"Ce rol elimini din lista?", description=text,
                                      color=discord.Color.from_rgb(105, 105, 105))
                mesaj = await ctx.send(embed=embed)
                try:
                    msg = await self.client.wait_for('message', check=check2, timeout=120)
                    pref = str(msg.content)
                    await mesaj.delete()
                    try:
                        canal = re.search('<@&(.+?)>', pref).group(1)
                    except AttributeError:
                        canal = int(pref)
                    for key in match_keys:
                        if int(data[key] == int(canal)):
                            data[key] = 0
                            data[f"rol{int(canal)}"] = 0
                            with open("pad/data/data.json", "w") as jsonFile:
                                json.dump(data, jsonFile)
                                jsonFile.close()
                    embed = discord.Embed(title=f"Gata, am eliminat rolul din lista", description=f"da, lmao.*",
                                          color=discord.Color.from_rgb(105, 105, 105))
                    mesaj = await ctx.send(embed=embed)
                except:
                    await mesaj.delete()
                    return
                return
            await mesaj.delete()
            match_keys = {key: val for key, val in data.items() if key.startswith(f"{ctx.guild.id}rol")}
            i = len(match_keys) + 1
            embed = discord.Embed(title=f"Ce rol vrei sa setez?",
                                  description=f"Te rog trimite un mesaj **doar cu** rolul sau id-ul acestuia (exemplu: @Rolpentru20xp)",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.send(embed=embed)
            try:
                msg = await self.client.wait_for('message', check=check2, timeout=120)
                pref = str(msg.content)
                await mesaj.delete()
                try:
                    canal = re.search('<@&(.+?)>', pref).group(1)
                except AttributeError:
                    canal = int(pref)
                embed = discord.Embed(title=f"La ce numar de xp acumulat ai vrea sa ofer rolul?",
                                      description=f"Te rog trimite un mesaj **doar cu** cu xp-ul necesar (exemplu: 2000)\n\n*Recomandam sa setati roluri pentru valori mai mari de 1000xp, dar e alegerea voastra.*",
                                      color=discord.Color.from_rgb(105, 105, 105))
                mesaj = await ctx.send(embed=embed)
                try:
                    msg = await self.client.wait_for('message', check=check2, timeout=120)
                    nr = int(msg.content)
                    await mesaj.delete()
                    embed = discord.Embed(title=f"Esti sigur?",
                                          description=f"Voi da rolul de <@&{canal}> tuturor utilizatorilor care vor face {nr}xp. Este ok? ",
                                          color=discord.Color.from_rgb(105, 105, 105))
                    mesaj = await ctx.send(embed=embed)
                    await mesaj.add_reaction(da)
                    await mesaj.add_reaction(nu)
                    try:
                        reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
                        if str(reaction.emoji) == nu:
                            await mesaj.delete()
                            return
                        await mesaj.delete()
                        data[f"{ctx.guild.id}rol{i}"] = int(canal)
                        data[f"rol{int(canal)}"] = int(nr)
                        with open("pad/data/data.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                            jsonFile.close()
                        embed = discord.Embed(title=f"Bun smechere.",
                                              description=f"Am setat rolul de <@&{canal}> pentru {nr}xp. Daca mai vrei sa setezi vreun rol, ruleaza iar comanda!",
                                              color=discord.Color.from_rgb(105, 105, 105))
                        mesaj = await ctx.reply(embed=embed)
                    except:
                        await mesaj.delete()
                        return
                except:
                    await mesaj.delete()
                    return
            except:
                await mesaj.delete()
                return
        except:
            await mesaj.delete()
            return

    @commands.command(aliases=['setrank'])
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def setxp(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"xp{ctx.guild.id}" not in data or data[f"xp{ctx.guild.id}"] == 0:
            xp = 0
        else:
            xp = 1
        if xp == 0:
            embed = discord.Embed(title=f"Xp-ul este dezactivat pe acest server.", description=f"Vrei sa îl activezi?",
                                  color=discord.Color.from_rgb(105, 105, 105))
        else:
            embed = discord.Embed(title=f"Xp-ul este activat pe acest server.", description=f"Vrei sa îl dezactivezi?",
                                  color=discord.Color.from_rgb(105, 105, 105))
        mesaj = await ctx.reply(embed=embed)
        nu = '⛔'
        da = '✅'
        await mesaj.add_reaction(da)
        await mesaj.add_reaction(nu)

        def check1(reaction, user):
            return reaction.message.id == mesaj.id and user.id == ctx.author.id and (
                    str(reaction.emoji) == nu or str(reaction.emoji) == da)

        def check2(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
            if str(reaction.emoji) == nu:
                raise Exception("nu")
            await mesaj.delete()
            if xp == 0:
                embed = discord.Embed(title=f"Ok, am activat xp-ul!",
                                      description=f"De acum membrii serverului pot folosi comenzi precum `.xp`, `.top`",
                                      color=discord.Color.from_rgb(105, 105, 105))
                data[f"xp{ctx.guild.id}"] = 1
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
            else:
                embed = discord.Embed(title=f"Ok, am dezactivat xp-ul!",
                                      description=f"De acum membrii serverului **nu** mai pot folosi comenzi precum `.xp`, `.top`\n\nPoti folosi comanda `.setrol` pentru a seta roluri pe xp!",
                                      color=discord.Color.from_rgb(105, 105, 105))
                data[f"xp{ctx.guild.id}"] = 0
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
            mesaj = await ctx.reply(embed=embed)
        except:
            await mesaj.delete()
            return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def db(self, ctx, key=None, valoare=None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if ctx.author.id != 852673995563597875 and ctx.author.id != 306769101592985610:
            await ctx.send("nu")
            return
        if key == None:
            await ctx.send("???")
            return
        if valoare == None:
            await ctx.send("???")
            return
        data[key] = valoare
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()
        await ctx.send("k")

    @commands.command(aliases=['eventxp'])
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def xpevent(self, ctx, numar: int = 1):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if numar > 3:
            await ctx.reply("Bai domnule, maximul acceptat e xp triplu")
            return
        elif numar <= 0:
            await ctx.reply("nu")
            return
        elif numar == 1:
            data["eventxp"] = 1
            embed = discord.Embed(title="Gata eventul.", description="De acum primiti xp normal. ",
                                  color=default_color)
        elif numar == 2:
            data["eventxp"] = 2
            embed = discord.Embed(title="Bunn", description="De acum se primeste xp dublu", color=default_color)
        elif numar == 3:
            data["eventxp"] = 3
            embed = discord.Embed(title="Bunn", description="De acum se primeste xp triplu",
                                  color=default_color)
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def resetprefix(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"prefix{ctx.guild.id}" in data and data[f"prefix{ctx.guild.id}"] != 0:
            pref = data[f"prefix{ctx.guild.id}"]
        else:
            pref = "."
        embed = discord.Embed(title=f"Prefixul actual este `{pref}`", description=f"Vrei sa îl resetezi?",
                              color=discord.Color.from_rgb(105, 105, 105))
        embed.set_footer(text=f"Prefixul prestabilit este `.`")
        mesaj = await ctx.reply(embed=embed)
        nu = '⛔'
        da = '✅'
        await mesaj.add_reaction(da)
        await mesaj.add_reaction(nu)

        def check1(reaction, user):
            return reaction.message.id == mesaj.id and user.id == ctx.author.id and (
                    str(reaction.emoji) == nu or str(reaction.emoji) == da)

        def check2(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
            if str(reaction.emoji) == nu:
                raise Exception("nu")
            await mesaj.delete()
            data[f"prefix{ctx.guild.id}"] = 0
            embed = discord.Embed(title=f"Ok, am resetat prefixul!",
                                  description=f"De acum veti putea utiliza comenzile prin prefixul `.` (exemplu: .help)",
                                  color=discord.Color.from_rgb(105, 105, 105))
            data[f"xp{ctx.guild.id}"] = 1
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()
            mesaj = await ctx.reply(embed=embed)
        except:
            await mesaj.delete()
            return

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def setmesaj(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        nu = '⛔'
        da = '✅'
        p = '🇵'
        w = '🇼'
        embed = discord.Embed(title=f"Ce mesaj vrei sa setezi?",
                              description=f"Poti seta urmatoarele tipuri de mesaje:\n    {p} - mesaj privat (membrii noi primesc un mesaj in DM)\n    {w} - mesaj public (membrii noi primesc un mesaj pe un canal)\n\n    {nu} - renunta",
                              color=discord.Color.from_rgb(105, 105, 105))
        embed.set_footer(
            text=f"Poti rula oricand comanda iar pentru a seta un alt tip de mesaj, poti folosi ambele tipuri.")
        mesaj = await ctx.reply(embed=embed)
        await mesaj.add_reaction(p)
        await mesaj.add_reaction(w)
        await mesaj.add_reaction(nu)

        def check1(reaction, user):
            return reaction.message.id == mesaj.id and user.id == ctx.author.id and (
                    str(reaction.emoji) == nu or str(reaction.emoji) == da or str(reaction.emoji) == p or str(
                reaction.emoji) == w)

        def check2(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=35, check=check1)
            if str(reaction.emoji) == nu:
                raise Exception("nu")
            if str(reaction.emoji) == p:
                await mesaj.delete()
                if f"mesajintrareprivverif{ctx.guild.id}" not in data or data[
                    f"mesajintrareprivverif{ctx.guild.id}"] == 0:
                    verif = 0
                else:
                    verif = 1
                if verif == 1:
                    embed = discord.Embed(title=f"Mesajul privat este activat.",
                                          description=f"Doresti sa dezactivezi mesajul trimis in privat?",
                                          color=discord.Color.from_rgb(105, 105, 105))
                    mesaj = await ctx.send(embed=embed)
                    await mesaj.add_reaction(da)
                    await mesaj.add_reaction(nu)
                    try:
                        reaction, user = await self.client.wait_for('reaction_add', timeout=35, check=check1)
                        if str(reaction.emoji) == nu:
                            raise Exception("nu")
                        data[f"mesajintrareprivverif{ctx.guild.id}"] = 0
                        data[f"mesajintrarepriv{ctx.guild.id}"] = 0
                        with open("pad/data/data.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                            jsonFile.close()
                        embed = discord.Embed(title=f"Mesajul privat este dezactivat.",
                                              description=f"Nimeni nu va mai primi mesaj in privat.",
                                              color=discord.Color.from_rgb(105, 105, 105))
                        await ctx.send(embed=embed)
                    except:
                        await mesaj.delete()
                        return
                else:
                    embed = discord.Embed(title=f"Mesajul privat nu e activat.",
                                          description=f"Doresti sa activezi mesajul trimis in privat? Daca da, va urma o scurta initializare a mesajului, care va fi trimis membrilor nou-intrati pe server.",
                                          color=discord.Color.from_rgb(105, 105, 105))
                    mesaj = await ctx.send(embed=embed)
                    await mesaj.add_reaction(da)
                    await mesaj.add_reaction(nu)
                    try:
                        reaction, user = await self.client.wait_for('reaction_add', timeout=35, check=check1)
                        if str(reaction.emoji) == nu:
                            raise Exception("nu")
                        await mesaj.delete()
                        embed = discord.Embed(title=f"Ce mesaj vrei sa trimit membrilor noi?",
                                              description=f"Trimite doar mesajul. Exemplu: `Bun venit in server!`",
                                              color=discord.Color.from_rgb(105, 105, 105))
                        mesaj = await ctx.send(embed=embed)
                        msg = await self.client.wait_for('message', check=check2, timeout=30)
                        await mesaj.delete()
                        pref = str(msg.content)
                        embed = discord.Embed(
                            title=f"Esti sigur ca vrei sa trimit urmatorul mesaj in privat noilor membrii?",
                            description=f"Mesaj: {pref}", color=discord.Color.from_rgb(105, 105, 105))
                        mesaj = await msg.reply(embed=embed)
                        await mesaj.add_reaction(da)
                        await mesaj.add_reaction(nu)
                        try:
                            reaction, user = await self.client.wait_for('reaction_add', timeout=35, check=check1)
                            if str(reaction.emoji) == nu:
                                raise Exception("nu")
                            await mesaj.delete()
                            await msg.delete()
                            data[f"mesajintrareprivverif{ctx.guild.id}"] = 1
                            data[f"mesajintrarepriv{ctx.guild.id}"] = pref
                            with open("pad/data/data.json", "w") as jsonFile:
                                json.dump(data, jsonFile)
                                jsonFile.close()
                            embed = discord.Embed(title=f"Ok, am activat mesajul privat!",
                                                  description=f"De acum membrii noi vor fi intampinati in privat cu mesajul ales.",
                                                  color=discord.Color.from_rgb(105, 105, 105))
                            await ctx.send(embed=embed)
                        except:
                            await mesaj.delete()
                            await msg.delete()
                            embed = discord.Embed(title=f"Ok, nu am schimbat nimic", description=f"Bun.",
                                                  color=discord.Color.from_rgb(105, 105, 105))
                            await ctx.send(embed=embed)
                            return
                    except:
                        await mesaj.delete()
                        return

            if str(reaction.emoji) == w:
                await mesaj.delete()
                if f"mesajintrarecanalverif{ctx.guild.id}" not in data or data[
                    f"mesajintrarecanalverif{ctx.guild.id}"] == 0:
                    verif = 0
                else:
                    verif = 1
                if verif == 1:
                    embed = discord.Embed(title=f"Mesajul de intampinare este activat.",
                                          description=f"Doresti sa dezactivezi mesajul de intampinare?",
                                          color=discord.Color.from_rgb(105, 105, 105))
                    mesaj = await ctx.send(embed=embed)
                    await mesaj.add_reaction(da)
                    await mesaj.add_reaction(nu)
                    try:
                        reaction, user = await self.client.wait_for('reaction_add', timeout=35, check=check1)
                        if str(reaction.emoji) == nu:
                            raise Exception("nu")
                        data[f"mesajintrarecanalverif{ctx.guild.id}"] = 0
                        data[f"mesajintrarecanal{ctx.guild.id}"] = 0
                        data[f"canalmesajintrare{ctx.guild.id}"] = 0
                        with open("pad/data/data.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                            jsonFile.close()
                        embed = discord.Embed(title=f"Mesajul de intampinare este dezactivat.",
                                              description=f"Nimeni nu va mai primi mesaj.",
                                              color=discord.Color.from_rgb(105, 105, 105))
                        await ctx.send(embed=embed)
                    except:
                        await mesaj.delete()
                        return
                else:
                    embed = discord.Embed(title=f"Mesajul de intampinare nu e activat.",
                                          description=f"Doresti sa activezi mesajul de intampinare? Daca da, va urma o scurta initializare a mesajului, care va fi trimis membrilor nou-intrati pe server pe un canal ales.",
                                          color=discord.Color.from_rgb(105, 105, 105))
                    mesaj = await ctx.send(embed=embed)
                    await mesaj.add_reaction(da)
                    await mesaj.add_reaction(nu)
                    try:
                        reaction, user = await self.client.wait_for('reaction_add', timeout=35, check=check1)
                        if str(reaction.emoji) == nu:
                            raise Exception("nu")
                        await mesaj.delete()
                        embed = discord.Embed(title=f"Pe ce canal vrei sa trimit mesajul de intampinare?",
                                              description=f"Trimite un mesaj continand doar canalul sau id-ul acestuia. Exemplu: `#general`\n\nPentru a evita erorile, incearca sa trimiti canalul/id-ul corect.",
                                              color=discord.Color.from_rgb(105, 105, 105))
                        mesaj = await ctx.send(embed=embed)
                        msg = await self.client.wait_for('message', check=check2, timeout=30)
                        await mesaj.delete()
                        pref = str(msg.content)
                        try:
                            canal = re.search('<#(.+?)>', pref).group(1)
                        except AttributeError:
                            canal = int(pref)
                        embed = discord.Embed(title=f"Esti sigur ca vrei sa intampin noii membrii pe <#{canal}>?",
                                              description=f"Daca da, va urma si initializarea mesajului.",
                                              color=discord.Color.from_rgb(105, 105, 105))
                        mesaj = await msg.reply(embed=embed)
                        await mesaj.add_reaction(da)
                        await mesaj.add_reaction(nu)
                        try:
                            reaction, user = await self.client.wait_for('reaction_add', timeout=35, check=check1)
                            if str(reaction.emoji) == nu:
                                raise Exception("nu")
                            await mesaj.delete()
                            await msg.delete()
                            embed = discord.Embed(title=f"Ce mesaj vrei sa trimit membrilor noi?",
                                                  description=f"Trimite doar mesajul. Exemplu: `Bun venit in server!`",
                                                  color=discord.Color.from_rgb(105, 105, 105))
                            mesaj = await ctx.send(embed=embed)
                            msg = await self.client.wait_for('message', check=check2, timeout=30)
                            await mesaj.delete()
                            pref = str(msg.content)
                            embed = discord.Embed(
                                title=f"Esti sigur ca vrei sa trimit urmatorul mesaj in privat noilor membrii?",
                                description=f"Mesaj: {pref}", color=discord.Color.from_rgb(105, 105, 105))
                            mesaj = await msg.reply(embed=embed)
                            await mesaj.add_reaction(da)
                            await mesaj.add_reaction(nu)
                            try:
                                reaction, user = await self.client.wait_for('reaction_add', timeout=35, check=check1)
                                if str(reaction.emoji) == nu:
                                    raise Exception("nu")
                                await mesaj.delete()
                                await msg.delete()
                                data[f"mesajintrarecanalverif{ctx.guild.id}"] = 1
                                data[f"mesajintrarecanal{ctx.guild.id}"] = pref
                                data[f"canalmesajintrare{ctx.guild.id}"] = canal
                                with open("pad/data/data.json", "w") as jsonFile:
                                    json.dump(data, jsonFile)
                                    jsonFile.close()
                                embed = discord.Embed(title=f"Ok, am activat mesajul de intampinare!",
                                                      description=f"De acum membrii noi vor fi intampinati pe <#{canal}> cu mesajul ales.",
                                                      color=discord.Color.from_rgb(105, 105, 105))
                                await ctx.send(embed=embed)
                            except:
                                await mesaj.delete()
                                await msg.delete()
                                embed = discord.Embed(title=f"Ok, nu am schimbat nimic", description=f"Bun.",
                                                      color=discord.Color.from_rgb(105, 105, 105))
                                await ctx.send(embed=embed)
                                return
                        except:
                            await mesaj.delete()
                            return
                    except:
                        await mesaj.delete()
                        await msg.delete()
                        return
        except:
            await mesaj.delete()
            return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setbirthday(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        embed = discord.Embed(title=f"Ce vrei sa setezi pentru comanda .birthday? (reactioneaza mai jos)",
                              description=f"🇨: Canalul pe care sa trimit urari\n🇷: rolul pe care il voi da tuturor sarbatoritilor\n⛔: renunta",
                              color=discord.Color.from_rgb(105, 105, 105))
        mesaj = await ctx.reply(embed=embed)
        nu = '⛔'
        c = '🇨'
        r = '🇷'
        await mesaj.add_reaction(c)
        await mesaj.add_reaction(r)
        await mesaj.add_reaction(nu)

        def check1(reaction, user):
            return reaction.message.id == mesaj.id and user.id == ctx.author.id and (
                    str(reaction.emoji) == nu or str(reaction.emoji) == c or str(reaction.emoji) == r)

        def check2(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=45, check=check1)
            if str(reaction.emoji) == nu:
                raise Exception("nu")
            if str(reaction.emoji) == c:
                embed = discord.Embed(title=f"Bun mestere",
                                      description=f"Te rog trimite un mesaj care contine **doar** canalul/id-ul canalului pe care voi trimite urari. *Poate fi un canal creat special sau unul simplu pe care se vorbeste in general.*",
                                      color=discord.Color.from_rgb(105, 105, 105))
                mesaj = await ctx.send(embed=embed)
                msg = await self.client.wait_for('message', check=check2, timeout=30)
                pref = str(msg.content)
                await mesaj.delete()
                try:
                    canal = re.search('<#(.+?)>', pref).group(1)
                except AttributeError:
                    canal = int(pref)
                data[f"birthdaycanal{ctx.guild.id}"] = canal
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                embed = discord.Embed(title=f"Gata.",
                                      description=f"Voi trimite urari pe <#{canal}>. Daca vrei sa setezi si un rol pe care sa il dau sarbatoritilor, ruleaza comanda din nou!",
                                      color=discord.Color.from_rgb(105, 105, 105))
                await ctx.send(embed=embed)
                return
            if str(reaction.emoji) == r:
                embed = discord.Embed(title=f"Bun mestere",
                                      description=f"Te rog trimite un mesaj care contine **doar** rolul/id-ul rolului pe care il voi da sarbatoritilor.",
                                      color=discord.Color.from_rgb(105, 105, 105))
                mesaj = await ctx.send(embed=embed)
                msg = await self.client.wait_for('message', check=check2, timeout=30)
                pref = str(msg.content)
                await mesaj.delete()
                try:
                    canal = re.search('<@&(.+?)>', pref).group(1)
                except AttributeError:
                    canal = int(pref)
                data[f"birthdayrol{ctx.guild.id}"] = canal
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                embed = discord.Embed(title=f"Gata.",
                                      description=f"Voi da sarbatoritilor rolul de <@&{canal}>. Daca vrei sa setezi si un canal pe care sa trimit urari, ruleaza comanda din nou!",
                                      color=discord.Color.from_rgb(105, 105, 105))
                await ctx.send(embed=embed)
                return

        except:
            await mesaj.delete()
            return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setlogs(self, ctx, *, channel=None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if channel is not None:
            try:
                canal = re.search('<#(.+?)>', channel).group(1)
            except AttributeError:
                canal = int(channel)
            embed = discord.Embed(title=f"Hmmmmmmmmm",
                                  description=f"Sigur vrei sa setezi <#{canal}> ca si logs channel?",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.reply(embed=embed)
            nu = '⛔'
            da = '✅'
            await mesaj.add_reaction(da)
            await mesaj.add_reaction(nu)

            def check1(reaction, user):
                return reaction.message.id == mesaj.id and user.id == ctx.author.id and (
                        str(reaction.emoji) == nu or str(reaction.emoji) == da)

            def check2(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
                if str(reaction.emoji) == nu:
                    raise Exception("nu")
                await mesaj.delete()
                data[f"logs{ctx.guild.id}"] = canal
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                embed = discord.Embed(title=f"Gata mestere",
                                      description=f"Voi trimite pe <#{canal}> mesajele/pozele/videoclipurile sterse, activitatea de pe vocal, activitatea staff si multe altele.",
                                      color=discord.Color.from_rgb(105, 105, 105))
                await ctx.send(embed=embed)
            except:
                await mesaj.delete()
                return
        else:
            def check1(reaction, user):
                return reaction.message.id == mesaj.id and user.id == ctx.author.id and (
                        str(reaction.emoji) == nu or str(reaction.emoji) == da)

            def check2(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

            embed = discord.Embed(title=f"Bun mestere",
                                  description=f"Te rog trimite un mesaj care contine **doar** canalul/id-ul canalului pe care vreti sa il folositi ca si logs. Exemplu: `#logs`",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.reply(embed=embed)
            msg = await self.client.wait_for('message', check=check2, timeout=30)
            pref = str(msg.content)
            await mesaj.delete()
            try:
                canal = re.search('<#(.+?)>', pref).group(1)
            except AttributeError:
                canal = int(pref)
            await msg.delete()
            embed = discord.Embed(title=f"Hmmmmmmmmm",
                                  description=f"Sigur vrei sa setezi <#{canal}> ca si logs channel?",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.send(embed=embed)
            nu = '⛔'
            da = '✅'
            await mesaj.add_reaction(da)
            await mesaj.add_reaction(nu)
            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
                if str(reaction.emoji) == nu:
                    raise Exception("nu")
                await mesaj.delete()
                data[f"logs{ctx.guild.id}"] = canal
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                embed = discord.Embed(title=f"Gata mestere",
                                      description=f"Voi trimite pe <#{canal}> mesajele/pozele/videoclipurile sterse, activitatea de pe vocal, activitatea staff si multe altele.",
                                      color=discord.Color.from_rgb(105, 105, 105))
                await ctx.send(embed=embed)
            except:
                await mesaj.delete()
                return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def download(self, ctx):
        with open("pad/data/data.json", "w") as f:
            print("nu")
            # db[k]=data[k]
            # print(k,db[k])

    @commands.command(aliases=['setvocal'])
    @commands.has_permissions(administrator=True)
    async def setvoice(self, ctx, *, channel=None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if channel is not None:
            try:
                canal = re.search('<#(.+?)>', channel).group(1)
            except AttributeError:
                canal = int(channel)
            embed = discord.Embed(title=f"Hmmmmmmmmm",
                                  description=f"Sigur vrei sa setezi <#{canal}> ca si canal de voice?",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.reply(embed=embed)
            nu = '⛔'
            da = '✅'
            await mesaj.add_reaction(da)
            await mesaj.add_reaction(nu)

            def check1(reaction, user):
                return reaction.message.id == mesaj.id and user.id == ctx.author.id and (
                        str(reaction.emoji) == nu or str(reaction.emoji) == da)

            def check2(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
                if str(reaction.emoji) == nu:
                    raise Exception("nu")
                await mesaj.delete()
                data[f"voice{ctx.guild.id}"] = canal
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                embed = discord.Embed(title=f"Gata mestere",
                                      description=f"Toate persoanele care vor intra pe <#{canal}> vor fi mutati pe un canal propriu",
                                      color=discord.Color.from_rgb(105, 105, 105))
                await ctx.send(embed=embed)
            except:
                await mesaj.delete()
                return
        else:
            nu = '⛔'
            da = '✅'

            def check1(reaction, user):
                return reaction.message.id == mesaj.id and user.id == ctx.author.id and (
                        str(reaction.emoji) == nu or str(reaction.emoji) == da)

            def check2(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

            embed = discord.Embed(title=f"Bun mestere",
                                  description=f"Vrei sa se creeze automat un canal pentru voice sau stii sa faci singur? (+ sa iei id-ul canalului)\n\n✅-Fac automat (de preferat)\n⛔-Nu fac canal (daca alegi asta, va urma sa imi dai tu ping la canal sau id-ul canalului)",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.reply(embed=embed)
            await mesaj.add_reaction(da)
            await mesaj.add_reaction(nu)
            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=25, check=check1)
                if str(reaction.emoji) == nu:
                    raise Exception("nu")
                await mesaj.delete()
                chanal = await ctx.guild.create_voice_channel('canal vocal intermediar')
                data[f"voice{ctx.guild.id}"] = chanal.id
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                embedd2 = discord.Embed(title=f"Gata mestere",
                                        description=f"Am setat canalul <#{chanal.id}> pentru voice intermediar. Poti schimba numele canalului, pozitia sau orice alta setare fara a avea probleme.\n\n*recomandam sa testati canalul pentru a vedea daca va place optiunea*",
                                        color=discord.Color.from_rgb(105, 105, 105))
                mesaj = await ctx.send(embed=embedd2)
                return


            except Exception as ex:
                print(ex)
                pass

            embed = discord.Embed(title=f"Bun mestere",
                                  description=f"Te rog trimite un mesaj care contine **doar** canalul/id-ul canalului pe care vreti sa il folositi ca intermediar pentru voice. Exemplu: `#intra_voice`",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.reply(embed=embed)
            msg = await self.client.wait_for('message', check=check2, timeout=120)
            pref = str(msg.content)
            await mesaj.delete()
            try:
                canal = re.search('<#(.+?)>', pref).group(1)
            except:
                canal = int(pref)
            await msg.delete()
            embed = discord.Embed(title=f"Hmmmmmmmmm",
                                  description=f"Sigur vrei sa setezi <#{canal}> ca si canal de voice intermediar?",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.send(embed=embed)
            nu = '⛔'
            da = '✅'
            await mesaj.add_reaction(da)
            await mesaj.add_reaction(nu)
            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
                if str(reaction.emoji) == nu:
                    raise Exception("nu")
                await mesaj.delete()
                data[f"voice{ctx.guild.id}"] = canal
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                embed = discord.Embed(title=f"Gata mestere",
                                      description=f"Voi trimite oamenii de pe <#{canal}> pe canalul lor propriu.",
                                      color=discord.Color.from_rgb(105, 105, 105))
                await ctx.send(embed=embed)
            except:
                await mesaj.delete()
                return

    @commands.command(aliases=['setinvite'])
    @commands.has_permissions(administrator=True)
    async def setinvites(self, ctx, channel=None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if channel is not None:
            try:
                canal = re.search('<#(.+?)>', channel).group(1)
            except AttributeError:
                canal = int(channel)
            embed = discord.Embed(title=f"Hmmmmmmmmm",
                                  description=f"Sigur vrei sa setezi <#{canal}> ca si canal de invites? Voi pune aici membrii nou-intrati si informatii despre cine i-a invitat",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.reply(embed=embed)
            nu = '⛔'
            da = '✅'
            await mesaj.add_reaction(da)
            await mesaj.add_reaction(nu)

            def check1(reaction, user):
                return reaction.message.id == mesaj.id and user.id == ctx.author.id and (
                        str(reaction.emoji) == nu or str(reaction.emoji) == da)

            def check2(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
                if str(reaction.emoji) == nu:
                    raise Exception("nu")
                await mesaj.delete()
                data[f"invites{ctx.guild.id}"] = canal
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                embed = discord.Embed(title=f"Gata mestere",
                                      description=f"De acum folosesc <#{canal}> pentru a anunta cine a invitat pe cine. ",
                                      color=discord.Color.from_rgb(105, 105, 105))
                await ctx.send(embed=embed)
            except:
                await mesaj.delete()
                return
        else:
            def check1(reaction, user):
                return reaction.message.id == mesaj.id and user.id == ctx.author.id and (
                        str(reaction.emoji) == nu or str(reaction.emoji) == da)

            def check2(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

            embed = discord.Embed(title=f"Bun mestere",
                                  description=f"Te rog trimite un mesaj care contine **doar** canalul/id-ul canalului pe care vreti sa il folositi pentru informatii despre invitati. Exemplu: `#invites`",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.reply(embed=embed)
            msg = await self.client.wait_for('message', check=check2, timeout=120)
            pref = str(msg.content)
            await mesaj.delete()
            try:
                canal = re.search('<#(.+?)>', pref).group(1)
            except:
                canal = int(pref)
            await msg.delete()
            embed = discord.Embed(title=f"Hmmmmmmmmm",
                                  description=f"Sigur vrei sa setezi <#{canal}> ca si canal de invites? Voi pune aici membrii nou-intrati si informatii despre cine i-a invitat",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.send(embed=embed)
            nu = '⛔'
            da = '✅'
            await mesaj.add_reaction(da)
            await mesaj.add_reaction(nu)
            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
                if str(reaction.emoji) == nu:
                    raise Exception("nu")
                await mesaj.delete()
                data[f"invites{ctx.guild.id}"] = canal
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                embed = discord.Embed(title=f"Gata mestere",
                                      description=f"De acum folosesc <#{canal}> pentru a anunta cine a invitat pe cine.",
                                      color=discord.Color.from_rgb(105, 105, 105))
                await ctx.send(embed=embed)
            except:
                await mesaj.delete()
                return

    @commands.command(aliases=['setjoin', 'setleave', 'joinleave'])
    @commands.has_permissions(administrator=True)
    async def setjoinleave(self, ctx, channel=None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if channel is not None:
            try:
                canal = re.search('<#(.+?)>', channel).group(1)
            except AttributeError:
                canal = int(channel)
            embed = discord.Embed(title=f"Hmmmmmmmmm",
                                  description=f"Sigur vrei sa setezi <#{canal}> ca si canal de intrari-iesiri?",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.reply(embed=embed)
            nu = '⛔'
            da = '✅'
            await mesaj.add_reaction(da)
            await mesaj.add_reaction(nu)

            def check1(reaction, user):
                return reaction.message.id == mesaj.id and user.id == ctx.author.id and (
                        str(reaction.emoji) == nu or str(reaction.emoji) == da)

            def check2(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
                if str(reaction.emoji) == nu:
                    raise Exception("nu")
                await mesaj.delete()
                data[f"join{ctx.guild.id}"] = canal
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                embed = discord.Embed(title=f"Gata mestere",
                                      description=f"De acum anunt pe <#{canal}> cand iese/intra cineva.",
                                      color=discord.Color.from_rgb(105, 105, 105))
                await ctx.send(embed=embed)
            except:
                await mesaj.delete()
                return
        else:
            def check1(reaction, user):
                return reaction.message.id == mesaj.id and user.id == ctx.author.id and (
                        str(reaction.emoji) == nu or str(reaction.emoji) == da)

            def check2(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

            embed = discord.Embed(title=f"Bun mestere",
                                  description=f"Te rog trimite un mesaj care contine **doar** canalul/id-ul canalului pe care vreti sa il folositi ca join-leave. Exemplu: `#intra_voice`",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.reply(embed=embed)
            msg = await self.client.wait_for('message', check=check2, timeout=120)
            pref = str(msg.content)
            await mesaj.delete()
            try:
                canal = re.search('<#(.+?)>', pref).group(1)
            except:
                canal = int(pref)
            await msg.delete()
            embed = discord.Embed(title=f"Hmmmmmmmmm",
                                  description=f"Sigur vrei sa setezi <#{canal}> ca si canal de join-leave?",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.send(embed=embed)
            nu = '⛔'
            da = '✅'
            await mesaj.add_reaction(da)
            await mesaj.add_reaction(nu)
            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
                if str(reaction.emoji) == nu:
                    raise Exception("nu")
                await mesaj.delete()
                data[f"join{ctx.guild.id}"] = canal
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                embed = discord.Embed(title=f"Gata mestere",
                                      description=f"De acum anunt pe <#{canal}> cand iese/intra cineva.",
                                      color=discord.Color.from_rgb(105, 105, 105))
                await ctx.send(embed=embed)
            except:
                await mesaj.delete()
                return

    @commands.command(aliases=['setmembercount'])
    @commands.has_permissions(administrator=True)
    async def setcount(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        embed = discord.Embed(title=f"Vrei sa setezi canalul de membercount?",
                              description=f"Numele acestuia va fi schimbat periodic in numarul de membrii de pe server.",
                              color=discord.Color.from_rgb(105, 105, 105))
        mesaj = await ctx.reply(embed=embed)
        nu = '⛔'
        da = '✅'
        await mesaj.add_reaction(da)
        await mesaj.add_reaction(nu)

        def check1(reaction, user):
            return reaction.message.id == mesaj.id and user.id == ctx.author.id and (
                    str(reaction.emoji) == nu or str(reaction.emoji) == da)

        def check2(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
            if str(reaction.emoji) == nu:
                raise Exception("nu")
            await mesaj.delete()
            embed = discord.Embed(title=f"Bun mestere",
                                  description=f"Vrei sa se creeze automat un canal pentru voice sau stii sa faci singur? (+ sa iei id-ul canalului)\n\n✅-Fac automat (de preferat)\n⛔-Nu fac canal (daca alegi asta, va urma sa imi dai tu ping la canal sau id-ul canalului)",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.reply(embed=embed)
            await mesaj.add_reaction(da)
            await mesaj.add_reaction(nu)
            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=25, check=check1)
                if str(reaction.emoji) == nu:
                    raise Exception("nu")
                await mesaj.delete()
                chanal = await ctx.guild.create_voice_channel('Membrii: in curs de generare')
                data[f"voice{ctx.guild.id}"] = chanal.id
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                # embedd2 = discord.Embed(title=f"Gata mestere",description=f"Am setat canalul <#{chanal.id}> pentru voice intermediar. Poti schimba numele canalului, pozitia sau orice alta setare fara a avea probleme.\n\n*recomandam sa testati canalul pentru a vedea daca va place optiunea*",color=discord.Color.from_rgb(105, 105, 105))
                # mesaj = await ctx.send(embed=embedd2)
                # return
                embed = discord.Embed(title=f"Doresti sa folosesti un nume personalizat?",
                                      description=f"Numele prestabilit al canalului este |🌲| Membrii (exemplu: |🌲| Membrii: {ctx.guild.member_count}), insa il poti schimba dupa preferintele tale!",
                                      color=discord.Color.from_rgb(105, 105, 105))
                mesaj = await ctx.send(embed=embed)
                await mesaj.add_reaction(da)
                await mesaj.add_reaction(nu)
                try:
                    reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
                    if str(reaction.emoji) == nu:
                        raise Exception("nu")
                    await mesaj.delete()
                    embed = discord.Embed(title=f"Ce nume vrei sa aiba canalul?",
                                          description=f"Te rog trimite un mesaj ce contine numele (exemplu: Membrii acestui server)",
                                          color=discord.Color.from_rgb(105, 105, 105))
                    mesaj = await ctx.send(embed=embed)
                    msg = await self.client.wait_for('message', check=check2, timeout=120)
                    pref = str(msg.content)
                    await mesaj.delete()
                    embed = discord.Embed(title=f"Esti sigur de alegerea facuta?",
                                          description=f"Canalul tau se va numi {pref} (sub forma {pref}: {ctx.guild.member_count})",
                                          color=discord.Color.from_rgb(105, 105, 105))
                    mesaj = await ctx.send(embed=embed)
                    await mesaj.add_reaction(da)
                    await mesaj.add_reaction(nu)
                    try:
                        reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
                        if str(reaction.emoji) == nu:
                            raise Exception("nu")
                        await mesaj.delete()
                        data[f"count{ctx.guild.id}"] = int(chanal.id)
                        data[f"name{ctx.guild.id}"] = pref
                        with open("pad/data/data.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                            jsonFile.close()
                        embed = discord.Embed(title=f"S-a rezolvat!",
                                              description=f"In cateva momente vor fi actualizati membrii pe canalul {chanal.mention} (sub forma: {pref}: {ctx.guild.member_count}).",
                                              color=discord.Color.from_rgb(105, 105, 105))
                        await ctx.send(embed=embed)
                        return
                    except:
                        await mesaj.delete()
                        data[f"count{ctx.guild.id}"] = chanal.id
                        data[f"name{ctx.guild.id}"] = 0
                        with open("pad/data/data.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                            jsonFile.close()
                        embed = discord.Embed(title=f"S-a rezolvat!",
                                              description=f"In cateva momente vor fi actualizati membrii pe canalul {chanal.mention} (sub forma: |🌲| Membrii: 2000).",
                                              color=discord.Color.from_rgb(105, 105, 105))
                        await ctx.send(embed=embed)
                        return
                except:
                    await mesaj.delete()
                    return

            except Exception as ex:
                print(ex)
                pass
            embed = discord.Embed(title=f"Ok, hai sa setam canalul!",
                                  description=f"Te rog trimite un mesaj care contine canalul/id-ul canalului pe care vrei sa il folosesti. Exemplu: #membercount\n\n*recomandam ca acest canal sa fie unul vocal, special facut pentru membercount*",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.reply(embed=embed)
            msg = await self.client.wait_for('message', check=check2, timeout=120)
            pref = str(msg.content)
            await mesaj.delete()
            try:
                canal = re.search('<#(.+?)>', pref).group(1)
            except:
                canal = int(pref)
            await msg.delete()
            embed = discord.Embed(title=f"Hmmmmmmmmm",
                                  description=f"Sigur vrei sa setezi <#{canal}> ca si canal de afisare membercount? Numele acestuia va fi schimbat conform numarului de membrii.",
                                  color=discord.Color.from_rgb(105, 105, 105))
            mesaj = await ctx.send(embed=embed)
            nu = '⛔'
            da = '✅'
            await mesaj.add_reaction(da)
            await mesaj.add_reaction(nu)
            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
                if str(reaction.emoji) == nu:
                    raise Exception("nu")
                await mesaj.delete()
                embed = discord.Embed(title=f"Doresti sa folosesti un nume personalizat?",
                                      description=f"Numele prestabilit al canalului este |🌲| Membrii (exemplu: |🌲| Membrii: {ctx.guild.member_count}), insa il poti schimba dupa preferintele tale!",
                                      color=discord.Color.from_rgb(105, 105, 105))
                mesaj = await ctx.send(embed=embed)
                await mesaj.add_reaction(da)
                await mesaj.add_reaction(nu)
                try:
                    reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
                    if str(reaction.emoji) == nu:
                        raise Exception("nu")
                    await mesaj.delete()
                    embed = discord.Embed(title=f"Ce nume vrei sa aiba canalul?",
                                          description=f"Te rog trimite un mesaj ce contine numele (exemplu: Membrii acestui server)",
                                          color=discord.Color.from_rgb(105, 105, 105))
                    mesaj = await ctx.send(embed=embed)
                    msg = await self.client.wait_for('message', check=check2, timeout=120)
                    pref = str(msg.content)
                    await mesaj.delete()
                    embed = discord.Embed(title=f"Esti sigur de alegerea facuta?",
                                          description=f"Canalul tau se va numi {pref} (sub forma {pref}: {ctx.guild.member_count})",
                                          color=discord.Color.from_rgb(105, 105, 105))
                    mesaj = await ctx.send(embed=embed)
                    await mesaj.add_reaction(da)
                    await mesaj.add_reaction(nu)
                    try:
                        reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check1)
                        if str(reaction.emoji) == nu:
                            raise Exception("nu")
                        await mesaj.delete()
                        data[f"count{ctx.guild.id}"] = int(canal)
                        data[f"name{ctx.guild.id}"] = pref
                        with open("pad/data/data.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                            jsonFile.close()
                        embed = discord.Embed(title=f"S-a rezolvat!",
                                              description=f"In cateva momente vor fi actualizati membrii pe canalul selectat (sub forma: {pref}: {ctx.guild.member_count}).",
                                              color=discord.Color.from_rgb(105, 105, 105))
                        await ctx.send(embed=embed)
                    except:
                        await mesaj.delete()
                        data[f"count{ctx.guild.id}"] = canal
                        data[f"name{ctx.guild.id}"] = 0
                        with open("pad/data/data.json", "w") as jsonFile:
                            json.dump(data, jsonFile)
                            jsonFile.close()
                        embed = discord.Embed(title=f"S-a rezolvat!",
                                              description=f"In cateva momente vor fi actualizati membrii pe canalul selectat (sub forma: |🌲| Membrii: 2000).",
                                              color=discord.Color.from_rgb(105, 105, 105))
                        await ctx.send(embed=embed)
                        return
                except:
                    await mesaj.delete()
                    data[f"count{ctx.guild.id}"] = canal
                    data[f"name{ctx.guild.id}"] = 0
                    with open("pad/data/data.json", "w") as jsonFile:
                        json.dump(data, jsonFile)
                        jsonFile.close()
                    embed = discord.Embed(title=f"S-a rezolvat!",
                                          description=f"In cateva momente vor fi actualizati membrii pe canalul selectat (sub forma: |🌲| Membrii: 2000).",
                                          color=discord.Color.from_rgb(105, 105, 105))
                    await ctx.send(embed=embed)
                    return
            except:
                await mesaj.delete()
                return
        except Exception as ex:
            print(ex)
            await mesaj.delete()
            return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup(self, ctx, panel=None):
        if panel == None:
            embed = discord.Embed(title="Setup bot",
                                  description="Botul va ofera o serie de chestii de setat. Sunt total optionale, insa recomandate!",
                                  color=discord.Color.from_rgb(105, 105, 105))
            embed.add_field(name="Rulati `.setup general`", value="pentru a vedea sectiunea generala de setari\n\n",
                            inline=False)
            embed.add_field(name="Rulati `.setup fun`",
                            value="pentru a vedea sectiunea de setari a functiilor 'amuzante'\n\n", inline=False)
        elif "GENERAL" in panel.upper():
            embed = discord.Embed(title="Chestii generale de setat", description="",
                                  color=discord.Color.from_rgb(105, 105, 105))
            embed.add_field(name="Rulati `.setup importante`",
                            value="pentru a vedea setarile mai importante (prefix, sistem xp, reacyion roles, etc)",
                            inline=False)
            embed.add_field(name="Rulati `.setup canale`",
                            value="pentru a vedea setarile ce implica canale (logs, join-leave, membercount, invites, etc)",
                            inline=False)

        elif "IMPORTANT" in panel.upper():
            embed = discord.Embed(title="Chestii 'importante' de setat", description="",
                                  color=discord.Color.from_rgb(105, 105, 105))
            embed.add_field(name="Prefixul", value="""il puteti schimba cu comanda `.setprefix`
(prefixul standard este '.' sau <@885503634710884412> )""", inline=False)
            embed.add_field(name="Sistemul de XP",
                            value="""il puteti porni/opri cu ajutorul comenzii `.setxp`.\n*Membrii vor primi xp pe mesajele scrise si vor avea acces la comenzile .xp si .top.""",
                            inline=False)
            embed.add_field(name="Comanda `.setrol`",
                            value="E o extensie a sitemului xp. Folositi comanda pentru a recompensa membrii cu un numar mare de xp\n*Explicatii: daca setezi un rol creat de tine, spre exemplu* **Maestru** *pentru 100xp, toti membrii care vor atinge 100xp vor primi rolul de Maestru.*",
                            inline=False)
            embed.add_field(name="Reaction roles", value="""le puteti adauga in sistem cu comanda `.setreactionroles` (`.setreaction`). 
        *Puteti seta mesaje personalizate, cand cineva va reactiona cu un anumit emoji va primi un rol setat.*""",
                            inline=False)

        elif "CANAL" in panel.upper():
            embed = discord.Embed(title="Chestii ce contin canale de setat", description="",
                                  color=discord.Color.from_rgb(105, 105, 105))
            embed.add_field(name="Canalul de logs", value="""il puteti adauga in sistem cu comanda `.setlogs`. 
*Pe canalul de logs vor aparea: mesajele,sterse/editate, pozele si videoclipurile sterse, comenzile folosite, membrii intrati/ieșiți si multe altele.*""",
                            inline=False)
            embed.add_field(name="Canalul de intrari-iesiri", value="""il puteți adauga in sistem cu comanda `.setjoinleave`.
*Pe acest canal va aparea un mesaj cand intra sau iese un membru.*""", inline=False)
            embed.add_field(name="Canalul de invite-uri", value="""il puteți adauga in sistem cu comanda `.setinvites`.
*Pe acest canal va aparea un mesaj cand intra cine, plus informatii despre cine l-a invitat pe server.*""",
                            inline=False)
            embed.add_field(name="Un mesaj de întâmpinare pentru cei nou veniti", value="""il puteti adauga in sistem cu comanda `.setmesaj`.
*Membrii noi vor fi intampinati in privat și/sau pe un canal ales cu acel mesaj.*""", inline=False)
            embed.add_field(name="Canalul intermediar de voice", value="""il puteți adauga cu comanda `.setvoice`.
*Oricine va intra pe canalul vocal setat va fi mutat pe un alt canal personalizat (ex: membrul DENIS#5251 va fi mutat pe 'CANALUL LUI DENIS#5251'), avand mai multe permisiuni (rulează .help voice)*""",
                            inline=False)
            embed.add_field(name="Canalul de evidenta a membrilor", value="""il puteti adauga in sistem cu comanda `.setcount`/`.setmembercount`.
*Numele canalului va fi schimbat odata la ceva timp , conținând numarul de membrii aflati in server. (exemplu: `Membrii:200`)*""",
                            inline=False)
            embed.set_footer(
                text=f"Comenzile va ajuta la configurare, pentru orice neintelegeri, adresati-va fondatorilor bot-ului pe serverul de asistenta tehnica (comanda `.support `).")

        elif "FUN" in panel.upper() or "AMUZAMENT" in panel.upper():
            embed = discord.Embed(title="Chestii 'amuzante' de setat", description="",
                                  color=discord.Color.from_rgb(105, 105, 105))
            embed.add_field(name="Birthday (comanda `.setbirthday`)",
                            value="Botul contine comanda `.birthday` prin care membrii isi pot seta ziua de nastere.\nTu, ca si administrator al serverului poti sa le oferi un rol de sarbatorit (care va fi automat dat la inceputul zilei si scos in ziua urmatoare) si un canal pe care doriti ca botul sa ii trimita o urare.",
                            inline=False)

        embed.set_footer(
            text=f"Comenzile va ajuta la configurare, pentru orice neintelegeri, adresati-va fondatorilor bot-ului pe serverul de asistenta tehnica (comanda `.support `).")
        await ctx.reply(embed=embed)

    @commands.command(aliases=['suport'])
    async def support(self, ctx):
        try:
          guild = self.client.get_guild(619454105869352961)
          if int(guild.premium_subscription_count) < 30:
            embed = discord.Embed(title="Salut! Spune-ne ce e gresit pe serverul nostru! ",
                                  description="https://discord.gg/JatxtRC", color=default_color)
          else:
            embed = discord.Embed(title="Salut! Spune-ne ce e gresit pe serverul nostru! ",
                                  description="https://discord.gg/baneasa", color=default_color)
          await ctx.reply(embed=embed)
        except:
          embed = discord.Embed(title="Salut! Spune-ne ce e gresit pe serverul nostru! ",
                                  description="https://discord.gg/JatxtRC", color=default_color)
          await ctx.reply(embed=embed)
          

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mesajowneriservere(self, ctx, *, mesaj):
        if ctx.author.id != 852673995563597875:
            await ctx.reply("nu")
            return
        for guild in self.client.guilds:
            try:
                await guild.owner.send(mesaj)
            except:
                pass


async def setup(client):
    await client.add_cog(Setup(client))