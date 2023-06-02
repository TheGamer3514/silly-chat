#Install Modules
try: 
    import os
    import discord  
except ImportError: 
    print("Discord Not Found...\nInstalling...")
    os.system("pip install discord")
    print("Discord Installed")
try: 
    import os
    import pytz  
except ImportError: 
    print("Pytz Not Found...\nInstalling...")
    os.system("pip install pytz")
    print("Pytz Installed")
try: 
    import os
    import psutil  
except ImportError: 
    print("Psutil Not Found...\nInstalling...")
    os.system("pip install psutil")
    print("Psutil Installed")
try: 
    import os
    import requests  
except ImportError: 
    print("requests Not Found...\nInstalling...")
    os.system("pip install requests")
    print("requests Installed")
try: 
    import os
    import stability_sdk  
except ImportError: 
    print("stability_sdk Not Found...\nInstalling...")
    os.system("pip install stability_sdk")
    print("stability_sdk Installed")
try: 
    import os
    import better_profanity  
except ImportError: 
    print("better-profanity Not Found...\nInstalling...")
    os.system("pip install better-profanity")
    print("better-profanity Installed")
try: 
    import os
    import pymongo  
except ImportError: 
    print("pymongo Not Found...\nInstalling...")
    os.system("pip install pymongo")
    print("pymongo Installed")
#import Modules
import os
from datetime import datetime
import asyncio
import pymongo
import discord
import pytz
import base64
from better_profanity import profanity
from stability_sdk import client as aiclient
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import string
from PIL import Image
import multiprocessing
from discord.ext import commands
import psutil
from io import BytesIO
import io
import re
from giffy import giffy
websites = giffy.data.data
from discord import Message, Guild, TextChannel, Permissions
import json
from contextlib import redirect_stdout
from importlib.metadata import version
import time
import textwrap
import traceback
import requests
import platform
import random
import aiohttp
import shutil
last_usage = {}
deathoptions=["Instantly Died","Had death appear at their door","Had Death Occur","Fell of a cliff","got too bored","vanished","got shot in the head with a laser","got too comftorable around bears","got depression and gave up","ended up in hell","dissapeared","Jumped Off A Building","Died","Fell up a flight of stairs.","Thought a necular power plant was a good place to go on holiday","Liked Jazz","Became a musician","Ate McDonalds","Became an artist","Turned to the dark side","Liked limes for some reason","Became a meme","Got 360 NO SCOPED BY A FOUR YEAR OLD!","Tried to play fortnite mobile","Didn't die!","Didn't have death occur!"]
ball8answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
heads_tails = ['<:Heads:1043603482474721331> Heads <:Heads:1043603482474721331>', '<:Tails:1043603443689988096> Tails <:Tails:1043603443689988096>']
#Logging
import logging
handler = logging.FileHandler(filename='errors.log', encoding='utf-8', mode='w')
#Load Config
with open('config/config.json') as f:
  data = json.load(f)
  for c in data['botConfig']:
        print('Prefix: ' + c['prefix'])
