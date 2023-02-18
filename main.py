#Install Modules
import os
os.system("pip install --user discord pytz psutil discord_webhook requests pyjokes py-dactyl")

#import Modules
import urllib.request
from datetime import datetime
import asyncio
import discord
import shutil
import pytz
import discord_webhook
import multiprocessing
import psutil
import pyjokes
from discord import Message, Guild, TextChannel, Permissions, app_commands
from discord.ext import commands
import json
import time
import requests
import random
import aiohttp
import pydactyl
import base64
from io import BytesIO
from pydactyl import PterodactylClient

#Logging
import logging
handler = logging.FileHandler(filename=os.path.join('errors.log'), encoding='utf-8', mode='w')

#Load Config
with open(os.path.join('config', 'config.json')) as f:
    data = json.load(f)
    for c in data['botConfig']:
        print(f"Prefix: {c['prefix']}")

#Define Bot
bot = commands.Bot(command_prefix=c['prefix'], intents=discord.Intents.all(), status=discord.Status.idle, case_insensitive=True)
bot.remove_command('help')

#Ptero Api
api = PterodactylClient('https://panel.sillydev.co.uk', c['ptero_account_key'])

#Load Server File
if os.path.isfile(os.path.join('config', 'servers.json')):
    with open(os.path.join('config', 'servers.json'), encoding='utf-8') as f:
        servers = json.load(f)
else:
    servers = {"servers": []}
    with open(os.path.join('config', 'servers.json'), 'w') as f:
        json.dump(servers, f, indent=4)

#Load Banned Users
if os.path.isfile(os.path.join('config', 'banned.json')):
    with open(os.path.join('config', 'banned.json'), encoding='utf-8') as f:
        banned = json.load(f)
else:
    banned = {"banned": []}
    with open(os.path.join('config', 'banned.json'), 'w') as f:
        json.dump(banned, f, indent=4)

#Load Admin Users
if os.path.isfile(os.path.join('config', 'admins.json')):
    with open(os.path.join('config', 'admins.json'), encoding='utf-8') as f:
        adminusers = json.load(f)
else:
    adminusers = {"admins": []}
    with open(os.path.join('config', 'admins.json'), 'w') as f:
        json.dump(adminusers, f, indent=4)

#------------------------------------------Bot Events-------------------------------------------------

# Auto Updating Status
async def StatusChange():
    while True:
        usercount = len([m for m in bot.users if not m.bot])
        await bot.change_presence(activity=Game(f'g!help | {len(bot.guilds)} Servers'))
        await asyncio.sleep(35)
        await bot.change_presence(activity=Game(f'g!help | {usercount} Users'))
        await asyncio.sleep(35)
        await bot.change_presence(activity=Game(f'g!help | discord.gg/3qvpkgWSbF'))
        await asyncio.sleep(35)
        await bot.change_presence(activity=Game(f'g!help | Invite Me Today!'))
        await asyncio.sleep(35)
        await bot.change_presence(activity=Game(f'g!help | Silly Chat'))
        await asyncio.sleep(35)
        await bot.change_presence(activity=Game(f'g!help | Downloading 2024'))
        await asyncio.sleep(35)
        await bot.change_presence(activity=Game(f'g!help | Gamer3514#7679'))
        await asyncio.sleep(35)
        await asyncio.sleep(420)  # Combined delay of 7 minutes

# Webhook Logging
async def Webhooklogging(channel, message):
    webhook = Webhook.from_url(channel, adapter=AsyncWebhookAdapter(bot.session))
    response = await webhook.send(content=message)
    print(message)

# Event that runs when bot is online
@bot.event
async def on_ready():
    print(f'{bot.user} Is Now Online And Ready To Send Messages!')
    await bot.loop.create_task(StatusChange())

