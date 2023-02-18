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
    import discord_webhook  
except ImportError: 
    print("discord_webhook Not Found...\nInstalling...")
    os.system("pip install discord_webhook")
    print("discord_webhook Installed")
try: 
    import os
    import requests  
except ImportError: 
    print("requests Not Found...\nInstalling...")
    os.system("pip install requests")
    print("requests Installed")
try: 
    import os
    import pydactyl  
except ImportError: 
    print("pydactyl Not Found...\nInstalling...")
    os.system("pip install py-dactyl")
    print("pydactyl Installed")
try: 
    import os
    import pyjokes  
except ImportError: 
    print("pyjokes Not Found...\nInstalling...")
    os.system("pip install pyjokes")
    print("pyjokes Installed")
#import Modules
import os
import urllib.request
from datetime import datetime
import asyncio
import discord
import shutil
import pytz
import string
import discord_webhook
from discord_webhook import DiscordWebhook
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
last_usage = {675589895137394705}
ball8answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
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
bot = commands.Bot(command_prefix = c['prefix'],intents=discord.Intents.all(),status=discord.Status.idle,case_insensitive=True)
bot.remove_command('help')
#Ptero Api
api = PterodactylClient('https://panel.sillydev.co.uk', c['ptero_account_key'])
#Load Server File
if os.path.isfile("config/servers.json"):
    with open('config/servers.json', encoding='utf-8') as f:
        servers = json.load(f)
else:
    servers = {"servers": []}
    with open('config/servers.json', 'w') as f:
        json.dump(servers, f, indent=4)
#Load Banned Users
if os.path.isfile("config/banned.json"):
    with open('config/banned.json', encoding='utf-8') as f:
        banned = json.load(f)
else:
    banned = {"banned": []}
    with open('config/banned.json', 'w') as f:
        json.dump(banned, f, indent=4)
#Load Admin Users
if os.path.isfile("config/admins.json"):
    with open('config/admins.json', encoding='utf-8') as f:
        adminusers = json.load(f)
else:
    adminusers = {"admins": []}
    with open('config/admins.json', 'w') as f:
        json.dump(adminusers, f, indent=4)
#------------------------------------------Bot Events-------------------------------------------------
#Auto Updating Status
async def StatusChange():
    while True:
        usercount = len(list(filter(lambda m: m.bot == False, bot.users)))
        await bot.change_presence(activity=discord.Game(f'g!help | {len(bot.guilds)} Servers'))
        await asyncio.sleep(35)
        await bot.change_presence(activity=discord.Game(f'g!help | {usercount} Users'))
        await asyncio.sleep(35)
        await bot.change_presence(
            activity=discord.Game('g!help | discord.gg/3qvpkgWSbF')
        )
        await asyncio.sleep(35)
        await bot.change_presence(activity=discord.Game('g!help | Invite Me Today!'))
        await asyncio.sleep(35)
        await bot.change_presence(activity=discord.Game('g!help | Silly Chat'))
        await asyncio.sleep(35)
        await bot.change_presence(activity=discord.Game('g!help | Downloading 2024'))
        await asyncio.sleep(35)
        await bot.change_presence(activity=discord.Game('g!help | Gamer3514#7679'))
        await asyncio.sleep(35)
#Webhook Logging
async def Webhooklogging(channel,message):
        webhook = DiscordWebhook(url=channel, content=message)
        response = webhook.execute()
        print(message)
#Event that runs when bot is online
@bot.event
async def on_ready():
    print(f'{bot.user} Is Now Online And Ready To Send Messages!')
    await bot.loop.create_task(StatusChange())
#Event for when a message is sent
@bot.event
async def on_message(message):
    staffonly = False
    adminz = [int(admin["userid"]) for admin in adminusers["admins"]]
    bannedusers = [int(buser["userid"]) for buser in banned["banned"]]
    possiblechannels = [
        int(channel["channelid"]) for channel in servers["servers"]
    ]
    if message.author.bot:
        return
    if staffonly and message.author.id in adminz:
        print("User = Staff, Sending!")
        if get_globalChat(message.guild.id, message.channel.id):
            await sendAll(message)
    elif not staffonly:
        if message.author.id in bannedusers and message.channel.id in possiblechannels:
            user = message.author
            embed = discord.Embed(description="**You Are Bannned!**\r\n"
            "It seems you have been banned from using this feature!\nBelieve this is a mistake? Please join our support server!",
            color=0x2ecc71)
            await user.send(embed=embed)
            await message.delete()
        elif get_globalChat(message.guild.id, message.channel.id):
            if message.content.startswith('g!'):
                await message.delete()
            else:
                await sendAll(message)
    else:
        user = message.author
        embed = discord.Embed(description="**Silly Chat Is Locked!**\r\n"
        "It seems that a bot mod has disabled Silly Chat! Please try send your message later!\nBelieve this is a mistake? Please join our support server!",
        color=0x2ecc71)
        await user.send(embed=embed)
        await message.delete()
    await bot.process_commands(message)
