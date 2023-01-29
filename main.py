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
from discord import Message, Guild, TextChannel, Permissions
from discord.ext import commands
import json
import requests
import random
#Logging
import logging
handler = logging.FileHandler(filename='errors.log', encoding='utf-8', mode='w')
#Load Config
with open('./config.json') as f:
  data = json.load(f)
  for c in data['botConfig']:
        print('Prefix: ' + c['prefix'])
        print('Log Channel: ' + c['logid'])
#No token found
if c['token'] == "token here" or c['token'] == "" or c['token'] == " ":
    print("It would appear you have not set the bot token in config.json! This is required to make the bot run!")
#Define Bot
bot = commands.Bot(command_prefix = c['prefix'],intents=discord.Intents.all(),status=discord.Status.idle,case_insensitive=True)
#Load Server File
if os.path.isfile("servers.json"):
    with open('servers.json', encoding='utf-8') as f:
        servers = json.load(f)
else:
    servers = {"servers": []}
    with open('servers.json', 'w') as f:
        json.dump(servers, f, indent=4)
#Load Banned Users
if os.path.isfile("banned.json"):
    with open('banned.json', encoding='utf-8') as f:
        banned = json.load(f)
else:
    banned = {"banned": []}
    with open('banned.json', 'w') as f:
        json.dump(banned, f, indent=4)
#Load Admin Users
if os.path.isfile("admins.json"):
    with open('admins.json', encoding='utf-8') as f:
        adminusers = json.load(f)
else:
    adminusers = {"admins": []}
    with open('admins.json', 'w') as f:
        json.dump(adminusers, f, indent=4)
#Auto Updating Status
async def StatusChange():
    while True:
        usercount = len(list(filter(lambda m: m.bot == False, bot.users)))
        await bot.change_presence(activity=discord.Game(f'g!help | {len(bot.guilds)} Servers'))
        await asyncio.sleep(35)
        await bot.change_presence(activity=discord.Game(f'g!help | {usercount} Users'))
        await asyncio.sleep(35)
        await bot.change_presence(activity=discord.Game(f'g!help | discord.gg/3qvpkgWSbF'))
        await asyncio.sleep(35)
        await bot.change_presence(activity=discord.Game(f'g!help | Invite Me Today!'))
        await asyncio.sleep(35)
        await bot.change_presence(activity=discord.Game(f'g!help | Silly Chat'))
        await asyncio.sleep(35)
        await bot.change_presence(activity=discord.Game(f'g!help | Downloading 2024'))
        await asyncio.sleep(35)
#Remove Temp Files Every Hour
async def ClearTemp():
    while True:
        shutil.rmtree('temp')
        os.mkdir('temp')
        await asyncio.sleep(3600)
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
    await bot.loop.create_task(ClearTemp())
#Commands
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
        else:
            embed = discord.Embed(description="You have already setup the bot!\r\n"
                                              "To setup the bot again do `g!removeGlobal` then run this command again!",
                                  color=0x2ecc71)
            await ctx.send(embed=embed)
            await ctx.channel.edit(slowmode_delay=5)
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
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description="No Global Channel Set.\r\n"
                                              "Use `g!setGlobal` to set one!\nBelieve this is a mistake? Join our support server!",
                                  color=0x2ecc71)
            await ctx.send(embed=embed)