# Event for when a message is sent
@bot.event
async def on_message(message):
    bannedusers = [int(user['userid']) for user in banned['banned']]
    possiblechannels = [int(channel['channelid']) for

#------------------------------------------Command Menus-------------------------------------------------
class HelpMenu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    async def create_embed(self, title, description, fields):
        embed = discord.Embed(
            title=title,
            description=f"**Prefix: g!**\n{description}",
            color=discord.Color.random()
        )
        embed.set_footer(text="Thank you for using Silly Chat!")
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/8lntiVCa9JwRxnqX6rxvWdEWWmwIiz5xFeTxmdRSydE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1051199485168066610/d40794f36524ec9e9a4e723679d14d6d.png?width=670&height=670")
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        return embed

    async def send_embed(self, interaction, title, description, fields):
        embed = await self.create_embed(title, description, fields)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="Setup", style=discord.ButtonStyle.grey, emoji="🧰")
    async def setupmenu(self, interaction: discord.Interaction, button: discord.ui.Button):
        fields = [("g!setGlobal", "Add global chat to a channel!", False), 
                  ("g!removeGlobal", "Remove global chat from a channel!", False)]
        await self.send_embed(interaction, "Silly Chat - Setup", "", fields)

    @discord.ui.button(label="Info", style=discord.ButtonStyle.grey, emoji="<:info:1071407819670175774>")
    async def infomenu(self, interaction: discord.Interaction, button: discord.ui.Button):
        fields = [("g!ping", "Check the bot's ping", False), 
                  ("g!stats", "Check the bot's stats!", False), 
                  ("g!invite", "Invite me to your server!", False), 
                  ("g!support", "Get a link to our support server!", False), 
                  ("g!github", "Get a link to the bot's github!", False), 
                  ("g!credits", "View the creators of the bot!", False), 
                  ("g!vote", "Vote for the bot!", False)]
        await self.send_embed(interaction, "Silly Chat - Info", "", fields)

    @discord.ui.button(label="Fun", style=discord.ButtonStyle.grey, emoji="🤣")
    async def funmenu(self, interaction: discord.Interaction, button: discord.ui.Button):
        fields = [("g!ai", "Chat to Darren!", False), 
                  ("g!8ball", "Use Magic 8 Ball!", False), 
                  ("g!joke", "Generate A Random Joke!", False), 
                  ("g!rock", "Generate A Rock!", False), 
                  ("g!coinflip", "Flip A Coin!", False), 
                  ("g!kill", "Kill Someone!", False), 
                  ("g!meme", "Generate A Meme!", False), 
                  ("g!avatar", "Steal Someone's Avatar!", False)]
        await self.send_embed(interaction, "Silly Chat - Fun", "", fields)

    @discord.ui.button(label="Bot Moderator", style=discord.ButtonStyle.grey, emoji="<:Role:942348530117410826>")

#------------------------------------------Prefix Bot Commands (User)-------------------------------------------------
import random
import aiohttp
import discord
import pyjokes

from discord.ext import commands
from typing import List

bot = commands.Bot(command_prefix='g!')
heads_tails: List[str] = ['Heads', 'Tails']
ball8answers: List[str] = [
    'It is certain', 'It is decidedly so', 'Without a doubt',
    'Yes, definitely', 'You may rely on it', 'As I see it, yes',
    'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
    'Reply hazy try again', 'Ask again later',
    'Better not tell you now', 'Cannot predict now',
    'Concentrate and ask again', "Don't count on it",
    'Outlook not so good', 'My sources say no',
    'Very doubtful'
]
rand_footer = ["Thank You for using Silly Chat!",
               "Did You Know? Silly Chat is open source on Github! g!github",
               "Did You Know? Silly Chat is owned by Gamer3514#7679!"]

with open('servers.json') as f:
    servers = json.load(f)


async def Webhooklogging(webhook:str, log: str) -> None:
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(webhook, adapter=discord.AsyncWebhookAdapter(session))
        await webhook.send(log)


def guild_exists(guild_id: int) -> bool:
    for server in servers['servers']:
        if server['guildid'] == guild_id:
            return True
    return False


def get_globalChat_id(guild_id: int) -> int:
    for index, server in enumerate(servers['servers']):
        if server['guildid'] == guild_id:
            return index
    return -1


async def sendAllWelcome(ctx):
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(c['webhook'], adapter=discord.AsyncWebhookAdapter(session))
        embed = discord.Embed(title="**Welcome!**", description="Thank you for using our bot! Messages will now be sent and received! Have fun!",color=0x2ecc71)
        await webhook.send(embed=embed)


class HelpMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60.0)
        self.add_item(discord.ui.Button(style=discord.ButtonStyle.link, url='https://github.com/gamer3514/Silly-Chat'))
        self.add_item(discord.ui.Button(label="General Commands", style=discord.ButtonStyle.green, disabled=True))
        self.add_item(discord.ui.Button(label="g!coinflip", style=discord.ButtonStyle.blurple))
        self.add_item(discord.ui.Button(label="g!8ball", style=discord.ButtonStyle.blurple))
        self.add_item(discord.ui.Button(label="g!joke", style=discord.ButtonStyle.blurple))
        self.add_item(discord.ui.Button(label="g!meme", style=discord.ButtonStyle.blurple))
        self.add_item(discord.ui.Button(label="Admin Commands", style=discord.ButtonStyle.green, disabled=True))
        self.add_item(discord.ui.Button(label="g!setGlobal", style=discord.ButtonStyle.red))
        self.add_item(discord.ui.Button(label="g!removeGlobal", style=discord.ButtonStyle.red))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user == self.ctx.author


# Help Command
@bot.command()
async def help

#------------------------------------------ Prefix Bot Commands (Bot Mod)-------------------------------------------------
@bot.command(name='dm', aliases=['dmuser'])
async def dm(ctx, user: discord.User = None, *, value=None):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!dm {user} {value}')

    adminz = [int(admin["userid"]) for admin in adminusers["admins"]]
    if ctx.message.author.id not in adminz:
        embed = discord.Embed(
            title = 'Error!',
            description = 'You are not permitted to use this command!',
            color = 0x662a85
        )
        return await ctx.send(embed=embed)

    if user is None:
        return await ctx.send(f'**{ctx.message.author},** Please mention somebody to DM.')

    if user == ctx.message.author:
        await user.send("**You can't DM yourself, or maybe you can?**")
        return await ctx.message.delete()

    if value is None:
        return await ctx.send(f'**{ctx.message.author},** Please send a message to DM.')

    await user.send(value)
    await ctx.message.delete()

@bot.command()
async def ban(ctx, user: discord.User = None):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!ban {user}')
    
    admin_ids = [int(admin["userid"]) for admin in adminusers["admins"]]
    banned_ids = [buser["userid"] for buser in banned["banned"]]
    
    if ctx.message.author.id not in admin_ids or ctx.message.author.id in banned_ids:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color = 0x662a85
        )
        await ctx.send(embed = embed)
        return
    
    if user is None:
        embed = discord.Embed(
            title = f'Error!',
            description = "Please mention a user to ban!",
            color = 0x662a85
        )
        await ctx.send(embed = embed)
        return
    
    if user.id in banned_ids:
        embed = discord.Embed(
            title = "User is already banned!",
            color = 0x662a85
        )
        await ctx.send(embed = embed)
        return
    
    banned_user = {"userid": user.id}
    banned["banned"].append(banned_user)
    
    with open('banned.json', 'w') as f:
        json.dump(banned, f, indent = 4)
    
    embed = discord.Embed(title = "Banned!", color = 0x662a85)
    dm_embed = discord.Embed(title = "You Have Been Banned From Silly Chat!", color = 0x662a85)
    
    try:
        await user.send(embed = dm_embed)
    except discord.Forbidden:
        pass
    
    await ctx.send(embed = embed)


#Scan Image Command
@bot.command()
async def scanimage(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!scanimage')
    adminz = []
    for admin in adminusers["admins"]:
        adminz.append(int(admin["userid"]))
    if ctx.message.author.id in adminz:
        attachments = ctx.message.attachments
        if len(attachments) > 0:
            img = attachments[0]
            randomname = await get_random_string(8)
            await ctx.message.attachments[0].save(f'temp/{randomname}.png')
            headers = {"Authorization": f"Bearer {c['edenai_key']}"}
            url="https://api.edenai.run/v2/image/explicit_content"
            data={"providers": "google"}
            await asyncio.sleep(1.5)
            files={'file': open(f"temp/{randomname}.png",'rb')}
            response = requests.post(url, data=data, files=files, headers=headers)
            result = json.loads(response.text)
            embed = discord.Embed(
            title = f'Image Scanned!',
            description = f"Nsfw Rating: {result['google']['nsfw_likelihood']}",
            color=0x662a85)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
            title = f'Error!',
            description = "You have not provided an image to scan!",
            color=0x662a85)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        await ctx.send(embed=embed)