#Send All Message
async def sendAll(message: Message):
    await Webhooklogging(c['webhook'],f'Message "{message.content}" was sent by "{message.author.id}" in guild {message.guild.id}!')
    adminz = [int(admin["userid"]) for admin in adminusers["admins"]]
    role = "Bot Moderator" if message.author.id in adminz else "Member"
    conent = message.content
    author = message.author
    attachments = message.attachments
    de = pytz.timezone('Europe/London')
    embed = discord.Embed(description=conent, timestamp=datetime.now().astimezone(tz=de), color=author.color)
    icon = message.author.avatar.url
    username = f"{author.name}#{author.discriminator} - {role}"
    embed.set_author(name=username, icon_url=icon)
    try :
        footer_icon_url = message.guild.icon.url
    except AttributeError:
        footer_icon_url = "https://ia903204.us.archive.org/4/items/discordprofilepictures/discordgrey.png"
    embed.set_footer(
        text=f'{message.guild.name} | {message.guild.member_count} Members!',
        icon_url = footer_icon_url
        )
    embed.set_thumbnail(url=message.author.avatar.url)
    embed.add_field(name="** **", value="`📌`[Support](https://discord.gg/3qvpkgWSbF)・`🤖`[Bot-Invite](https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands)", inline=False)
    if len(attachments) > 0:
            img = attachments[0]
            randomname = await get_random_string(8)
            await message.attachments[0].save(f'temp/{randomname}.png')
            await asyncio.sleep(3.75)
            headers = {"Authorization": f"Bearer {c['edenai_key']}"}
            url="https://api.edenai.run/v2/image/explicit_content"
            data={"providers": "google"}
            files={'file': open(f"temp/{randomname}.png",'rb')}
            response = requests.post(url, data=data, files=files, headers=headers)
            result = json.loads(response.text)
            score = result['google']['nsfw_likelihood']
            score2 = int(score)
    for server in servers["servers"]:
        if guild := bot.get_guild(int(server["guildid"])):
            if channel := guild.get_channel(int(server["channelid"])):
                perms: Permissions = channel.permissions_for(guild.get_member(bot.user.id))
                if perms.send_messages:
                    if perms.embed_links and perms.attach_files and perms.external_emojis:
                        try:
                            if score2 in [3, 4, 5]:
                                await message.delete()
                                user = message.author
                                embed = discord.Embed(
                                    title="NSFW Detected!",
                                    description=f"Our Systems Have Detected NSFW In Your Image!\nIf you believe this is a mistake please contact our support.",
                                    color=0x662A85,
                                )
                                await user.send(embed=embed)
                            else:
                                file = discord.File(f"temp/{randomname}.png", filename=f"{randomname}.png")
                                embed.set_image(url=f"attachment://{randomname}.png")
                                await channel.send(file=file, embed=embed)
                        except UnboundLocalError:
                            await channel.send(embed=embed)
                    else:
                        await channel.send('ERROR: I seem to be missing required permissions! I require ``Embed Links``, ``Attach Files`` and ``External Emojis``')
    await message.delete()
#System Message
async def sendsystemmessage(systemmessage):
    conent = str(systemmessage)
    print(systemmessage)
    de = pytz.timezone('Europe/London')
    embed = discord.Embed(description=conent, timestamp=datetime.now().astimezone(tz=de), color=0xe74c3c)
    embed.set_author(name="SYSTEM MESSAGE", icon_url="https://images-ext-1.discordapp.net/external/wkzBNe0CFnA8pCMJAkRUMQpc3i_wWJS07j9wezmMbnQ/%3Fwidth%3D670%26height%3D670/https/images-ext-2.discordapp.net/external/8lntiVCa9JwRxnqX6rxvWdEWWmwIiz5xFeTxmdRSydE/%253Fsize%253D1024/https/cdn.discordapp.com/avatars/1051199485168066610/d40794f36524ec9e9a4e723679d14d6d.png?width=603&height=603")
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/wkzBNe0CFnA8pCMJAkRUMQpc3i_wWJS07j9wezmMbnQ/%3Fwidth%3D670%26height%3D670/https/images-ext-2.discordapp.net/external/8lntiVCa9JwRxnqX6rxvWdEWWmwIiz5xFeTxmdRSydE/%253Fsize%253D1024/https/cdn.discordapp.com/avatars/1051199485168066610/d40794f36524ec9e9a4e723679d14d6d.png?width=603&height=603")
    embed.add_field(name="** **", value="`📌`[Support](https://discord.gg/3qvpkgWSbF)・`🤖`[Bot-Invite](https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands)", inline=False)
    for server in servers["servers"]:
        if guild := bot.get_guild(int(server["guildid"])):
            if channel := guild.get_channel(int(server["channelid"])):
                perms: Permissions = channel.permissions_for(guild.get_member(bot.user.id))
                if perms.send_messages:
                    if perms.embed_links and perms.attach_files and perms.external_emojis:
                            await channel.send(embed=embed)
                    else:
                        await channel.send('ERROR: I seem to be missing required permissions! I require ``Embed Links``, ``Attach Files`` and ``External Emojis``')
