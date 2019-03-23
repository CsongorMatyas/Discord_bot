#!/usr/bin/python3
# -*- coding: utf-8 -*-

#556469765842010123
#1074133056
#https://discordapp.com/api/oauth2/authorize?client_id=556469765842010123&permissions=1074133056&scope=bot
#

import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'Bot is online and connected to Discord as {client.user}!')

@client.event
async def on_message(message):
    print(f'{message.channel}: {message.author}: {message.author.name}: {message.content}')

    if message.content.upper() == 'COOKIE':
        await message.channel.send(':cookie:')

    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await message.channel.send(f'<@{userID}> Pong!')

    if message.content.upper().startswith('!SAY'):
        args = message.content.split(' ')
        await message.channel.send('{}'.format(' '.join(args[1:])))

    if message.content.upper().startswith('?HERO'):
        args = message.content.split(' ')
        if len(args) > 1:
            argsss = False
            for a in args[1:]:
                if a.upper() in ['PANDA', 'KUNG', 'FUCIUS']:
                    argsss = True
            if argsss:
                await message.channel.send('Best one ;)')

client.run('NTU2NDY5NzY1ODQyMDEwMTIz.D26bvg.ts-dQkBS1pHPwGu8jMPYMekGwns')
