# Library Management System

A Python command-line Library Management System built with **Object-Oriented Programming (OOP)**.

The project currently supports book and member management with JSON-based data persistence. It is still a **work in progress**, with more features and improvements planned.

## Features

### Book Management

* Add books
* View all books
* Remove books
* Update book details
* Store title, author, ISBN, category, and copies

### Member Management

* Add members
* View members
* Remove members
* Update member details
* Store member ID and membership type

### Data Persistence

* Save books to `library.json` and members to `members.json`
* Automatically load saved data when the program starts
* Reset library data on demand

`library.json` and `members.json` are used for local data storage and are generated automatically when data is saved.

## How to Use

You'll see a menu with the available options:

```text
1. Add book
2. View books
3. Remove book
4. Update book
5. Add Member
6. View Members
7. Remove Member
8. Update Member
0. Reset Library
```

Enter the number of the action you want to perform.

### Adding a Book

Choose `1` and enter:

* Book title
* Author
* ISBN
* Category
* Number of copies

The book will be added to the library and saved automatically.

### Managing Members

Choose `5` to add a member. You'll be asked for:

* Member name
* Member ID
* Membership type

You can then view, update, or remove members using options `6`, `7`, and `8`.

### Updating or Removing Data

Choose the corresponding menu option and enter the book title or member name when prompted.

### Resetting the Library

Choose `0` to remove all currently stored books and members and reset the library data.

### Exiting

Enter `q` at any time to exit the program.

## Tech Stack

* Python
* Object-Oriented Programming
* Classes and inheritance
* Lists and dictionaries
* JSON
* File handling
* Exception handling
* Command-line interface

## How to Run

Make sure Python 3 is installed.

```bash
python main.py
```

## Current Status

**Work in Progress**

The core book and member management features are implemented, but the project is still being developed. More functionality, validation, and code improvements will be added.

## Expected Future Improvements

* Book borrowing, renewing and reserving
* Search functionality
* Better input validation
* Library statistics (most borrowed books, active members, etc.)