#Gen Random String
async def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
#Event for when someone sets up the bot
async def sendAllWelcome(ctx):
    try :
        footer_icon_url = ctx.guild.icon.url
    except AttributeError:
        footer_icon_url = "https://ia903204.us.archive.org/4/items/discordprofilepictures/discordgrey.png"
    de = pytz.timezone('Europe/London')
    embed = discord.Embed(
        title="Welcome!",
        description=f'Thank you {ctx.guild.name} for adding the bot!\nIf you experience any issues please join our support server!',
        color=0x662A85,
        timestamp=datetime.now().astimezone(tz=de),
    )
    embed.set_footer(text=f'{ctx.guild.name} | {ctx.guild.member_count} Members!',
                     icon_url=f'{footer_icon_url}')
    embed.set_thumbnail(url=footer_icon_url)
    embed.add_field(name="** **", value=f"Silly Chat Is Now In {len(bot.guilds)} Servers!", inline=False)
    embed.add_field(name="** **", value="`📌`[Support](https://discord.gg/3qvpkgWSbF)・`🤖`[Bot-Invite](https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands)", inline=False)
    for server in servers["servers"]:
        if guild := bot.get_guild(int(server["guildid"])):
            if channel := guild.get_channel(int(server["channelid"])):
                await channel.send(embed=embed)
    await ctx.message.delete()
def guild_exists(guildid):
    return any(
        int(server['guildid'] == int(guildid)) for server in servers['servers']
    )
def get_globalChat(guild_id, channelid=None):
    globalChat = None
    for server in servers["servers"]:
        if int(server["guildid"]) == int(guild_id):
            if channelid:
                if int(server["channelid"]) == int(channelid):
                    globalChat = server
            else:
                globalChat = server
    return globalChat
def get_globalChat_id(guild_id):
    globalChat = -1
    for i, server in enumerate(servers["servers"]):
        if int(server["guildid"]) == int(guild_id):
            globalChat = i
    return globalChat
def get_banned_id(user_id):
    globalChat = -1
    for i, bannedusr in enumerate(banned["banned"]):
        if int(bannedusr["userid"]) == int(user_id):
            globalChat = i
    return globalChat
#Bot join event
@bot.event
async def on_guild_join(guild):
    await Webhooklogging(c['webhook'],f'I Have Been Added To {guild.name} !')
#Bot leave event
@bot.event
async def on_guild_remove(guild):
    await Webhooklogging(c['webhook'],f'I Have Been Removed From {guild.name} !')
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
            description="**Prefix: g!**",
            color=discord.Color.random()
        )
    embed.add_field(name="g!setGlobal", value="Add global chat to a channel!", inline=False)
    embed.add_field(name="g!removeGlobal", value="Remove global chat from a channel!", inline=False)
    embed.set_footer(text="Thank You For Using Silly Chat!")
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/8lntiVCa9JwRxnqX6rxvWdEWWmwIiz5xFeTxmdRSydE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1051199485168066610/d40794f36524ec9e9a4e723679d14d6d.png?width=670&height=670")
    await interaction.response.edit_message(embed=embed)
  @discord.ui.button(label="Info", style=discord.ButtonStyle.grey, emoji="<:info:1071407819670175774>")
  async def infomenu(self, interaction: discord.Interaction, button: discord.ui.Button):
    embed = discord.Embed(
            title="**Silly Chat - Info**",
            description="**Prefix: g!**",
            color=discord.Color.random()
        )
    embed.add_field(name="g!ping", value="Check the bot's ping", inline=False)
    embed.add_field(name="g!stats", value="Check the bot's stats!", inline=False)
    embed.add_field(name="g!invite", value="Invite me to your server!", inline=False)
    embed.add_field(name="g!support", value="Get a link to our support server!", inline=False)
    embed.add_field(name="g!github", value="Get a link to the bot's github!", inline=False)
    embed.add_field(name="g!credits", value="View the creators of the bot!", inline=False)
    embed.add_field(name="g!vote", value="Vote for the bot!", inline=False)
    embed.set_footer(text="Thank You For Using Silly Chat!")
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/8lntiVCa9JwRxnqX6rxvWdEWWmwIiz5xFeTxmdRSydE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1051199485168066610/d40794f36524ec9e9a4e723679d14d6d.png?width=670&height=670")
    await interaction.response.edit_message(embed=embed)
  @discord.ui.button(label="Fun", style=discord.ButtonStyle.grey, emoji="🤣")
  async def funmenu(self, interaction: discord.Interaction, button: discord.ui.Button):
    embed = discord.Embed(
            title="**Silly Chat - Fun**",
            description="**Prefix: g!**",
            color=discord.Color.random()
        )
    embed.add_field(name="g!ai", value="Chat to Darren!", inline=False)
    embed.add_field(name="g!8ball", value="Use Magic 8 Ball!", inline=False)
    embed.add_field(name="g!joke", value="Generate A Random Joke!", inline=False)
    embed.add_field(name="g!rock", value="Generate A Rock!", inline=False)
    embed.add_field(name="g!coinflip", value="Flip A Coin!", inline=False)
    embed.add_field(name="g!kill", value="Kill Someone!", inline=False)
    embed.add_field(name="g!meme", value="Generate A Meme!", inline=False)
    embed.add_field(name="g!avatar", value="Steal Someone's Avatar!", inline=False)
    embed.set_footer(text="Thank You For Using Silly Chat!")
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/8lntiVCa9JwRxnqX6rxvWdEWWmwIiz5xFeTxmdRSydE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1051199485168066610/d40794f36524ec9e9a4e723679d14d6d.png?width=670&height=670")
    await interaction.response.edit_message(embed=embed)
  @discord.ui.button(label="Bot Moderator", style=discord.ButtonStyle.grey, emoji="<:Role:942348530117410826>")
  async def botmodmenu(self, interaction: discord.Interaction, button: discord.ui.Button):
    embed = discord.Embed(
            title="**Silly Chat - Bot Moderator**",
            description="**Prefix: g!**",
            color=discord.Color.random()
        )
    embed.add_field(name="g!ban", value="Ban a user from using the bot!", inline=False)
    embed.add_field(name="g!unban", value="Remove a user from the banned list!", inline=False)
    embed.add_field(name="g!dm", value="Dm a specified user!", inline=False)
    embed.set_footer(text="Thank You For Using Silly Chat!")
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/8lntiVCa9JwRxnqX6rxvWdEWWmwIiz5xFeTxmdRSydE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1051199485168066610/d40794f36524ec9e9a4e723679d14d6d.png?width=670&height=670")
    await interaction.response.edit_message(embed=embed)
