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
#import Modules
import os
from datetime import datetime
import asyncio
import discord
import pytz
from discord import Message, Guild, TextChannel, Permissions
from discord.ext import commands
import json
#Load Config
with open('./config.json') as f:
  data = json.load(f)
  for c in data['botConfig']:
        print('Prefix: ' + c['prefix'])
#Define Bot
bot = commands.Bot(command_prefix = c['prefix'],intents=discord.Intents.all(),status=discord.Status.dnd,case_insensitive=True)
#Load Server File
if os.path.isfile("servers.json"):
    with open('servers.json', encoding='utf-8') as f:
        servers = json.load(f)
else:
    servers = {"servers": []}
    with open('servers.json', 'w') as f:
        json.dump(servers, f, indent=4)
#Auto Updating Status
async def UpdateMemberCount():
    while True:
        usercount = len(list(filter(lambda m: m.bot == False, bot.users)))
        await bot.change_presence(activity=discord.Game(f'🌎 | {len(bot.guilds)} Servers'))
        await asyncio.sleep(50)
#Event that runs when bot is online
@bot.event
async def on_ready():
    print(f'{bot.user} is Now Online!')
    await bot.loop.create_task(UpdateMemberCount())
#Commands
@bot.command()
async def setGlobal(ctx):
    if ctx.author.guild_permissions.administrator:
        if not guild_exists(ctx.guild.id):
            server = {
                "guildid": ctx.guild.id,
                "channelid": ctx.channel.id,
                "invite": f'{(await ctx.channel.create_invite()).url}'
            }
            servers["servers"].append(server)
            with open('servers.json', 'w') as f:
                json.dump(servers, f, indent=4)
            embed = discord.Embed(title="**Welcome!**",
                                  description="Thank you for using our bot!"
                                              " Messages will now be sent and recieved!"
                                              " Have fun!",
                                  color=0x2ecc71)
            embed.set_footer(text='To reduce the chances of your server being banned, please set a slowmode of atleast 5 seconds!')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description="You have already setup the bot!\r\n"
                                              "To setup the bot again do `g!removeGlobal` then run this command again!",
                                  color=0x2ecc71)
            await ctx.send(embed=embed)
            await ctx.channel.edit(slowmode_delay=5)
@bot.command()
async def removeGlobal(ctx):
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
    if message.author.bot:
        return
    if not message.content.startswith('g!'):
        if get_globalChat(message.guild.id, message.channel.id):
            await sendAll(message)
    await bot.process_commands(message)
async def sendAll(message: Message):
    conent = message.content
    author = message.author
    attachments = message.attachments
    de = pytz.timezone('Europe/London')
    embed = discord.Embed(description=conent, timestamp=datetime.now().astimezone(tz=de), color=author.color)
    icon = message.author.avatar.url
    embed.set_author(name=author.name, icon_url=icon)
    icon_url = "https://images-ext-1.discordapp.net/external/UhuF1jw07zSR1onvtJ3vs1xxctys7s5gsFTjUdPdmcM/%3Fsize%3D1024/https/cdn.discordapp.com/icons/793403717859803156/1f7ed4541dfbafe1f3d4f3a11aa5c454.webp?width=178&height=178"
    embed.set_thumbnail(url=icon_url)
    embed.set_footer(
        text=f'{message.guild.name} | {message.guild.member_count} Members!'
        )
    embed.set_thumbnail(url=message.author.avatar.url)
    embed.add_field(name="** **", value="`📌`[Support](https://discord.gg/3qvpkgWSbF)・`🤖`[Bot-Invite](https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands)", inline=False)
    


    if len(attachments) > 0:
        img = attachments[0]
        embed.set_image(url=img.url)

    for server in servers["servers"]:
        guild: Guild = bot.get_guild(int(server["guildid"]))
        if guild:
            channel: TextChannel = guild.get_channel(int(server["channelid"]))
            if channel:
                perms: Permissions = channel.permissions_for(guild.get_member(bot.user.id))
                if perms.send_messages:
                    if perms.embed_links and perms.attach_files and perms.external_emojis:
                        await channel.send(embed=embed)
                    else:
                        await channel.send('{0}: {1}'.format(author.name, conent))
                        await channel.send('I seem to be missing some permissions Please give me required permissions and run this command again!')
    await message.delete()
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

class NewHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.context
        embed = discord.Embed(
            title="**Silly Chat**",
            description="**Prefix: g!**",
            color=discord.Color.blue()
        )
        embed.add_field(name='g!setGlobal', value='Add global chat to a channel!', inline=False)
        embed.add_field(name='g!removeGlobal', value='Remove global chat from a channel!', inline=False)
        embed.add_field(name='g!invite', value='Invite me to your server!', inline=False)
        embed.add_field(name='g!support', value='Get a link to our support server!', inline=False)
        await destination.send(embed=embed)
bot.help_command = NewHelpCommand()
#Bot join event
@bot.event
async def on_guild_join(guild):
    print(f'I Have Been Added To {guild.name} !')
    channel = bot.get_channel(997744873656549496)
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
    print(f'I Have Been Removed From {guild.name} !')
    channel = bot.get_channel(997744873656549496)
    if channel:
        embed = discord.Embed(
            title='I have left a server!',
            description=
            f'Server Name: {guild.name}\nServer ID: {guild.id}\nMember Count: {guild.member_count}\n\n**New Server Count: {len(bot.guilds)}**'
        )
        await channel.send(embed=embed)
#More Commands
@bot.command()
async def invite(ctx):
    embed=discord.Embed(title="\n<a:discord:942344157618405416>Invite<a:discord:942344157618405416>\n", url="https://discord.com/api/oauth2/authorize?client_id=1051199485168066610&permissions=8&scope=bot%20applications.commands",color=0x662a85)
    await ctx.send(embed=embed)

@bot.command(name='support', aliases=['ss'])
async def support(ctx):
		
		embed = discord.Embed(
				title = f'<a:discord:942344157618405416> Do you need support? Join our support server! <a:discord:942344157618405416>',
				description = '**[Support server](https://discord.gg/3qvpkgWSbF)**',
				color=0x662a85)
		await ctx.send(embed=embed)

#Start the bot!
bot.run(c['token'])