#Define Bot
botversion = "2.2.6"
servcountgoal = 100
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = discord.ext.commands.AutoShardedBot(command_prefix = c['prefix'],intents=intents,case_insensitive=True, help_command=None, status=discord.Status.online, activity=discord.Game(name=f'/help | Booting...'))
#Load Mongodb
client = pymongo.MongoClient(c['mongodb'])
db = client['SillyChat']
print("Connected to MongoDB")
#------------------------------------------Bot Events-------------------------------------------------
#Auto Updating Status
async def StatusChange():
    while True:
        count = 0
        servercollection = db['servers']
        servercursor = servercollection.find()
        for server in servercursor:
            count = count + 1
        channelcount = 0
        for guild in bot.guilds:
            channelcount += len(guild.channels)
        usercount = len(list(filter(lambda m: m.bot == False, bot.users)))
        await bot.change_presence(activity=discord.Game(f'/help | {len(bot.guilds)} Servers'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | {usercount} Users'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | discord.gg/3qvpkgWSbF'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Invite Me Today!'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Silly Chat'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | {channelcount} Channels'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | not your average global chat bot!'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Downloading 2024'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Is the red I see, the same as you see?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Gamer3514#7679'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | {count} connected channels'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | 99.99% uptime'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Does everyone see the same colour?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Version: {botversion}'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Cats are better than dogs.'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Dogs are worse than cats.'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | ⠉⠕⠕⠇⠀⠃⠕⠞'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Made In Python'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Born In The UK'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | {round(bot.latency * 1000)}ms Ping'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Server Count Goal: {servcountgoal}'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Made By Gamer3514#7679'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | 100% Free'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Open Source'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Disney +'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Netflix'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Amazon Prime'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Spotify'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Apple Music'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | YouTube Music'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Deezer'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | SoundCloud'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Twitch'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Hulu'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Crunchyroll'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Apple TV +'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | YouTube Premium'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | 3514 Server'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | RIP #4551'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Messages'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | 3514'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Discord Servers'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | T-Series'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | star wars'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | marvel'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | dc'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | disney'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | pixar'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | fox'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | national geographic'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Han Solo'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Luke Skywalker'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Princess Leia'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Darth Vader'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Obi-Wan Kenobi'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Chewbacca'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Yoda'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | R2-D2'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | C-3PO'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Jabba the Hutt'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Boba Fett'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Lando Calrissian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Kylo Ren'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Rey'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Finn'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Poe Dameron'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Supreme Leader Snoke'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Maz Kanata'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Captain Phasma'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | General Hux'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | BB-8'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | DJ'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Rose Tico'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Vice Admiral Holdo'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Jannah'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Zorii Bliss'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Babu Frik'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | D-O'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | The Mandalorian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | The Child'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Cara Dune'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Greef Karga'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Moff Gideon'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | IG-11'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Kuiil'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | The Armorer'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bo-Katan Kryze'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | PewDiePie'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Cocomelon'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | SET India'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | 5-Minute Crafts'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | WWE'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | ✨'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | 🎉'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Thanos'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Iron Man'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Captain America'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Thor'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Hulk'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Black Widow'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Hawkeye'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Black Panther'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Vision'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Scarlet Witch'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | beautiful code'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | The Flash'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Batman'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Superman'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Free Guy'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Discord.py'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Python'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Cats'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Dogs'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Birds'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Fishes'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Rabbits'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Hamsters'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Mice'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Rats'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Guinea Pigs'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Ferrets'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Chinchillas'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Gerbils'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Horses'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Ponies'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Donkeys'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Mules'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Zebras'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Goats'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Sheep'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Pigs'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Cows'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | United Kingdom'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | United States'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Canada'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Australia'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | New Zealand'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | India'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Pakistan'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | China'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Japan'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | South Korea'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | North Korea'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Germany'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | France'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Spain'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Italy'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Greece'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Brazil'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Argentina'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Mexico'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Colombia'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Venezuela'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Peru'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Chile'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Ecuador'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bolivia'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Paraguay'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Uruguay'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Guyana'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Suriname'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | French Guiana'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Falkland Islands'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | South Georgia and the South Sandwich Islands'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Anguilla'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Antigua and Barbuda'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Aruba'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bahamas'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Barbados'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Belize'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bermuda'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | British Virgin Islands'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Canada'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Cayman Islands'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Costa Rica'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Cuba'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Dominica'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Dominican Republic'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | El Salvador'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Greenland'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Grenada'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Guadeloupe'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Guatemala'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Haiti'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Honduras'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Jamaica'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Martinique'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Montserrat'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Nicaragua'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Panama'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Puerto Rico'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Saint Barthélemy'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Saint Kitts and Nevis'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Saint Lucia'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Saint Martin'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Saint Pierre and Miquelon'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Saint Vincent and the Grenadines'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Sint Maarten'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Trinidad and Tobago'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Turks and Caicos Islands'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | United States'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | United States Virgin Islands'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Argentina'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bolivia'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Brazil'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Chile'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Colombia'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Ecuador'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Falkland Islands'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | French Guiana'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Guyana'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Olympics'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Paraguay'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Peru'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Guardians of the Galaxy'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Linus Cat Tips'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Linus Tech Tips'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Mr Beast'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | John Nolan'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Lucy Chen'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Tim Bradford'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Jackson West'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Angela Lopez'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Wesley Evers'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Nyla Harper'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Henry Nolan'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Grace Sawyer'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Abigail'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | The Rookie'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | The Rookie Season 1'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | The Rookie Season 2'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | The Rookie Season 3'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | The Rookie Season 4'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | The Rookie Season 5'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Nick Armstrong'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Doug Stanton'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Sarah Brooks'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Zoe Andersen'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Talia Bishop'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Jim Street'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Hondo'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Deacon'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Chris'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Luca'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Tan'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Street'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Hicks'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Mumford'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Evan Buckley'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Eddie Diaz'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Chimney'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Hen'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bobby'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Athena'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Maddie'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Buck'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Eddie'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Silly Chat'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "The purpose of our lives is to be happy."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "Life is what happens when you’re busy making other plans."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "Get busy living or get busy dying."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "You only live once, but if you do it right, once is enough."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "Many of life’s failures are people who did not realize how close they were to success when they gave up."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "If you want to live a happy life, tie it to a goal, not to people or things."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "Never let the fear of striking out keep you from playing the game."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "Money and success don’t change people; they merely amplify what is already there."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "Your time is limited, so don’t waste it living someone else’s life."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "Not how long, but how well you have lived is the main thing."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "If life were predictable it would cease to be life, and be without flavor."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "The whole secret of a successful life is to find out what is one’s destiny to do, and then do it."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "In order to write about life first you must live it."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "The big lesson in life, baby, is never be scared of anyone or anything."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "Sing like no one’s listening, love like you’ve never been hurt, dance like nobody’s watching, and live like it’s heaven on earth."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Albert Einstein'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "The purpose of our lives is to be happy."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | "Life is what happens when you’re busy making other plans."'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Isaac Newton'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Stephen Hawking'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Atlas'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #KeepMovingForward'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #StayStrong'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreNotAlone'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreLoved'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreStrong'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreBeautiful'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreWorthy'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreImportant'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreBrave'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreAmazing'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreTalented'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreUnique'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreIncredible'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreStrongerThanYouThink'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreNotYourMistakes'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreNotYourPast'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreNotYourIllness'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreNotYourDisability'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreNotYourTrauma'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreNotYourPain'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreNotYourStruggles'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #YouAreNotYourEmotions'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Emoji Movie'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Sheldon Cooper'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Tam Nguyen'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Silly Chat'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Silly Development'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Mr Bean'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Mr Bean The Animated Series'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Teddy'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Fortnite'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Minecraft'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Roblox'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Among Us'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #StaySafe'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #StayHealthy'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Intense'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | #StayPositive'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Gaming'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Github Copilot'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Github Codespaces'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Github Actions'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Github Packages'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Github Discussions'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Github Pages'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Silly Development'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Too Many Statuses'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Send & recieve Messages!'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Panic! At The Disco'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Discord Nitro'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Discord'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Discord.js bad'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Discord.py good'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Hypixel'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Intel CPU'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | AMD CPU'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Nvidia GPU'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | AMD GPU'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Intel GPU'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | AMD APU'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Intel APU'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | AMD Threadripper'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Intel Xeon'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | AMD Ryzen'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Silly Chat'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Silly Development'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Silly Chat On Top'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Silly Development On Top'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Utility_'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Discord Bot'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Discord Bot Development'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Bard'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Search'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Images'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Maps'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Translate'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Docs'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Sheets'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Slides'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Forms'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Drive'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Meet'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Calendar'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Classroom'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Hangouts'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Keep'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Jamboard'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Earth'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Trends'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Alerts'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google AdSense'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google AdWords'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bing Chat'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bing'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bing Search'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bing Images'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bing Maps'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bing Translate'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bing Docs'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bing Sheets'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bing Slides'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bing Forms'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bing Drive'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bing Meet'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Monday'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Tuesday'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Wednesday'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Thursday'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Friday'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Saturday'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Sunday'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | January'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | February'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | March'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | April'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | May'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | June'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | July'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | August'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | September'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | October'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | November'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | December'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | 1'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | 2'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | 3'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | 4'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | 5'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | 6'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | 7'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | 8'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | 9'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | 10'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Why did i count to 10?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | A'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | B'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | C'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | D'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | E'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | F'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | G'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | H'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | J'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | K'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | L'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | M'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | N'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | O'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | P'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Q'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | R'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | S'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | T'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | U'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | V'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | W'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | X'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Y'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Z'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Why am i not in your server?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Breakfast'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Lunch'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Dinner'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Snack'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | What is the meaning of life?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | What is the meaning of death?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | What is the meaning of the universe?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | What is the meaning of everything?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | What is the meaning of nothing?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | What is the meaning of something?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | What is the meaning of my existence?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | What is the meaning of your existence?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | What is the meaning of our existence?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Runtime warning'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Runtime error'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Syntax error'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Syntax'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Runtime'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Error'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Warning'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Error: 404'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Dashboard coming soon'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Website coming soon'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | API coming soon'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bot Update coming soon'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bot Version: {version}'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Very cool'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Hooked on a feeling'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I am groot'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | The quick brown fox jumps over the lazy dog'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | touch grass'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go outside'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to sleep'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to bed'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to school'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to work'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the store'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the mall'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the park'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the beach'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the gym'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the movies'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the zoo'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the museum'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the aquarium'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the library'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the hospital'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the doctor'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the dentist'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the vet'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the police station'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the fire station'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the post office'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | go to the bank'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Dont forget to eat'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Dont forget to drink water'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Dont Buy Robux'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Dont Buy V-Bucks'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Atoms are small'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | The mitochondria is the powerhouse of the cell'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I am still groot'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Line 109 has an error'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Line 110 starts the bot'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f"/help | {sum(1 for line in open('main.py', errors='ignore'))} lines of code"))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | {len(bot.guilds)} servers'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Thanos knows'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I am groot'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | There are secret commands'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I am always watching'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I am always listening'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I am always waiting'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I am always lurking'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I am always watching you'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I am always listening to you'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I am always waiting for you'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I am always lurking on you'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I am always watching you sleep'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | g!secret is a secret command'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Do animals see in color?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Do animals see in black and white?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Do animals see in color or black and white?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I made way too many of these'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Hosted and born in the UK'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Join the support server'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | GROOT'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | VOTE FOR GROOT'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | g!groot will show you groot'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Over 900 statuses made'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Are ghosts real?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Are ghosts real or fake?'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Charities are good'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I WISH I WAS GROOT'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Some people are groot'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Very groot'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Very Fast'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Very Cool'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Very Cool and Very Groot'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | English'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | German'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | French'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Spanish'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Italian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Russian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Chinese'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Japanese'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Korean'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Arabic'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Hindi'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Turkish'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Polish'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Dutch'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Indonesian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Swedish'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Norwegian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Finnish'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Danish'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Greek'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Hungarian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Czech'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Romanian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Vietnamese'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Thai'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Slovak'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Croatian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bulgarian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Lithuanian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Slovenian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Latvian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Estonian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Serbian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Catalan'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Hebrew'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Filipino'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Indonesian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Malay'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Ukrainian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Hindi'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bengali'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Arabic'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Persian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Swahili'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Afrikaans'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Zulu'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Yoruba'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Igbo'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Hausa'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Cebuano'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Nepali'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Somali'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Marathi'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Punjabi'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Telugu'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Tamil'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Gujarati'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Kannada'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Malayalam'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Sinhala'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Khmer'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Lao'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Myanmar'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Mongolian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Uzbek'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Kazakh'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Kyrgyz'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Turkmen'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Tajik'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Azerbaijani'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Georgian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Armenian'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Tigrinya'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Amharic'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Oromo'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Somali'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Hausa'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Igbo'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Yoruba'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Zulu'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Afrikaans'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | We brought a Zoo'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | We brought a Museum'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | We brought a Aquarium'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | We brought a Library'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | We did not buy those things'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Subway'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | McDonalds'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Burger King'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | KFC'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Taco Bell'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Wendys'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Dominos'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Pizza Hut'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Chipotle'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Google Chrome'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Firefox'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Microsoft Edge'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Safari'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Opera'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Internet Explorer'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Brave'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Vivaldi'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Tor'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | DuckDuckGo'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Bing'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE RAM'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE CPU'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE GPU'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE SSD'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE HDD'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE MOTHERBOARD'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE POWER SUPPLY'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE CASE'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE MONITOR'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE KEYBOARD'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE MOUSE'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE HEADSET'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE MICROPHONE'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE WEBCAM'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE SPEAKERS'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE PRINTER'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE SCANNER'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I LIKE GRAPHICS TABLET'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I HATE VR HEADSETS'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | I HATE VR'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Ping Pong!'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Silly Chat'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | {len(bot.guilds)} Servers'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | {len(bot.users)} Users'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | {len(bot.emojis)} Emojis'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | {channelcount} Channels'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | The Lorax'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | The Cat in the Hat'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Green Eggs and Ham'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Oh, the Places You\'ll Go!'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | One Fish Two Fish Red Fish Blue Fish'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Fox in Socks'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Horton Hears a Who!'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | The Sneetches and Other Stories'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | The Butter Battle Book'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | Yertle the Turtle and Other Stories'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | How the Grinch Stole Christmas!'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | This is the final status until the loop restarts'))
        await asyncio.sleep(120)
#Logging
async def Logging(title,message):
        channel = int(c['logchannel'])
        channel = bot.get_channel(channel)
        embed = discord.Embed(title=title,description=message,color=discord.Colour.random())
        embed.add_field(name="Bot Version",value=f"{botversion}",inline=True)
        embed.add_field(name="Bot Prefix",value=f"{c['prefix']}",inline=True)
        embed.add_field(name="Bot ID",value=f"{bot.user.id}",inline=True)
        embed.add_field(name="Bot Name",value=f"{bot.user.name}",inline=True)
        embed.add_field(name="Bot Discriminator",value=f"{bot.user.discriminator}",inline=True)
        embed.add_field(name="Ping",value=f"{round(bot.latency * 1000)}ms",inline=True)
        embed.add_field(name="Python Version",value=f"{platform.python_version()}",inline=True)
        embed.add_field(name="Discord.py Version",value=f"{discord.__version__}",inline=True)
        embed.add_field(name="OS",value=f"{platform.system()}-{platform.release()}",inline=True)
        embed.set_author(name=bot.user.name,icon_url=bot.user.avatar.url)
        embed.set_thumbnail(url=bot.user.avatar.url)
        embed.set_footer(text=f"Powered By: Silly Development")
        await channel.send(embed=embed)
#Screenshot Page
def take_screenshot(url, output_path):
    api_url = f"http://143.47.249.115:3514/screenshot?token={c['screenshotkey']}"
    payload = {'url': url,'waitFor': 305, 'options': { 'type': "png", 'clip': {'height': 796, 'width': 800, 'x': 0, 'y': 0}}}
    response = requests.post(api_url, json=payload, stream=True)
    response.raise_for_status()
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
#Event that runs when bot is online
@bot.event
async def on_ready():
    folder = './temp'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    await Logging("Bot Ready!",f'{bot.user} Is Now Online And Ready To Send & recieve Messages!')
    print(f'{bot.user} Is Now Online And Ready To Send & recieve Messages!')
    await bot.loop.create_task(StatusChange())
#Event for when a message is sent
@bot.event
async def on_message(message: Message):
    cooldown = 7
    message50 = False
    message100 = False
    possiblechannels = []
    userz = []
    bannedusers = []
    adminz = []
    usercollection = db['users']
    servercollection = db['servers']
    usercursor = usercollection.find()
    usercursore = usercollection.find()
    servercursor = servercollection.find()
    for userid in usercursor:
        userz.append(int(userid["userid"]))
        if userid["isbotmod"] == "True":
            adminz.append(int(userid["userid"]))
        if userid["isbanned"] == "True":
            bannedusers.append(int(userid["userid"]))
        if message.author.id == int(userid['userid']):
            if int(userid['messages']) >= 50:
                message50=True
            if int(userid['messages']) >= 100:
                message100=True
    if message50 == True:
        cooldown = 4
    for channel in servercursor:
        possiblechannels.append(int(channel["channelid"]))
    if message.author.bot:
        return
    if message.author.id in bannedusers and message.channel.id in possiblechannels:
        try:
            user = message.author
            embed = discord.Embed(description="**You Are Bannned!**\r\n"
            "It seems you have been banned from using this feature!\nBelieve this is a mistake? Please join our support server!",
            color=0x2ecc71)
            await user.send(embed=embed)
            await message.delete()
        except:
            pass
    else:
        try:
                if message.reference:
                    embedmessage = await message.channel.fetch_message(message.reference.message_id)
                    if embedmessage.embeds:
                        if embedmessage.author.id == bot.user.id:
                            author = embedmessage.embeds[0].author.name
                            footertext = embedmessage.embeds[0].footer.text
                            message.content = f"Replying to **{author}** ({footertext}):\n{message.content}"
                if message.author.id not in userz:
                    user = {
                        "userid": message.author.id,
                        "messages": 0,
                        "isbanned": "False",
                        "isbotmod": "False"
                    }
                    usercollection.insert_one(user)
                if not message.content.startswith(f"{c['prefix']}"):
                    if message.channel.id not in possiblechannels:
                        return
                    if message.author.id not in last_usage:
                        last_usage[message.author.id] = 0
                    elapsed_time = time.time() - last_usage[message.author.id]
                    if elapsed_time < cooldown and message.author.id not in adminz:
                        embed = discord.Embed(description="**Chill!**\r\n"
                        f"Please wait {cooldown - elapsed_time:.2f} seconds before using global chat again!",
                        color=0x2ecc71)
                        await message.channel.send(embed=embed)
                        await message.delete()
                        return
                    elif message.author.id in adminz:
                        last_usage[message.author.id] = time.time()
                        profanity_check = profanity.contains_profanity(message.content)
                        for userid in usercursore:
                            if int(userid["userid"]) == message.author.id:
                                    messages = int(userid["messages"])
                                    newmessage = messages + 1
                                    newvalues = { "$set": { "messages": int(newmessage) } }
                                    if newmessage == 50:
                                        embed = discord.Embed(description="**50 Messages!**\r\n"
                                                              f"You have reached 50 messages on Silly Chat!\n**New Perks:**\n• Shorter Message Cooldown\n• Chatter Rank",
                                                              color=discord.Colour.blurple())
                                        await message.author.send(embed=embed)
                                    if newmessage == 100:
                                        embed = discord.Embed(description="**100 Messages!**\r\n"
                                                              f"You have reached 100 messages on Silly Chat!\n**New Perks:**\n• Active Chatter Rank",
                                                              color=discord.Colour.blurple())
                                        await message.author.send(embed=embed)
                                    if newmessage == 150:
                                        embed = discord.Embed(description="**150 Messages!**\r\n"
                                                              f"You have reached 150 messages on Silly Chat!\n**New Perks:**\n• </aiart:1079002951265300541>",
                                                              color=discord.Colour.blurple())
                                        await message.author.send(embed=embed)
                                    usercollection.update_one(userid, newvalues)
                        if message.content[:3] == "@ai" or message.content[:3] == "@AI":
                            uid = message.author.id
                            message.content = message.content[3:]
                            async with aiohttp.ClientSession() as session:
                                async with session.get(f"http://api.brainshop.ai/get?bid={c['bid']}&key={c['key']}&uid={uid}&msg={message.content}") as resp:
                                    responce = await resp.json()
                                    responce = responce["cnt"]
                                    responce = f"Replying to **{message.author}**:\n{responce}"
                                    await sendAll(message)
                                    await sendAiAll(responce)
                                    return
                        else:
                            await sendAll(message)
                            return
                    else:
                        profanity.load_censor_words(whitelist_words=['lmao', 'lmfao', 'ugly'])
                        profanity_check = profanity.contains_profanity(message.content)
                        if profanity_check == True and message.channel.id in possiblechannels:
                            if any(word in message.content for word in allowedwords):
                                return
                            await Logging("Banned Word/s Detected:",f'User: ``{message.author} ({message.author.id})``\nGuild: ``{message.guild.id}``\nMessage: ``{message.content}``')
                            await message.delete()
                            embed = discord.Embed(description="**Take a chill pill!**\r\n"
                            f"Our systems blocked your message due to it containing swear words.\nBelieve this is a mistake? Contact support!",
                            color=0x2ecc71)
                            await message.channel.send(embed=embed)
                        else:
                            last_usage[message.author.id] = time.time()
                            usercollection = db['users']
                            usercursorr = usercollection.find()
                            for userid in usercursorr:
                                if int(userid['userid']) == message.author.id:
                                    messages = int(userid["messages"])
                                    newmessage = messages + 1
                                    newvalues = { "$set": { "messages": int(newmessage) } }
                                    if newmessage == 50:
                                        embed = discord.Embed(description="**50 Messages!**\r\n"
                                                              f"You have reached 50 messages on Silly Chat!\n**New Perks:**\n• Shorter Message Cooldown\n• Chatter Rank",
                                                              color=discord.Colour.blurple())
                                        await message.author.send(embed=embed)
                                    if newmessage == 100:
                                        embed = discord.Embed(description="**100 Messages!**\r\n"
                                                              f"You have reached 100 messages on Silly Chat!\n**New Perks:**\n• Active Chatter Rank",
                                                              color=discord.Colour.blurple())
                                        await message.author.send(embed=embed)
                                    if newmessage == 150:
                                        embed = discord.Embed(description="**150 Messages!**\r\n"
                                                              f"You have reached 150 messages on Silly Chat!\n**New Perks:**\n• </aiart:1079002951265300541>",
                                                              color=discord.Colour.blurple())
                                        await message.author.send(embed=embed)
                                    usercollection.update_one(userid, newvalues)
                            if message.content[:3] == "@ai" or message.content[:3] == "@AI" and message.channel.id in possiblechannels:
                                uid = message.author.id
                                message.content = message.content[3:]
                                async with aiohttp.ClientSession() as session:
                                    async with session.get(f"http://api.brainshop.ai/get?bid={c['bid']}&key={c['key']}&uid={uid}&msg={message.content}") as resp:
                                        responce = await resp.json()
                                        responce = responce["cnt"]
                                        responce = f"Replying to **{message.author}**:\n{responce}"
                                        await sendAll(message)
                                        await sendAiAll(responce)
                                        return
                            else:
                                await sendAll(message)
                                return
                else:
                    if message.channel.id in possiblechannels:
                        await message.delete()
        except:
            pass
    await bot.process_commands(message)
#Send All Message
async def sendAll(message: Message):
    adminz = []
    message50 = False
    message100 = False
    usercollection = db['users']
    servercollection = db['servers']
    usercursor = usercollection.find()
    servercursor = servercollection.find()
    servercursore = servercollection.find()
    for userid in usercursor:
        if userid["isbotmod"] == "True":
            adminz.append(int(userid["userid"]))
        if message.author.id == int(userid['userid']):
            messages = int(userid['messages'])
            if int(userid['messages']) >= 50:
                message50=True
            if int(userid['messages']) >= 100:
                message100=True
    if len(message.attachments) > 0:
        attachments = True
        giffyavailable = False
    else:
        attachments = False
    try:
        if attachments == False:
            url= re.search("(?P<url>https?://[^\s]+)", message.content).group("url")
            image = (giffy.main(url))
            imgurl = url
            message.content = message.content.replace(imgurl, "")
            attachments = True
            giffyavailable = True
        else:
            attachments = True
    except:
        attachments = False
        giffyavailable = False
    print(attachments)
    await Logging("New Message!",f'User: ``{message.author} ({message.author.id})``\nUser Messages: ``{messages}``\nGuild: ``{message.guild.id}``\nAttachments: ``{attachments}``\nMessage: ``{message.content}``')
    if message.author.id in adminz and message.author.id != 763471049894527006:
        role = "Bot Moderator"
    elif message50 == True and message.author.id not in adminz and message.author.id != 763471049894527006 and message100 == False:
        role = "Chatter"
    elif message100 == True and message.author.id not in adminz and message.author.id != 763471049894527006:
        role = "Active Chatter"
    elif message.author.id == 763471049894527006:
        role = "Owner"
    else:
        role = "Member"
    conent = message.content
    author = message.author
    uk = pytz.timezone('Europe/London')
    embed = discord.Embed(description=conent, timestamp=datetime.now().astimezone(tz=uk), color=author.color)
    try:
        icon = message.author.guild_avatar.url
    except:
        icon = message.author.avatar.url
    username = author.name + "#" + author.discriminator + " - " + role
    embed.set_author(name=username, icon_url=icon)
    try :
        footer_icon_url = message.guild.icon.url
    except AttributeError:
        footer_icon_url = "https://ia903204.us.archive.org/4/items/discordprofilepictures/discordgrey.png"
    embed.set_footer(
        text=f"Message ID: {await get_random_string(10)}",
        icon_url = footer_icon_url
        )
    embed.set_thumbnail(url=icon)
    for guild in servercursore:
        if guild["guildid"] == message.guild.id:
            invite = guild["invite"]
    guildname = profanity.censor(message.guild.name)
    guildcheck = profanity.contains_profanity(message.guild.name)
    if invite == "null" or guildcheck == True:
        embed.add_field(name="", value=f" `📌`Sent From: {guildname} ・`🤖`[Bot-Invite](https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands)", inline=False)
    else:
        embed.add_field(name="", value=f" `📌`Sent From: [{guildname}]({invite}) ・`🤖`[Bot-Invite](https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands)", inline=False)
    if attachments == True:
        if giffyavailable == True:
            image = imgurl
            image = (giffy.main(image))
            if imgurl.startswith('https://sillydev.co.uk'):
                image = image[:-1]
            url = 'https://cdn.sillychat.tech/'  # Replace with the actual URL of your PHP script
            file_path = f"./temp/{image}"
            if file_path.endswith("None"):
                for server in servercursor:
                    guild: Guild = bot.get_guild(int(server["guildid"]))
                    if guild:
                        channel: TextChannel = guild.get_channel(int(server["channelid"]))
                        if channel:
                            perms: Permissions = channel.permissions_for(guild.get_member(bot.user.id))
                            if perms.send_messages:
                                if perms.embed_links and perms.attach_files and perms.external_emojis:
                                    await channel.send(embed=embed)
                                    await message.delete()
                return
            with open(file_path, 'rb') as file:
                files = {'file': file}
                data = {'auth_key': c['cdnkey']}
                response = requests.post(url, files=files, data=data)
            if response.status_code == 200:
                file_url = response.text
                try:
                    url=f"https://api.sillychat.tech/detectnsfw?url={file_url}&key={c['sillychatapikey']}"
                    response = requests.get(url)
                    result = json.loads(response.text)
                    result2 = result['data']['is_nsfw']
                except:
                    result2 = "Down"
            else:
                result2 = "Down"
        else:
            image = message.attachments[0].url
            try:
                url=f"https://api.sillychat.tech/detectnsfw?url={image}&key={c['sillychatapikey']}"
                response = requests.get(url)
                result = json.loads(response.text)
                result2 = result['data']['is_nsfw']
            except:
                result2 = "Down"
    if len(message.attachments) > 0:
        randomname = await get_random_string(8)
        await message.attachments[0].save(f'temp/{randomname}.png')
        url = 'https://cdn.sillychat.tech/'  # Replace with the actual URL of your PHP script
        file_path = f"./temp/{randomname}.png"
        with open(file_path, 'rb') as file:
            files = {'file': file}
            data = {'auth_key': c['cdnkey']}
            response = requests.post(url, files=files, data=data)
    for server in servercursor:
        guild: Guild = bot.get_guild(int(server["guildid"]))
        if guild:
            channel: TextChannel = guild.get_channel(int(server["channelid"]))
            if channel:
                if channel.id == message.channel.id:
                    perms: Permissions = channel.permissions_for(guild.get_member(bot.user.id))
                    print(perms.add_reactions)
                    if perms.add_reactions:
                        if len(message.attachments) > 0:
                            if message.attachments[0].url.endswith('mp4') or message.attachments[0].url.endswith('mov') or message.attachments[0].url.endswith('webm'):
                               await message.add_reaction("<a:sendfailed:937311948318572584>")
                        else:
                            try:
                                await message.add_reaction("<a:sent:937311880836436009>")
                            except:
                                await message.add_reaction("<a:sendfailed:937311948318572584>")
                    else:
                        try:
                            channel.send("ERROR: I seem to be missing required permissions! I require ``Add Reactions``\nThis message will go away once i recieve the permissions i require.\nYour message will still be sent.")
                        except:
                            pass
                else:
                    perms: Permissions = channel.permissions_for(guild.get_member(bot.user.id))
                    if perms.send_messages:
                        if perms.embed_links and perms.attach_files and perms.external_emojis:
                                try:
                                    if result2 == True or result2 == "true" or int(result['data']['hentai']) >= 60:
                                        await message.delete()
                                        user = message.author
                                        embed = discord.Embed(
                                            title=f"NSFW Detected!",
                                            description=f"Our Systems Have Detected NSFW In Your Image!\nIf you believe this is a mistake please contact our support.",
                                            color=0x662a85)
                                        await user.send(embed=embed)
                                        return
                                    elif result2 == "Down":
                                        embed = discord.Embed(
                                            title=f"Api Is Down! - Unable to send image",
                                            description=f"Our systems appear to be unable to handle the request, please try and send the image again later or contact support.",
                                            color=0x662a85)
                                        await message.author.send(embed=embed)
                                        return
                                    else:
                                        if giffyavailable == True:
                                            embed.set_image(url=file_url)
                                            await channel.send(embed=embed)
                                        else:
                                            if response.status_code == 200:
                                                file_url = response.text
                                            embed.set_image(url=file_url)
                                            await channel.send(embed=embed)
                                except Exception as e:
                                    #print(f"error: {e}")
                                    await channel.send(embed=embed)
                        else:
                            await channel.send('ERROR: I seem to be missing required permissions! I require ``Embed Links``, ``Manage Messages``,``Attach Files`` and ``External Emojis``\nThis message will go away once i recieve the permissions i require.')
    #await message.delete()
#Send All Impersonate
async def sendAllImpersonate(user, message):
    user = bot.get_user(user)
    adminz = []
    message50 = False
    message100 = False
    usercollection = db['users']
    servercollection = db['servers']
    usercursor = usercollection.find()
    servercursor = servercollection.find()
    servercursore = servercollection.find()
    for userid in usercursor:
        if userid["isbotmod"] == "True":
            adminz.append(int(userid["userid"]))
        if user.id == int(userid['userid']):
            messages = int(userid['messages'])
            if int(userid['messages']) >= 50:
                message50=True
            if int(userid['messages']) >= 100:
                message100=True
    if user.id in adminz and user.id != 763471049894527006:
        role = "Bot Moderator"
    elif message50 == True and user.id not in adminz and user.id != 763471049894527006 and message100 == False:
        role = "Chatter"
    elif message100 == True and user.id not in adminz and user.id != 763471049894527006:
        role = "Active Chatter"
    elif user.id == 763471049894527006:
        role = "Owner"
    else:
        role = "Member"
    conent = message
    author = user
    uk = pytz.timezone('Europe/London')
    embed = discord.Embed(description=conent, timestamp=datetime.now().astimezone(tz=uk), color=discord.Colour.random())
    icon = user.avatar.url
    username = user.name + "#" + user.discriminator + " - " + role
    embed.set_author(name=username, icon_url=icon)
    footer_icon_url = "https://ia903204.us.archive.org/4/items/discordprofilepictures/discordgrey.png"
    embed.set_footer(
        text=f"Message ID: {await get_random_string(10)}",
        icon_url = footer_icon_url
        )
    embed.set_thumbnail(url=user.avatar.url)
    embed.add_field(name="", value=f" `📌`Sent From: [3514](https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley) ・`🤖`[Bot-Invite](https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands)", inline=False)
    for server in servercursor:
        guild: Guild = bot.get_guild(int(server["guildid"]))
        if guild:
            channel: TextChannel = guild.get_channel(int(server["channelid"]))
            if channel:
                perms: Permissions = channel.permissions_for(guild.get_member(bot.user.id))
                if perms.send_messages:
                    if perms.embed_links and perms.attach_files and perms.external_emojis:
                        await channel.send(embed=embed)
                    else:
                        await channel.send('ERROR: I seem to be missing required permissions! I require ``Embed Links``, ``Manage Messages``,``Attach Files`` and ``External Emojis``\nThis message will go away once i recieve the permissions i require.')
    await message.delete()
#Slash Move Message
async def slashmovemessage(ctx):
    embed = discord.Embed(description="**Silly Chat Is Moving To Slash Commands!**\r\n"
    "</help:1071743627329548339> to view them!",
    color=0x2ecc71)
    return embed
#Cleanup Code (For Eval Command)
async def cleanup_code(content: str) -> str:
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])
        return content.strip('` \n')