#Event for when a message is sent
@bot.event
async def on_message(message):
    bannedusers = []
    possiblechannels = []
    adminz = []
    staffonly = False
    for admin in adminusers["admins"]:
        adminz.append(int(admin["userid"]))
    for buser in banned["banned"]:
        bannedusers.append(int(buser["userid"]))
    for channel in servers["servers"]:
        possiblechannels.append(int(channel["channelid"]))
    if message.author.bot:
        return
    if staffonly == True and message.author.id in adminz:
        print("User = Staff, Sending!")
        if get_globalChat(message.guild.id, message.channel.id):
            await sendAll(message)
    elif staffonly == False:
        if message.author.id in bannedusers and message.channel.id in possiblechannels:
            user = message.author
            embed = discord.Embed(description="**You Are Bannned!**\r\n"
            "It seems you have been banned from using this feature!\nBelieve this is a mistake? Please join our support server!",
            color=0x2ecc71)
            await user.send(embed=embed)
            await message.delete()
        else:
            if get_globalChat(message.guild.id, message.channel.id):
                if not message.content.startswith('g!'):
                    await sendAll(message)
                else:
                    await message.delete()
    else:
        user = message.author
        embed = discord.Embed(description="**Silly Chat Is Locked!**\r\n"
        "It seems that a bot mod has disabled Silly Chat! Please try send your message later!\nBelieve this is a mistake? Please join our support server!",
        color=0x2ecc71)
        await user.send(embed=embed)
        await message.delete()
    await bot.process_commands(message)
#Message
async def sendAll(message: Message):
    await Webhooklogging(c['webhook'],f'Message "{message.content}" was sent by "{message.author.id}" in guild {message.guild.id}!')
    adminz = []
    for admin in adminusers["admins"]:
        adminz.append(int(admin["userid"]))
    if message.author.id in adminz:
        role = "Bot Moderator"
    else:
        role = "Member"
    conent = message.content
    author = message.author
    attachments = message.attachments
    de = pytz.timezone('Europe/London')
    embed = discord.Embed(description=conent, timestamp=datetime.now().astimezone(tz=de), color=author.color)
    icon = message.author.avatar.url
    username = author.name + "#" + author.discriminator + " - " + role
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
        guild: Guild = bot.get_guild(int(server["guildid"]))
        if guild:
            channel: TextChannel = guild.get_channel(int(server["channelid"]))
            if channel:
                perms: Permissions = channel.permissions_for(guild.get_member(bot.user.id))
                if perms.send_messages:
                    if perms.embed_links and perms.attach_files and perms.external_emojis:
                        try:
                            if score2 == 3 or score2 == 4 or score2 == 5:
                                await message.delete()
                                user = message.author
                                embed = discord.Embed(
                                    title=f"NSFW Detected!",
                                    description=f"Our Systems Have Detected NSFW In Your Image!\nIf you believe this is a mistake please contact our support.",
                                    color=0x662a85)
                                await user.send(embed=embed)
                            else:
                                file = discord.File(f"temp/{randomname}.png", filename=f"{randomname}.png")
                                embed.set_image(url=f"attachment://{randomname}.png")
                                await channel.send(file=file, embed=embed)
                        except UnboundLocalError:
                            await channel.send(embed=embed)
                    else:
                        await channel.send('{0}: {1}'.format(author.name, conent))
                        await channel.send('I seem to be missing required permissions! I require ``Embed Links``, ``Attach Files`` and ``Eternal Emojis``')
    await message.delete()

#Gen Random String
async def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

#Event for when someone sets up the bot
async def sendAllWelcome(ctx):
    embed = discord.Embed(
        title=f"Welcome!",
        description=f'Thank you {ctx.guild.name} for adding the bot!',
        color=0x662a85,
        timestamp=datetime.datetime.utcnow())
    embed.set_footer(text=f'{ctx.guild.name} | {ctx.guild.member_count} User',
                     icon_url=f'{ctx.guild.icon_url}')
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name=f'⠀', value='⠀', inline=False)
    embed.add_field(
        name=f'Support & Bot Invite',
        value=
        f'[Support](https://discord.gg/3qvpkgWSbF)・[Bot invite](https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands)',
        inline=False)

    for server in servers["servers"]:
        guild: Guild = bot.get_guild(int(server["guildid"]))
        if guild:
            channel: TextChannel = guild.get_channel(int(server["channelid"]))
            if channel:
                await channel.send(embed=embed)
    await ctx.message.delete()


def guild_exists(guildid):
    for server in servers['servers']:
        if int(server['guildid'] == int(guildid)):
            return True
    return False


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
    i = 0
    for server in servers["servers"]:
        if int(server["guildid"]) == int(guild_id):
            globalChat = i
        i += 1
    return globalChat
