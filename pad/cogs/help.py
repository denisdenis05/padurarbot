import discord
import random
from discord.ext import commands
from main import default_color
from discord.ui import Button, View

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True, aliases=['ajutor'])
    async def help(self, ctx):
        embed = discord.Embed(
            title="Comenzi", description="", color=default_color)
        embed.add_field(name="Admin", value="Categorie pentru comenzile staffului", inline=True)
        embed.add_field(name="Utile", value="Categorie pentru comenzile utile", inline=True)
        embed.add_field(name="Set", value="Categorie pentru comenzile de setare a botului (pentru ownerii serverului)",
                        inline=True)
        embed.add_field(name="haZz", value="Categorie pentru comenzile amuzante", inline=True)
        # embed.add_field(name="Admin",value="`addrole`, `adminspune`, `announcement`, `ban`, `goals`, `helper`, `kick`, `mute`, `purge`, `regulament`, `remove`, `removerole`, `searchpurge`,  `setnick`, `softban`, `unban`, `unmute`",inline=True)
        # embed.add_field(name="Utilitati",value="`avatar`, `editsnipe`, `purge`, `random`, `invite`, `serveravatar`, `slowmode`, `snipe`, `xp`, `top`, `servere`, `membercount`, `bumps`, `topbumps`,`whois`",inline=True)
        # embed.add_field(name="Setup",value="`setup`, `prefix`, `setjoinleave`, `setlogs`, `setmembercount`, `setmute`, `setvoice`",inline=True)
        # embed.add_field(name="Amuzament",value="`birthday`, `cuddle`, `divort`, `facebook`, `fraier`, `gay`, `howgay`, `casatorie`, `party`, `pp`, `pup`, `ship`, `simp`, `sot`, `spune`, `tembel`, `wanted`, `imbratisare`, `palmă`, `limbă`, `supremacy`,`clan`",inline=True)
        embed.set_footer(text=f"Apasa pe butoanele de mai jos pentru mai multe informatii despre o categorie")
        view = View()    
        view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="admin",label="Admin"))
        view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="setup",label="Set"))
        view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="utilitati",label="Utile"))
        view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,custom_id="amuzament",label="haZz"))
        await ctx.reply(embed=embed, view=view)

    @help.command(aliases=['vocal', 'Voice'])
    async def voice(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(name="Comenzile voice", value="""Intra pe canalul INTRA AICI pentru a iti face un canal vocal temporar.

**.voice limit [numar]** e o comanda care limitează numărul de persoane de pe un canal vocal. 
Ex: .voice limit 3.
**.voice lock/unlock** e o comanda care blochează sau deblocheaza canalul. Odata blocat, nimeni nu mai poate intra. Deblocat, orice membru are acces la canalul vocal.
**.voice permit/deny [user]** e o comanda ce permite sau nu unei persoane sa intre pe vocal. 
Ex.voice permit @rnmdenis
.voice deny @rnmdenis
**.voice name [nume]** e o comanda cu care iti schimbi numele canalului.
Ex:.voice name Cangur
**.voice claim** e o comanda pentru cei care vor control asupra unui canal. Daca cel care a făcut canalul vocal a iesit, puteți utiliza toate comenzile de mai sus (după ce folositi .voice claim)
	""")
        await ctx.reply(embed=embed)

    @help.command()
    async def purge(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .purge",
            value=
            """Descriere: Ștergi ultimele x mesaje de pe chat-ul pe care ești.
    Folosire: .purge [nr. mesaje]
    Exemplu:
    .purge 7""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def afk(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .afk",
            value=
            """Descriere: Anunti ca esti afk. Toata lumea care iti va da ping va fi anuntata ca esti ocupat
    Folosire: .afk [motiv]
    Exemplu:
    .afk Merg sa comit crime de razboi in Slatina""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def mute(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .mute",
            value=
            """Descriere: Este folosită în cazul în care un membru încalcă regulamentul intern al acestui server, este setat în minute.
    Folosire: .mute [nume] [timpul sancțiunii+u.m.] [motiv]
    Exemplu:
       .mute @Optimus Prime 5m Spam
       .mute @lil dani nbn de la kuweit nmw 7s injurii""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def clan(self, ctx):
        embed = discord.Embed(
            title="**Comenzile `clan`",
            description="Comenzile `clan` fac parte dintr-un sistem prin care puteti sa va distrati cu prietenii. Acestea contin:**\n",
            color=default_color)
        embed.add_field(name="Comanda `.creare clan`",
                        value="Va permite sa va creati propriul clan, cu un nume ales. \nExemplu: `.creare clan Smecherii`, comanda va creeaza clanul 'Smecherii'",
                        inline=False)
        embed.add_field(name="Comanda `.intra clan`",
                        value="Va permite sa intrati intr-un clan existent, precizand numele acestuia. \nExemplu: `.intra clan Smecherii`, comanda va trimie o cerere de intrare liderului clanului 'Smecherii'",
                        inline=False)
        embed.add_field(name="Comanda `.accept clan`",
                        value="Permite accesul unui membru in clanul tau (valabil exclusiv pentru liderii clanului, doar daca membrul a depus o cerere de intrare in clan). \nExemplu: `.accept clan @Denis`, comanda il va baga automat pe @Denis in clan.",
                        inline=False)
        embed.add_field(name="Comanda `.iesire clan`",
                        value="Va permite sa iesiti dintr-un clan, precizand numele acestuia. \nExemplu: `.iesire clan 'Smecherii'`, comanda va va elimina din clan.",
                        inline=False)
        embed.add_field(name="Comanda `.inchide clan`",
                        value="Va permite sa stergeti clanul in care sunteti (doar daca sunteti liderul clanului.)\nExemplu: `.inchide clan`, comanda va trimite un mesaj de confirmare, apoi va sterge clanul daca este confirmata stergerea.",
                        inline=False)
        await ctx.reply(embed=embed)

    @help.command()
    async def unmute(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .unmute",
            value=
            """Descriere: Îi redai cuiva accessul de a putea conversa cu ceilalți membri
    Folosire: .unmute [membru] 
    La alegerea voastră puteți scrie și motivul pentru care respectivul a primit unmute
    Exemplu: 
       .unmute @Optimus Prime 
       .unmute @lil dani nbn de la kuweit nmw mute greșit""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command(aliases=['av', 'Av', 'Avatar'])
    async def avatar(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .avatar",
            value=
            """Descriere: Cu ajutorul acestei comenzi poți vedea avatarul într un format mai mare al unei persoane.
    Folosire: .av [nume]
    Exemplu: 
       .av @Optimus Prime 
       .avatar @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def kick(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .kick",
            value=
            """Descriere: Folosind această comandă dai afară pe cineva de pe server.
    Folosire: .kick [membru] [motiv]
    Exemplu: 
       .kick @Optimus Prime 
       .kick @lil dani nbn de la kuweit nmw Ieși mă de aici""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def snipe(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .snipe",
            value=
            """Descriere: Cu ajutorul acestei comenzi poți vedea ce mesaj a șters un membru.
    Folosire: .snipe
    Exemplu:
       .snipe""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command(aliases=['roleadd'])
    async def addrole(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .addrole",
            value=
            """Descriere: Folosind această  comandă îi adaugi un grad unui membru.
    Folosire: .addrole [nume] [grad]
    Exemplu: 
       .addrole @Daani#5822 Helper""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command(aliases=['roleremove'])
    async def removerole(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .removerole",
            value=
            """Descriere: Folosind această  comandă îi stergi un grad unui membru.
    Folosire: .removerole [nume] [grad]
    Exemplu: 
       .removerole @Daani#5822 Helper""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command(aliases=['casatorie'])
    async def marry(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .casatorie",
            value=
            """Descriere: ii propui unei persoane sa se casatoreasca cu tine sau accepti o cerere in casatorie .
            Utilizare :
            .casatorie [@persoana] [mesaj de dragoste]
    Exemplu:
    .casatorie @Optimus Prime te iubesc si te ador""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command(aliases=['staffwarn'])
    async def warn(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda . warn",
            value=
            """Descriere: Dai warn cuiva din staff.
    Folosire: .staffwarn <nume>
    Exemplu: 
    .staffwarn @lil dani nbn de la kuweit nmw comportament inadecvat""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command(aliases=['staffwarns'])
    async def warns(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda . warns",
            value=
            """Descriere: Îi verifici antecedentele cuiva din staff.
    Folosire: .staffwarns <nume>
    Exemplu:
    .staffwarns @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def warnlist(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda . warnlist",
            value=
            """Descriere: O listă cu toate warn-urile tuturor membrilor staff.
    Folosire: .warnlist""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def delwarn(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda . delwarn",
            value=
            """Descriere: Îi scoți warn-ul cuiva.
    Folosire: .delwarn <nume>
    Exemplu:
    .delwarn @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def remove(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda . remove",
            value=
            """Descriere: Îi scoți funcția unui membru staff.
    Folosire: .remove <nume>
    Exemplu:
    .remove @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def avertisment(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda . avertisment",
            value=
            """Descriere: Dai un avertisment cuiva din staff.
    Folosire: .avertisment <nume>
    Exemplu:
    .avertisment @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def wanted(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda . wanted",
            value=
            """Descriere: Dai în urmărire pe cineva.
    Folosire: .wanted <nume>
    Exemplu:
    .wanted @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def tembel(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .tembel",
            value=
            """Descriere: Arăți cu degetu către cineva și l  faci tembel.
    Folosire: .tembel <nume>
    Exemplu:
    .tembel @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def gay(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda . gay",
            value=
            """Descriere: Pune anunț pe Instagram pe o pagină de LGBT cu poza de profil.
    Folosire: .gay <nume>
    Exemplu:
    .gay @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command(aliases=['divorce'])
    async def divort(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .divort",
            value=
            """Descriere: divortezi de persoana cu care esti casatorita .

            !Atentie! nu va fi nicio verificare 

    Exemplu:
    .divort""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def accept(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .accept",
            value=
            """Descriere: Cu ajutorul acestei comenzi accepti o sugestie.
    Folosire: .accept lui <nume>
    Exemplu:
    .accept lui @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def refuz(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .refuz",
            value=
            """Descriere: Cu ajutorul acestei comenzi refuzi o sugestie.
    Folosire: .refuz lui <nume>
    Exemplu:
    .refuz lui @Optimus Prime""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def editsnipe(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .editsnipe",
            value=
            """Descriere: Cu ajutorul acestei comenzi poți vedea ce mesaj a editat un membru.
    Folosire: .editsnipe""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def serveravatar(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .serveravatar",
            value=
            """Descriere: Îți arată care este avatarul serverului.
    Folosire: .serveravatar""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def savatar(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .serveravatar",
            value=
            """Descriere: Îți arată care este avatarul serverului.
    Folosire: .serveravatar""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def servere(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .servere",
            value=
            """Descriere: Verifici în câte servere de discord se află botul.
    Folosire: .servere""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def random(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .random",
            value=
            """Descriere: Folosind această comandă se generează un numar random de la 1 la x.
    Folosire: .random
    Exemplu:
    .random 15""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def sugestie(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .sugestie",
            value=
            """Descriere: Cu ajutorul acestei comenzi trimiți o sugestie către administrația serverului.
    Folosire: .sugestie <ce propui>
    Exemplu:
    .sugestie să adăugați la bot comanda .frumos.""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def suggest(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .sugestie",
            value=
            """Descriere: Cu ajutorul acestei comenzi trimiți o sugestie către administrația serverului.
    Folosire: .sugestie <ce propui>
    Exemplu:
    .sugestie să adăugați la bot comanda .frumos.""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def suggestion(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .sugestie",
            value=
            """Descriere: Cu ajutorul acestei comenzi trimiți o sugestie către administrația serverului.
    Folosire: .sugestie <ce propui>
    Exemplu:
    .sugestie să adăugați la bot comanda .frumos.""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def whois(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .whois",
            value=
            """Descriere: Verifici cine este un membru, primind informații guvernamentale.
    Folosire: .whois <nume>
    Exemplu:
    .whois @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def fraier(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .fraier",
            value=
            """Descriere: Verifici cât de fraier e cineva.
    Folosire: .fraier <nume>
    Exemplu:
    .fraier @Optimus Prime""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def gayrate(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .gay",
            value=
            """Descriere: Aflii nivelul de gay al cuiva.
    Folosire: .gay <nume>
    Exemplu:
    .gay @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def howgay(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .gay",
            value=
            """Descriere: Aflii nivelul de gay al cuiva.
    Folosire: .gay <nume>
    Exemplu:
    .gay @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def pp(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .pp",
            value=
            """Descriere: Îți măsori p**a.
    Folosire: .pp <nume>
    Exemplu:
    .pp @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def dick(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .pp",
            value=
            """Descriere: Îți măsori p**a.
    Folosire: .pp <nume>
    Exemplu:
    .pp @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def pula(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .pp",
            value=
            """Descriere: Îți măsori p**a.
    Folosire: .pp <nume>
    Exemplu:
    .pp @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def pup(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .pup",
            value=
            """Descriere: Îi dai un pupic cuiva, ce drăguț.
    Folosire: .pup <nume>
    Exemplu:
    .pup @Optimus Prime""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def pwp(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .pup",
            value=
            """Descriere: Îi dai un pupic cuiva, ce drăguț.
    Folosire: .pup <nume>
    Exemplu:
    .pup @Optimus Prime""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def kiss(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .pup",
            value=
            """Descriere: Îi dai un pupic cuiva, ce drăguț.
    Folosire: .pup <nume>
    Exemplu:
    .pup @Optimus Prime""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def ship(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .ship",
            value=
            """Descriere: Verifici dacă ești compatibil cu cineva, poate o combini, cine știe.
    Folosire: .ship <nume1> <nume2> sau .ship <nume>
    Exemplu:
    .ship @Optimus Prime @Giuliuka""",
            inline=True)
        ctx.reply(embed=embed)

    @help.command(aliases=['say'])
    async def spune(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .spune",
            value=
            """Descriere: Pui botul să zică ce vrei tu.
    Folosire: .spune <text>
    Exemplu:
    .spune În pădure la Băneasa e cel mai tare server!!!""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def ban(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .ban",
            value=
            """Descriere: Îi privezi unui membru libertatea permanent.
    Folosire: .ban [membru] [motiv]
    Exemplu: 
       .ban @Optimus Prime ai fost obraznic !!!
       .ban @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def softban(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .softban",
            value=
            """Descriere: Dai un membru afara si ii stergi toate mesajele.
    Folosire: .softban [membru] [motiv]
    Exemplu: 
       .softban @Optimus Prime ai fost obraznic !!!
       .softban @lil dani nbn de la kuweit nmw""",
            inline=True)
        await ctx.reply(embed=embed)

    @help.command()
    async def unban(self, ctx):
        embed = discord.Embed(
            title="", description="", color=default_color)
        embed.add_field(
            name="Comanda .unban",
            value=
            """ Descriere: Îi înapoiezi cuiva accessul de a putea intra pe server
    Folosire: .unban [id] [motiv opțional]
        La alegerea voastră puteți să spuneți și motivul pentru care respectivul a primit unban
    Exemplu: 
       .unban 470995082145824798
       .unban 470995082145824798  a fost cuminte""",
            inline=True)
        await ctx.reply(embed=embed)


async def setup(client):
    await client.add_cog(Help(client))