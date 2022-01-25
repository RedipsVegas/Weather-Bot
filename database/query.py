import sqlite3


conn = sqlite3.connect('bot_db')
cur = conn.cursor()

conn.execute("""CREATE TABLE IF NOT EXISTS user(
    id BIGINT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    user_name VARCHAR(255),
    city VARCHAR(255)
)""")


def insert_user(first_name, last_name, user_name, city):
    cur.execute('INSERT INTO students (first_name, last_name, user_name, city')





