import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Discord_Client = discord.Client()
client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
    print('Bot is online and connected to Discord!')


@client.event
async def on_message(message):
    if message.content.upper() == '!COOKIE':
        await client.send_message(message.channel, ':cookie:')

@client.event
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, '<@{}> Pong!'.format(userID))

@client.event
async def on_message(message):
    if message.content.upper().startswith('!SAY'):
        args = message.content.split(' ')
        await client.send_message(message.channel, '{}'.format(' '.join(args[1:])))



client.run('NTU2NDY5NzY1ODQyMDEwMTIz.D26bvg.ts-dQkBS1pHPwGu8jMPYMekGwns')
