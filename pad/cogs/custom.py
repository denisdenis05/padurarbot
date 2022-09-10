import discord
import random
import json
import time
import datetime
from discord.ext import commands
from discord.ui import Button, View
from random import randint
from datetime import datetime
from main import default_color

class Custom(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def allie(self, ctx):
        await ctx.reply("+10 social credits")

    @commands.command()
    async def testbuton(self, ctx):
        view = View()
        button=discord.ui.Button(label="Voteaza-ma pe top.gg!",style=discord.ButtonStyle.danger,custom_id="lmao",emoji="<a:bucimesi:960985978972033054>")
        view.add_item(button)
        msg = await ctx.send(
            "test", view=view)

    @commands.command()
    async def luv(self, ctx, member: discord.Member = None):
        with open("pad/data/data.json", "r") as jsonFile:
            data = json.load(jsonFile)
            jsonFile.close()
        if ctx.author.id != 528890858657939456:
            return
        if member == None:
            await ctx.reply("mna pe cn iubesti???")
            return
        rand = randint(1, 3)
        if rand == 1:
            situatie = randint(1, 10)
            if situatie == 1:
                embed = discord.Embed(title="", description="", color=default_color)
                embed.add_field(name="Wtf", value=f"Ai facut sex cu {member.mention} dar ai foot fetish", inline=True)
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
                embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/874999910863364177.gif?v=1&size=40')
            elif situatie == 2:
                embed = discord.Embed(
                    title="", description="", color=discord.Color.from_rgb(255, 182, 193))
                embed.add_field(name="Frumos", value=f"L-ai satisfacut pe {member.mention}", inline=True)
                embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/828260808608972801.gif?v=1&size=40')
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
            elif situatie == 3:
                embed = discord.Embed(
                    title="", description="", color=discord.Color.from_rgb(255, 182, 193))
                embed.add_field(name="Mmmmmm", value=f"Ai facut seggs senzual cu {member.mention}", inline=True)
                embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/828282925102923806.gif?v=1&size=40')
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
            elif situatie == 4:
                embed = discord.Embed(
                    title="", description="", color=discord.Color.from_rgb(255, 182, 193))
                embed.add_field(name="Sex...", value=f"...pe covor cu {member.mention}", inline=True)
                embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/792574177139621909.gif?v=1&size=40')
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
            elif situatie == 5:
                embed = discord.Embed(
                    title="", description="", color=discord.Color.from_rgb(255, 182, 193))
                embed.add_field(name="Felicitari!", value=f"Ai procreat un copil cu {member.mention}", inline=True)
                embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/795275310349418497.gif?v=1&size=40')
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
            elif situatie == 6:
                embed = discord.Embed(
                    title="", description="", color=default_color)
                embed.add_field(name="Uhhhh", value=f"Cred ca vei fi mamica {member.mention}", inline=True)
                embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/821053795726655518.png?v=1&size=40')
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
            elif situatie == 6:
                embed = discord.Embed(
                    title="", description="", color=default_color)
                embed.add_field(name="Uhhhh", value=f"Cred ca vei fi tatic {member.mention}", inline=True)
                embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/821053795726655518.png?v=1&size=40')
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
            if situatie == 7:
                embed = discord.Embed(
                    title="", description="", color=default_color)
                embed.add_field(name="Scuze",
                                value=f"{member.mention} ti-a refuzat cererea de sex, motiv: `o are mica da-l dracu`",
                                inline=True)
                embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/825735245965950996.gif?v=1&size=40')
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
            if situatie == 8:
                embed = discord.Embed(
                    title="", description="", color=default_color)
                embed.add_field(name="Scuze", value=f"{member.mention} ti-a refuzat cererea de sex, motiv: `sunt gay`",
                                inline=True)
                embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/788522211161407498.gif?v=1&size=40')
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
            elif situatie == 9:
                embed = discord.Embed(
                    title="", description="", color=discord.Color.from_rgb(255, 182, 193))
                embed.add_field(name="Woah woah be careful",
                                value=f"Ai procreat un copil cu {member.mention}, poti ramane bankrupt", inline=True)
                embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/879375203040391169.gif?v=1&size=40')
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
            elif situatie == 10:
                embed = discord.Embed(
                    title="", description="", color=discord.Color.from_rgb(255, 182, 193))
                timp = randint(2, 44)
                embed.add_field(name="Sunteti tari", value=f"Ai facut sex cu {member.mention} timp de {timp} ore",
                                inline=True)
                embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/736665975939792936.gif?v=1&size=40')
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
            await ctx.reply(embed=embed)
        elif rand == 2:
            random = randint(1, 9)
            if random == 1:
                sot = data[f"Cas{ctx.author.id}"]
                data[f"Cas{ctx.author.id}"] = 0
                data[f"Cas{sot}"] = 0

                embed = discord.Embed(title="", decription="", color=default_color)
                embed.add_field(name=f'Ce prost',
                                value="Ti-ai strans partenerul prea tare si a murit. Sunteti divorțați acum.")
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
                await ctx.reply(embed=embed)
            elif random == 2:
                id = data[f"Cas{ctx.author.id}"]
                sot = self.client.get_user(id)
                embed = discord.Embed(title="", decription="", color=default_color)
                embed.add_field(name=f'Ce prost', value=f"Ti s-a sculat unealta si {sot.mention} s-a speriat .")
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
                await ctx.reply(embed=embed)
            elif random == 3:
                id = data[f"Cas{ctx.author.id}"]
                sot = self.client.get_user(id)
                embed = discord.Embed(title="", decription="", color=default_color)
                embed.add_field(name=f'Ce dragut!!', value=f"Tu si {sot.mention} va iubiti probabil.")
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
                await ctx.reply(embed=embed)
            elif random == 4:
                id = data[f"Cas{ctx.author.id}"]
                sot = self.client.get_user(id)
                embed = discord.Embed(title="", decription="", color=default_color)
                embed.add_field(name=f'Bruh', value=f"Bruh")
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
                await ctx.reply(embed=embed)
            elif random == 5:
                id = data[f"Cas{ctx.author.id}"]
                sot = self.client.get_user(id)
                embed = discord.Embed(title="", decription="", color=default_color)
                embed.add_field(name=f'Ce dragut!!', value=f"Ti-ai imbratisat amanta, vezi sa nu stie {sot}")
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
                await ctx.reply(embed=embed)
            elif random == 6:
                id = data[f"Cas{ctx.author.id}"]
                sot = self.client.get_user(id)
                embed = discord.Embed(title="", decription="", color=default_color)
                embed.add_field(name=f'oh wow', value=f"e ariana grand")
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
                await ctx.reply(embed=embed)
            elif random == 7:
                id = data[f"Cas{ctx.author.id}"]
                sot = self.client.get_user(id)
                embed = discord.Embed(title="", decription="", color=default_color)
                embed.add_field(name=f'Misto', value=f"Tu si {sot} va iubiti reciproc.")
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
                await ctx.reply(embed=embed)
            elif random == 8:
                id = data[f"Cas{ctx.author.id}"]
                sot = self.client.get_user(id)
                embed = discord.Embed(title="", decription="", color=default_color)
                embed.add_field(name=f'Aaaah ghinion', value=f"Ti-ai pierdut v-cardul.")
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
                await ctx.reply(embed=embed)
            elif random == 9:
                id = data[f"Cas{ctx.author.id}"]
                sot = ctx.guild.get_member(id)
                await ctx.reply("Ati recurs la segss!")
        else:
            sansa = randint(0, 100)
            if sansa < 10:
                embed = discord.Embed(title="", description="", color=default_color)
                embed.add_field(name=f"Pfaiaiaia", value=f"{ctx.author.mention} ce-ti pute gura vere")
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/735155822736179201/831858603899486229/unknown.png')
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
                embed.timestamp = datetime.utcnow()
                await ctx.reply(embed=embed)
                return
            embed = discord.Embed(title="", description="", color=discord.Color.from_rgb(255, 182, 193))
            # embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/834101384504672347.png?v=1")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/726174197931573398/860244442479853608/809234952570011676.jpg")
            embed.add_field(name=f'Ce drăguț!!!', value=f"{ctx.author.mention} âi da un pupik lui {member.mention}")
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
            embed.timestamp = datetime.utcnow()
            await ctx.reply(embed=embed)


async def setup(client):
    await client.add_cog(Custom(client))