#Gen Random String
async def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
#Ai Art
async def get_ai_art(prompt, ctx):
    key = c['dreamstudiokey']
    stability_api = aiclient.StabilityInference(
        key= key,
        verbose=True,
        engine="stable-diffusion-v1-5",
    )
    answers = stability_api.generate(
        prompt= prompt,
        steps=10,
        cfg_scale=20,
        width=512,
        height=512,
        samples=1,
        sampler=generation.SAMPLER_K_DPMPP_2M
    )
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                embed = discord.Embed(
                    title=f"Error!",
                    description=f"Your request activated the API's safety filters and was unable to be processed.\nPlease modify the prompt and try again.",
                    color=0x662a85
                    )
                await ctx.send(embed=embed)
            elif artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                filename = str(artifact.seed)
                img.save("temp/" + filename + ".png")
                embed = discord.Embed(
                    title=f"Success!",
                    description=f"Image Has Been Generated!",
                    color=discord.Color.random()
                    )
                file = discord.File(f"temp/{filename}.png", filename=f"{filename}.png")
                embed.set_image(url=f"attachment://{filename}.png")
                await ctx.send(file = file, embed=embed)
#Slash Ai Art
async def slash_get_ai_art(prompt, interaction):
    key = c['dreamstudiokey']
    await interaction.response.defer()
    stability_api = aiclient.StabilityInference(
        key= key,
        verbose=True,
        engine="stable-diffusion-v1-5",
    )
    answers = stability_api.generate(
        prompt= prompt,
        steps=10,
        cfg_scale=20,
        width=512,
        height=512,
        samples=1,
        sampler=generation.SAMPLER_K_DPMPP_2M
    )
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                embed = discord.Embed(
                    title=f"Error!",
                    description=f"Your request activated the API's safety filters and could not be processed.\nPlease modify the prompt and try again.",
                    color=0x662a85
                    )
                await interaction.followup.send(embed=embed)
            elif artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                filename = str(artifact.seed)
                img.save("temp/" + filename + ".png")
                embed = discord.Embed(
                    title=f"Success!",
                    description=f"Image Has Been Generated!",
                    color=discord.Color.random()
                    )
                file = discord.File(f"temp/{filename}.png", filename=f"{filename}.png")
                embed.set_image(url=f"attachment://{filename}.png")
                await interaction.followup.send(file = file, embed=embed)
#System Message
async def sendsystemmessage(systemmessage):
    conent = str(systemmessage)
    uk = pytz.timezone('Europe/London')
    embed = discord.Embed(description=conent, timestamp=datetime.now().astimezone(tz=uk), color=0xe74c3c)
    embed.set_author(name="SYSTEM MESSAGE", icon_url=bot.user.avatar.url)
    embed.set_thumbnail(url=bot.user.avatar.url)
    embed.add_field(name="", value="`📌`[Support](https://discord.gg/3qvpkgWSbF)・`🤖`[Bot-Invite](https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands)", inline=False)
    servercollection = db['servers']
    servercursor = servercollection.find()
    for server in servercursor:
        guild: Guild = bot.get_guild(int(server["guildid"]))
        if guild:
            channel: TextChannel = guild.get_channel(int(server["channelid"]))
            if channel:
                perms: Permissions = channel.permissions_for(guild.get_member(bot.user.id))
                if perms.send_messages:
                    if perms.embed_links and perms.attach_files and perms.external_emojis:
                            await channel.send(embed=embed)
                    else:
                        await channel.send('ERROR: I seem to be missing required permissions! I require ``Embed Links``, ``Manage Messages``,``Attach Files`` and ``External Emojis``\nThis message will go away once i recieve the permissions i require.')
