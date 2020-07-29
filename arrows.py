#!/usr/bin/env python3
import json
import sqlite3
from random import randint

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)

database = 'words.db'
conn = create_connection(database)
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS words')
c.execute('CREATE TABLE words (adjective TEXT, noun TEXT)')

with open('word_files/adjectives/28K_adjectives.txt', 'r') as f:
    for line in f:
        data = line.split()
        c.execute('INSERT INTO words (adjective) VALUES (?)', (data[0],))
        if 'str' in line:
            break

with open('word_files/adjectives/28K_adjectives.txt', 'r') as f:
    for line in f:
        data = line.split()
        c.execute('INSERT INTO words (adjective) VALUES (?)', (data[0],))
        if 'str' in line:
            break


conn.commit()
conn.close()