# padurarbot
A multifunctional python bot (w discord.py API). The official release can be used [here](https://top.gg/bot/885503634710884412).

Bot's main language: Romanian

# Bot's functions:
> Administration (mute,kick,ban,etx)

> Logging

> Fun

> Miscelanous

# Some examples:

### Pic manipulation (using the profile pic or any attached image):
<br><br>
![main2](https://imgur.com/98clWHm.jpeg)
<br><br>
![main2](https://imgur.com/UGEOwpu.jpeg)
<br><br>
![main2](https://imgur.com/1cE8ZiB.jpeg)

### Economy system:
<br><br>
![main2](https://imgur.com/gFlpUtD.jpeg)
<br><br>
![main2](https://imgur.com/VRPfRCz.jpeg)
<br><br>
![main2](https://imgur.com/LgBTZAk.jpeg)
<br><br>
![main2](https://imgur.com/HI7H0EL.jpeg)
<br><br>

# Important stuff:

## How to config:
> Inside the pad/main.py file insert your bot's token (Line 71)

> Change the defined colors in the main file with an RGB code (Line 12 and 13)

> Run pad/main.py

> Use the `.setup` command to set up things such as the prefix, logging channel, etc

### If you change the "pad" folder's name the bot won't work.

## Why is everything in the "pad" folder:
Good question. I run the bot on a Ubuntu server from the "pad" folder.

If you'll ever run the bot on a server, it may not work as intended. The scripts are made to work in the "root/pad" folder (example: "root/pad/cogs/help.py"), it can be easily changed to "./cogs/help.py". You need to know this if you'll change the folder's name

## Where is the data saved:
The data is saved in pad/data/data.json as a basic python dictionary ( {"key":"value", "key2":"value2"} )

