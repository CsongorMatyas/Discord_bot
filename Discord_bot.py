# -*- coding: utf-8 -*-

#556469765842010123
#1074133056
#https://discordapp.com/api/oauth2/authorize?client_id=556469765842010123&permissions=1074133056&scope=bot
#

import discord

client = discord.Client()

helpMessage = ('''
    !help          --> Brings up this message
    !ping          --> To test is bot is online and working, 
                       it will send "<@userID> Pong!" as response
    ?hg            --> Prints High Growth related information
    ?levelup       --> Prints Level-up related information
    ?map           --> Prints map general starting positions
    ?events        --> Prints all events
    ?events 4      --> Prints 4th event
    ?events -10    --> Prints last 10 events
    ?heroes        --> Prints a list of heroes
    ?heroes nature --> Prints a list of nature heroes 
                       similarly (order, chaos, ranged, melee, building,
                       mental, shield, evasion, block, poison, freeze,
                       fly, damage, death, rune, attack, health, heal,
                       pierce, summon, kill, attacked, immune, transform, 
                       silence, common, rare, epic, legendary) 
                       or multiple keywords separated by (" ", ",", ";")
    ?hero death    --> Prints information regarding the hero
    ?pit           --> Prints table of Pit bosses vs league
    ?elixir        --> Elixir usage - How much will give how many
    ?guild doh     --> Information about the guild
    ''')

@client.event
async def on_ready():
    print('Bot is online and connected to Discord as {}!'.format(client.user))

@client.event
async def on_message(message):
    print('{}: {}: {}: {}'.format(message.channel, message.author, message.author.name, message.content))

    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await message.channel.send('<@{}> Pong!'.format(userID))

    if message.content.upper().startswith('!HELP'):
        await message.channel.send('{}'.format(helpMessage))

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
