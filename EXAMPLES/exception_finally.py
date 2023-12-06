import sqlite3

conn = None

try:
    conn = sqlite3.connect('spam.db')
    cursor = conn.cursor()
except sqlite3.DatabaseError as err:
    print(err)
    print("Quitting program")
    exit()
else:
    # do query()
    pass
finally:
    # clear resourses
    if conn:
        conn.close()
