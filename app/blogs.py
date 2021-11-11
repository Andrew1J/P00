# Kazimierz Major -- Andrew Juang, Noakai Aronesty, Eric Guo, Qina Liu
# SoftDev
# P00 -- Web Log Hosting Site

""" Blogs Database """

import sqlite3
import random

DB_FILE = "discobandit.db"

def create_db():
    ''' Creates / Connects to DB File '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS blogs (usernames TEXT, blognames TEXT, id INTEGER, entryname TEXT, content TEXT);")
    # c.execute("CREATE TABLE IF NOT EXISTS blogs (usernames TEXT, blognames TEXT, id INTEGER, content TEXT);")
    db.close()


def create_blog(title,text,username, entryname):
    ''' Publishes a blog '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    id = generate_id()
    #id = generate_id(title, username)
    c.execute("INSERT INTO blogs VALUES (?, ?, ?, ?, ?);", (username, title, id, entryname, text))

    db.commit()

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    db.commit()
    c.execute("SELECT * FROM blogs")
    print(c.fetchall())


def generate_id():
    ''' Generate random ID for user '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    id = 0
    c.execute("SELECT id FROM blogs")
    blogids = []
    for a_tuple in c.fetchall():
        blogids.append(a_tuple[0])

    '''
    id = blog_exists(title,username)
    if id:
        return id;
    else:
        while id in blogids:
            id++
        return id
    '''
    while id in blogids:
        id += 1
    return id


def blog_exist(title, username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    database = []
    c.execute("SELECT id FROM blogs WHERE usernames = username AND blognames = title")
    return id


def update_blog(username,id,entryname,text):
    ''' Updates blog '''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO blogs VALUES (?, ?, ?, ?, ?);", (username, title, id, entryname, text))
    db.commit()

    return True


def delete_blog():
    ''' Delete blog '''

    return True


def fetch_blogs():
    ''' Fetch list of blog names '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM blogs")
    blogs = []
    users = []
    for a_tuple in c.fetchall():
        if a_tuple[1] not in blogs:
            blogs.append(a_tuple[1])
            users.append(a_tuple[0])

    return zip(blogs,users)


def fetch_user_blogs(username):
    ''' Fetch list of a USER's blog names '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM blogs")
    blogs = []
    for a_tuple in c.fetchall():
        if a_tuple[0] == username and a_tuple[1] not in blogs:
            blogs.append(a_tuple[1])

    return blogs


def get_ids(username):
    ''' Returns the blog ids of the user '''

    ids = []
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM blogs")
    for a_tuple in c.fetchall():
        if(a_tuple[0] == username):
            ids.append(a_tuple[2])
    return ids

def get_title_from_id(blogID):
    ''' returns the title of corrresponding blog using the blog id '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT blognames FROM blogs WHERE id = "+ str(blogID))
    for content in c.fetchall():
        return content[0]


def get_content_from_id(blogID):
    ''' returns the content of corrresponding blog using the blog id '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT content FROM blogs WHERE id = "+ str(blogID))
    for content in c.fetchall():
        return content[0]

def fetch_entry_names(blogtitle):
    ''' retrieves all entries names in database that belongs to the specified
        blog (has the specified blog title) '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT entryname FROM blogs WHERE blognames = '" + blogtitle + "'")
    names = []
    for a_tuple in c.fetchall():
        names.append(a_tuple[0])
    return names

def fetch_entry_contents(blogtitle):
    ''' retrieves all entries names in database that belongs to the specified
        blog (has the specified blog title) '''

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT content FROM blogs WHERE blognames = '" + blogtitle + "'")
    contents = []
    for a_tuple in c.fetchall():
        contents.append(a_tuple[0])
    return contents


# TESTS
create_db()
