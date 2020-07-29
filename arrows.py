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

#logic to populate db
c.execute('DROP TABLE IF EXISTS adjective')
c.execute('CREATE TABLE adjective (adjective TEXT)')

c.execute('DROP TABLE IF EXISTS noun')
c.execute('CREATE TABLE noun (noun TEXT)')

with open('word_files/adjectives/4843_common_adjectives.txt', 'r') as f:
    for line in f:
        data = line.split()
        c.execute('INSERT INTO adjective (adjective) VALUES (?)', (data[0],))

with open('word_files/nouns/91K_nouns.txt', 'r') as f:
    for line in f:
        data = line.split()
        c.execute('INSERT INTO noun (noun) VALUES (?)', (data[0],))

conn.commit()


#slow logic but is probably ok for now
c.execute("select * from adjective")
results = c.fetchall()
maxadj = len(results)

c.execute("select * from noun")
results = c.fetchall()
maxnoun = len(results)

for _ in range(50):
    radnum = randint(1, maxadj)
    c.execute("select adjective FROM adjective WHERE rowid = "+str(radnum)+";")
    results = c.fetchone()
    adjective = results[0]

    radnum = randint(1, maxnoun)
    c.execute("select noun FROM noun WHERE rowid = "+str(radnum)+";")
    results = c.fetchone()
    noun = results[0]

    print(adjective +" "+ noun)

conn.close()