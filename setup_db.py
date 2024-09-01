import sqlite3

def add_rating_column():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    cursor.execute('ALTER TABLE movies ADD COLUMN rating REAL')

    conn.commit()
    conn.close()

add_rating_column()
