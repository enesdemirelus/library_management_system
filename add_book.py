import tkinter as tk
from tkinter import ttk, END
from ttkbootstrap import Style
from PIL import Image, ImageTk
import sqlite3
from tkinter import filedialog
from tkinter.messagebox import showerror, showinfo

class addBook(tk.Tk):
    def __init__(self):
        super().__init__()

        self.file_path = ""
        style = Style(theme='united')
        style.master = self

        self.book_name_str = tk.StringVar()
        self.book_author_str = tk.StringVar()
        self.book_genre_str = tk.StringVar()
        self.book_language_str = tk.StringVar()
        self.page_count_str = tk.StringVar()


        self.image = self.load_and_resize_image("default_image.png", (250, 375))

        self.geometry("700x400")
        self.title("Add Book")
        self.resizable(False, False)

        self.columnconfigure((0,1), weight= 1)
        self.rowconfigure(0, weight= 1)

        self.creating_widgets()
        self.packing_widgets()
        self.image_widgets()


        self.mainloop()

    def load_and_resize_image(self, filepath, size):
        """Load and resize an image using Pillow."""
        pil_image = Image.open(filepath)
        pil_image = pil_image.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(pil_image)
    
    def select_file(self, event):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png")])
        if self.file_path:
            self.image = self.load_and_resize_image(f"{self.file_path}", (250, 375))
            self.image_widgets()

    def image_widgets(self):
        self.book_cover = ttk.Label(self, image= self.image)
        self.book_cover.bind("<Button-1>", self.select_file)
        self.book_cover.grid(row = 0, column= 0, padx= 10, pady= 10)


    def creating_widgets(self):
        self.right_frame = ttk.Frame(master = self)
        self.right_frame.rowconfigure((0,1,2,3,4,5,6), weight= 1)
        self.right_frame.columnconfigure((0,1), weight= 1)

        self.biglabel = ttk.Label(self.right_frame, text= "Please enter book details below!", font= "inconsolata 20")

        self.book_name = ttk.Label(self.right_frame, text= "Enter the book title: ", font= "inconsolata 15")
        self.book_name_entry = ttk.Entry(self.right_frame, textvariable= self.book_name_str)

        self.book_author = ttk.Label(self.right_frame, text= "Enter the book author: ", font= "inconsolata 15")
        self.book_author_entry = ttk.Entry(self.right_frame, textvariable= self.book_author_str)

        self.book_genre = ttk.Label(self.right_frame, text= "Enter the book genre: ", font= "inconsolata 15")
        self.book_genre_entry = ttk.Entry(self.right_frame, textvariable= self.book_genre_str)

        self.book_language = ttk.Label(self.right_frame, text= "Enter the book language: ", font= "inconsolata 15")
        self.book_language_entry = ttk.Entry(self.right_frame, textvariable= self.book_language_str)

        self.book_page_count = ttk.Label(self.right_frame, text= "Enter the book page count: ", font= "inconsolata 15")
        self.book_page_count_entry = ttk.Entry(self.right_frame, textvariable= self.page_count_str)

        self.add_button = ttk.Button(self.right_frame, text= "Click to add!", command= self.addbook_clicked)

    def packing_widgets(self):
        self.right_frame.grid(row = 0, column= 1)
        self.biglabel.grid(row = 0, column= 0, columnspan= 2, pady= 20)
        self.book_name.grid(row = 1, column= 0, pady= 10)
        self.book_name_entry.grid(row = 1, column= 1, padx = (0,10))
        self.book_author.grid(row = 2, column= 0, pady= 10)
        self.book_author_entry.grid(row = 2, column= 1, padx = (0,10))
        self.book_genre.grid(row = 3, column= 0, pady= 10)
        self.book_genre_entry.grid(row = 3, column= 1, padx = (0,10))
        self.book_language.grid(row = 4, column= 0, pady= 10)
        self.book_language_entry.grid(row = 4, column= 1, padx = (0,10))
        self.book_page_count.grid(row = 5, column= 0, pady= 10)
        self.book_page_count_entry.grid(row = 5, column=1, padx = (0,10))
        self.add_button.grid(row = 6, column= 0, columnspan=2, pady= 10)

    def addbook_clicked(self):
        book_title = self.book_name_str.get()
        book_author = self.book_author_str.get()
        book_genre = self.book_genre_str.get()
        book_language = self.book_language_str.get()
        book_page_count = self.page_count_str.get()
        if book_title and book_author and book_genre and book_language and book_page_count and self.file_path != "":
            print("success")
        else:
            showerror(message= "Please enter all the field and put an image!")


if __name__ == "__main__":
    addBook()