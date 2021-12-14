# Network programming lab 11 - Sqlite
# created by Osman Said 08-12-2021

import sqlite3

conn = sqlite3.connect('mydatabase.db')
conn.execute("PRAGMA foreign_keys = 1")
c = conn.cursor()
f = open('score2.txt', 'r')
players = f.readlines()


c.execute("""CREATE TABLE IF NOT EXISTS persons (
             identity INTEGER PRIMARY KEY,
             firstName TEXT,
             lastName TEXT,
             UNIQUE(firstName, lastName)
             )""")

c.execute("""CREATE TABLE IF NOT EXISTS scores (
            task INTEGER,
            points INTEGER,
            idPerson INTEGER,
            FOREIGN KEY (idPerson) REFERENCES persons(identity) ON DELETE CASCADE,
            UNIQUE(idPerson, task)
            )""")

def enter_data(players):
    for player in players:
        lines = player.split()
        person = (lines[2], lines[3])
        taskPoints = (lines[1], lines[4], lines[2], lines[3])
        c.execute("INSERT OR IGNORE INTO persons(firstName, lastName) VALUES(?,?)", person)
        c.execute("INSERT OR IGNORE INTO scores(task, points, idPerson) VALUES(?,?,(SELECT identity FROM persons WHERE firstName=? AND lastName=?))",taskPoints)


enter_data(players)

c.execute("SELECT firstName,lastName, SUM(points) FROM persons JOIN scores ON identity=idPerson GROUP BY firstName,lastName ORDER BY SUM(points) DESC LIMIT 10")
#c.execute("SELECT SUM(points),task FROM scores GROUP BY task ORDER BY SUM(points) ASC LIMIT 10")
print(c.fetchall())
conn.commit()
conn.close()