def get_banned_id(user_id):
    globalChat = -1
    i = 0
    for bannedusr in banned["banned"]:
        if int(bannedusr["userid"]) == int(user_id):
            globalChat = i
        i += 1
    return globalChat

class NewHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.context
        embed = discord.Embed(
            title="**Silly Chat**",
            description="**Prefix: g!**",
            color=discord.Color.blue()
        )
        embed.add_field(name="g!setGlobal", value="Add global chat to a channel!", inline=False)
        embed.add_field(name="g!removeGlobal", value="Remove global chat from a channel!", inline=False)
        embed.add_field(name="g!ping", value="Check the bot's ping", inline=False)
        embed.add_field(name="g!stats", value="Check the bot's stats!", inline=False)
        embed.add_field(name="g!invite", value="Invite me to your server!", inline=False)
        embed.add_field(name="g!support", value="Get a link to our support server!", inline=False)
        embed.add_field(name="g!github", value="Get a link to the bot's github!", inline=False)
        embed.add_field(name="g!credits", value="View the creators of the bot!", inline=False)
        embed.add_field(name="g!vote", value="Vote for the bot!", inline=False)
        embed.add_field(name ="", value="**Bot Moderator Commands:**", inline=False)
        embed.add_field(name="g!ban", value="Ban a user from using the bot!", inline=False)
        embed.add_field(name="g!unban", value="Remove a user from the banned list!", inline=False)
        embed.add_field(name="g!dm", value="Dm a specified user!", inline=False)
        embed.add_field(name="g!guildinfo", value="Command coming soon!", inline=False)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/8lntiVCa9JwRxnqX6rxvWdEWWmwIiz5xFeTxmdRSydE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1051199485168066610/d40794f36524ec9e9a4e723679d14d6d.png?width=670&height=670")
        embed.set_footer(text="Thank You For Using Silly Chat!")
        await destination.send(embed=embed)
bot.help_command = NewHelpCommand()
#Bot join event
@bot.event
async def on_guild_join(guild):
    await Webhooklogging(c['webhook'],f'I Have Been Added To {guild.name} !')
    channel = bot.get_channel(c['logid'])
    if channel:
        embed = discord.Embed(
            title='I have joined a new server!',
            description=
            f'Server Name: {guild.name}\nServer ID: {guild.id}\nMember Count: {guild.member_count}\n\n**New Server Count: {len(bot.guilds)}**'
        )
        await channel.send(embed=embed)
#Bot leave event
@bot.event
async def on_guild_remove(guild):
    await Webhooklogging(c['webhook'],f'I Have Been Removed From {guild.name} !')
    channel = bot.get_channel(c['logid'])
    if channel:
        embed = discord.Embed(
            title='I have left a server!',
            description=
            f'Server Name: {guild.name}\nServer ID: {guild.id}\nMember Count: {guild.member_count}\n\n**New Server Count: {len(bot.guilds)}**'
        )
        await channel.send(embed=embed)

#Admin Commands
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










@bot.command()
async def ban(ctx, user: discord.User = None):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!ban {user}')
    adminz = []
    currentbanned = []
    for buser in banned["banned"]:
        currentbanned.append(buser["userid"])
    for admin in adminusers["admins"]:
        adminz.append(int(admin["userid"]))
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
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="User Is Already Banned!",color=0x662a85)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        await ctx.send(embed=embed)
@bot.command()
async def unban(ctx, user: discord.User = None):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!unban {user}')
    adminz = []
    currentbanned = []
    for buser in banned["banned"]:
        currentbanned.append(buser["userid"])
    for admin in adminusers["admins"]:
        adminz.append(int(admin["userid"]))
    if ctx.message.author.id in adminz and ctx.message.author.id not in currentbanned:
        if user.id in currentbanned:
            userid = get_banned_id(user.id)
            banned["banned"].pop(userid)
            with open('banned.json', 'w') as f:
                json.dump(banned, f, indent=4)
            embed=discord.Embed(title="Unbanned!",color=0x662a85)
            dmembed = discord.Embed(title="You Have Been Unbanned From Silly Chat!",color=0x662a85)
            await user.send(embed=dmembed)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="User Is Not Banned!",color=0x662a85)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        await ctx.send(embed=embed)
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
            embed=discord.Embed(title="Removing Admins Comin Soon",color=0x662a85)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        await ctx.send(embed=embed)
