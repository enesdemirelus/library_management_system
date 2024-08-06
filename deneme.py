import sqlite3

connection = sqlite3.connect("library.db")
cursor = connection.cursor()
cursor.execute(f"SELECT * FROM book_properties")
rows = cursor.fetchall()
connection.close()

books = []
for book in rows:
    books.append(book)

print(books[0][3])