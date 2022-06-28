import sqlite3
from user import User


def check_if_user_exists(user):
    conn = sqlite3.connect('sqlite.db')
    cursor = conn.cursor()
    print(f"""SELECT * FROM user WHERE name='{user.name}' AND pass = '{user.hashpass}';""")
    cursor.execute(f"""
    SELECT * FROM user 
    WHERE 
    name = '{user.name}' 
    AND 
    pass = '{user.hashpass}';
    """)

    return len(cursor.fetchall()) != 0