@bot.command(name='guildinfo', aliases=['serverinfo'])
async def guildinfo(ctx, value=None):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!guildinfo')
    adminz = []
    for admin in adminusers["admins"]:
        adminz.append(int(admin["userid"]))
    if ctx.message.author.id in adminz:
        servinfo = []
        for server in servers["servers"]:
            servinfo.append(server["guildid"])
            print(servinfo)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        await ctx.send(embed=embed)
@bot.command(name='dm', aliases=['dmuser'])
async def dm(ctx, user: discord.User = None, *, value=None):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!dm {user} {value}')
    adminz = []
    for admin in adminusers["admins"]:
        adminz.append(int(admin["userid"]))
    if ctx.message.author.id in adminz:
        if user == ctx.message.author:
            await user.send("**You can't DM yourself, or maybe you can?**")
            await ctx.message.delete()
        else:
            await ctx.message.delete()
        if user == None:
            await ctx.send(f'**{ctx.message.author},** Please mention somebody to DM.')
        else:
            if value == None:
                    await ctx.send(f'**{ctx.message.author},** Please send a message to DM.')
            else:
                await user.send(value)
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        await ctx.send(embed=embed)
#More Commands
@bot.command()
async def invite(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!invite')
    embed=discord.Embed(title="\n<a:discord:942344157618405416>Invite<a:discord:942344157618405416>\n", url="https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands",color=0x662a85)
    await ctx.send(embed=embed)
@bot.command(name='database', aliases=['viewdatabase'])
async def database(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!database')
    owner = await bot.fetch_user("763471049894527006")
    if owner == ctx.message.author:
        print("Database Export:")
        f = open('servers.json')
        data = json.load(f)
        for i in data['servers']:
            print(i)
            embed = discord.Embed(
                title = f'DataBase Export! (Servers)',
                description = i,
                color=0x662a85)
            user = await bot.fetch_user("763471049894527006")
            await user.send(embed=embed)
            f.close()
        bannedE = open('banned.json')
        data = json.load(bannedE)
        for i in data['banned']:
            print(i)
            embed = discord.Embed(
                title = f'DataBase Export! (Banned Users)',
                description = i,
                color=0x662a85)
            user = await bot.fetch_user("763471049894527006")
            await user.send(embed=embed)
            bannedE.close()
        adminz = open('admins.json')
        data = json.load(adminz)
        for i in data['admins']:
            print(i)
            embed = discord.Embed(
                title = f'DataBase Export! (Admin Users)',
                description = i,
                color=0x662a85)
            user = await bot.fetch_user("763471049894527006")
            await user.send(embed=embed)
            adminz.close()
    else:
        embed = discord.Embed(
            title = f'Error!',
            description = "You are not permitted to use this command!",
            color=0x662a85)
        await ctx.send(embed=embed)
@bot.command(name='ping', aliases=['botping'])
async def ping(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!ping')
    embed = discord.Embed(
        title = f'Pong!',
        description = f'**{round(bot.latency * 1000)}ms**',
        color=0x662a85)
    await ctx.send(embed=embed)
@bot.command(name='gamer', aliases=['gamer3514'])
async def gamer(ctx):
		await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!gamer')
		embed = discord.Embed(
				title = f'Gamer Is Cool!',
				description = f'<@763471049894527006> is a super cool human! He is cracked at fortnite and he made this bot!',
				color=0x662a85)
		await ctx.send(embed=embed)
@bot.command(name='youtube', aliases=['yt'])
async def youtube(ctx):
		await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!youtube')
		embed = discord.Embed(
				title = f'Subscribe On Youtube!',
				description = f'[Here!](https://youtube.com/c/thegamer3514)',
				color=0x662a85)
		await ctx.send(embed=embed)
@bot.command(name='tiktok', aliases=['tk'])
async def tiktok(ctx):
		await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!tiktok')
		embed = discord.Embed(
				title = f'Follow On Tiktok!',
				description = f'@elon_fan.1',
				color=0x662a85)
		await ctx.send(embed=embed)
@bot.command(name='cai', aliases=['ukcai'])
async def cai(ctx):
		await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!cai')
		embed = discord.Embed(
				title = f'Ukcai',
				description = f'<@967904098047381587> assisted in development of silly chat in multiple ways! He helped by suggesting loads of new features and helped with commands such as g!stats command. You can find his website [here!](https://ukcai.me) Very cool!',
				color=0x662a85)
		await ctx.send(embed=embed)
@bot.command(name='stats', aliases=['botstats'])
async def stats(ctx):	
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!stats')
    embed = discord.Embed(
        title = f'My Stats:',
        color=0x662a85)
    embed.add_field(name="Bot Owner", value="<@763471049894527006> (763471049894527006) Gamer3514#7679", inline=False)
    embed.add_field(name="Cpu Cores", value=multiprocessing.cpu_count(), inline=False)
    embed.add_field(name="Server Count", value=f"{len(bot.guilds)}", inline=False)
    embed.add_field(name="Bot Latency", value=f"{round(bot.latency * 1000)}ms", inline=False)
    embed.add_field(name="Cpu Usage", value=f"{psutil.cpu_percent()}%", inline=False)
    embed.add_field(name="Memory Usage", value=f"{psutil.virtual_memory().percent}%", inline=False)
    embed.add_field(name="Total Memory", value=f"{round(psutil.virtual_memory().total / (1024.0 **3))} GB", inline=False)
    await ctx.send(embed=embed)
@bot.command(name='botlists', aliases=['vote'])
async def botlists(ctx):	
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!botlists')
    embed = discord.Embed(
        title = f'My Stats:',
        color=0x662a85)
    embed.add_field(name="Top.gg", value="[Vote Here!](https://top.gg/bot/1051199485168066610)", inline=True)
    embed.add_field(name="Spectrum Lists", value="[Vote Here!](https://spectrumlists.xyz/bot/1051199485168066610)", inline=True)
    embed.add_field(name="Discord Bot List", value="[Vote Here!](https://discordbotlist.com/bots/silly-chat)", inline=True)
    await ctx.send(embed=embed)

@bot.command(name='github', aliases=['source'])
async def github(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!github')
    embed = discord.Embed(
        title = "Github",
        color=0x662a85)
    embed.add_field(name="", value="This Bot's Github Can Be Found [Here](https://github.com/TheGamer3514/silly-chat)")  
    await ctx.send(embed=embed)
    
@bot.command(name='credits', aliases=['botcredits'])
async def credits(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!credits')
    embed = discord.Embed(
        title = "Credits",
        color=0x662a85)
    embed.add_field(name="Gamer3514#7679", value="Bot Owner! Maintains the bot, made most systems!")  
    embed.add_field(name="ukcai#7121", value="Bot Developer & Moderator! Helped improve systems and made comamnds such as g!stats")  
    embed.add_field(name="Luke The Nyan Gamer#9910", value="Bot Moderator! Helps keep the chat SFW.")
    await ctx.send(embed=embed)
@bot.command(name='support', aliases=['ss'])
async def support(ctx):
    await Webhooklogging(c['webhook'],f'{ctx.author} | {ctx.guild.id} -> g!support')
    embed = discord.Embed(
        title = f'<a:discord:942344157618405416> Do you need support? Join our support server! <a:discord:942344157618405416>',
        description = '**[Support server](https://discord.gg/3qvpkgWSbF)**',
        color=0x662a85)
    await ctx.send(embed=embed)
#Start the bot!
bot.run(c['token'], log_handler=handler, log_level=logging.ERROR)
