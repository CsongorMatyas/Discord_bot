#!/usr/bin/python3
# -*- coding: utf-8 -*-

#556469765842010123
#1611005120
#https://discordapp.com/api/oauth2/authorize?client_id=556469765842010123&permissions=1611005120&scope=bot
#MP_Bot#8005

import discord
import sqlite3

def connect_SQL(SQL_file):
    conn = sqlite3.connect(SQL_file)
    c = conn.cursor()
    return(conn, c)

def disconnect_SQL(conn, c):
    c.close()
    conn.close()

def read_SQL(SQL_file, table, COMMANDS):
    conn, c = connect_SQL(SQL_file)
    LIST = []
    for r in c.execute("SELECT * FROM " + table + COMMANDS):
        LIST.append(r)
    conn.commit()
    disconnect_SQL(conn, c)
    return(LIST)

#-----------------------------------------------------------------------------------------------------

client = discord.Client()

future_helpMessage = ('''
    !ping          --> To test if bot is online and working, 
                   it will send "<@userID> Pong!" as response

?help          --> Brings up this message
?hg            --> Prints High Growth related information
?levelup       --> Prints Level-up related information
?map           --> Prints map general starting positions
?events        --> Prints all events
?events 4      --> Prints 4th event
?events -10    --> Prints last 10 events
?heroes        --> Prints a list of heroes
?heroes xy     --> Prints a list of nature heroes 
                   similarly (order, chaos, ranged, melee, building,
                   mental, shield, evasion, block, poison, freeze,
                   fly, damage, death, rune, attack, health, heal,
                   pierce, summon, kill, attacked, immune, transform, 
                   silence, common, rare, epic, legendary) 
                   or multiple keywords separated by (" ", ",", ";")
?hero xy       --> Prints information regarding the hero
?pit           --> Prints table of Pit bosses vs league
?elixir        --> Elixir usage - How much will give how many
?guild xy      --> Information about the guild
''')

helpMessage = ('''
    !ping          --> To test if MP_bot is online and working, 
                   it will send "<@userID> Pong!" as response

?help          --> Brings up this message
?events        --> Prints all events
?event 4       --> Prints 4th event
?event -10     --> Prints last 10 events
''')

@client.event
async def on_ready():
    print('Bot is online and connected to Discord as {}!'.format(client.user))

@client.event
async def on_message(message):
    print('{}: {}: {}: {}'.format(message.channel, message.author, message.author.name, message.content))
    if message.author.name != 'MP_Bot':
        if message.content.upper().startswith('!PING'):
            userID = message.author.id
            await message.channel.send('<@{}> Pong!'.format(userID))

        if message.content.upper().startswith('?HELP'):
            await message.channel.send('{}'.format(helpMessage))

        if message.content.upper().startswith('?EVENT'):
            args = message.content.split(' ')
            if args[0].upper() == '?EVENT':
                if len(args) > 1:
                    is_it_integer = False
                    try:
                        int(args[1])
                        is_it_integer = True
                    except:
                        pass

                    if is_it_integer:
                        if int(args[1]) > 0:
                            event_ID = int(args[1])
                            READ = read_SQL('Mighty_Party_events.sql', 'events', ' WHERE event_id = "{}" '.format(event_ID))
                            for event in READ:
                                TEXT = '{}\t- {}:\t{},\t{},\t{}'.format(event[0], event[1], event[2], event[3], event[4])
                                await message.channel.send('{}'.format(TEXT))
                        elif int(args[1]) < 0:
                            READ = read_SQL('Mighty_Party_events.sql', 'events', '')
                            for event in READ[int(args[1]):]:
                                TEXT = '{}\t- {}:\t{},\t{},\t{}'.format(event[0], event[1], event[2], event[3], event[4])
                                await message.channel.send('{}'.format(TEXT))

            elif args[0].upper() == '?EVENTS':
                READ = read_SQL('Mighty_Party_events.sql', 'events', '')
                for event in READ:
                    TEXT = '{}\t- {}:\t{},\t{},\t{}'.format(event[0], event[1], event[2], event[3], event[4])
                    await message.channel.send('{}'.format(TEXT))
                            
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
