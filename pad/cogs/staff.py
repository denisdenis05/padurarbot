import discord
import random
import json
import os
import datetime
from discord.ext import commands
from discord.utils import get
from discord.ext import tasks
from datetime import datetime
from main import default_color

class Staff(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def remove(self, ctx, membru: discord.Member = None, *, motiv=None):
        if membru == None:
            await ctx.reply("????")
            return
        guild = ctx.guild
        unu = discord.utils.get(guild.roles, name='💣 | 1/3')
        doi = discord.utils.get(guild.roles, name='💣 | 2/3')
        staff = discord.utils.get(guild.roles, name='✴ | Discord Staff')
        helper = discord.utils.get(guild.roles, name='✴ | Helper')
        mod = discord.utils.get(guild.roles, name='✴ | Moderator')
        admin = discord.utils.get(guild.roles, name='✴ | Administrator')
        trial = discord.utils.get(guild.roles, name='✴ | Semi-Admin')
        stafflos = self.client.get_channel(787332862902665237)
        await membru.remove_roles(unu)
        await membru.remove_roles(doi)
        await membru.remove_roles(staff)
        await membru.remove_roles(helper)
        await membru.remove_roles(mod)
        await membru.remove_roles(admin)
        await membru.remove_roles(trial)
        embed = discord.Embed(title=f"Saracul", description=f"{membru.mention} are remove.",
                              color=default_color)
        await ctx.reply(embed=embed)
        if motiv == None:
            with open(f'pad/fisiere/stafflogs.txt', 'a+') as f:
                f.write(
                    f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year} {membru.name} - Remove | {motiv}" + "\n")
                await stafflos.send(f"""```
{membru.name} - remove | dababy
```""")
        else:
            with open(f'pad/fisiere/stafflogs.txt', 'a+') as f:
                f.write(
                    f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year} {membru.name} - Remove | {motiv}" + "\n")
                await stafflos.send(f"""```
{membru.name} - remove | {motiv}
```""")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def helper(self, ctx, membru: discord.Member = None):
        guild = ctx.guild
        if membru == None:
            await ctx.reply("???")
            return
        staff = discord.utils.get(guild.roles, name='✴ | Discord Staff')
        helper = discord.utils.get(guild.roles, name='✴ | Helper')
        stafflos = self.client.get_channel(787332862902665237)
        category = get(guild.categories, id=792354214449905714)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            membru: discord.PermissionOverwrite(view_channel=True, send_messages=False)
        }
        await membru.add_roles(staff)
        await membru.add_roles(helper)
        canalevidenta = await guild.create_text_channel(name=f" ╠✶┊{membru.name}", category=category,
                                                        overwrites=overwrites)
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        embed = discord.Embed(title="", description="", color=default_color)
        if f"{ctx.guild.id}XP{membru.id}" not in data:
            xp = 0
        else:
            xp = data[f"{ctx.guild.id}XP{membru.id}"]
        embed.add_field(name=f"Xp-ul lui {membru.name}:", value=f"{xp} XP")
        await canalevidenta.send(embed=embed)
        await ctx.reply(f"Gg {membru.mention}")
        with open(f'pad/fisiere/stafflogs.txt', 'a+') as f:
            f.write(
                f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year} {membru.name} - Helper | gg" + "\n")
            await stafflos.send(f"""```
{membru.name} - Helper | gg
```""")
        embed = discord.Embed(title=f"❗❗INSTRUIRE❗❗", description="""
`I.Conduita`
Helperii trebuie sa se comporte frumos cu toate persoanele, evitând cearta.
Cearta intre staff e interzisa 
.

`II.Atributii`
Aveți acces la:
-stergere mesaje
-pin mesaje
-comanda mute
-mute/move/disconnect (pe canalele vocale)
Helperii au atribuția de a tine chatul curat. In caz de cineva pune conținut nepotrivit, puteți șterge mesajul.
Aveți acces la comanda .mute, comandă ce ii limitează pe membrii din a scrie pe chat și/sau vorbi pe canalele vocale. 

Mute-ul se da de forma .mute timp motiv . Exemplu : .mute @Denis 😎  5m că e rău" ii va da mute 5 minute lui @denis pe motivul "e rău". 
La fiecare mute dat trebuie sa scrieți pe #╠✶┊dovezi-mute-ban║ numele, timpul motivul și un screenshot al motivului.
.

`III.Rapoarte și "obligatii"`
Fiecare membru staff are cate ceva de făcut. Pe lângă păstrarea staff-ului curat aveți:
-un număr de mesaje, de bump-uri si de voturi săptămânale (afișate prin comanda .evidenta)
-minisedinta obligatorie în fiecare duminică , pe #╠✶┊general-staff
-invite-uri (va invitați prietenii pe server) 

La finalul fiecărei săptămâni, la ședința discutam situația fiecărui membru staff. Dacă te descurci extrem de bine și ai multa activitate (mesaje+bumps+voturi+invite-uri), poți câștiga rolul de **StAfF oF tHe WeEk** , având șanse mai mari de a deveni moderator, eventual admin. 

DUPA CE CITITI ASTA, RULAȚI COMANDA `.regulament` si `.evidenta` PENTRU A AFLA MAI MULTE. (verificăm)

""", color=default_color)
        await membru.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def stafflogs(self, ctx):
        await ctx.author.send(file=discord.File("pad/fisiere/stafflogs.txt"))

    @commands.command(aliases=['statsstaff', 'kicks', 'bans', 'banuri', 'kickuri', 'muteuri', 'mutes'])
    @commands.has_permissions(manage_messages=True)
    async def staffstats(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if f"{ctx.guild.id}mutes{member.id}" not in data:
            mutes = 0
        else:
            mutes = int(data[f"{ctx.guild.id}mutes{member.id}"])
        if f"{ctx.guild.id}unmutes{member.id}" not in data:
            unmutes = 0
        else:
            unmutes = int(data[f"{ctx.guild.id}unmutes{member.id}"])
        if f"{ctx.guild.id}kicks{member.id}" not in data:
            kicks = 0
        else:
            kicks = int(data[f"{ctx.guild.id}kicks{member.id}"])
        if f"{ctx.guild.id}bans{member.id}" not in data:
            bans = 0
        else:
            bans = int(data[f"{ctx.guild.id}bans{member.id}"])
        embed = discord.Embed(title=f"Activitatea lui {member.display_name}",
                              description=f"*pe serverul {ctx.guild.name}", color=default_color)
        embed.add_field(name="Mute-uri date:", value=mutes, inline=True)
        embed.add_field(name="Unmute-uri date:", value=unmutes, inline=True)
        embed.add_field(name="Kick-uri date:", value=kicks, inline=True)
        embed.add_field(name="Ban-uri date:", value=bans, inline=True)
        await ctx.reply(embed=embed)

    @commands.command(aliases=['warn'])
    @commands.has_permissions(ban_members=True)
    async def staffwarn(self, ctx, membru: discord.Member = None, *, motiv=None):
        if membru == None:
            await ctx.reply("????")
            return
        guild = ctx.guild
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        zero = discord.utils.get(guild.roles, name='💣 | 0,5/3')
        unu = discord.utils.get(guild.roles, name='💣 | 1/3')
        unup = discord.utils.get(guild.roles, name='💣 | 1,5/3')
        doi = discord.utils.get(guild.roles, name='💣 | 2/3')
        doip = discord.utils.get(guild.roles, name='💣 | 2,5/3')
        sanctiuni = discord.utils.get(guild.roles, name='━━━━━━━━》 Sanctiuni《 ━━━━━━━━ ')
        staff = discord.utils.get(guild.roles, name='✴ | Discord Staff')
        helper = discord.utils.get(guild.roles, name='✴ | Helper')
        mod = discord.utils.get(guild.roles, name='✴ | Moderator')
        admin = discord.utils.get(guild.roles, name='✴ | Administrator')
        trial = discord.utils.get(guild.roles, name='✴ | Semi-Admin')
        sanctiuni = discord.utils.get(guild.roles, name='━━━━━━━━》 Sanctiuni《 ━━━━━━━━ ')
        stafflos = self.client.get_channel(787332862902665237)

        with open(f'pad/fisiere/warns/<@{membru.id}>.txt', 'a+') as f:
            if f"<@{membru.id}>" not in data:
                data[f"<@{membru.id}>"] = 1
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
            else:
                nr = float(data[f"<@{membru.id}>"]) + 1
                data[f"<@{membru.id}>"] = nr
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
            if motiv is not None:
                f.write(f"{motiv}" + "\n")
                embed = discord.Embed(title=f"F in chat", description=f"{membru.mention} are warn pe motivul {motiv}",
                                      color=default_color)
                await ctx.reply(embed=embed)
                with open(f'pad/fisiere/stafflogs.txt', 'a+') as f:
                    f.write(
                        f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year} {membru.name} - Warn | {motiv}" + "\n")
                await stafflos.send(f"""```
{membru.name} - Warn | {motiv}
```""")
            else:
                f.write(f"Warn fara motiv" + "\n")
                embed = discord.Embed(title=f"F in chat", description=f"{membru.mention} are warn",
                                      color=default_color)
                await ctx.reply(embed=embed)
                with open(f'pad/fisiere/stafflogs.txt', 'a+') as f:
                    f.write(
                        f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year} {membru.name} - Warn | dababy" + "\n")
                    await stafflos.send(f"""```
{membru.name} - Warn | asa a zis dababy
```""")
            if float(data[f"<@{membru.id}>"]) == 0.5:
                await membru.add_roles(sanctiuni)
                await membru.add_roles(zero)
            elif float(data[f"<@{membru.id}>"]) == 1:
                await membru.remove_roles(zero)
                await membru.add_roles(unu)
            elif float(data[f"<@{membru.id}>"]) == 1.5:
                await membru.remove_roles(zero)
                await membru.remove_roles(unu)
                await membru.add_roles(unup)
            elif float(data[f"<@{membru.id}>"]) == 2:
                await membru.remove_roles(zero)
                await membru.remove_roles(unu)
                await membru.remove_roles(unup)
                await membru.add_roles(doi)
            elif float(data[f"<@{membru.id}>"]) == 2.5:
                await membru.remove_roles(zero)
                await membru.remove_roles(unu)
                await membru.remove_roles(unup)
                await membru.remove_roles(doi)
                await membru.add_roles(doip)
            elif float(data[f"<@{membru.id}>"]) == 3:
                await ctx.reply(f"{membru.mention} are 3 staff warns, luati-va papa.")
                await membru.remove_roles(doip)
                await membru.remove_roles(doi)
                await membru.remove_roles(staff)
                await membru.remove_roles(helper)
                await membru.remove_roles(sanctiuni)
                await membru.remove_roles(mod)
                await membru.remove_roles(admin)
                await membru.remove_roles(trial)
                data[f"<@{membru.id}>"] = 0
                f.truncate(0)
                os.remove(f"pad/fisiere/warns/<@{membru.id}>.txt")
                await stafflos.send(f"""```
{membru.name} - remove | 3 warn-uri
```""")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def avertisment(self, ctx, membru: discord.Member = None, *, motiv=None):
        if membru == None:
            await ctx.reply("????")
            return
        guild = ctx.guild
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        zero = discord.utils.get(guild.roles, name='💣 | 0,5/3')
        unu = discord.utils.get(guild.roles, name='💣 | 1/3')
        unup = discord.utils.get(guild.roles, name='💣 | 1,5/3')
        doi = discord.utils.get(guild.roles, name='💣 | 2/3')
        doip = discord.utils.get(guild.roles, name='💣 | 2,5/3')
        sanctiuni = discord.utils.get(guild.roles, name='━━━━━━━━》 Sanctiuni《 ━━━━━━━━ ')
        sanctiuni = discord.utils.get(guild.roles, name='━━━━━━━━》 Sanctiuni《 ━━━━━━━━ ')
        staff = discord.utils.get(guild.roles, name='✴ | Discord Staff')
        helper = discord.utils.get(guild.roles, name='✴ | Helper')
        mod = discord.utils.get(guild.roles, name='✴ | Moderator')
        admin = discord.utils.get(guild.roles, name='✴ | Administrator')
        trial = discord.utils.get(guild.roles, name='✴ | Semi-Admin')
        stafflos = self.client.get_channel(787332862902665237)
        sanctiuni = discord.utils.get(guild.roles, name='━━━━━━━━》 Sanctiuni《 ━━━━━━━━ ')

        with open(f'pad/fisiere/warns/<@{membru.id}>.txt', 'a+') as f:
            if f"<@{membru.id}>" not in data:
                data[f"<@{membru.id}>"] = 0.5
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
            else:
                nr = float(data[f"<@{membru.id}>"]) + 0.5
                data[f"<@{membru.id}>"] = nr
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
            if motiv is not None:
                nrr = float(data[f"<@{membru.id}>"])
                if nrr == 1 or nrr == 2 or nrr == 3:
                    f.write(f"2 averismente" + "\n")
                embed = discord.Embed(title=f"F in chat", description=f"{membru.mention} are warn pe motivul {motiv}",
                                      color=default_color)
                await ctx.reply(embed=embed)
                with open(f'pad/fisiere/stafflogs.txt', 'a+') as f:
                    f.write(
                        f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year} {membru.name} - avertisment | {motiv}" + "\n")
                    await stafflos.send(f"""```
{membru.name} - Av | {motiv}
```""")
            else:
                nrr = float(data[f"<@{membru.id}>"])
                if nrr == 1 or nrr == 2 or nrr == 3:
                    f.write(f"2 averismente" + "\n")
                embed = discord.Embed(title=f"F in chat", description=f"{membru.mention} are un avertisment",
                                      color=default_color)
                await ctx.reply(embed=embed)
                with open(f'pad/fisiere/stafflogs.txt', 'a+') as f:
                    f.write(
                        f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year} {membru.name} - Avertisment | dababy " + "\n")
                    await stafflos.send(f"""```
{membru.name} - Av | asa a zis dababy
```""")
            if float(data[f"<@{membru.id}>"]) == 0.5:
                await membru.add_roles(sanctiuni)
                await membru.add_roles(zero)
            elif float(data[f"<@{membru.id}>"]) == 1:
                await membru.remove_roles(zero)
                await membru.add_roles(unu)
            elif float(data[f"<@{membru.id}>"]) == 1.5:
                await membru.remove_roles(zero)
                await membru.remove_roles(unu)
                await membru.add_roles(unup)
            elif float(data[f"<@{membru.id}>"]) == 2:
                await membru.remove_roles(zero)
                await membru.remove_roles(unu)
                await membru.remove_roles(unup)
                await membru.add_roles(doi)
            elif float(data[f"<@{membru.id}>"]) == 2.5:
                await membru.remove_roles(zero)
                await membru.remove_roles(unu)
                await membru.remove_roles(unup)
                await membru.remove_roles(doi)
                await membru.add_roles(doip)
            elif float(data[f"<@{membru.id}>"]) == 3:
                await ctx.reply(f"{membru.mention} are 3 staff warns, luati-va papa.")
                await membru.remove_roles(doip)
                await membru.remove_roles(doi)
                await membru.remove_roles(staff)
                await membru.remove_roles(helper)
                await membru.remove_roles(sanctiuni)
                await membru.remove_roles(mod)
                await membru.remove_roles(admin)
                await membru.remove_roles(trial)
                data[f"<@{membru.id}>"] = 0
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                f.truncate(0)
                os.remove(f"<@{membru.id}>.txt")
                await stafflos.send(f"""```
{membru.name} - remove | 3 warn-uri
```""")

    @commands.command(aliases=['startcereri', 'deschidecereri', 'cereristaf', 'stopcereri', 'cereristaff'])
    @commands.has_permissions(administrator=True)
    async def cereri(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if "cererideschise" not in data or data["cererideschise"] == 0:
            data["cererideschise"] = 1;
            await ctx.reply("am deschis cererile, comanda /cerere poate fi folosita")
        else:
            data["cererideschise"] = 0
            await ctx.reply("am inchis cererile, comanda /cerere NU MAI POATE fi folosita")
        with open("pad/data/data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
            jsonFile.close()

    @commands.command(aliases=['warndelete', 'delwarn', 'delwarns'])
    @commands.has_permissions(administrator=True)
    async def warndel(self, ctx, membru: discord.Member):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        guild = ctx.guild
        zero = discord.utils.get(guild.roles, name='💣 | 0,5/3')
        unu = discord.utils.get(guild.roles, name='💣 | 1/3')
        unup = discord.utils.get(guild.roles, name='💣 | 1,5/3')
        doi = discord.utils.get(guild.roles, name='💣 | 2/3')
        doip = discord.utils.get(guild.roles, name='💣 | 2,5/3')
        sanctiuni = discord.utils.get(guild.roles, name='━━━━━━━━》 Sanctiuni《 ━━━━━━━━')
        if membru == None:
            await ctx.reply("???")
            return
        await membru.remove_roles(zero)
        await membru.remove_roles(unu)
        await membru.remove_roles(unup)
        await membru.remove_roles(doi)
        await membru.remove_roles(doip)
        await membru.remove_roles(sanctiuni)
        with open(f'pad/fisiere/warns/<@{membru.id}>.txt', 'a+') as f:
            if f"<@{membru.id}>" not in data or float(data[f"<@{membru.id}>"]) == 0:
                embed = discord.Embed(title=f"Nah", description=f"{membru.mention} n-are warn-uri",
                                      color=default_color)
                await ctx.reply(embed=embed)
            else:
                f.truncate(0)
                data[f"<@{membru.id}>"] = 0
                with open("pad/data/data.json", "w") as jsonFile:
                    json.dump(data, jsonFile)
                    jsonFile.close()
                embed = discord.Embed(title=f"Ok bos", description=f"{membru.mention} e curat",
                                      color=default_color)
                await ctx.reply(embed=embed)
                os.remove(f"pad/fisiere/warns/<@{membru.id}>.txt")

    @commands.command(aliases=['warns'])
    @commands.has_permissions(administrator=True)
    async def staffwarns(self, ctx, membru: discord.Member = None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if membru == None:
            membru = ctx.author
        with open(f'pad/fisiere/warns/<@{membru.id}>.txt', 'r') as f:
            if f"<@{membru.id}>" not in data or float(data[f"<@{membru.id}>"]) == 0:
                embed = discord.Embed(title=f"Nah", description=f"{membru.mention} n-are warn-uri",
                                      color=default_color)
                await ctx.reply(embed=embed)
            else:
                warns = float(data[f"<@{membru.id}>"])
                embed = discord.Embed(title=f"{membru} are {warns} warn-uri", description="",
                                      color=default_color)
                embed.add_field(name="Warn-uri:", value=f.read())
                await ctx.reply(embed=embed)

    @staffwarns.error
    async def staffwarns_error(self, ctx, error):
        await ctx.reply("Ceva n-a mers bine, probabil n-are warn-uri ")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def warnlist(self, ctx):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        match_keys = {key: val for key, val in data.items()
                      if key.startswith("<@")}
        embed = discord.Embed(title="Warn-urile din acest server", description="", color=default_color)
        lenght = 0
        for k in match_keys:
            if float(data[k]) != 0:
                lenght = int(lenght) + 1
        if int(lenght) == 0:
            embed = discord.Embed(title="Gg tuturor", description="Nu-s warnuri", color=default_color)
            await ctx.reply(embed=embed)
            return
        for k in match_keys:
            if int(data[k]) != 0:
                embed.add_field(name="Membrul:", value=f"{k}, {float(data[k])} warn-uri")
        await ctx.reply(embed=embed)


async def setup(client):
    await client.add_cog(Staff(client))