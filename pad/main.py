import discord
import discord_components
import os
import aiohttp
import datetime
import json
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle


custom_prefixes = {}
default_prefixes=['.', '<@885503634710884412> ','<!@885503634710884412> ']
async def determine_prefix(bot, message):
    guild = message.guild
    with open("pad/data/data.json", "r") as jsonFile:
      data = json.load(jsonFile)
      jsonFile.close()
    if f"prefix{guild.id}" in data and data[f"prefix{guild.id}"]!=0:
        return data[f"prefix{guild.id}"]
    else:
        return default_prefixes

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = determine_prefix,help_command=None, intents=intents,case_insensitive=True)
client.session = aiohttp.ClientSession()
DiscordComponents(client)

invites={}
membriicache={}
topxplist={}
paginaxp={}
timpdelatop={}
motivafk={}
numeafk={}
incaafk={}

async def timeout_user(*, user_id: int, guild_id: int, until):
    headers = {"Authorization": f"Bot {client.http.token}"}
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}"
    timeout = (datetime.datetime.utcnow() + datetime.timedelta(minutes=until)).isoformat()
    json = {'communication_disabled_until': timeout}
    async with client.session.patch(url, json=json, headers=headers) as session:
        if session.status in range(200, 299):
           return True
        return False


@client.command()
async def load(ctx,extension):
  client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
  client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('pad/cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
