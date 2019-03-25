#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3

def connect(SQL_file):
    conn = sqlite3.connect(SQL_file)
    c = conn.cursor()
    return(conn, c)

def disconnect(conn, c):
    c.close()
    conn.close()

def create_table(SQL_file, COMMANDS):
    conn, c = connect(SQL_file) 
    c.execute('CREATE TABLE IF NOT EXISTS ' + COMMANDS)
    disconnect(conn, c)

def enter_data(SQL_file, table, values):
    conn, c = connect(SQL_file)
    c.execute('INSERT INTO ' + table + ' VALUES' + values)
    conn.commit()
    disconnect(conn, c)

#Creating events table
#create_table('Mighty_Party_events.sql',
#             'events(event_id INT, event_name TEXT, hero_1 TEXT, hero_2 TEXT, hero_3 TEXT)')

#Data for Events table
events_table = ('''(1, "Pumpkin Party", "Leader Nilen", "Koschei the Immortal", "Chernomor")''',
                '''(2, "Learn to Fly", "Enlil Wind of Change", "Matriarch Eona", "Anak Princess Dragon")''',
                '''(3, "XMAS", "Iceberg", 'Evil "Santa"', "Ghosta")''',
                '''(4, "Guardians of Forest", "Loath Spore Loser", "Groot Silent Guardian", "Tengu Ravencrest")''',
                '''(5, "Love is in the Air", "Mi Ten-Tailed Fox", "Grand Ma Reaper", "Super Mary")''',
                '''(6, "Coven of Reborn", "Red Woman", "Draggara", "Blair")''',
                '''(7, "The Rescue Mission", "Strik the Fiery Heart", "Fury the Great Warrior", "High Tinker Gear")''',
                '''(8, "The Maw of Madness", "TNT Crazy Demolitionist", "General Zor'Ma", "Ysh'Tmala The Old God")''',
                '''(9, "Guilds Betrayers", "Aphrodite", "Hanzo Sama", "Titania")''',
                '''(10, "The Lost Temple", "Hoodoo", "Coba Temple Keeper", "Tani Windrunner")''',
                '''(11, "Monster Hunt", "Axe", "Koschei the Immortal", "Goliath")''',
                '''(12, "The Lost Heart", "El Mariachi", "Marquis de Sat", "Erik the Grey")''',
                '''(13, "Cataclysm", "Bravi Deadly Blade", "Diana Amazonian Queen", "Mjolnir Lightning God")''',
                '''(14, "Intrigues of the Dead", "Hanako Lady Banshee", "Yorik the Risen One", "Apep Aspect of Chaos")''',
                '''(15, "Cross It Off", "D'Arc Iron Maiden", "Athena", "Alexandria")''',
                '''(16, "Water World", "Mizu the Sea Foam", "Triton the Bottom Herald", "Morgan the Sea Tusk")''',
                '''(17, "The Dark Knight Returns", "Discordia", "Chernomor", "Stormrage")''',
                '''(18, "For the Love of Art", "Apollo", "Angelia the Lightbringer", "Prince")''',
                '''(19, "Into the Labyrinth", "Cernun Archdruid", "Melia Forest’s Daughter", "King Taurus")''',
                '''(20, "The Eye of Chaos", "Regardus Diplius", "Lady Medusa", "Dead Lord")''',
                '''(21, "A Knight's Tale", "Sir Lancelot", "Blair", "Shao Lin")''',
                '''(22, "Plants & Roses", "Maeve", "Bastet", "Poison Flos")''',
                '''(23, "The Demon’s Quest", "Leader Nilen", "Grand Ma Reaper", "Necro Master Lich")''',
                '''(24, "Metal Fist of Fury", "Miss Lapin", "Super Mary", "Jaxy Thunderfist")''',
                '''(25, "Night of the Lizards", "Matriarch Eona", "Anak Princess Dragon", "Snake Lizard Prince")''',
                '''(26, "Island of The Dead", "Death", "Count Vlad", "Mr. Flap")''',
                '''(27, "Xmas in Dungeon", 'Evil "Santa"', "Iceberg", "Frost the Snow Queen")''',
                '''(28, "Great Pangean Fire", "Tani Windrunner", "Hanzo Sama", "Madam Agony")''',
                '''(29, "In the Year of the Pig", "TNT Crazy Demolitionist", "Shao Lin", "Kung Fucius")''',
                '''(30, "Love Hurts", "Ghosta", "Fury the Great Warrior", "Griffius the Celestial")''',
                '''(31, "Cycle of Life", "General Zor'Ma", "Discordia", "Ogrok the Leader")''',
                '''(32, "Wizard Patrick", "Mi Ten-Tailed Fox", "Marquis de Sat", "Tsukumogami")''')

'''
#Entering data in events table
for event in events_table[-1:]:
    enter_data('Mighty_Party_events.sql', 'events', event)
#'''

