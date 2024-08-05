import sqlite3

con = sqlite3.connect("library.db")
cur = con.cursor()
username = "admin"

cur.execute("SELECT isadmin FROM userdatabase WHERE name = ?", (username,))

value = cur.fetchall()[0][0]

print(value)