#------------------------------------------ Prefix Bot Commands (Owner)-------------------------------------------------
#Sync Slash Commands Command
@bot.command()
async def sync(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!sync')
    if ctx.message.author.id == 763471049894527006:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f"Synced {len(fmt)} commands")
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        await ctx.send(embed=embed)
#Update User Command
@bot.command()
async def updateuser(ctx, user: discord.User = None):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!updateuser {user}')
    adminz = []
    for admin in adminusers["admins"]:
        adminz.append(int(admin["userid"]))
    if ctx.message.author.id == 763471049894527006:
        if user.id not in adminz:
            adminuserz = {
                "userid": user.id
                }
            adminusers["admins"].append(adminuserz)
            with open('admins.json', 'w') as f:
                json.dump(adminusers, f, indent=4)
            embed=discord.Embed(title="User Modified!",color=0x662a85)
            dmembed = discord.Embed(title="Your Role Has Been Changed!",color=0x662a85)
            await user.send(embed=dmembed)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="Removing Admins Coming Soon",color=0x662a85)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        await ctx.send(embed=embed)
#Power Action Command
@bot.command()
async def sync(ctx):
    await Webhooklogging(c['webhook'], f'{ctx.author} | {ctx.guild.id} -> g!sync')
    if ctx.author.id == 763471049894527006:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f"Synced {len(fmt)} commands")
    else:
        embed = discord.Embed(
            title=f'Error!',
            description="You are not permitted to use this command!",
            color=0x662a85)
        await ctx.send(embed=embed)

@bot.command()
async def updateuser(ctx, user: discord.User = None):
    await Webhooklogging(c['webhook'], f'{ctx.author} | {ctx.guild.id} -> g!updateuser {user}')
    adminz = {int(admin["userid"]) for admin in adminusers["admins"]}
    if ctx.author.id == 763471049894527006:
        if user.id not in adminz:
            adminusers["admins"].append({"userid": user.id})
            with open('admins.json', 'w') as f:
                json.dump(adminusers, f, indent=4)
            embed = discord.Embed(title="User Modified!", color=0x662a85)
            dmembed = discord.Embed(title="Your Role Has Been Changed!", color=0x662a85)
            await user.send(embed=dmembed)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Removing Admins Coming Soon", color=0x662a85)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f'Error!', description="You are not permitted to use this command!", color=0x662a85)
        await ctx.send(embed=embed)

@bot.command()
async def scanimage(ctx):
    await Webhooklogging(c['webhook'], f'{ctx.author} | {ctx.guild.id} -> g!scanimage')
    adminz = {int(admin["userid"]) for admin in adminusers["admins"]}
    if ctx.author.id not in adminz:
        embed = discord.Embed(title=f'Error!', description="You are not permitted to use this command!", color=0x662a85)
        await ctx.send(embed=embed)
        return
    attachments = ctx.message.attachments
    if not attachments:
        embed = discord.Embed(title=f'Error!', description="You have not provided an image to scan!", color=0x662a85)
        await ctx.send(embed=embed)
        return
    img = attachments[0]
    randomname = await get_random_string(8)
    await ctx.message.attachments[0].save(f'temp/{randomname}.png')
    headers = {"Authorization": f"Bearer {c['edenai_key']}"}
    url = "https://api.edenai.run/v2/image/explicit_content"
    data = {"providers": "google"}
    await asyncio.sleep(1.5)
    files = {'file': open(f"temp/{randomname}.png", 'rb')}
    response = requests.post(url, data=data, files=files, headers=headers)
    result = json.loads(response.text)
    embed = discord.Embed(title=f'Image Scanned!', description=f"Nsfw Rating: {result['google']['nsfw_likelihood']}", color=0x662a85)
    await ctx.send(embed=embed)