#Event for when someone puts @ai at the start of their message
async def sendAiAll(response):
    conent = str(response)
    gb = pytz.timezone('Europe/London')
    embed = discord.Embed(description=conent, timestamp=datetime.now().astimezone(tz=gb), color=0xe74c3c)
    embed.set_author(name="Darren#2740 - Ai", icon_url="https://images-ext-1.discordapp.net/external/aNOrIabEcGhxu0RnS-8dChSto7vRkGnEEbceZzEKWwE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1026047715622264873/768afbc6b70691ae2062c1331cb37b1e.png?width=670&height=670")
    embed.set_footer(text=f'@ai [message] to use me ',icon_url='https://images-ext-1.discordapp.net/external/aNOrIabEcGhxu0RnS-8dChSto7vRkGnEEbceZzEKWwE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1026047715622264873/768afbc6b70691ae2062c1331cb37b1e.png?width=670&height=670')
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/aNOrIabEcGhxu0RnS-8dChSto7vRkGnEEbceZzEKWwE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1026047715622264873/768afbc6b70691ae2062c1331cb37b1e.png?width=670&height=670")
    embed.add_field(name="", value="`📌`[Support](https://discord.gg/3qvpkgWSbF)・`🤖`[Bot-Invite](https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands)", inline=False)
    servercollection = db['servers']
    servercursor = servercollection.find()
    for server in servercursor:
        guild: Guild = bot.get_guild(int(server["guildid"]))
        if guild:
            channel: TextChannel = guild.get_channel(int(server["channelid"]))
            if channel:
                perms: Permissions = channel.permissions_for(guild.get_member(bot.user.id))
                if perms.send_messages:
                    if perms.embed_links and perms.attach_files and perms.external_emojis:
                            await channel.send(embed=embed)
                    else:
                        await channel.send('ERROR: I seem to be missing required permissions! I require ``Embed Links``, ``Manage Messages``,``Attach Files`` and ``External Emojis``\nThis message will go away once i recieve the permissions i require.')
#Event for when someone sets up the bot with slash commands
async def slashsendAllWelcome(interaction):
    try :
        footer_icon_url = interaction.guild.icon.url
    except AttributeError:
        footer_icon_url = "https://ia903204.us.archive.org/4/items/discordprofilepictures/discordgrey.png"
    guildname = profanity.censor(interaction.guild.name)
    uk = pytz.timezone('Europe/London')
    embed = discord.Embed(
        title=f"Welcome!",
        description=f'Thank you {guildname} for adding the bot!\nIf you experience any issues please join our support server!',
        color=0x662a85,
        timestamp=datetime.now().astimezone(tz=de))
    embed.set_footer(text=f'Message ID: {await get_random_string(10)} | {interaction.guild.member_count} Members!',
                     icon_url=f'{footer_icon_url}')
    embed.set_thumbnail(url=footer_icon_url)
    embed.add_field(name="", value=f"Silly Chat Is Now In {len(bot.guilds)} Servers!", inline=False)
    embed.add_field(name="", value="`📌`[Support](https://discord.gg/3qvpkgWSbF)・`🤖`[Bot-Invite](https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands)", inline=False)
    servercollection = db['servers']
    servercursor = servercollection.find()
    for server in servercursor:
        guild: Guild = bot.get_guild(int(server["guildid"]))
        if guild:
            channel: TextChannel = guild.get_channel(int(server["channelid"]))
            if channel:
                await channel.send(embed=embed)
#Bot join event
@bot.event
async def on_guild_join(guild):
    if len(bot.guilds) == servcountgoal:
        await Logging("Joined Server | Goal Reached!",f'**{len(bot.guilds)}** Servers!')
    else:
        await Logging("Joined Server!",f'I Have Been Added To ``{guild.name}``!\nI am now in {len(bot.guilds)} Servers\nAway From Goal: {servcountgoal - len(bot.guilds)} Servers')
#Bot leave event
@bot.event
async def on_guild_remove(guild):
    await Logging("Left Server!",f'I Have Been Removed From ``{guild.name}``!\nI am now in {len(bot.guilds)} Servers\nAway From Goal: {servcountgoal - len(bot.guilds)} Servers')
#------------------------------------------Command Menus-------------------------------------------------
#Help Command 
class HelpMenu(discord.ui.View):
  def _init_(self):
         super()._init_()
         self.value = None
  @discord.ui.button(label="Setup", style=discord.ButtonStyle.grey, emoji="🧰")
  async def setupmenu(self, interaction: discord.Interaction, button: discord.ui.Button):
    embed = discord.Embed(
            title="**Silly Chat - Setup**",
            description=f"**Version: {botversion}**",
            color=discord.Color.random()
        )
    embed.add_field(name="</setglobal:1074285744765554789>", value="Add global chat to a channel!", inline=False)
    embed.add_field(name="</removeglobal:1074278902987489320>", value="Remove global chat from a channel!", inline=False)
    embed.add_field(name="</setinvite:1078747763401035866>", value="Add invite link!", inline=False)
    embed.add_field(name="</removeinvite:1078747763401035867>", value="Remove invite link!", inline=False)
    embed.set_footer(text="Thank You For Using Silly Chat!")
    embed.set_thumbnail(url=bot.user.avatar.url)
    await interaction.response.edit_message(embed=embed)
  @discord.ui.button(label="Info", style=discord.ButtonStyle.grey, emoji="<:info:1071407819670175774>")
  async def infomenu(self, interaction: discord.Interaction, button: discord.ui.Button):
    embed = discord.Embed(
            title="**Silly Chat - Info**",
            description=f"**Version: {botversion}**",
            color=discord.Color.random()
        )
    embed.add_field(name="</rules:1079002951265300540>", value="Check the bot's rules", inline=False)
    embed.add_field(name="</ping:1071740263208325192>", value="Check the bot's ping", inline=False)
    embed.add_field(name="</stats:1071520283866976317>", value="Check the bot's stats!", inline=False)
    embed.add_field(name="</invite:1071740263208325193>", value="Invite me to your server!", inline=False)
    embed.add_field(name="</support:1071517092844675143>", value="Get a link to our support server!", inline=False)
    embed.add_field(name="</github:1071518618933796934>", value="Get a link to the bot's github!", inline=False)
    embed.add_field(name="</credits:1071518616090050651>", value="View the creators of the bot!", inline=False)
    embed.add_field(name="</vote:1071520283866976316>", value="Vote for the bot!", inline=False)
    embed.add_field(name="</leaderboard:1105192668356694111>", value="View the leaderboard!", inline=False)
    embed.add_field(name="</modlist:1105192668356694109>", value="View the bot moderators!", inline=False)
    embed.add_field(name="</tutorial:1108848275475398868>", value="View the bot tutorial!", inline=False)
    embed.set_footer(text="Thank You For Using Silly Chat!")
    embed.set_thumbnail(url=bot.user.avatar.url)
    await interaction.response.edit_message(embed=embed)
  @discord.ui.button(label="Fun", style=discord.ButtonStyle.grey, emoji="🤣")
  async def funmenu(self, interaction: discord.Interaction, button: discord.ui.Button):
    embed = discord.Embed(
            title="**Silly Chat - Fun**",
            description=f"**Version: {botversion}**",
            color=discord.Color.random()
        )
    embed.add_field(name="</ai:1074363775953682635>", value="Chat to Darren!", inline=False)
    embed.add_field(name=f"{c['prefix']}cat", value="Generate an image of a cat!", inline=False)
    embed.add_field(name=f"{c['prefix']}dog", value="Generate an image of a dog!", inline=False)
    embed.add_field(name=f"{c['prefix']}8ball", value="Use Magic 8 Ball!", inline=False)
    embed.add_field(name=f"{c['prefix']}joke", value="Generate A Random Joke!", inline=False)
    embed.add_field(name=f"{c['prefix']}coffee", value="Generate A Coffee!", inline=False)
    embed.add_field(name=f"{c['prefix']}coinflip", value="Flip A Coin!", inline=False)
    embed.add_field(name=f"{c['prefix']}kill", value="Kill Someone!", inline=False)
    embed.add_field(name=f"{c['prefix']}meme", value="Generate A Meme!", inline=False)
    embed.add_field(name=f"{c['prefix']}donaldtweet",value="Post a tweet as Donald Trump.",inline=False)
    embed.add_field(name=f"{c['prefix']}texttobraille",value="Convert text into braille.",inline=False)
    embed.add_field(name="</aiart:1079002951265300541>", value="Generate Art Using Ai!", inline=False)
    embed.add_field(name="</aiart2:1105192668356694110>", value="Generate Art Using A Slower Ai!", inline=False)
    embed.set_footer(text="Thank You For Using Silly Chat!")
    embed.set_thumbnail(url=bot.user.avatar.url)
    await interaction.response.edit_message(embed=embed)
  @discord.ui.button(label="Utility", style=discord.ButtonStyle.grey, emoji="<:Maintenance:926794294017286165>")
  async def utilitymenu(self, interaction: discord.Interaction, button: discord.ui.Button):
    embed = discord.Embed(
            title="**Silly Chat - Utility**",
            description=f"**Version: {botversion}**",
            color=discord.Color.random()
        )
    embed.add_field(name=f"{c['prefix']}avatar", value="Steal Someone's Avatar!", inline=False)
    embed.add_field(name=f"{c['prefix']}nsfwrating", value="Get the nsfw rating of an image!", inline=False)
    embed.add_field(name=f"{c['prefix']}userinfo", value="Get a user's discord info!", inline=False)
    embed.add_field(name=f"{c['prefix']}serverinfo", value="Get info on the server!", inline=False)
    embed.add_field(name=f"{c['prefix']}web", value="Generate a screenshot of a website!", inline=False)
    embed.add_field(name="</report:1079002951265300542>", value="Report Someone Breaking Silly Chat Rules!", inline=False)
    embed.set_footer(text="Thank You For Using Silly Chat!")
    embed.set_thumbnail(url=bot.user.avatar.url)
    await interaction.response.edit_message(embed=embed)
  @discord.ui.button(label="Bot Moderator", style=discord.ButtonStyle.grey, emoji="<:Role:942348530117410826>")
  async def botmodmenu(self, interaction: discord.Interaction, button: discord.ui.Button):
    embed = discord.Embed(
            title="**Silly Chat - Bot Moderator**",
            description=f"**Version: {botversion}**",
            color=discord.Color.random()
        )
    embed.add_field(name=f"{c['prefix']}ban", value="Ban a user from using the bot!", inline=False)
    embed.add_field(name=f"{c['prefix']}unban", value="Remove a user from the banned list!", inline=False)
    embed.add_field(name=f"{c['prefix']}deletemessage", value="Delete a message!", inline=False)
    embed.set_footer(text="Thank You For Using Silly Chat!")
    embed.set_thumbnail(url=bot.user.avatar.url)
    await interaction.response.edit_message(embed=embed)
#Tutorial Command 
class TutorialMenu(discord.ui.View):
  def __init__(self, userid):
         super().__init__()
         self.value = None
         self.userid = userid
  @discord.ui.button(label="Setup", style=discord.ButtonStyle.grey, emoji="🧰")
  async def SetupTutorial(self, interaction: discord.Interaction, button: discord.ui.Button):
    if interaction.user.id == self.userid:
        embed = discord.Embed(
            title="**Silly Chat - Setup Tutorial**",
            description=f"**Version: {botversion}**",
            color=discord.Color.random()
        )
        file = discord.File("images/tutorial2.png", filename="tutorial.png")
        embed.set_image(url="attachment://tutorial.png")
        embed.add_field(name="</setglobal:1074285744765554789>", value="Add global chat to a channel!", inline=False)
        embed.add_field(name="</setinvite:1078747763401035866>", value="Add invite link!", inline=False)
        embed.set_footer(text="Thank You For Using Silly Chat!")
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/8lntiVCa9JwRxnqX6rxvWdEWWmwIiz5xFeTxmdRSydE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1051199485168066610/d40794f36524ec9e9a4e723679d14d6d.png?width=603&height=603")
        await interaction.response.edit_message(embed=embed, attachments=[file])
    else:
        embed = discord.Embed(
            title="**Silly Chat - Setup Tutorial**",
            description=f"**Version: {botversion}**",
            color=discord.Color.random()
        )
        file = discord.File("images/tutorial2.png", filename="tutorial.png")
        embed.set_image(url="attachment://tutorial.png")
        embed.add_field(name="</setglobal:1074285744765554789>", value="Add global chat to a channel!", inline=False)
        embed.add_field(name="</setinvite:1078747763401035866>", value="Add invite link!", inline=False)
        embed.set_footer(text="Thank You For Using Silly Chat!")
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/8lntiVCa9JwRxnqX6rxvWdEWWmwIiz5xFeTxmdRSydE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1051199485168066610/d40794f36524ec9e9a4e723679d14d6d.png?width=603&height=603")
        await interaction.response.send_message(embed=embed, file=file, ephemeral=True)
  @discord.ui.button(label="Usage", style=discord.ButtonStyle.grey, emoji="🕵️‍♀️")
  async def UsageTutorial(self, interaction: discord.Interaction, button: discord.ui.Button):
    if interaction.user.id == self.userid:
        embed = discord.Embed(
            title="**Silly Chat - Usage Tutorial**",
            description=f"**Version: {botversion}**",
            color=discord.Color.random()
        )
        file = discord.File("images/tutorial3.png", filename="tutorial.png")
        embed.set_image(url="attachment://tutorial.png")
        embed.set_footer(text="Thank You For Using Silly Chat!")
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/8lntiVCa9JwRxnqX6rxvWdEWWmwIiz5xFeTxmdRSydE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1051199485168066610/d40794f36524ec9e9a4e723679d14d6d.png?width=603&height=603")
        await interaction.response.edit_message(embed=embed, attachments=[file])
    else:
        embed = discord.Embed(
            title="**Silly Chat - Usage Tutorial**",
            description=f"**Version: {botversion}**",
            color=discord.Color.random()
        )
        file = discord.File("images/tutorial3.png", filename="tutorial.png")
        embed.set_image(url="attachment://tutorial.png")
        embed.set_footer(text="Thank You For Using Silly Chat!")
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/8lntiVCa9JwRxnqX6rxvWdEWWmwIiz5xFeTxmdRSydE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1051199485168066610/d40794f36524ec9e9a4e723679d14d6d.png?width=603&height=603")
        await interaction.response.send_message(embed=embed, file=file, ephemeral=True)
class StatsDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label='Bot Stats', description='View bot stats', emoji='<:bot:1110634062776901662>'),
            discord.SelectOption(label='Server Stats', description='View the bot server stats', emoji='<:servers:1107262987145838612>'),
            discord.SelectOption(label='Other Stats', description='View other stats', emoji='❓'),
        ]
        super().__init__(placeholder='Silly Chat', min_values=1, max_values=1, options=options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == 'Bot Stats':
            usercount = len(list(filter(lambda m: m.bot == False, bot.users)))
            count = 0
            servercollection = db['servers']
            servercursor = servercollection.find()
            for server in servercursor:
                count = count + 1
            embed = discord.Embed(
            title="**Silly Chat - Bot Stats**",
            color=discord.Color.random()
            )
            embed.add_field(name="👑Bot Owner", value="Gamer3514#7679 - 763471049894527006", inline=False)
            embed.add_field(name="<:Python:1092114615095283772>Bot Version", value=f"{botversion}", inline=False)
            embed.add_field(name="<:servers:1107262987145838612>Server Count", value=f"{len(bot.guilds)}", inline=False)
            embed.add_field(name="<a:users:1107263168021012500>User Count", value=f"{usercount}", inline=False)
            embed.add_field(name="<:channel:942348293759979521>Connected Channels", value=f"{count}", inline=False)
            embed.add_field(name="🏓Bot Latency", value=f"{round(bot.latency * 1000)}ms", inline=False)
            embed.add_field(name="✏️Creation Date", value=f"10/12/22 (10th December 2022)", inline=False)
            embed.set_footer(text=f"Requested by {interaction.user}")
            embed.set_thumbnail(url=bot.user.avatar.url)
            await interaction.response.edit_message(embed=embed)
        elif self.values[0] == 'Server Stats':
            embed = discord.Embed(
            title="**Silly Chat - Server Stats**",
            color=discord.Color.random()
            )
            embed.add_field(name="<:Ubuntu:1107261447790153758>OS", value=platform.system(), inline=False)
            embed.add_field(name="<:CPU:1107261665260621894>Cpu Cores", value=multiprocessing.cpu_count(), inline=False)
            embed.add_field(name="<:CPU:1107261665260621894>Cpu Usage", value=f"{psutil.cpu_percent()}%", inline=False)
            embed.add_field(name="<:Ram:1107261980437385337>Memory Usage", value=f"{psutil.virtual_memory().percent}%", inline=False)
            embed.add_field(name="<:Ram:1107261980437385337>Total Memory", value=f"{round(psutil.virtual_memory().total / (1024.0 **3))} GB", inline=False)
            embed.add_field(name="<:Python:1092114615095283772>Python Version", value=platform.python_version(), inline=False)
            embed.add_field(name="<:dpy:1107262368272093215>Discord.py Version", value=version('discord.py'), inline=False)
            embed.set_footer(text=f"Requested by {interaction.user}")
            embed.set_thumbnail(url=bot.user.avatar.url)
            await interaction.response.edit_message(embed=embed)
        elif self.values[0] == 'Other Stats':
            embed = discord.Embed(
            title="**Silly Chat - Other Stats**",
            color=discord.Color.random()
            )
            file = open("main.py", errors="ignore")
            data = file.read()
            number_of_characters = len(data)
            lines = sum(1 for line in open('main.py', errors='ignore'))
            giffy = os.listdir('./giffy')
            tests = os.listdir('./tests')
            for file in giffy:
                if file.endswith('.py') or file.endswith('.pyc'):
                    dafile = open(f"./giffy/{file}", errors="ignore")
                    data = dafile.read()
                    number_of_characters = number_of_characters + len(data)
                    lines = lines + sum(1 for line in open(f"./giffy/{file}", errors='ignore'))
            for file in tests:
                if file.endswith('.py') or file.endswith('.pyc') or file.endswith('.json'):
                    dafile = open(f"./tests/{file}", errors="ignore")
                    data = dafile.read()
                    number_of_characters = number_of_characters + len(data)
                    lines = lines + sum(1 for line in open(f"./tests/{file}", errors='ignore'))
            embed.add_field(name="<:VSCode:1107263369175646258>Lines Of Code", value=f"{lines}", inline=False)
            embed.add_field(name="<:VSCode:1107263369175646258>Characters Of Code", value=f"{number_of_characters}", inline=False)
            embed.set_footer(text=f"Requested by {interaction.user}")
            embed.set_thumbnail(url=bot.user.avatar.url)
            await interaction.response.edit_message(embed=embed)
        else:
            embed = discord.Embed(
            title="**Silly Chat - Error!**",
            description=f"**Version: {botversion}**",
            color=discord.Color.random()
            )
            embed.add_field(name="**Error!**", value=f"An error occured! Please try again later!", inline=False)
            embed.set_footer(text=f"Requested by {interaction.user}")
            embed.set_thumbnail(url=bot.user.avatar.url)
            await interaction.response.edit_message(embed=embed)
class StatsView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(StatsDropdown())
#------------------------------------------Prefix Bot Commands (User)-------------------------------------------------
#DEPRECATED  Command
@bot.command(aliases=['help','ai','invite','ping','youtube','tiktok','stats','vote','github','credits','support','removeInvite','setInvite','removeGlobal','setGlobal'])
async def DEPRECATED(ctx):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}**DEPRECATED** command")
    embed = await slashmovemessage(ctx)
    await ctx.send(embed=embed)
#Web capture Command
@bot.command(aliases=['webcapture','webshot','screenshot'])
async def web(ctx,*,url):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}web {url}")
    try:
        votecheck = requests.get(f'https://top.gg/api/bots/1051199485168066610/check?userId={ctx.author.id}', headers={'Authorization': c['topggauthkey']})
        votecheck = json.loads(votecheck.text)
        if int(votecheck['voted']) == 1:
            embed = discord.Embed(
                title="**Silly Chat - Web Capture**",
                color=discord.Color.random()
            )
            output_path = f'temp/{ctx.author.id}-webcapture.png'
            if "porn" in url:
                embed.add_field(name="**NSFW Detected!**", value="NSFW was detected in the website! Please try again!", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author}")
                return await ctx.send(embed=embed)
            take_screenshot(url, output_path)
            await asyncio.sleep(1.978)
            with open(output_path, 'rb') as file:
                url = "https://cdn.sillychat.tech"
                files = {'file': file}
                data = {'auth_key': c['cdnkey']}
                response = requests.post(url, files=files, data=data)
            cdnresponse = response.text
            apiurl=f"https://api.sillychat.tech/detectnsfw?url={cdnresponse}&key={c['sillychatapikey']}"
            response = requests.get(apiurl)
            result = json.loads(response.text)
            result2 = result['data']['is_nsfw']
            if result2 == True:
                embed.add_field(name="**NSFW Detected!**", value="NSFW was detected in the website! Please try again!", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author}")
                return await ctx.send(embed=embed)
            if response.status_code == 200:
                embed.set_image(url=cdnresponse)
                embed.add_field(name="**Success!**", value="The website was captured successfully!\nIf it did not load correctly, please report the issue", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author}")
                await ctx.send(embed=embed)
            else:
                embed.add_field(name="**Error!**", value="An error occured! Please try again later!", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author}")
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="**Silly Chat - Web Capture**",
                color=discord.Color.random()
            )
            embed.add_field(name="**Error!**", value="This command has been locked to voters only.\nYou can vote [here](https://top.gg/bot/1051199485168066610/vote)", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)
    except:
        embed = discord.Embed(
                title="**Silly Chat - Web Capture**",
                color=discord.Color.random()
            )
        embed.add_field(name="**Error!**", value="An error occured! Please try again later!", inline=False)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
#Rules Command
@bot.command()
async def rules(ctx):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}rules")
    embed = discord.Embed(
            title="**Silly Chat - Rules**",
            color=discord.Color.blue()
        )
    embed.add_field(name="**1. Have respect**", value="You should always be friendly to other user of Silly Chat. We aim a nice and friendly community, not a toxic community.", inline=False)
    embed.add_field(name="**2. No NSFW**", value="No sending NSFW at all. Doing so will get you banned with no Appeal (if it gets past filters)!", inline=False)
    embed.add_field(name="**3. Don't Spam**", value="Spamming is not just sending messages in quick repetition, but is also sending the same message over and over again, intentionally splitting sentences up into different messages.example: message 1: ``hi`` message 2: ``how`` message 3: ``are`` message 4: ``you?``!", inline=False)
    embed.add_field(name="**4. Use Common Sense**", value="There are some common rules, that are not mentioned here, but it is the most logical thing to follow them. The easiest way to know them is to think for 2 seconds before sending messages.", inline=False)
    embed.add_field(name="**5. No Advertising**", value="No advertising of any kind. This includes, but is not limited to: Discord servers, YouTube channels, Twitch channels, etc. Doing so will get you banned with no Appeal!", inline=False)
    embed.add_field(name="**6. No Racism**", value="No racism of any kind. Doing so will get you banned with no Appeal!", inline=False)
    embed.add_field(name="**7. No Toxicity**", value="No toxicity of any kind. Doing so will get you banned with no Appeal!", inline=False)
    embed.set_footer(text="Thank You For Using Silly Chat!")
    embed.set_thumbnail(url=bot.user.avatar.url)
    await ctx.send(embed=embed)
#Groot Command
@bot.command()
async def groot(ctx):
    grootimages = ["https://cdn.s7.shopdisney.eu/is/image/DisneyStoreES/461033153499?fmt=jpeg&qlt=90&wid=652&hei=652&defaultImage=no-image-image_uk", "https://hips.hearstapps.com/digitalspyuk.cdnds.net/17/11/1489667130-baby-groot-switches-guardians-of-the-galaxy-vol-2.jpg?crop=1.00xw:0.883xh;0,0.0372xh&resize=1200:*", "https://images.bauerhosting.com/legacy/media/5d4c/0143/e091/db00/be8b/19e2/GrootPuke.jpg?format=jpg&quality=80&width=960&height=540&ratio=16-9&resize=aspectfill", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSTnDA6LeAhWmcEGQcCgPyu_pSMsz2yWKzuQ&usqp=CAU", "https://cdn.marvel.com/content/1x/024grt_ons_crd_02.jpg", "https://cdn.europosters.eu/image/750/posters/guardians-of-the-galaxy-vol-2-angry-groot-i40497.jpg", "https://cdn.europosters.eu/image/1300/posters/guardians-of-the-galaxy-vol-2-groot-i64376.jpg", "https://m.media-amazon.com/images/M/MV5BNDAxODI2NTctZGQ3NC00ZDgyLTk1ZGEtMjNiMDUxOWExOWM1XkEyXkFqcGdeQWRpZWdtb25n._V1_.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkj0EN4OOpsizsUmzpRoDRWkNHZbS6LjRrDQ&usqp=CAU", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPMCRVXXn8U29LfX7TmseGs9t0V7CGucTUug&usqp=CAU", "https://www.sideshow.com/wp/wp-content/uploads/2017/05/marvel-guardians-of-the-galaxy-groot-life-size-figure-hot-toys-feature-903025.jpg", "https://d23.com/app/uploads/2022/08/00_1180w-600h_groot_080222.jpg"]
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}groot")
    embed = discord.Embed(title="I AM GROOT!", color=0xa58a61)
    embed.set_image(url=random.choice(grootimages))
    embed.set_footer(text="Thank You For Using Silly Chat!")
    await ctx.send(embed=embed)
#Coin Flip Command
@bot.command(aliases=['headsortails'])
async def coinflip(ctx):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}coinflip")
    embed=discord.Embed(title="Coinflip", description=heads_tails[random.randint(0, len(heads_tails)-1)], color=0xFCBA03)
    embed.set_footer(text="Thank You For Using Silly Chat!")
    await ctx.send(embed=embed)
#8Ball Command
@bot.command(aliases=['8ball'])
async def magic8ball(ctx):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}8ball")
    embed=discord.Embed(title=":8ball: Magic 8 Ball :8ball:", description=ball8answers[random.randint(0, len(ball8answers)-1)], color=0xFCBA03)
    embed.set_footer(text="Thank You For Using Silly Chat!")
    await ctx.send(embed=embed)
#Meme Command
@bot.command(aliases=['genmeme'])
async def meme(ctx):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}meme")
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://meme-api.com/gimme") as resp:
            data = await resp.json()
            embed = discord.Embed(title=f"Meme Generated! - {data['title']}",color=discord.Color.random())
            embed.set_image(url=f"{data['url']}")
            randfooter = ["Thank You for using Silly Chat!", "Did You Know? Silly Chat is owned by Gamer3514#7679!"]
            embed.set_footer(text=randfooter[random.randint(0, len(randfooter)-1)])
            await ctx.send(embed=embed)