#------------------------------------------Prefix Bot Commands (User)-------------------------------------------------
#Help Command
@bot.command()
async def help(ctx):
    embed = discord.Embed(
            title="**Silly Chat**",
            description="**Prefix: g!**",
            color=discord.Color.blue()
        )
    embed.set_footer(text="Thank You For Using Silly Chat!")
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/8lntiVCa9JwRxnqX6rxvWdEWWmwIiz5xFeTxmdRSydE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1051199485168066610/d40794f36524ec9e9a4e723679d14d6d.png?width=670&height=670")
    view = HelpMenu()
    await ctx.reply(embed=embed,view=view)
#Set Global Command
@bot.command()
async def setGlobal(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!setGlobal')
    if ctx.author.guild_permissions.administrator:
        if not guild_exists(ctx.guild.id):
            server = {
                "guildid": ctx.guild.id,
                "channelid": ctx.channel.id,
                "invite": "null"
            }
            servers["servers"].append(server)
            with open('servers.json', 'w') as f:
                json.dump(servers, f, indent=4)
            embed = discord.Embed(title="**Welcome!**",
                                  description="Thank you for using our bot!"
                                              " Messages will now be sent and recieved!"
                                              " Have fun!",
                                  color=0x2ecc71)
            embed.set_footer(text="To reduce the chances of your user's being banned, please set a slowmode of atleast 5 seconds!")
            await ctx.send(embed=embed)
            await sendAllWelcome(ctx)
        else:
            embed = discord.Embed(description="You have already setup the bot!\r\n"
                                              "To setup the bot again do `g!removeGlobal` then run this command again!",
                                  color=0x2ecc71)
            await ctx.send(embed=embed)
#Remove Global Command
@bot.command()
async def removeGlobal(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!removeGlobal')
    if ctx.author.guild_permissions.administrator:
        if guild_exists(ctx.guild.id):
            globalid = get_globalChat_id(ctx.guild.id)
            if globalid != -1:
                servers["servers"].pop(globalid)
                with open('servers.json', 'w') as f:
                    json.dump(servers, f, indent=4)
            embed = discord.Embed(title="**Goodbye!**",
                                  description="Sad to see you go! If you want to setup the bot again use"
                                              " `g!setGlobal`!",
                                  color=0x2ecc71)
        else:
            embed = discord.Embed(description="No Global Channel Set.\r\n"
                                              "Use `g!setGlobal` to set one!\nBelieve this is a mistake? Join our support server!",
                                  color=0x2ecc71)

        await ctx.send(embed=embed)
#Coin Flip Command
@bot.command(aliases=['headsortails'])
async def coinflip(ctx):
        embed=discord.Embed(title="Coinflip", description=heads_tails[random.randint(0, len(heads_tails)-1)], color=0xFCBA03)
        await ctx.send(embed=embed)
#8Ball Command
@bot.command(aliases=['8ball'])
async def magic8ball(ctx):
        embed=discord.Embed(title=":8ball: Magic 8 Ball :8ball:", description=ball8answers[random.randint(0, len(ball8answers)-1)], color=0xFCBA03)
        await ctx.send(embed=embed)
#Joke Command
@bot.command(aliases=['randomjoke'])
async def joke(ctx):
        joke1 = pyjokes.get_joke(language='en', category='all')
        embed=discord.Embed(title="Random Joke Machine", description=joke1, color=discord.Color.random())
        await ctx.send(embed=embed)
#Meme Command
@bot.command(aliases=['genmeme'])
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://meme-api.com/gimme") as resp:
            data = await resp.json()
            embed = discord.Embed(title=f"Meme Generated! - {data['title']}",color=discord.Color.random())
            embed.set_image(url=f"{data['url']}")
            randfooter = ["Thank You for using Silly Chat!", "Did You Know? Silly Chat is open source on Github! g!github", "Did You Know? Silly Chat is owned by Gamer3514#7679!"]
            embed.set_footer(text=randfooter[random.randint(0, len(randfooter)-1)])
            await ctx.send(embed=embed)
#Hitman Command
deathoptions=["Instantly Died","Had death appear at their door","Had Death Occur","Fell of a cliff","got too bored","vanished","got shot in the head with a laser","got too comftorable around bears","got depression and gave up","ended up in hell","dissapeared","Jumped Off A Building","Died","Fell up a flight of stairs.","Thought a necular power plant was a good place to go on holiday","Liked Jazz","Became a musician","Ate McDonalds","Became an artist","Turned to the dark side","Liked limes for some reason","Became a meme","Got 360 NO SCOPED BY A FOUR YEAR OLD!","Tried to play fortnite mobile","Didn't die!","Didn't have death occur!"]
@bot.command(aliases=['hitman'])
async def kill(ctx, person : discord.Member = None):
    randfooter = ["Thank You for using Silly Chat!", "Did You Know? Silly Chat is open source on Github! g!github", "Did You Know? Silly Chat is owned by Gamer3514#7679!"]
    if not person:
            embed=discord.Embed(title="No User Selected", description="Correct Usage:\ng!kill @user\ng!hitman userid", color=0xFCBA03)
            embed.set_footer(text=randfooter[random.randint(0, len(randfooter)-1)])
            await ctx.send(embed=embed)
    embed = discord.Embed(
        title="DEAD!",
        description=f"{person.mention} {random.choice(deathoptions)}",
    )
    embed.set_footer(text=randfooter[random.randint(0, len(randfooter)-1)])
    await ctx.send(embed=embed)
#Rock Command
@bot.command(aliases=['genrock'])
async def rock(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://rockapi.apiworks.tech/rock/random") as api:
            data = await api.json()
            rok_name = data["name"]
            rok_desc = data["description"]
            rok_img = data["image"]
            embed = discord.Embed(title=rok_name, description=rok_desc)
            if rok_img != "none":
                embed.set_image(url=rok_img)
            await ctx.send(embed=embed)
#Ai Command
@bot.command()
async def ai(ctx, *, prompt: str):
    async with aiohttp.ClientSession() as session:
        randfooter = ["Thank You for using Silly Chat!", "Did You Know? Darren was originally just a seperate bot but now its here aswell!", "Did You Know? Silly Chat is open source on Github! g!github", "Did You Know? Silly Chat is owned by Gamer3514#7679!"]
        uid = ctx.message.author.id
        async with session.get(f"http://api.brainshop.ai/get?bid={c['bid']}&key={c['key']}&uid={uid}&msg={prompt}") as resp:
            responce = await resp.json()
            embed = discord.Embed(title="Darren Has Spoken!", description=responce["cnt"])
            embed.set_footer(text=randfooter[random.randint(0, len(randfooter)-1)])
            await ctx.reply(embed=embed)
#Invite Command
@bot.command()
async def invite(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!invite')
    embed=discord.Embed(title="\n<a:discord:942344157618405416>Invite<a:discord:942344157618405416>\n", url="https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands",color=0x662a85)
    await ctx.send(embed=embed)
#Avatar Command
@bot.command()
async def avatar(ctx,  member: discord.Member = None):
        if not member:
            embed=discord.Embed(title="No User Selected", description="Correct Usage:\n!avatar @user\n!avatar userid", color=0xFCBA03)
            await ctx.send(embed=embed)
        embed = discord.Embed(colour=discord.Colour.random(), title=f"{member}'s avatar")
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)
#Ping Command
@bot.command(name='ping', aliases=['botping'])
async def ping(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!ping')
    embed = discord.Embed(
        title='Pong!',
        description=f'**{round(bot.latency * 1000)}ms**',
        color=0x662A85,
    )
    await ctx.send(embed=embed)
#Youtube Command
@bot.command(name='youtube', aliases=['yt'])
async def youtube(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!youtube')
    embed = discord.Embed(
        title='Subscribe On Youtube!',
        description='[Here!](https://youtube.com/c/thegamer3514)',
        color=0x662A85,
    )
    await ctx.send(embed=embed)
#TikTok Command
@bot.command(name='tiktok', aliases=['tk'])
async def tiktok(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!tiktok')
    embed = discord.Embed(
        title='Follow On Tiktok!', description='@elon_fan.1', color=0x662A85
    )
    await ctx.send(embed=embed)
#Stats Command
@bot.command(name='stats', aliases=['botstats'])
async def stats(ctx):	
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!stats')
    embed = discord.Embed(title='My Stats:', color=0x662a85)
    embed.add_field(name="Bot Owner", value="<@763471049894527006> (763471049894527006) Gamer3514#7679", inline=False)
    embed.add_field(name="Cpu Cores", value=multiprocessing.cpu_count(), inline=False)
    embed.add_field(name="Server Count", value=f"{len(bot.guilds)}", inline=False)
    embed.add_field(name="Bot Latency", value=f"{round(bot.latency * 1000)}ms", inline=False)
    embed.add_field(name="Cpu Usage", value=f"{psutil.cpu_percent()}%", inline=False)
    embed.add_field(name="Memory Usage", value=f"{psutil.virtual_memory().percent}%", inline=False)
    embed.add_field(name="Total Memory", value=f"{round(psutil.virtual_memory().total / (1024.0 **3))} GB", inline=False)
    await ctx.send(embed=embed)
#Botlists Command
@bot.command(name='botlists', aliases=['vote'])
async def botlists(ctx):	
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!botlists')
    embed = discord.Embed(title='Vote For Me!', color=0x662a85)
    embed.add_field(name="Top.gg", value="[Vote Here!](https://top.gg/bot/1051199485168066610)", inline=True)
    embed.add_field(name="Spectrum Lists", value="[Vote Here!](https://spectrumlists.xyz/bot/1051199485168066610)", inline=True)
    embed.add_field(name="Discord Bot List", value="[Vote Here!](https://discordbotlist.com/bots/silly-chat)", inline=True)
    await ctx.send(embed=embed)
#Github Command
@bot.command(name='github', aliases=['source'])
async def github(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!github')
    embed = discord.Embed(
        title = "Github",
        color=0x662a85)
    embed.add_field(name="", value="This Bot's Github Can Be Found [Here](https://github.com/TheGamer3514/silly-chat)")  
    await ctx.send(embed=embed)
#Credits Command
@bot.command(name='credits', aliases=['botcredits'])
async def credits(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!credits')
    embed = discord.Embed(
        title = "Credits",
        color=0x662a85)
    embed.add_field(name="Gamer3514#7679", value="Bot Owner! Maintains the bot, made most systems!")  
    embed.add_field(name="ukcai#7121", value="Bot Developer & Moderator! Helped improve systems and made comamnds such as g!stats")
    embed.add_field(name="AlpineVr#0001", value="Bot Moderator! Helps keep the chat SFW. Helped with slash commands and more!")
    await ctx.send(embed=embed)
#Support Command
@bot.command(name='support', aliases=['ss'])
async def support(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!support')
    embed = discord.Embed(
        title='<a:discord:942344157618405416> Do you need support? Join our support server! <a:discord:942344157618405416>',
        description='**[Support server](https://discord.gg/3qvpkgWSbF)**',
        color=0x662A85,
    )
    await ctx.send(embed=embed)
#Gamer Command
@bot.command(name='gamer', aliases=['gamer3514'])
async def gamer(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!gamer')
    embed = discord.Embed(
        title='Gamer Is Cool!',
        description='<@763471049894527006> is a super cool human! He is cracked at fortnite and he made this bot!',
        color=0x662A85,
    )
    await ctx.send(embed=embed)
#Cai Command
@bot.command(name='cai', aliases=['ukcai'])
async def cai(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!cai')
    embed = discord.Embed(
        title='Ukcai',
        description='<@967904098047381587> assisted in development of silly chat in multiple ways! He helped by suggesting loads of new features and helped with commands such as g!stats command. You can find his website [here!](https://ukcai.me) Very cool!',
        color=0x662A85,
    )
    await ctx.send(embed=embed)
#Alpine Command
@bot.command(name='alpine', aliases=['alpinevr'])
async def alpine(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!alpine')
    embed = discord.Embed(
        title='AlpineVR',
        description='<@675589895137394705>  is pretty awesome and helps moderate this bot. He also owns a bot: [Studio](https://studiobot.xyz/)',
        color=0x662A85,
    )
    await ctx.send(embed=embed)
#------------------------------------------ Prefix Bot Commands (Bot Mod)-------------------------------------------------
#Dm Command
@bot.command(name='dm', aliases=['dmuser'])
async def dm(ctx, user: discord.User = None, *, value=None):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!dm {user} {value}')
    adminz = [int(admin["userid"]) for admin in adminusers["admins"]]
    if ctx.message.author.id in adminz:
        if user == ctx.message.author:
            await user.send("**You can't DM yourself, or maybe you can?**")
        await ctx.message.delete()
        if user is None:
            await ctx.send(f'**{ctx.message.author},** Please mention somebody to DM.')
        elif value is None:
            await ctx.send(f'**{ctx.message.author},** Please send a message to DM.')
        else:
            await user.send(value)
    else:
        embed = discord.Embed(
            title='Error!',
            description="You are not permitted to use this command!",
            color=0x662A85,
        )
        await ctx.send(embed=embed)
#Ban Command
@bot.command()
async def ban(ctx, user: discord.User = None):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!ban {user}')
    currentbanned = [buser["userid"] for buser in banned["banned"]]
    adminz = [int(admin["userid"]) for admin in adminusers["admins"]]
    if ctx.message.author.id in adminz and ctx.message.author.id not in currentbanned:
        if user.id not in currentbanned:
            banned2 = {
                "userid": user.id
                }
            banned["banned"].append(banned2)
            with open('banned.json', 'w') as f:
                json.dump(banned, f, indent=4)
            embed=discord.Embed(title="Banned!",color=0x662a85)
            dmembed = discord.Embed(title="You Have Been Banned From Silly Chat!",color=0x662a85)
            await user.send(embed=dmembed)
        else:
            embed=discord.Embed(title="User Is Already Banned!",color=0x662a85)
    else:
        embed = discord.Embed(
            title='Error!',
            description="You are not permitted to use this command!",
            color=0x662A85,
        )

    await ctx.send(embed=embed)
#Unban Command
@bot.command()
async def unban(ctx, user: discord.User = None):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!unban {user}')
    currentbanned = [buser["userid"] for buser in banned["banned"]]
    adminz = [int(admin["userid"]) for admin in adminusers["admins"]]
    if ctx.message.author.id in adminz and ctx.message.author.id not in currentbanned:
        if user.id in currentbanned:
            userid = get_banned_id(user.id)
            banned["banned"].pop(userid)
            with open('banned.json', 'w') as f:
                json.dump(banned, f, indent=4)
            embed=discord.Embed(title="Unbanned!",color=0x662a85)
            dmembed = discord.Embed(title="You Have Been Unbanned From Silly Chat!",color=0x662a85)
            await user.send(embed=dmembed)
        else:
            embed=discord.Embed(title="User Is Not Banned!",color=0x662a85)
    else:
        embed = discord.Embed(
            title='Error!',
            description="You are not permitted to use this command!",
            color=0x662A85,
        )

    await ctx.send(embed=embed)
#Scan Image Command
@bot.command()
async def scanimage(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!scanimage')
    adminz = [int(admin["userid"]) for admin in adminusers["admins"]]
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
                title='Image Scanned!',
                description=f"Nsfw Rating: {result['google']['nsfw_likelihood']}",
                color=0x662A85,
            )
        else:
            embed = discord.Embed(
                title='Error!',
                description="You have not provided an image to scan!",
                color=0x662A85,
            )
    else:
        embed = discord.Embed(
            title='Error!',
            description="You are not permitted to use this command!",
            color=0x662A85,
        )

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
            title='Error!',
            description="You are not permitted to use this command!",
            color=0x662A85,
        )
        await ctx.send(embed=embed)
#Update User Command
@bot.command()
async def updateuser(ctx, user: discord.User = None):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!updateuser {user}')
    if ctx.message.author.id == 763471049894527006:
        adminz = [int(admin["userid"]) for admin in adminusers["admins"]]
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
        else:
            embed=discord.Embed(title="Removing Admins Coming Soon",color=0x662a85)
    else:
        embed = discord.Embed(
            title='Error!',
            description="You are not permitted to use this command!",
            color=0x662A85,
        )

    await ctx.send(embed=embed)
#Power Action Command
#Delete From Here
@bot.command()
async def poweraction(ctx, value = None):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!poweraction {value}')
    adminz = [int(admin["userid"]) for admin in adminusers["admins"]]
    if ctx.message.author.id == 763471049894527006:
        embed = discord.Embed(
            title='Complete!', description="Power Action Sent!", color=0x662A85
        )
        await ctx.send(embed=embed)
        api.client.servers.send_power_action(c['ptero_srv_id'], value)
    else:
        embed = discord.Embed(
            title='Error!',
            description="You are not permitted to use this command!",
            color=0x662A85,
        )
        await ctx.send(embed=embed)
#To Here to remove the poweraction command (for people not using Pterodactyl Panel)
#Database Command
@bot.command(name='database', aliases=['viewdatabase'])
async def database(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!database')
    owner = await bot.fetch_user("763471049894527006")
    if owner == ctx.message.author:
        print("Database Export:")
        f = open('config/servers.json')
        data = json.load(f)
        for i in data['servers']:
            print(i)
            embed = discord.Embed(
                title='DataBase Export! (Servers)',
                description=i,
                color=0x662A85,
            )
            user = await bot.fetch_user("763471049894527006")
            await user.send(embed=embed)
            f.close()
        bannedE = open('config/banned.json')
        data = json.load(bannedE)
        for i in data['banned']:
            print(i)
            embed = discord.Embed(
                title='DataBase Export! (Banned Users)',
                description=i,
                color=0x662A85,
            )
            user = await bot.fetch_user("763471049894527006")
            await user.send(embed=embed)
            bannedE.close()
        adminz = open('config/admins.json')
        data = json.load(adminz)
        for i in data['admins']:
            print(i)
            embed = discord.Embed(
                title='DataBase Export! (Admin Users)',
                description=i,
                color=0x662A85,
            )
            user = await bot.fetch_user("763471049894527006")
            await user.send(embed=embed)
            adminz.close()
    else:
        embed = discord.Embed(
            title='Error!',
            description="You are not permitted to use this command!",
            color=0x662A85,
        )
        await ctx.send(embed=embed)
#System Message Command
@bot.command(name='systemmessage', aliases=['sendsystemmessage'])
async def systemmessage(ctx, message: str):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!systemmessage')
    if ctx.message.author.id == 763471049894527006:
        print(message)
        await sendsystemmessage(message)
        embed = discord.Embed(
            title='Complete!',
            description="Message Has Been Sent!",
            color=0x662A85,
        )
    else:
        embed = discord.Embed(
            title='Error!',
            description="You are not permitted to use this command!",
            color=0x662A85,
        )

    await ctx.send(embed=embed)
#------------------------------------------Slash Bot Commands (User)-------------------------------------------------
#Slash Support Command
@bot.tree.command(name="support", description="Get Bot Support!")
async def slashsupport(interaction):
    embed = discord.Embed(
        title='<a:discord:942344157618405416> Do you need support? Join our support server! <a:discord:942344157618405416>',
        description='**[Support server](https://discord.gg/3qvpkgWSbF)**',
        color=0x662A85,
    )
    await interaction.response.send_message(embed=embed)
#Slash Credits Command
@bot.tree.command(name="credits", description="View Bot Credits!")
async def slashcredits(interaction):
    embed = discord.Embed(
        title = "Credits",
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
    embed = discord.Embed(title='Vote For Me!', color=0x662a85)
    embed.add_field(name="Top.gg", value="[Vote Here!](https://top.gg/bot/1051199485168066610)", inline=True)
    embed.add_field(name="Spectrum Lists", value="[Vote Here!](https://spectrumlists.xyz/bot/1051199485168066610)", inline=True)
    embed.add_field(name="Discord Bot List", value="[Vote Here!](https://discordbotlist.com/bots/silly-chat)", inline=True)
    await interaction.response.send_message(embed=embed)
#Slash Stats Command
@bot.tree.command(name="stats", description="View Bot Stats!")
async def slashstats(interaction):	
    embed = discord.Embed(title='My Stats:', color=0x662a85)
    embed.add_field(name="Bot Owner", value="<@763471049894527006> (763471049894527006) Gamer3514#7679", inline=False)
    embed.add_field(name="Cpu Cores", value=multiprocessing.cpu_count(), inline=False)
    embed.add_field(name="Server Count", value=f"{len(bot.guilds)}", inline=False)
    embed.add_field(name="Bot Latency", value=f"{round(bot.latency * 1000)}ms", inline=False)
    embed.add_field(name="Cpu Usage", value=f"{psutil.cpu_percent()}%", inline=False)
    embed.add_field(name="Memory Usage", value=f"{psutil.virtual_memory().percent}%", inline=False)
    embed.add_field(name="Total Memory", value=f"{round(psutil.virtual_memory().total / (1024.0 **3))} GB", inline=False)
    await interaction.response.send_message(embed=embed)
#Slash TikTok Command
@bot.tree.command(name="tiktok", description="Get A Link To Our TikTok!")
async def slashtiktok(interaction):
    embed = discord.Embed(
        title='Follow Me On Tiktok!', description='@elon_fan.1', color=0x662A85
    )
    await interaction.response.send_message(embed=embed)
#Slash Youtube Command
@bot.tree.command(name="youtube", description="Get A Link To Our Youtube!")
async def slashyoutube(interaction):
    embed = discord.Embed(
        title='Subscribe On Youtube!',
        description='[Here!](https://youtube.com/c/thegamer3514)',
        color=0x662A85,
    )
    await interaction.response.send_message(embed=embed)
#Slash Ping Command
@bot.tree.command(name="ping", description="Get Bot Ping!")
async def slashping(interaction):
    embed = discord.Embed(
        title='Pong!',
        description=f'**{round(bot.latency * 1000)}ms**',
        color=0x662A85,
    )
    await interaction.response.send_message(embed=embed)
#Slash Invite Command
@bot.tree.command(name="invite", description="Invite The Bot!")
async def slashinvite(interaction):
    embed=discord.Embed(title="\n<a:discord:942344157618405416>Invite<a:discord:942344157618405416>\n", url="https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands",color=0x662a85)
    await interaction.response.send_message(embed=embed)
#Slash Help Command
@bot.tree.command(name="help", description="Get Bot Help!")
async def help(interaction):
    embed = discord.Embed(
            title="**Silly Chat**",
            description="**Prefix: g!**",
            color=discord.Color.blue()
        )
    embed.set_footer(text="Thank You For Using Silly Chat!")
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/8lntiVCa9JwRxnqX6rxvWdEWWmwIiz5xFeTxmdRSydE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1051199485168066610/d40794f36524ec9e9a4e723679d14d6d.png?width=670&height=670")
    view = HelpMenu()
    await interaction.response.send_message(embed=embed,view=view)
#Start the bot!
bot.run(c['token'], log_handler=handler, log_level=logging.ERROR)
