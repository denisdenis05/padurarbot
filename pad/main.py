import discord
import os
import datetime
import aiohttp
import json
import asyncio
from discord.ext import commands


custom_prefixes = {}
default_prefixes = ['.', '<@885503634710884412> ', '<!@885503 634710884412> ']
default_color=discord.Color.from_rgb(255, 255, 0)
secondary_color=discord.Color.from_rgb(255, 0, 0)


async def determine_prefix(bot, message):
    guild = message.guild
    with open("pad/data/data.json", "r") as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()
    if f"prefix{guild.id}" in data and data[f"prefix{guild.id}"] != 0:
        return data[f"prefix{guild.id}"]
    else:
        return default_prefixes

class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

class Select(discord.ui.Select):
    def __init__(self):
        super().__init__(placeholder="Alege o optiune",max_values=1,min_values=1)
      
intents = discord.Intents.all() #all
intents.members = True
client = commands.Bot(command_prefix=determine_prefix,
                      help_command=None,
                      intents=intents,
                      case_insensitive=True)


invites={}
membriicache={}
topxplist={}
paginaxp={}
timpdelatop={}
motivafk={}
numeafk={}
incaafk={}




@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

async def load_extensions():
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
    async with client:
        await load_extensions()
        await client.start('TOKEN')

try:
    asyncio.run(main())
except:
    pass