#Hitman Command
@bot.command(aliases=['hitman'])
async def kill(ctx, person : discord.Member = None):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}kill")
    randfooter = ["Thank You for using Silly Chat!", "Did You Know? Silly Chat is owned by Gamer3514#7679!"]
    if not person:
            embed=discord.Embed(title="No User Selected", description=f"Correct Usage:\n{c['prefix']}kill @user\n{c['prefix']}hitman userid", color=0xFCBA03)
            embed.set_footer(text=randfooter[random.randint(0, len(randfooter)-1)])
            await ctx.send(embed=embed)
    embed = discord.Embed(title=f"DEAD!", description=f"{person.mention} {random.choice(deathoptions)}")
    embed.set_footer(text=randfooter[random.randint(0, len(randfooter)-1)])
    await ctx.send(embed=embed)
#Rock Command
@bot.command(aliases=['genrock'])
async def rock(ctx):
  await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}rock")
  async with aiohttp.ClientSession() as session:
    async with session.get("https://rockapi.apiworks.tech/rock/random") as api:
        data = await api.json()
        rok_name = data["name"]
        rok_desc = data["description"]
        rok_img = data["image"]
        embed = discord.Embed(title=rok_name, description=rok_desc)
        if not rok_img == "none":
            embed.set_image(url=rok_img)
        embed.set_footer(text="Thank You For Using Silly Chat!")
        await ctx.send(embed=embed)
#Coffee Command
@bot.command(aliases=['gencoffee'])
async def coffee(ctx):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}coffee")
    async with aiohttp.ClientSession() as session:
        async with session.get("https://coffee.alexflipnote.dev/random.json") as api:
            data = await api.json()
            coffee_img = data["file"]
            embed = discord.Embed(title="Generated!")
            embed.set_footer(text="Thank You For Using Silly Chat!")
            embed.set_image(url=coffee_img)
            await ctx.send(embed=embed)
#Avatar Command
@bot.command()
async def avatar(ctx,  member: discord.Member = None):
        await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}avatar {member}")
        if not member:
            member = ctx.author
        embed = discord.Embed(colour=discord.Colour.random(), title=f"{member}'s avatar")
        embed.set_footer(text="Thank You For Using Silly Chat!")
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)
#Ai Art Command
@bot.command()
async def aiart(ctx, *, prompt = None):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}aiart {prompt}")
    usercollection = db['users']
    usercursor = usercollection.find()
    for userid in usercursor:
        if userid['userid'] == ctx.author.id:
            if int(userid['messages']) >= 150:
                canuse = True
            else:
                canuse = False
    if canuse == True:
        if prompt == None:
            embed = discord.Embed(
                title = f'Error!',
                description = "No input Provided!",
                color=0x662a85)
            await ctx.send(embed=embed)
        else:
            await get_ai_art(prompt, ctx)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You need to send 150 messages on Silly Chat to be able to use this command!",
            color=0x662a85)
        embed.set_footer(text="Sorry for the inconvenience! Once we have more resources we will remove this limit!")
        await ctx.send(embed=embed)
#NSFW Rating Command
@bot.command(name='nsfwrating', aliases=['imageraiting'])
async def nsfwrating(ctx):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}nsfwrating")
    attachments = ctx.message.attachments
    if len(attachments) > 0:
            image = ctx.message.attachments[0].url
            url=f"https://api.sillychat.tech/detectnsfw?url={image}&key={c['sillychatapikey']}"
            response = requests.get(url)
            result = json.loads(response.text)
            result2 = result['data']['is_nsfw']
            embed = discord.Embed(
            title = f'Image Scanned!',
            description = f"**Nsfw:**\n{result2}\n**Advanced Ratings:**\nDrawings = {result['data']['drawings']}\nHentai = {result['data']['hentai']}\nNeutral = {result['data']['neutral']}\nPorn = {result['data']['porn']}\nSexy = {result['data']['sexy']}",
            color=0x662a85)
            embed.add_field(name="", value=f" `📌`Command Powered By: [Silly Chat Api](https://api.sillychat.tech/)", inline=False)
            await ctx.send(embed=embed)
    else:
            embed = discord.Embed(
            title = f'Error!',
            description = "You have not provided an image to scan!",
            color=0x662a85)
            await ctx.send(embed=embed)
#Userinfo Command
@bot.command(name='userinfo', aliases=['infouser'])
async def userinfo(ctx,  member: discord.Member = None):
    bannedusers = []
    usercollection = db['users']
    usercursor = usercollection.find()
    for userid in usercursor:
        if userid["isbanned"] == "True":
            bannedusers.append(int(userid["userid"]))
    if not member:
            member = ctx.author
    if member.id in bannedusers:
        banned = True
    else:
        banned = False
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}userinfo {member}")
    try:
        embed = discord.Embed(
            color=0x662a85)
        roles = list(member.roles)
        embed.set_author(name=f"User Info - {member}")
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Display Name:", value=member.display_name)
        embed.add_field(name="Created Account:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Server:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name=f"Roles ({len(roles)}):", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Top Role:", value=member.top_role.mention)
        embed.add_field(name="Bot:", value=member.bot)
        embed.add_field(name="Bot Banned:", value=(banned))
        embed.add_field(name="User Password:", value=f"||{await get_random_string(5)}-notreal||")
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(
            title = f'{member}',
            description = f"Error occured! Please try again later.",
            color=0x662a85)
        await ctx.send(embed=embed)
#Serverinfo Command
@bot.command()  
async def serverinfo(ctx):
    role_count = len(ctx.guild.roles)
    if ctx.guild.id == 921530640510382100:
        supportserver = True
    else:
        supportserver = False
    emoji_count = len(ctx.guild.emojis)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
    embed = discord.Embed(title=f"Server Info - {ctx.guild.name}", color=discord.Color.random())
    embed.add_field(name="Server ID", value=ctx.guild.id, inline=False)
    embed.add_field(name="Server Owner", value=ctx.guild.owner, inline=False)
    embed.add_field(name="Silly Chat Support Server", value=supportserver, inline=False)
    embed.add_field(name="Verification Level", value=ctx.guild.verification_level, inline=False)
    embed.add_field(name="Total Members", value=ctx.guild.member_count, inline=False)
    embed.add_field(name="Total Bots", value=len(list_of_bots), inline=False)
    embed.add_field(name="Total Text Channels", value=len(ctx.guild.text_channels), inline=False)
    embed.add_field(name="Total Voice Channels", value=len(ctx.guild.voice_channels), inline=False)
    embed.add_field(name="Total Categories", value=len(ctx.guild.categories), inline=False)
    embed.add_field(name="Total Roles", value=role_count, inline=False)
    embed.add_field(name="Total Emojis", value=emoji_count, inline=False)
    embed.add_field(name="Created At", value=ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}")
    try:
        embed.set_thumbnail(url=ctx.guild.icon.url)
    except:
        embed.set_thumbnail(url="https://ia903204.us.archive.org/4/items/discordprofilepictures/discordgrey.png")
    await ctx.send(embed=embed)
#Cat Command
@bot.command(aliases=['catimage'])
async def cat(ctx):
    response = requests.get(f"https://api.sillychat.tech/cat?key={c['sillychatapikey']}", stream=True)
    with open('temp/cat.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}cat")
    embed=discord.Embed(title="Cat 🐈", colour=discord.Colour.random())
    file = discord.File("temp/cat.png", filename="cat.png")
    embed.set_image(url="attachment://cat.png")
    embed.set_footer(text="Thank You For Using Silly Chat!")
    await ctx.send(file=file,embed=embed)
#Dog Command
@bot.command(aliases=['dogimage'])
async def dog(ctx):
    response = requests.get(f"https://api.sillychat.tech/dog?key={c['sillychatapikey']}", stream=True)
    with open('temp/dog.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}dog")
    embed=discord.Embed(title="Dog 🐕", colour=discord.Colour.random())
    file = discord.File("temp/dog.png", filename="dog.png")
    embed.set_image(url="attachment://dog.png")
    await ctx.send(file=file,embed=embed)
#donaldtweet Command
@bot.command(aliases=['trumptweet'])
async def donaldtweet(ctx, *, text = None):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}donaldtweet {text}")
    if not text:
        embed=discord.Embed(title="Error!", description= f"Incorrect Usage!\n Correct Usage: {c['[prefix]']}donaldtweet [text]",colour=discord.Colour.red())
        await ctx.send(embed=embed)
    response = requests.get(f"https://un5vyw.deta.dev/tweet?text={text}", stream=True)
    with open(f'temp/donaldtweet-{ctx.author.id}.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    embed=discord.Embed(title="Tweet Successful!", colour=discord.Colour.random())
    file = discord.File(f"temp/donaldtweet-{ctx.author.id}.png", filename="tweet.png")
    embed.set_image(url="attachment://tweet.png")
    await ctx.send(file=file,embed=embed)  
#Texttobraille Command
@bot.command(aliases=['braille'])
async def texttobraille(ctx, *, text = None):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}texttobraille {text}")
    if not text:
        embed=discord.Embed(title="Error!", description= f"Incorrect Usage!\n Correct Usage: {c['[prefix]']}texttobraille [text]",colour=discord.Colour.red())
        await ctx.send(embed=embed)
    response = requests.get(f"https://api.sillychat.tech/texttobraille?text={text}")
    response = response.json()
    embed=discord.Embed(title="Braille Generated! | ⠃⠗⠁⠊⠇⠇⠑⠀⠛⠑⠝⠑⠗⠁⠞⠑⠙", description=f"Text: {text}\nBraille: {response[0]['Braille']}", colour=discord.Colour.random())
    embed.set_footer(text="Thank You For Using Silly Chat!")
    await ctx.send(embed=embed)
#------------------------------------------ Prefix Bot Commands (Bot Mod)-------------------------------------------------
#Delete Message Command
@bot.command(name='deletemessage', aliases=['deletemsg'])
async def deletemessage(ctx, messageid):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}deletemessage {messageid}")
    usercollection = db['users']
    usercursor = usercollection.find()
    adminz = []
    for userid in usercursor:
        if userid["isbotmod"] == "True":
            adminz.append(int(userid["userid"]))
    if ctx.message.author.id in adminz:
        try:
            servercollection = db['servers']
            servercursor = servercollection.find()
            for server in servercursor:
                guild: Guild = bot.get_guild(int(server["guildid"]))
                if guild:
                    channel: TextChannel = guild.get_channel(int(server["channelid"]))
                    if channel:
                        perms: Permissions = channel.permissions_for(guild.get_member(bot.user.id))
                        if perms.send_messages:
                            if perms.embed_links and perms.attach_files and perms.external_emojis:
                                messages = [message async for message in channel.history(limit=None)]
                                for message in messages:
                                    if message.embeds:
                                        footer = message.embeds[0].footer.text
                                        if footer:
                                            if footer.startswith("Message ID: "):
                                                if footer == f"Message ID: {messageid}":
                                                    await message.delete()
                                                    embed = discord.Embed(
                                                        title = f'Message Deleted!',
                                                        description = f"Responsible Bot Moderator: **{ctx.author}**\nFor more info, please check our support server",
                                                        color=0x662a85)
                                                    embed.set_footer(text=f"Requested by {ctx.author}")
            try:
                await ctx.send(embed=embed)
            except:
                print("Failed to send embed / delete message")
        except:
            embed = discord.Embed(
                title = f'Error!',
                description = "Message ID is invalid!",
                color=0x662a85)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
#Ban Command
@bot.command()
async def ban(ctx, user: discord.User = None):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}ban {user}")
    adminz = []
    currentbanned = []
    usercollection = db['users']
    usercursor = usercollection.find()
    usercursore = usercollection.find()
    for userid in usercursor:
        if userid["isbotmod"] == "True":
            adminz.append(int(userid["userid"]))
        if userid["isbanned"] == "True":
            currentbanned.append(int(userid["userid"]))
    if ctx.message.author.id in adminz and ctx.message.author.id not in currentbanned:
        if user.id not in currentbanned:
            if user.id == 763471049894527006:
                embed=discord.Embed(title="Error!",color=0x662a85)
                embed.add_field(name="You Cannot Ban The Owner Of Silly Chat!", value="DON'T TRY AGAIN", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author}")
                await ctx.send(embed=embed)
                return
            for usere in usercursore:
                if usere["userid"] == user.id:
                    newvalues = { "$set": { "isbanned": "True" } }
                    usercollection.update_one(usere, newvalues)
            embed=discord.Embed(title="Banned!",color=0x662a85)
            dmembed = discord.Embed(title="You Have Been Banned From Silly Chat!",color=0x662a85)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await user.send(embed=dmembed)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="User Is Already Banned!",color=0x662a85)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
#Unban Command
@bot.command()
async def unban(ctx, user: discord.User = None):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}unban {user}")
    adminz = []
    currentbanned = []
    usercollection = db['users']
    usercursor = usercollection.find()
    usercursore = usercollection.find()
    for userid in usercursor:
        if userid["isbotmod"] == "True":
            adminz.append(int(userid["userid"]))
        if userid["isbanned"] == "True":
            currentbanned.append(int(userid["userid"]))
    if ctx.message.author.id in adminz and ctx.message.author.id not in currentbanned:
        if user.id in currentbanned:
            for usere in usercursore:
                if usere["userid"] == user.id:
                    newvalues = { "$set": { "isbanned": "False" } }
                    usercollection.update_one(usere, newvalues)
            embed=discord.Embed(title="Unbanned!",color=0x662a85)
            dmembed = discord.Embed(title="You Have Been Unbanned From Silly Chat!",color=0x662a85)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await user.send(embed=dmembed)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="User Is Not Banned!",color=0x662a85)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
