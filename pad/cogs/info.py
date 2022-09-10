import discord
import random
import json
import datetime
import asyncio
import re
from discord.ext import commands
from datetime import datetime
from discord import Spotify
from main import numeafk, motivafk, incaafk
from main import default_color

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(name="Invita-ne botul pe serverul tau!",
                        value="[Click pentru invite](https://discord.com/oauth2/authorize?client_id=790607817128017920&scope=bot&permissions=8589934591)")
        await ctx.reply(embed=embed)

    @commands.command()
    async def embeds(self, ctx, id):
        mesajjee = await ctx.channel.history(limit=200).flatten()
        for mesaj in mesajjee:
            if mesaj.id == int(id):
                message = mesaj
        embeds = message.embeds
        for embed in embeds:
            emb = embed.to_dict()
            # print(emb)
            openinbrowser = emb['fields'][0]['value']
            print(openinbrowser)

    @commands.command(aliases=['invites', 'invitatii'])
    async def inviteuri(self, ctx, member: discord.Member = None):
        with open("pad/data/invites.json", "r") as jsonFile:
            invitedata = json.load(jsonFile)
            jsonFile.close()
        if member == None:
            member = ctx.author
        if f"{ctx.guild.id}invites{member.id}" in invitedata:
            intrari = int(invitedata[f"{ctx.guild.id}invites{member.id}"])
        else:
            intrari = 0
        if f"{ctx.guild.id}iesiri{member.id}" in invitedata:
            iesiri = int(invitedata[f"{ctx.guild.id}iesiri{member.id}"])
        else:
            iesiri = 0
        if f"{ctx.guild.id}fakeinvites{member.id}" in invitedata:
            fake = int(invitedata[f"{ctx.guild.id}fakeinvites{member.id}"])
        else:
            fake = 0
        embed = discord.Embed(title="Invitatiile de pe acest server:",
                              description=f"~\n\n*am executat comanda in {self.client.latency:.2f}ms, ai mai jos toate cele necesare!*\n\n~",
                              color=default_color)
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"Cerut de {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.add_field(name="Na domnule, ai:",
                        value=f"✅ **{intrari}** intrari\n⛔ **{iesiri}** iesiri\n🚮 **{fake}** false\n\n", inline=False)
        embed.add_field(name=f"**IN TOTAL AI {intrari - iesiri} INVITATII**", value=f"*felicitari?*", inline=False)
        await ctx.reply(embed=embed)

    @commands.command()
    async def cover(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        ok = 0
        for activity in member.activities:
            if isinstance(activity, Spotify):
                ok = 1
                embed = discord.Embed(
                    title=f"Ce asculta {member.name}",
                    description=f"**{activity.title}** de **{activity.artist}**",
                    color=0x1DB954)
                embed.set_image(url=activity.album_cover_url)
                embed.set_footer(text=member,
                                 icon_url="https://media.discordapp.net/attachments/920425074882904104/1001178951168839765/spotify-logo-png-7053.png")
                await ctx.send(embed=embed)
        if ok == 0:
            embed = discord.Embed(
                title=f"{member.name} nu asculta nimic.",
                description="nasol",
                color=0x1DB954)
            embed.set_thumbnail(
                url="https://media.discordapp.net/attachments/920425074882904104/1001178951168839765/spotify-logo-png-7053.png")
            await ctx.send(embed=embed)

    @commands.command(aliases=['track', 'melodie', 'muzica', 'spotif'])
    async def spotify(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        ok = 0
        for activity in member.activities:
            if isinstance(activity, Spotify):
                ok = 1
                embed = discord.Embed(
                    title=f"Ce asculta {member.name}",
                    description=activity.title,
                    color=0x1DB954)
                embed.set_thumbnail(url=activity.album_cover_url)
                embed.add_field(name="Artist", value=activity.artist)
                embed.add_field(name="Album", value=activity.album)
                embed.set_footer(text=member,
                                 icon_url="https://media.discordapp.net/attachments/920425074882904104/1001178951168839765/spotify-logo-png-7053.png")
                await ctx.send(embed=embed)
        if ok == 0:
            embed = discord.Embed(
                title=f"{member.name} nu asculta nimic.",
                description="nasol",
                color=0x1DB954)
            embed.set_thumbnail(
                url="https://media.discordapp.net/attachments/920425074882904104/1001178951168839765/spotify-logo-png-7053.png")
            await ctx.send(embed=embed)

    @commands.command()
    async def afk(self, ctx, *, motiv=None):

        if len(str(ctx.author.display_name)) > 27:
            numar = 27 - len(str(ctx.author.display_name))
            nume = "[AFK]" + str(ctx.author.display_name)[:-numar]
        else:
            nume = "[AFK]" + str(ctx.author.display_name)

        motivafk[f"{ctx.guild.id}{ctx.author.id}"] = str(motiv)
        incaafk[f"{ctx.guild.id}{ctx.author.id}"] = 1
        numeafk[f"{ctx.guild.id}{ctx.author.id}"] = str(ctx.author.display_name)
        await ctx.author.edit(nick=nume)

        embed = discord.Embed(title="Fa-ti treaba frate", description=f"Esti afk, daca te deranjeaza cineva il tai.",
                              color=default_color)
        embed.set_footer(text="Cand te intorci iti scot automat afk-ul.")
        embed.set_thumbnail(url="https://i.pinimg.com/564x/26/04/37/260437648bf92a03527a7f624741056d.jpg")
        await ctx.reply(embed=embed)

    @commands.command()
    async def id(self, ctx):
        if ctx.message.reference is not None:
            await ctx.reply(ctx.message.reference.message_id)

    @commands.command(aliases=['vot'])
    async def vote(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(name="Voteaza-ne botul!",
                        value="[Click pentru a vota!](https://top.gg/bot/885503634710884412)")  # https://top.gg/bot/790607817128017920 pentru premii in padure
        await ctx.reply(embed=embed)

    @commands.command(aliases=['informatii', 'informații'])
    async def info(self, ctx):
        embed = discord.Embed(
            title="Informatii utile(sau nu) despre bot", description="", color=default_color)
        membrii = 4200
        for g in self.client.guilds:
            membrii = membrii + len(g.members)
        embed.add_field(name="Data creeari botului:", value="21 Decembrie 2020")
        embed.add_field(name="Numar de utilizatori", value=membrii)
        embed.add_field(name="Numarul de servere pe care ma aflu:",
                        value=f"{30 + len(self.client.guilds)} la acest moment")
        embed.add_field(name="Server principal:", value="https://discord.gg/JatxtRC")
        embed.add_field(name="Link top.gg", value="[Click pentru a vota!](https://top.gg/bot/790607817128017920)")
        embed.set_thumbnail(url=self.client.user.avatar.url)
        await ctx.reply(embed=embed)

    @commands.command()
    async def servere(self, ctx):
        await ctx.reply(f"Sunt in {30 + len(self.client.guilds)} servere")

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def setdb(self, ctx, db, value):
        if ctx.author.id == 852673995563597875:
            with open("pad/data/data.json", "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()
            try:
                value = int(value)
            except:
                pass
            data[db] = value
            await ctx.reply("ok");
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def printdb(self, ctx, db):
        if ctx.author.id == 852673995563597875:
            with open("pad/data/data.json", "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()
            await ctx.reply(data[db])
            with open("pad/data/data.json", "w") as jsonFile:
                json.dump(data, jsonFile)
                jsonFile.close()

    @commands.command()
    async def realservere(self, ctx):
        await ctx.reply(f"Sunt in {len(self.client.guilds)} servere")

    @commands.command()
    async def listaservere(self, ctx):
        servere = self.client.guilds
        lista = ""
        for k in servere:
            canale = k.text_channels
            for b in canale:
                canal = b
                break
            try:
                invite = await canal.create_invite()
            except:
                invite = ""
            lista = lista + f"{k.name} <{invite}>\n"
        await ctx.reply(lista)

    @commands.command()
    async def test(self, ctx):
        await ctx.reply("Aici sunt bos")

    @commands.command()
    async def guildid(self, ctx):
        await ctx.reply(ctx.guild.id)

    @commands.command(aliases=['membri', 'membrecount', 'membercout', 'membrii'])
    async def membercount(self, ctx):
        embed = discord.Embed(
            title="Numarul de șmecheri in acest server",
            description=f"Yeah yeah adevaratul dababy zice ca sunt **{ctx.guild.member_count}** șmecheri in padure la Băneasa.",
            color=default_color)
        await ctx.reply(embed=embed)

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        if ctx.guild.id == 619454105869352961:
            rol20 = ctx.guild.get_role(735514211580510240)
            if rol20 not in ctx.author.roles:
                ctx.eroare()
        if member.id == 790607817128017920:
            await ctx.reply("Chiar vrei sa ma vezi la fata?")
            await asyncio.sleep(5)
            await ctx.reply(f"Na bine {ctx.author.mention}, uite-ma")
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(name="Avatar", value=f'{member}', inline=True)
        embed.set_image(url=member.avatar.url)
        await ctx.reply(embed=embed)

    @avatar.error
    async def avatar_error(self, ctx, error):
        embed = discord.Embed(title="", description="", color=default_color)
        embed.add_field(name="Foaie verde si-o lalea", value="N-ai acces in p*la mea", inline=True)
        await ctx.reply(embed=embed)

    @commands.command(aliases=['serveravatar'])
    async def savatar(self, ctx, member: discord.Member = None):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(name="Server avatar", value="Asta e avatarul serverului", inline=True)
        embed.set_image(url=ctx.guild.icon_url)
        await ctx.reply(embed=embed)

    @commands.command()
    async def whois(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.message.author
        if ctx.guild.id == 619454105869352961:
            rol50 = ctx.guild.get_role(793924431566077953)
            if rol50 not in ctx.author.roles:
                ctx.eroaree
        roles = [role for role in member.roles]
        embed = discord.Embed(
            colour=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f'Informatii  despre {member}')
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(
            text=f"Cerut de {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Nume", value=member.display_name)
        embed.add_field(
            name="Prima conectare :",
            value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(
            name="Data intrarii pe server :  ",
            value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(
            name=f"Grade({len(roles)})",
            value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Cel mai rol:", value=member.top_role.mention)
        await ctx.reply(embed=embed)

    @whois.error
    async def whois_error(self, ctx, error):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Foaie verde si-o lalea",
            value=f'N-ai acces in p*la mea ',
            inline=True)
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def regulament(self, ctx):
        embed = discord.Embed(title=f"Regulament || Comenzi", description="""
➤ .mute ➣ Este folosită în cazul în care un membru încalcă regulamentul intern al acestui server, este setat în minute.
➤ .unmute ➣ Îi redai cuiva accessul de a putea conversa cu ceilalți membri.
➤ .ban ➣ Îi privezi unui membru libertatea pe un termen determinat, permanent sau temporar.
➤ .unban ➣ Îi înapoiezi cuiva accessul de a putea intra pe server.
➤ .kick ➣ Folosind această comandă dai afară pe cineva de pe server.
➤ .purge ➣ Ștergi ultimele x mesaje de pe chat-ul pe care ești.
➤ .addrole 《roleadd》 ➣ Folosind această comandă îi adaugi un grad unui membru.
➤ .removerole 《roleremove》 ➣ Folosind această comandă îi scoți un grad la alegerea ta, cuiva.
➤ .accept ➣ Cu ajutorul acestei comenzi accepti o sugestie.
➤ .refuz ➣ Cu ajutorul acesti comenzi refuzi o sugestie.
〖〗Pentru mai multe detalii despre comenzi, foloseste .help <numele comenzi>〖〗""", color=default_color)
        await ctx.author.send(embed=embed)
        embed = discord.Embed(title=f"Sanctiuni", description="""
 ➤Neprezentarea la ședința săptămânală obligatorie este interzisă.
Sancțiune: 1 SW.
 ➤Schimbare numelui fără să anunți este sancționată cu 0,5 AV.
 ➤Inactivitatea mai mare de 48h (nu scrii nimic pe orice chat) este sancționată.
Sancțiune: 1 SW.
 ➤Fraudarea raportului este sancționată strict. 
Sancțiune: 1 SW.
 ➤Dacă pe chat vei avea activitate mai mare de 72h (nu scrii nimic pe niciun chat) o să fiți aspru sancționați.
Sancțiune: REMOVE
 ➤În cazul în care aveți făcute mesajele complet dar bump-urile nu, o să fiți sancționați cu Staff-Warn.
 ➤În cazul în care aveți făcute bump-urile complet dar mesajele nu, o să fiți sancționați cu Staff-Warn.
 ➤Prima săptămână în echipa STAFF-ului este de acomodare, o să evităm să vă sancționăm.
 ➤Echivalentul unui AV (Avertisment) este 0,5 puncte iar un SW (Staff-Warn) este egal cu 1 punct.
 ➤În momentul în care acumulați 2/2 AV o să primiți un SW iar AV-urile o să dispară.
 ➤Dacă aveți ocazia să acumulați 3/3 puncte o să fiți dați afară din echipă.
 ➤Dacă aveți o activitate mare este foarte posibil să vă ștergem din puncte, din bulinele negre.
  """, color=default_color)
        await ctx.author.send(embed=embed)
        copac = get(ctx.guild.emojis, name='pd_ranjit')
        await ctx.message.add_reaction(copac)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def channelid(self, ctx, *, channel):
        try:
            canal = re.search('<#(.+?)>', channel).group(1)
        except AttributeError:
            canal = re.search('<@&(.+?)>', channel).group(1)
        await ctx.reply(canal)

    @commands.command(aliases=['evidenta', 'evidență'])
    @commands.has_permissions(manage_messages=True)
    async def goals(self, ctx):
        embed = discord.Embed(title=f"Evidenta staff. Cum funcționează si cum a fost creata?", description=f"""Salut, din câte puteți vedea, a fost implementat un nou sistem de verificare a activității voastre, sistem prin care vă vom putea contoriza atât mesajele trimise de către voi, cât și bump-urile pe care voi le dați pentru server. Însă momentan nu este totul automatizat din motivul că nu avem un site care ne-ar putea ajută să ne facem un panel cu ajutorul căruia să avem totul automatizat.
   În fiecare duminică pana la ora 21:00 o să fie făcută evidența, ceea ce înseamnă ca xp-ul(activitatea pe chat), bump-urile si voturile vor fi calculate automat.
   Pentru fiecare grad aveți câte un raport pe care trebuie să îl faceți săptămânal. Dacă nu îl faceți deloc veți fi sancționați cu SW (Staff-Warn) sau remove in unele cazuri, dacă îl faceți parțial complet veți primi AV (Avertisment). Parțial complet însemnând că ați făcut mai putin de 95% din raportul complet. La două AV-uri o să primiți un SW iar la 3 SW o să primiți remove.
   Evidența staff a fost creată în urmă cu ceva timp, mai exact pe 27 decembrie în urma unor ample dezbateri intre Dani si Denis, crezând că o să fie o idee bună și chiar este.
   Explicatii rapide: `xp-ul` il câștigați pe mesajele scrise pe general, folositi comanda .xp pentru a vedea cat xp aveti)
""", color=default_color)
        await ctx.author.send(embed=embed)
        embed = discord.Embed(title=f"Care-i raportul săptămânal?", description=f"""Raportul săptămânal constă în activitate pe chat (mesaje) și în bump-urile acordate, fiind în felul următor :

`Helper` : 5500 **xp**/săptămână
`Moderator` : 4000 **xp**/săptămână
`Administrator` : 3550 **xp**/săptămână
  """, color=default_color)
        await ctx.author.send(embed=embed)
        copac = get(ctx.guild.emojis, name='pd_ranjit')
        await ctx.message.add_reaction(copac)

    @commands.command()
    async def shutdown(self, ctx):
        if ctx.message.author.id == 852673995563597875:
            print("shutdown")
            try:
                await self.bot.logout()
            except:
                print("EnvironmentError")
                self.bot.clear()
        else:
            await ctx.send("You do not own this bot!")


async def setup(client):
    await client.add_cog(Info(client))