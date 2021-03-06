import discord
import random
import json
import datetime
import asyncio
import re
from main import numeafk,motivafk,incaafk
from discord.ext import commands
from datetime import datetime


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            title="", description="", color=discord.Color.green())
        embed.add_field(name="Invita-ne botul pe serverul tau!",
                        value="[Click pentru invite](https://discord.com/oauth2/authorize?client_id=790607817128017920&scope=bot&permissions=8589934591)")
        await ctx.reply(embed=embed)

    @commands.command()
    async def embeds(self, ctx, id):
      mesajjee = await ctx.channel.history(limit=200).flatten()
      for mesaj in mesajjee:
        if mesaj.id==int(id):
          message = mesaj
      embeds = message.embeds
      for embed in embeds:
        emb=embed.to_dict()
        #print(emb)
        openinbrowser=emb['fields'][0]['value']
        print(openinbrowser)

    @commands.command(aliases=['invites','invitatii'])
    async def inviteuri(self, ctx,member:discord.Member = None):
      with open("pad/data/invites.json", "r") as jsonFile:
        invitedata = json.load(jsonFile)
        jsonFile.close()
      if member==None:
        member=ctx.author
      if f"{ctx.guild.id}invites{member.id}" in invitedata:
        intrari=int(invitedata[f"{ctx.guild.id}invites{member.id}"])
      else:
        intrari=0
      if f"{ctx.guild.id}iesiri{member.id}" in invitedata:
        iesiri=int(invitedata[f"{ctx.guild.id}iesiri{member.id}"])
      else:
        iesiri=0
      if f"{ctx.guild.id}fakeinvites{member.id}" in invitedata:
        fake=int(invitedata[f"{ctx.guild.id}fakeinvites{member.id}"])
      else:
        fake=0
      embed = discord.Embed(title="Invitatiile de pe acest server:", description=f"~\n\n*am executat comanda in {self.client.latency:.2f}ms, ai mai jos toate cele necesare!*\n\n~", color=discord.Color.green())
      embed.set_thumbnail(url=member.avatar_url)
      embed.set_footer(text=f"Cerut de {ctx.author} | generat de Padurar la Baneasa", icon_url=ctx.author.avatar_url)
      embed.add_field(name="Na domnule, ai:", value=f"??? **{intrari}** intrari\n??? **{iesiri}** iesiri\n???? **{fake}** false\n\n",inline=False)
      embed.add_field(name=f"**IN TOTAL AI {intrari-iesiri} INVITATII**", value=f"*felicitari?*",inline=False)
      await ctx.reply(embed=embed)


    @commands.command()
    async def afk(self, ctx, *, motiv=None):
      
      if len(str(ctx.author.display_name))>27:
        numar=27-len(str(ctx.author.display_name))
        nume="[AFK]"+str(ctx.author.display_name)[:-numar]
      else:
        nume="[AFK]"+str(ctx.author.display_name)

      motivafk[f"{ctx.guild.id}{ctx.author.id}"]=str(motiv)
      incaafk[f"{ctx.guild.id}{ctx.author.id}"]=1
      numeafk[f"{ctx.guild.id}{ctx.author.id}"]=str(ctx.author.display_name)
      await ctx.author.edit(nick=nume)
      
      embed = discord.Embed(title="Fa-ti treaba frate", description=f"Esti afk, daca te deranjeaza cineva il tai.", color=discord.Color.green())
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
            title="", description="", color=discord.Color.green())
        embed.add_field(name="Voteaza-ne botul!",
                        value="[Click pentru a vota!](https://top.gg/bot/885503634710884412)")#https://top.gg/bot/790607817128017920 pentru premii in padure
        await ctx.reply(embed=embed)

    @commands.command(aliases=['informatii', 'informa??ii'])
    async def info(self, ctx):
        embed = discord.Embed(
            title="Informatii utile(sau nu) despre bot", description="", color=discord.Color.green())
        membrii = 4200
        for g in self.client.guilds:
            membrii = membrii + len(g.members)
        embed.add_field(name="Data creeari botului:", value="21 Decembrie 2020")
        embed.add_field(name="Numar de utilizatori", value=membrii)
        embed.add_field(name="Numarul de servere pe care ma aflu:",
                        value=f"{30 + len(self.client.guilds)} la acest moment")
        embed.add_field(name="Server principal:", value="https://discord.gg/JatxtRC")
        embed.add_field(name="Link top.gg", value="[Click pentru a vota!](https://top.gg/bot/790607817128017920)")
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.reply(embed=embed)

    @commands.command()
    async def servere(self, ctx):
        await ctx.reply(f"Sunt in {30 + len(self.client.guilds)} servere")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def printdb(self, ctx, data):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        text = data[data]
        await ctx.reply(text)

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
            title="Numarul de ??mecheri in acest server",
            description=f"Yeah yeah adevaratul dababy zice ca sunt **{ctx.guild.member_count}** ??mecheri in padure la B??neasa.",
            color=discord.Color.green())
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
            title="", description="", color=discord.Color.green())
        embed.add_field(name="Avatar", value=f'{member}', inline=True)
        embed.set_image(url=member.avatar_url)
        await ctx.reply(embed=embed)

    @avatar.error
    async def avatar_error(self, ctx, error):
        embed = discord.Embed(title="", description="", color=discord.Color.green())
        embed.add_field(name="Foaie verde si-o lalea", value="N-ai acces in p*la mea", inline=True)
        await ctx.reply(embed=embed)

    @commands.command(aliases=['serveravatar'])
    async def savatar(self, ctx, member: discord.Member = None):
        embed = discord.Embed(
            title="", description="", color=discord.Color.green())
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
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(
            text=f"Cerut de {ctx.author}", icon_url=ctx.author.avatar_url)
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
            title="", description="", color=discord.Color.green())
        embed.add_field(
            name="Foaie verde si-o lalea",
            value=f'N-ai acces in p*la mea ',
            inline=True)
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def regulament(self, ctx):
        embed = discord.Embed(title=f"Regulament || Comenzi", description="""
??? .mute ??? Este folosit?? ??n cazul ??n care un membru ??ncalc?? regulamentul intern al acestui server, este setat ??n minute.
??? .unmute ??? ??i redai cuiva accessul de a putea conversa cu ceilal??i membri.
??? .ban ??? ??i privezi unui membru libertatea pe un termen determinat, permanent sau temporar.
??? .unban ??? ??i ??napoiezi cuiva accessul de a putea intra pe server.
??? .kick ??? Folosind aceast?? comand?? dai afar?? pe cineva de pe server.
??? .purge ??? ??tergi ultimele x mesaje de pe chat-ul pe care e??ti.
??? .addrole ???roleadd??? ??? Folosind aceast?? comand?? ??i adaugi un grad unui membru.
??? .removerole ???roleremove??? ??? Folosind aceast?? comand?? ??i sco??i un grad la alegerea ta, cuiva.
??? .accept ??? Cu ajutorul acestei comenzi accepti o sugestie.
??? .refuz ??? Cu ajutorul acesti comenzi refuzi o sugestie.
??????Pentru mai multe detalii despre comenzi, foloseste .help <numele comenzi>??????""", color=discord.Color.green())
        await ctx.author.send(embed=embed)
        embed = discord.Embed(title=f"Sanctiuni", description="""
 ???Neprezentarea la ??edin??a s??pt??m??nal?? obligatorie este interzis??.
Sanc??iune: 1 SW.
 ???Schimbare numelui f??r?? s?? anun??i este sanc??ionat?? cu 0,5 AV.
 ???Inactivitatea mai mare de 48h (nu scrii nimic pe orice chat) este sanc??ionat??.
Sanc??iune: 1 SW.
 ???Fraudarea raportului este sanc??ionat?? strict. 
Sanc??iune: 1 SW.
 ???Dac?? pe chat vei avea activitate mai mare de 72h (nu scrii nimic pe niciun chat) o s?? fi??i aspru sanc??iona??i.
Sanc??iune: REMOVE
 ?????n cazul ??n care ave??i f??cute mesajele complet dar bump-urile nu, o s?? fi??i sanc??iona??i cu Staff-Warn.
 ?????n cazul ??n care ave??i f??cute bump-urile complet dar mesajele nu, o s?? fi??i sanc??iona??i cu Staff-Warn.
 ???Prima s??pt??m??n?? ??n echipa STAFF-ului este de acomodare, o s?? evit??m s?? v?? sanc??ion??m.
 ???Echivalentul unui AV (Avertisment) este 0,5 puncte iar un SW (Staff-Warn) este egal cu 1 punct.
 ?????n momentul ??n care acumula??i 2/2 AV o s?? primi??i un SW iar AV-urile o s?? dispar??.
 ???Dac?? ave??i ocazia s?? acumula??i 3/3 puncte o s?? fi??i da??i afar?? din echip??.
 ???Dac?? ave??i o activitate mare este foarte posibil s?? v?? ??tergem din puncte, din bulinele negre.
  """, color=discord.Color.green())
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

    @commands.command(aliases=['evidenta', 'eviden????'])
    @commands.has_permissions(manage_messages=True)
    async def goals(self, ctx):
        embed = discord.Embed(title=f"Evidenta staff. Cum func??ioneaz?? si cum a fost creata?", description=f"""Salut, din c??te pute??i vedea, a fost implementat un nou sistem de verificare a activit????ii voastre, sistem prin care v?? vom putea contoriza at??t mesajele trimise de c??tre voi, c??t ??i bump-urile pe care voi le da??i pentru server. ??ns?? momentan nu este totul automatizat din motivul c?? nu avem un site care ne-ar putea ajut?? s?? ne facem un panel cu ajutorul c??ruia s?? avem totul automatizat.
   ??n fiecare duminic?? pana la ora 21:00 o s?? fie f??cut?? eviden??a, ceea ce ??nseamn?? ca xp-ul(activitatea pe chat), bump-urile si voturile vor fi calculate automat.
   Pentru fiecare grad ave??i c??te un raport pe care trebuie s?? ??l face??i s??pt??m??nal. Dac?? nu ??l face??i deloc ve??i fi sanc??iona??i cu SW (Staff-Warn) sau remove in unele cazuri, dac?? ??l face??i par??ial complet ve??i primi AV (Avertisment). Par??ial complet ??nsemn??nd c?? a??i f??cut mai putin de 95% din raportul complet. La dou?? AV-uri o s?? primi??i un SW iar la 3 SW o s?? primi??i remove.
   Eviden??a staff a fost creat?? ??n urm?? cu ceva timp, mai exact pe 27 decembrie ??n urma unor ample dezbateri intre Dani si Denis, crez??nd c?? o s?? fie o idee bun?? ??i chiar este.
   Explicatii rapide: `xp-ul` il c????tiga??i pe mesajele scrise pe general, folositi comanda .xp pentru a vedea cat xp aveti)
""", color=discord.Color.green())
        await ctx.author.send(embed=embed)
        embed = discord.Embed(title=f"Care-i raportul s??pt??m??nal?", description=f"""Raportul s??pt??m??nal const?? ??n activitate pe chat (mesaje) ??i ??n bump-urile acordate, fiind ??n felul urm??tor :

`Helper` : 5500 **xp**/s??pt??m??n??
`Moderator` : 4000 **xp**/s??pt??m??n??
`Administrator` : 3550 **xp**/s??pt??m??n??
  """, color=discord.Color.green())
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


def setup(client):
    client.add_cog(Info(client))