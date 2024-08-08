# library_management_system

This project is a personal project I worked in my free time as to practise Tkinter, Python and SQLite3. I aimed to create a fully functional Library Management Software for both library employees and regular users.

The software has these features for admins:

- Adding new books to database with these parameters = Image, Title, Author, Genre, Language, Page Count.
- Seeing all the books in the database with the information about the renter of the book if there is.
- Requesting the book from the user who rent it by sending an email (Sending e-mail function is not functional in the version of GitHub because I had to put my Google Account password)

Software has these features for users:

- Seeing all the books in the Library with the information about renter of the book if there is.
- Requesting a book from the books which is not rented to anyone else.
- Seeing all the book user rented in a table.

Login Page has these features:

- Understanding if the user is admin or not.
- Understanding if user entered their password wrong.
- Understanding if there is not user with that username.
- Understanding if user did not enter their username and/or their password.
- Understanding if user did enter a empty string into their username and/or password.
- Understanding if user put a space or capital letter in their username.

All of the user and book properties are stored in a SQLite file managed by SQLite3 library in Python.

Personal Outcomes: 
- Learned how to deal with app making when there is more than one Python file.
- Managed to improve my understanding of SQLite databases.
- Improved my ability to create Tkinter Graphical User Interfaces.

Dependencies: Pyhton, SQLite3, Tkinter.
  