#------------------------------------------ Prefix Bot Commands (Owner)-------------------------------------------------
#Sync Slash Commands Command
@bot.command(aliases=['syncslash'])
async def sync(ctx):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}sync")
    if ctx.message.author.id == 763471049894527006:
        fmt = await ctx.bot.tree.sync()
        embed = discord.Embed(
            title = f'Success!',
            description = f"Synced {len(fmt)} Slash Commands!",
            color=discord.Colour.blurple())
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
    else:
        return
#Delete Temp Files Command
@bot.command(aliases=['deletetemp'])
async def deletetempfiles(ctx):
    if ctx.message.author.id != 763471049894527006:
        return
    folder = './temp'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            embed = discord.Embed(title="Error!",description="Failed to delete %s. Reason: %s' % (file_path, e)",color=0x662a85)
            embed.set_footer(text=f"Requested by {ctx.author}")
            return await ctx.send(embed=embed)
    embed = discord.Embed(title="Success!",description="Deleted all temp files!",color=0x662a85)
    embed.set_footer(text=f"Requested by {ctx.author}")
    await ctx.send(embed=embed)
#Update Message Command
@bot.command()
async def updatemessage(ctx, user: discord.User = None, message: int = None):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}updatemessage {user} {message}")
    usercollection = db['users']
    usercursore = usercollection.find()
    if ctx.message.author.id == 763471049894527006:
            for usere in usercursore:
                if usere["userid"] == user.id:
                    newvalues = { "$set": { "messages": message } }
                    usercollection.update_one(usere, newvalues)
            embed=discord.Embed(title="User Messages Updated!",color=0x662a85)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
#Del User Data Command
@bot.command()
async def deleteuser(ctx, user: discord.User):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}deleteuser {user}")
    usercollection = db['users']
    usercursore = usercollection.find()
    if ctx.message.author.id == 763471049894527006:
            for usere in usercursore:
                if usere["userid"] == user.id:
                    usercollection.delete_one(usere)
            embed=discord.Embed(title="User Info has been deleted!",color=0x662a85)
            embed.add_field(name="User ID:", value=user.id, inline=False)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
#Del Server Data Command
@bot.command()
async def deleteserver(ctx, server: int):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}deleteserver {server}")
    servcollection = db['servers']
    servcursore = servcollection.find()
    if ctx.message.author.id == 763471049894527006:
            for guild in servcursore:
                if guild["guildid"] == server:
                    servcollection.delete_one(guild)
            embed=discord.Embed(title="Server Info has been deleted!",color=0x662a85)
            embed.add_field(name="Server ID:", value=server, inline=False)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
#Leave Guild Command
@bot.command(aliases=['leaveserver'])
async def leave(ctx, *, guildinput):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}leave {guildinput}")
    if ctx.message.author.id == 763471049894527006:
        try:
            guildid = int(guildinput)
        except:
            embed = discord.Embed(
            title = f'Error!',
            description = "Invalid guild: failed to convert to int",
            color=0x662a85)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)
        try:
            guild = bot.get_guild(guildid)
        except:
            embed = discord.Embed(
            title = f'Error!',
            description = "Invalid guild",
            color=0x662a85)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)
        try:
            await guild.leave()
            embed = discord.Embed(
            title = f'Success!',
            description = f"Left {guild.name} ({guildinput})",
            color=discord.Colour.green())
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(
            title = f'Error!',
            description = "Error Leaving. Please try again.",
            color=0x662a85)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)
    else:
        return
#List Guilds Command
@bot.command(aliases=['listguilds'])
async def guilds(ctx):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}guilds")
    if ctx.message.author.id == 763471049894527006:
        guilds = bot.guilds
        guildslist = []
        guildcount = 0
        embed = discord.Embed(
            title = f'Guilds!',
            color=discord.Colour.green())
        with open ("temp/guilds.txt", "a") as f:
            f.write("Silly Chat - Guilds\n\n")
        for guild in guilds:
            guildcount += 1
            with open ("temp/guilds.txt", "a") as f:
                f.write(f"{guild.name} - {guild.id} - {guild.owner}\n")
            if guildcount != 10:
                embed.add_field(name=f"{guild.name}", value=f"ID: {guild.id} | Owner: {guild.owner}", inline=False)
        embed.set_footer(text=f"Requested by {ctx.author} | {guildcount} Guilds")
        file = discord.File("temp/guilds.txt", filename="guilds.txt")
        message = await ctx.send(embed=embed)
        await message.reply("Full List",file=file)
    else:
        return
#Update User Command
@bot.command()
async def updateuser(ctx, user: discord.User = None):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}updateuser {user}")
    adminz = []
    usercollection = db['users']
    usercursor = usercollection.find()
    usercursore = usercollection.find()
    for userid in usercursor:
        if userid["isbotmod"] == "True":
            adminz.append(int(userid["userid"]))
    if ctx.message.author.id == 763471049894527006:
        if user.id not in adminz:
            for usere in usercursore:
                if usere["userid"] == user.id:
                    newvalues = { "$set": { "isbotmod": "True" } }
                    usercollection.update_one(usere, newvalues)
            embed=discord.Embed(title="User Promoted To Bot Moderator!",color=0x662a85)
            dmembed = discord.Embed(title="Your Role Has Been Changed To Bot Moderator!",description=f"For further info, please dm {ctx.author}",color=0x662a85)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await user.send(embed=dmembed)
            await ctx.send(embed=embed)
        else:
            for usere in usercursore:
                if usere["userid"] == user.id:
                    newvalues = { "$set": { "isbotmod": "False" } }
                    usercollection.update_one(usere, newvalues)
            embed=discord.Embed(title="User Demoted To Member!",color=0x662a85)
            embed.set_footer(text=f"Requested by {ctx.author}")
            dmembed = discord.Embed(title="Your Role Has Been Changed To Member!",description=f"For further info, please dm {ctx.author}",color=0x662a85)
            await user.send(embed=dmembed)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
#System Message Command
@bot.command(name='systemmessage', aliases=['sendsystemmessage'])
async def systemmessage(ctx, *, message: str):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}systemmessage")
    if ctx.message.author.id == 763471049894527006:
        await sendsystemmessage(message)
        embed = discord.Embed(
            title = f'Message Sent!',
            description = f"**Message:**\n{message}",
            color=0x662a85)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
#Purge Message Command
@bot.command(name='purge', aliases=['purgemessage'])
async def purge(ctx, amount: int):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}purge {amount}")
    if ctx.message.author.id == 763471049894527006:
        if amount >= 25:
            embed = discord.Embed(
            title = f'Error!',
            description = "You can not purge more than 25 messages at once!",
            color=0x662a85)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)
        else:
            servercollection = db['servers']
            servercursor = servercollection.find()
            for server in servercursor:
                try:
                    channelid = bot.get_channel(int(server["channelid"]))
                    await channelid.purge(limit=amount)
                    embed = discord.Embed(
                        title = f'Purged!',
                        description = f"Responsible Bot Moderator: **{ctx.author}**\nFor more info, please check our support server",
                        color=0x662a85)
                    await channelid.send(embed=embed)
                except:
                    try:
                        channelid = bot.get_channel(int(server["channelid"]))
                        embed = discord.Embed(
                        title = f'Purge Failed!',
                        description = f"We attempted to purge {amount} messages from this channel however the bot appears to be missing delete message permissions!\nWe recommend fixing this for next time we need to do a purge\nResponsible Bot Moderator: **{ctx.author}**",
                        color=0x662a85)
                        await channelid.send(embed=embed)
                    except:
                        await Logging(f"Purge ran by: **{ctx.author}**\nFailed to purge and send embed in: {server['guildid']}")
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
#Eval Command
@bot.command(name='eval', aliases=['evalstuff'])
async def eval(ctx, *, body: str):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}eval {body}")
    if ctx.message.author.id == 763471049894527006: # make it so only owner can use
        if "c[" in body: #stop owner getting stuff from config file
            embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to get stuff from config",
            color=0x662a85)
            embed.set_footer(text=f"Requested by {ctx.author}")
            await ctx.send(embed=embed)
            return
        env = { #set global stuff
            'bot': bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
        }
        env.update(globals())
        body = await cleanup_code(body) #cleanup the provided code
        stdout = io.StringIO()
        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'
        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass
            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                await ctx.send(f'```py\n{value}{ret}\n```')
    else:
        return
#Impersonate Command
@bot.command(name='impersonate', aliases=['sendas'])
async def impersonate(ctx, userid: int, *, message: str):
    await Logging("Command Ran",f"{ctx.author} | {ctx.guild.id} -> {c['prefix']}impersonate {userid} {message}")
    if ctx.message.author.id == 763471049894527006:
        embed = discord.Embed(
            title = f'Message Sent!',
            description = f"**Message:**\n{message}",
            color=0x662a85)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
        await sendAllImpersonate(userid, message)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)
#------------------------------------------Slash Bot Commands (User)-------------------------------------------------
#Slash Rules Command
@bot.tree.command(name="rules", description="View The Bot Rules!")
async def slashrules(interaction):
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /rules')
    await interaction.response.defer()
    embed = discord.Embed(
            title="**Silly Chat - Rules**",
            color=discord.Color.blue())
    embed.add_field(name="**1. Have respect**", value="You should always be friendly to other user of Silly Chat. We aim a nice and friendly community, not a toxic community.", inline=False)
    embed.add_field(name="**2. No NSFW**", value="No sending NSFW at all. Doing so will get you banned with no Appeal!", inline=False)
    embed.add_field(name="**3. Don't Spam**", value="Spamming is not just sending messages in quick repetition, but is also sending the same message over and over again, intentionally splitting sentences up into different messages.example: message 1: ``hi`` message 2: ``how`` message 3: ``are`` message 4: ``you?``!", inline=False)
    embed.add_field(name="**4. Use Common Sense**", value="There are some common rules, that are not mentioned here, but it is the most logical thing to follow them. The easiest way to know them is to think for 2 seconds before sending messages.")
    embed.set_footer(text=f"Requested by {interaction.user}")
    embed.set_thumbnail(url=bot.user.avatar.url)
    await interaction.followup.send(embed=embed)
#Slash Support Command
@bot.tree.command(name="support", description="Get Bot Support!")
async def slashsupport(interaction):
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /support')
    await interaction.response.defer()
    embed = discord.Embed(
        title = f'<a:discord:942344157618405416> Do you need support? Join our support server! <a:discord:942344157618405416>',
        description = '**[Support server](https://discord.gg/3qvpkgWSbF)**',
        color=0x662a85)
    embed.set_footer(text=f"Requested by {interaction.user}")
    await interaction.followup.send(embed=embed)
#Slash Credits Command
@bot.tree.command(name="credits", description="View Bot Credits!")
async def slashcredits(interaction):
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /credits')
    await interaction.response.defer()
    embed = discord.Embed(
        title = "Credits",
        color=0x662a85)
    embed.set_footer(text=f"Requested by {interaction.user}")
    embed.add_field(name="Gamer3514#7679", value="Bot Owner! Maintains the bot, made most systems!")  
    await interaction.followup.send(embed=embed)
#Slash ModList Command
@bot.tree.command(name="modlist", description="View A List Of Bot Mods!")
async def slashmodlist(interaction):
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /modlist')
    await interaction.response.defer()
    embed = discord.Embed(
        title = "Bot Moderator List",
        color=0x662a85)
    embed.set_footer(text=f"Requested by {interaction.user}")
    embed.add_field(name="Gamer3514#7679", value="Owner")
    embed.add_field(name="aeuito#0017", value="Bot Moderator")  
    await interaction.followup.send(embed=embed)
#Slash Github Command
@bot.tree.command(name="github", description="View Bot Source!")
async def slashgithub(interaction):
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /github')
    await interaction.response.defer()
    embed = discord.Embed(
        title = "Github",
        color=0x662a85)
    embed.set_footer(text=f"Requested by {interaction.user}")
    embed.add_field(name="", value="This Bot's Github Can Be Found [Here](https://github.com/TheGamer3514/silly-chat). The code is uploaded every few months, expect it to be missing some features from the current bot.")  
    await interaction.followup.send(embed=embed)
#Slash Vote Command
@bot.tree.command(name="vote", description="Vote For The Bot!")
async def slashvote(interaction):	
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /vote')
    await interaction.response.defer()
    embed = discord.Embed(
        title = f'Vote For Me!',
        color=0x662a85)
    embed.add_field(name="Top.gg", value="[Vote Here!](https://top.gg/bot/1051199485168066610)", inline=True)
    embed.add_field(name="Discord Bot List", value="[Vote Here!](https://discordbotlist.com/bots/silly-chat)", inline=True)
    embed.add_field(name="discord-botlist.eu", value="[Vote Here!](https://discord-botlist.eu/bots/1051199485168066610)", inline=True)
    embed.add_field(name="Void Bots", value="[Vote Here!](https://voidbots.net/bot/1051199485168066610/)", inline=True)
    embed.add_field(name="Discords", value="[Vote Here!](https://discords.com/bots/bot/1051199485168066610)", inline=True)
    embed.add_field(name="Botlist.me", value="[Vote Here!](https://botlist.me/bots/1051199485168066610)", inline=True)
    embed.add_field(name="Discord Bots", value="[Vote Here!](https://discord.bots.gg/bots/1051199485168066610)", inline=True)
    embed.add_field(name="Infinity Bots", value="[Vote Here!](https://infinitybots.gg/bot/1051199485168066610)", inline=True)
    embed.add_field(name="Bots For Discord", value="[Vote Here!](https://botsfordiscord.com/bot/1051199485168066610)", inline=True)
    embed.set_footer(text=f"Requested by {interaction.user}")
    await interaction.followup.send(embed=embed)
