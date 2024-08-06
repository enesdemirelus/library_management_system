import tkinter as tk
from tkinter import ttk, END
import sqlite3
from tkinter.messagebox import showerror, showinfo

class allBooks(tk.Tk):
    def __init__(self):
        super().__init__()

        self.books = []

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width = 1050
        height = 500
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2 - 100
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.title("All Books in the Demirel Library!")
        self.resizable(False, False)

        self.table_frame = ttk.Frame(self)
        self.table_frame.pack(expand=True, fill="both")

        self.getting_books()
        self.creating_table()
        self.packing_table()
        self.mainloop()

    def creating_table(self):
        self.table = ttk.Treeview(
            self.table_frame,
            columns=("Title", "Author", "Genre", "Language", "Page Count", "Is Taken?", "Who Took?", "E-Mail"),
            show="headings"
        )
        self.table.heading("Title", text="Title")
        self.table.heading("Author", text="Author")
        self.table.heading("Genre", text="Genre")
        self.table.heading("Language", text="Language")
        self.table.heading("Page Count", text="Page Count")
        self.table.heading("Is Taken?", text="Is Taken:")
        self.table.heading("Who Took?", text="Who Took:")
        self.table.heading("E-Mail", text= "E-Mail")

        self.table.column("Title", width=250, anchor="center")
        self.table.column("Author", width=120, anchor="center")
        self.table.column("Genre", width=100, anchor="center")
        self.table.column("Language", width=100, anchor="center")
        self.table.column("Page Count", width=80, anchor="center")
        self.table.column("Is Taken?", width=70, anchor="center")
        self.table.column("Who Took?", width=150, anchor="center")
        self.table.column("E-Mail", width=150, anchor="center")

    def packing_table(self):
        self.table.pack(expand=True, fill="both")
        for i in range(0, len(self.books)):
            self.table.insert(parent='', index= i + 1, values=(self.books[i][1], self.books[i][2], self.books[i][3], self.books[i][4], self.books[i][5], self.books[i][6], self.books[i][7], self.books[i][8]))

    def getting_books(self):
        connection = sqlite3.connect("library.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM book_properties")
        rows = cursor.fetchall()
        connection.close()

        for book in rows:
            self.books.append(book)



allBooks()