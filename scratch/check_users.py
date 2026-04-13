import sqlite3
try:
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM auth_user")
    users = cursor.fetchall()
    print("Users found:", users)
    conn.close()
except Exception as e:
    print("Error:", e)