@bot.command()
async def unban(ctx, user: discord.User = None):
    await Webhooklogging(c['webhook'], f'{ctx.author} |

#Delete From Here
@bot.command()
async def poweraction(ctx, value=None):
    await Webhooklogging(c['webhook'], f'{ctx.author} | {ctx.guild.id} -> g!poweraction {value}')
    if ctx.message.author.id != 763471049894527006:
        embed = discord.Embed(
            title=f'Error!',
            description="You are not permitted to use this command!",
            color=0x662a85)
        return await ctx.send(embed=embed)

    adminz = {int(admin["userid"]) for admin in adminusers["admins"]}
    if ctx.message.author.id not in adminz:
        embed = discord.Embed(
            title=f'Error!',
            description="You are not permitted to use this command!",
            color=0x662a85)
        return await ctx.send(embed=embed)

    embed = discord.Embed(
        title=f'Complete!',
        description="Power Action Sent!",
        color=0x662a85)
    await ctx.send(embed=embed)
    api.client.servers.send_power_action(c['ptero_srv_id'], value)
#To Here to remove the poweraction command (for people not using Pterodactyl Panel)
#Database Command
@bot.command(name='database', aliases=['viewdatabase'])
async def database(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!database')
    owner = await bot.fetch_user("763471049894527006")
    if owner != ctx.message.author:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        return await ctx.send(embed=embed)
    
    # Send servers
    with open('config/servers.json') as f:
        data = json.load(f)
        servers = data['servers']
        for server in servers:
            print(server)
            embed = discord.Embed(
                title = 'DataBase Export! (Servers)',
                description = server,
                color=0x662a85)
            user = await bot.fetch_user("763471049894527006")
            await user.send(embed=embed)

    # Send banned users
    with open('config/banned.json') as f:
        data = json.load(f)
        banned_users = data['banned']
        for user in banned_users:
            print(user)
            embed = discord.Embed(
                title = 'DataBase Export! (Banned Users)',
                description = user,
                color=0x662a85)
            user = await bot.fetch_user("763471049894527006")
            await user.send(embed=embed)

    # Send admin users
    with open('config/admins.json') as f:
        data = json.load(f)
        admin_users = data['admins']
        for user in admin_users:
            print(user)
            embed = discord.Embed(
                title = 'DataBase Export! (Admin Users)',
                description = user,
                color=0x662a85)
            user = await bot.fetch_user("763471049894527006")
            await user.send(embed=embed)

#System Message Command
@bot.command(name='systemmessage', aliases=['sendsystemmessage'])
async def systemmessage(ctx, message: str):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!systemmessage')
    if ctx.message.author.id != 763471049894527006:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        return await ctx.send(embed=embed)

    print(message)
    await sendsystemmessage(message)

    embed = discord.Embed(
        title = f'Complete!',
        description = "Message Has Been Sent!",
        color=0x662a85)
    await ctx.send(embed=embed)

#------------------------------------------Slash Bot Commands (User)-------------------------------------------------
#Slash Support Command
@bot.tree.command(name="support", description="Get Bot Support!")
async def slashsupport(interaction):
    embed = discord.Embed(
        title="<a:discord:942344157618405416> Do you need support? Join our support server! <a:discord:942344157618405416>",
        description="**[Support server](https://discord.gg/3qvpkgWSbF)**",
        color=0x662a85)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="credits", description="View Bot Credits!")
async def slashcredits(interaction):
    embed = discord.Embed(
        title="Credits",
        color=0x662a85)
    embed.add_field(name="Gamer3514#7679", value="Bot Owner! Maintains the bot, made most systems!")
    embed.add_field(name="ukcai#7121", value="Bot Developer & Moderator! Helped improve systems and made comamnds such as g!stats")
    embed.add_field(name="AlpineVr#0001", value="Bot Moderator! Helps keep the chat SFW. Helped with slash commands and more!")
    await interaction.response.send_message(embed=embed)

#Slash Github Command
@bot.tree.command(name="github", description="View Bot Source!")
async def slashgithub(interaction):
    embed = discord.Embed(
        title = "Github",
        color=0x662a85)
    embed.add_field(name="", value="This Bot's Github Can Be Found [Here](https://github.com/TheGamer3514/silly-chat)")  
    await interaction.response.send_message(embed=embed)
#Slash Vote Command
@bot.tree.command(name="vote", description="Vote For The Bot!")
async def slashvote(interaction):    
    embed = discord.Embed(
        title = f'Vote For Me!',
        color=0x662a85)
    embed.add_field(name="Top.gg", value="[Vote Here!](https://top.gg/bot/1051199485168066610)")
    embed.add_field(name="Spectrum Lists", value="[Vote Here!](https://spectrumlists.xyz/bot/1051199485168066610)")
    embed.add_field(name="Discord Bot List", value="[Vote Here!](https://discordbotlist.com/bots/silly-chat)")
    await interaction.response.send_message(embed=embed)

#Slash Stats Command
@bot.tree.command(name="stats", description="View Bot Stats!")
async def slashstats(interaction):
    cpu_cores = multiprocessing.cpu_count()
    guild_count = len(bot.guilds)
    bot_latency = round(bot.latency * 1000)
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    total_memory = round(psutil.virtual_memory().total / (1024.0 **3))
    
    embed = discord.Embed(title="My Stats:", color=0x662a85)
    embed.add_field(name="Bot Owner", value="<@763471049894527006> (763471049894527006) Gamer3514#7679", inline=False)
    embed.add_field(name="Cpu Cores", value=cpu_cores, inline=False)
    embed.add_field(name="Server Count", value=str(guild_count), inline=False)
    embed.add_field(name="Bot Latency", value=f"{bot_latency}ms", inline=False)
    embed.add_field(name="Cpu Usage", value=f"{cpu_usage}%", inline=False)
    embed.add_field(name="Memory Usage", value=f"{memory_usage}%", inline=False)
    embed.add_field(name="Total Memory", value=f"{total_memory} GB", inline=False)
    
    await interaction.response.send_message(embed=embed)

#Slash TikTok Command
@bot.tree.command(name="tiktok", description="Get A Link To Our TikTok!")
async def slashtiktok(interaction):
    embed = discord.Embed(title="Follow Me On Tiktok!", description="@elon_fan.1", color=0x662a85)
    await interaction.response.send_message(embed=embed)

#Slash Youtube Command
@bot.tree.command(name="youtube", description="Get a link to our YouTube!")
async def slashyoutube(interaction):
    embed = discord.Embed(
        title="Subscribe on YouTube!",
        description="[Here!](https://youtube.com/c/thegamer3514)",
        color=0x662a85
    )
    await interaction.response.send_message(embed=embed)

#Slash Ping Command
@bot.tree.command(name="ping", description="Get Bot Ping!")
async def slashping(interaction):
    embed = discord.Embed(
        title="Pong!",
        description=f"**{round(bot.latency * 1000)}ms**",
        color=0x662a85
    )
    await interaction.response.send_message(embed=embed)

#Slash Invite Command
@bot.tree.command(name="invite", description="Invite The Bot!")
async def slashinvite(interaction):
    embed = discord.Embed(
        title="Invite",
        description="Click [here](https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands) to invite the bot!",
        color=0x662a85
    )
    await interaction.response.send_message(embed=embed)

#Slash Help Command
@bot.tree.command(name="bot-help", description="Get Bot Help!")
async def bot_help(interaction):
    await interaction.defer()
    embed = discord.Embed(
        title="Silly Chat",
        description="Prefix: g!",
        color=0x662a85
    )
    embed.set_footer(text="Thank you for using Silly Chat!")
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/8lntiVCa9JwRxnqX6rxvWdEWWmwIiz5xFeTxmdRSydE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1051199485168066610/d40794f36524ec9e9a4e723679d14d6d.png?width=670&height=670")
    view = HelpMenu()
    await interaction.edit_original_message(embed=embed, view=view)

#Start the bot!
bot.run(c['token'], log_handler=handler, log_level=logging.ERROR)
