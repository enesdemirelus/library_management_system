import tkinter as tk
from tkinter import ttk, END
from ttkbootstrap import Style
import sqlite3
from tkinter.messagebox import showerror, showinfo
from datetime import datetime

class userDashboard(tk.Tk):
    def __init__(self, username):
        super().__init__()

        style = Style(theme='united')
        style.master = self
        style.configure('Medium.TButton', font=('inconsolata', 18))

        today = datetime.now()
        self.formatted_date = today.strftime("%B %-d, %Y.")

        self.username = username

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width = 500
        height = 300
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2 - 200
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.resizable(False, False)
        self.title("User Dashboard")

        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2, 3, 4), weight=1)

        self.creating_widgets()
        self.packing_widgets()

        self.mainloop()

    def creating_widgets(self):
        self.top_label = ttk.Label(self, text=f"Welcome {self.username}!", font="inconsolata 25")
        self.below_label = ttk.Label(self, text=f"It is currently: {self.formatted_date}", font="inconsolata 14")

        self.add_book_button = ttk.Button(self, text="All Books", style="Medium.TButton", command= self.all_books)
        self.request_book_button = ttk.Button(self, text="Request A Book", style="Medium.TButton", command= self.request_book)
        self.all_book_button = ttk.Button(self, text="My Books", style="Medium.TButton", command= self.my_books)

    def packing_widgets(self):
        self.top_label.grid(row=0, column=0)
        self.below_label.grid(row=1, column=0)
        self.add_book_button.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.request_book_button.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)
        self.all_book_button.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)

    def all_books(self):
        print("all books")

    def request_book(self):
        print("request book")

    def my_books(self):
        print("my books")

userDashboard("enesdemirel")