#Slash Stats Command
@bot.tree.command(name="stats", description="View Bot Stats!")
async def slashstats(interaction):
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /stats')
    await interaction.response.defer()
    embed = discord.Embed(
            title="**Silly Chat - Stats**",
            description="Use the dropdown below to view my stats!",
            color=discord.Color.random()
            )
    embed.set_footer(text=f"Requested by {interaction.user}")
    embed.set_thumbnail(url=bot.user.avatar.url)
    view = StatsView()
    await interaction.followup.send(embed=embed,view=view)
#Slash Ping Command
@bot.tree.command(name="ping", description="Get Bot Ping!")
async def slashping(interaction):
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /ping')
    await interaction.response.defer()
    embed = discord.Embed(
        title = f'Pong!',
        description = f'**{round(bot.latency * 1000)}ms**',
        color=0x662a85)
    url = 'https://status.sillychat.tech'
    output_path = 'temp/statuspageimage.png'
    take_screenshot(url, output_path)
    await asyncio.sleep(1.97)
    with open(output_path, 'rb') as file:
        url = "https://cdn.sillychat.tech"
        files = {'file': file}
        data = {'auth_key': c['cdnkey']}
        response = requests.post(url, files=files, data=data)
    if response.status_code == 200:
        file_url = response.text
        embed.set_image(url=file_url)
    embed.set_footer(text=f"Requested by {interaction.user}")
    await interaction.followup.send(embed=embed)
#Slash Invite Command
@bot.tree.command(name="invite", description="Invite The Bot!")
async def slashinvite(interaction):
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /invite')
    await interaction.response.defer()
    embed=discord.Embed(title="\n<a:discord:942344157618405416>Invite<a:discord:942344157618405416>\n", url="https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands",color=0x662a85)
    embed.set_footer(text=f"Requested by {interaction.user}")
    await interaction.followup.send(embed=embed)
#Slash Help Command
@bot.tree.command(name="help", description="Get Bot Help!")
async def slashhelp(interaction):
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /help')
    await interaction.response.defer()
    count = 0
    servercollection = db['servers']
    servercursor = servercollection.find()
    for server in servercursor:
        count = count + 1
    embed = discord.Embed(
            title="**Silly Chat**",
            description=f"**Version:** {botversion}\nA discord global chat bot. Instead of sending your message to 1 server, you could be sending to {count}! With a simple 1 command setup, it takes less than 2 minutes to have the bot fully setup in your discord server!\n**Discord:** [Here](https://discord.gg/3qvpkgWSbF)",
            color=discord.Color.blue()
        )
    embed.add_field(name="Guide", value="<a:sent:937311880836436009> - Message Sent\n<a:sendfailed:937311948318572584> - Message Failed To Send", inline=False)
    embed.set_thumbnail(url=bot.user.avatar.url)
    view = HelpMenu()
    embed.set_footer(text=f"Requested by {interaction.user}")
    await interaction.followup.send(embed=embed,view=view)
#SLash Ai Command
@bot.tree.command(name="ai", description="Talk To Darren!")
async def slashai(interaction, prompt: str):
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /ai {prompt}')
    await interaction.response.defer()
    async with aiohttp.ClientSession() as session:
        randfooter = ["Thank You for using Silly Chat!", "Did You Know? Darren was originally just a seperate bot but now its here aswell!", "Did You Know? Silly Chat is open source on Github!", "Did You Know? Silly Chat is owned by Gamer3514#7679!", "Did You Know? Silly Chat has secret commands :eyes:"]
        uid = interaction.user.id
        async with session.get(f"http://api.brainshop.ai/get?bid={c['bid']}&key={c['key']}&uid={uid}&msg={prompt}") as resp:
            responce = await resp.json()
            embed = discord.Embed(title="Darren Has Spoken!", description=responce["cnt"])
            embed.set_footer(text=f"Requested by {interaction.user} - {randfooter[random.randint(0, len(randfooter)-1)]}")
            await interaction.followup.send(embed=embed)
#SLash Aiart Command
@bot.tree.command(name="aiart", description="Generate Some Ai Art!")
async def slashaiart(interaction, prompt: str):
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /aiart {prompt}')
    usercollection = db['users']
    usercursor = usercollection.find()
    for userid in usercursor:
        if userid['userid'] == interaction.user.id:
            if int(userid['messages']) >= 150:
                canuse = True
            else:
                canuse = False
    if canuse == True:
        await slash_get_ai_art(prompt, interaction)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You need to send 150 messages on Silly Chat to be able to use this command!",
            color=0x662a85)
        embed.set_footer(text="Sorry for the inconvenience! Once we have more resources we will remove this limit!")
        await interaction.response.send_message(embed=embed, ephemeral=True)
#SLash Aiart2 Command
@bot.tree.command(name="aiart2", description="Use Dalle-Mini image generator to create some amazing images")
async def slashaiart2(interaction: discord.Interaction, *, prompt:str):
        await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /aiart2 {prompt}')
        await interaction.response.defer()
        embed = discord.Embed(title="Content Generated by **Craiyon.com*", description="Thanks for using Silly Chat!", color=discord.Colour.blue())
        async with aiohttp.request("POST", "https://backend.craiyon.com/generate", json={"prompt": prompt}) as resp:
            r = await resp.json()
            images = r['images']
        image = BytesIO(base64.decodebytes(images[0].encode("utf-8")))
        return await interaction.followup.send(content="Content Generated by **Craiyon.com**", file=discord.File(image, "generatedimage.png"))
#SLash Report Command
@bot.tree.command(name="report", description="Report A User Breaking Silly Chat Rules!")
async def slashreport(interaction, user: discord.Member, reason: str):
    await interaction.response.defer()
    channelid = bot.get_channel(int(1071930458998325258))
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /report {user}')
    successembed = discord.Embed(description="Report Submitted!",color=0x2ecc71)
    reportembed = discord.Embed(description=f"New Report!\nReporter: **{interaction.user}**\nSuspect: **{user}**\nReason Of Report **{reason}**",color=0x2ecc71)
    successembed.set_footer(text=f"Requested by {interaction.user}")
    await interaction.followup.send(embed=successembed)
    await channelid.send("<@&1007565578879377469>", embed=reportembed)
#Slash Leaderboard Command
@bot.tree.command(name="leaderboard", description="View Silly Chat message leaderboard")
async def leaderboard(interaction):
        await interaction.response.defer()
        await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /leaderboard')
        usercollection = db['users']
        users = usercollection.find().sort("messages", pymongo.DESCENDING)
        embed = discord.Embed(
            title="**Silly Chat - Leaderboard**",
            color=discord.Color.random()
        )
        count = 1
        for user in users:
            if count == 11:
                break
            if int(user['messages']) >= 1:
                botuser = bot.get_user(user['userid'])
                embed.add_field(name=f"**{count}.**", value=f"{botuser} - **{int(user['messages'])}** Messages", inline=False)
                count += 1
        embed.set_footer(text=f"Requested by {interaction.user}")
        embed.set_thumbnail(url=bot.user.avatar.url)
        await interaction.followup.send(embed=embed)
#Tutorial Command
@bot.tree.command(name="tutorial", description="View The Bot Tutorial!")
async def slashtutorial(interaction):
    view = TutorialMenu(interaction.user.id)
    await interaction.response.defer()
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /tutorial')
    count = 0
    servercollection = db['servers']
    servercursor = servercollection.find()
    for server in servercursor:
        count = count + 1
    embed = discord.Embed(
        title="**Silly Chat - Tutorial**",
        description=f"**Version:** {botversion}\nA discord global chat bot. Instead of sending your message to 1 server, you could be sending to {count}! With a simple 1 command setup, it takes less than 2 minutes to have the bot fully setup in your discord server!\n**Discord:** [Here](https://discord.gg/3qvpkgWSbF)",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=bot.user.avatar.url)
    embed.set_footer(text=f"Requested by {interaction.user}")
    await interaction.followup.send(embed=embed, view=view) 
#------------------------------------------Slash Bot Commands (Server Admin)-------------------------------------------------
#Slash Set Global Command
@bot.tree.command(name="setglobal", description="Setup Silly Chat!")
async def slashSetGlobal(interaction, channel: discord.TextChannel):
    await interaction.response.defer()
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /setglobal {channel}')
    servercollection = db['servers']
    servercursor = servercollection.find()
    if interaction.user.guild_permissions.administrator:
        for server in servercursor:
            if server['guildid'] == interaction.guild.id:
                embed = discord.Embed(description="You have already setup the bot!\r\n"
                                                  f"To setup the bot again do `{c['prefix']}removeGlobal` then run this command again!",
                                      color=0x2ecc71)
                embed.set_footer(text=f"Requested by {interaction.user}")
                await interaction.followup.send(embed=embed)
                return
        channel = channel.id
        server = {
                "guildid": interaction.guild.id,
                "channelid": channel,
                "invite": "null"
            }
        servercollection = db['servers']
        servercollection.insert_one(server)
        embed = discord.Embed(title="**Welcome!**",
                                description="Thank you for using our bot!"
                                            " Messages will now be sent and recieved!"
                                            " Have fun!",
                                color=0x2ecc71)
        embed.set_footer(text=f"Requested by {interaction.user}")
        await interaction.followup.send(embed=embed)
        await slashsendAllWelcome(interaction)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command! You require ``Administrator`` permissions to run this.",
            color=0x662a85)
        embed.set_footer(text=f"Requested by {interaction.user}")
        await interaction.followup.send(embed=embed,ephemeral=True)
#Slash Remove Global Command
@bot.tree.command(name="removeglobal", description="Remove Global Setup!")
async def slashRemoveGlobal(interaction):
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /removeglobal')
    await interaction.response.defer()
    servercollection = db['servers']
    servercursor = servercollection.find()
    if interaction.user.guild_permissions.administrator:
        for server in servercursor:
            if server['guildid'] == interaction.guild.id:
                servercollection.delete_one({"guildid": int(interaction.guild.id)})
                embed = discord.Embed(title="**Goodbye!**",
                                  description="Sad to see you go! If you want to setup the bot again use"
                                              "</setglobal:1074285744765554789>!",
                                  color=0x2ecc71)
                embed.set_footer(text=f"Requested by {interaction.user}")
                await interaction.followup.send(embed=embed)
                return
        embed = discord.Embed(description="No Global Channel Set.\r\n"
                                              "Use </setglobal:1074285744765554789> to set one!\nBelieve this is a mistake? Join our support server!",
                                  color=0x2ecc71)
        embed.set_footer(text=f"Requested by {interaction.user}")
        await interaction.followup.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command! You require ``Administrator`` permissions to run this.",
            color=0x662a85)
        embed.set_footer(text=f"Requested by {interaction.user}")
        await interaction.followup.send(embed=embed,ephemeral=True)
#Slash Set Invite Command
@bot.tree.command(name="setinvite", description="Set Global Chat Invite!")
async def slashsetInvite(interaction, channel: discord.TextChannel):
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /setinvite {channel}')
    await interaction.response.defer()
    servercollection = db['servers']
    servercursor = servercollection.find()
    if interaction.user.guild_permissions.administrator:
        for server in servercursor:
                if server['guildid'] == interaction.guild.id:
                    invite2 = await channel.create_invite()
                    invite = invite2.url
                    newvalues = { "$set": { "invite": f"{invite}" } }
                    servercollection.update_one(server, newvalues)
                    embed = discord.Embed(description="Invite Set!\r\n"
                                              f"Invite: {invite}",
                                  color=0x2ecc71)
                    await interaction.followup.send(embed=embed)
                    return
        embed = discord.Embed(description="You have not setup the bot!\r\n"
                                              "To setup the bot do </setglobal:1074285744765554789> then run this command again!",
                                  color=0x2ecc71)
        embed.set_footer(text=f"Requested by {interaction.user}")
        await interaction.followup.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command! You require ``Administrator`` permissions to run this.",
            color=0x662a85)
        embed.set_footer(text=f"Requested by {interaction.user}")
        await interaction.followup.send(embed=embed,ephemeral=True)
#Slash Remove Invite Command
@bot.tree.command(name="removeinvite", description="Remove Global Chat Invite!")
async def slashremoveInvite(interaction):
    await Logging("Command Ran",f'{interaction.user} | {interaction.guild.id} -> /removeinvite')
    await interaction.response.defer()
    servercollection = db['servers']
    servercursor = servercollection.find()
    if interaction.user.guild_permissions.administrator:
        for server in servercursor:
            if server['guildid'] == interaction.guild.id:
                newvalues = { "$set": { "invite": "null" } }
                servercollection.update_one(server, newvalues)
                embed = discord.Embed(description="Invite Removed!\r\n"
                                              f"Invite has been removed!",
                                  color=0x2ecc71)
                await interaction.followup.send(embed=embed)
                return
        embed = discord.Embed(description="You have not setup the bot!\r\n"
                                              "To setup the bot do </setglobal:1074285744765554789> then run this command again!",
                                  color=0x2ecc71)
        await interaction.followup.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command! You require ``Administrator`` permissions to run this.",
            color=0x662a85)
        await interaction.followup.send(embed=embed,ephemeral=True)
#Start status check page!
from threading import Thread
from flask import Flask
from functools import partial
flaskapp = Flask(__name__)
@flaskapp.route('/')
def statuscheck():
    return f'Silly Chat is online and ready to go! Ping: {round(bot.latency * 1000)}ms'
@flaskapp.route('/ping')
def ping():
    return f'{round(bot.latency * 1000)}ms'
partial_run = partial(flaskapp.run, host="0.0.0.0", port=6020, debug=False, use_reloader=False)
t = Thread(target=partial_run)
t.start()
#Start the bot!
bot.run(c['token'], log_handler=handler, log_level=logging.ERROR)
