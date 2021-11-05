# Kazimierz Major -- Andrew Juang, Noakai Aronesty, Eric Guo, Qina Liu
# SoftDev
# P00 -- Web Log Hosting Site

""" Article Database """

import sqlite3
import random

DB_FILE = "discobandit.db"

def create_db():
    ''' Creates / Connects to DB File '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS blogs (usernames TEXT, blognames TEXT, id INTEGER, content TEXT);")
    db.close()


# def create_blog(title,text):
#     ''' Publishes a blog '''

#     db = sqlite3.connect(DB_FILE)
#     c = db.cursor()
#     id = generate_id()
#     '''Work on tomorrow, somehow get the username'''
#     username = "bob"
#     c.execute("INSERT INTO blogs VALUES (?, ?, ?, ?);", (username, title, id, text))


# '''need a better way to generate id later probably'''
# def generate_id():
#     id = random.randint(0,999999)
#     c.execute("SELECT id FROM blogs")
#     blogids = []
#     for a_tuple in c.fetchall():
#         blogids.append(a_tuple[0])
#     while id in blogids:
#         id = random.randint(0,999999)
#     return id


def update_blog():
    ''' Updates blog '''

    return True


def delete_blog():
    ''' Delete blog '''

    return True

db = sqlite3.connect(DB_FILE)
c = db.cursor()
db.commit()
c.execute("SELECT usernames FROM blogs")
blogs = []
for a_tuple in c.fetchall():
    blogs.append(a_tuple[0])
print(blogs)