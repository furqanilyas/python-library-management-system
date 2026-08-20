import json


class Library:
    def __init__(self, title, author, isbn, category, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.copies = copies


class Information(Library):
    def __init__(self, title, author, isbn, category, copies, name, member_id, membership, new_title, new_author,
                 new_isbn, new_category):
        super().__init__(title, author, isbn, category, copies)
        self.name = name
        self.member_id = member_id
        self.membership = membership
        self.new_title = new_title
        self.new_author = new_author
        self.new_isbn = new_isbn
        self.new_category = new_category
        self.copies = copies

        self.books = []
        self.members = {}

    def add_book(self):
        print("<-- Add Book -->")
        self.title = input("Enter book title: ")
        self.author = input("Enter author: ")
        self.isbn = input("Enter ISBN: ")
        self.category = input("Enter category: ")
        self.copies = int(input("Enter copies: "))

        self.books.append(Library(self.title, self.author, self.isbn, self.category, self.copies))

        print(f"> Book added: '{self.title}' by {self.author}.\n")

        object1.save_data_list()

    def view_books(self):
        if len(self.books) == 0:
            print("> No books added.")
            return

        for count, book in enumerate(self.books, 1):
            print(
                f"{count}. Title: {book.title} | Author: {book.author} | ISBN: {book.isbn} "
                f"| Category: {book.category} | Copies: {book.copies}")

    def remove_book(self):
        if len(self.books) == 0:
            print("> No books added.")
            return

        book_to_remove = input("Enter book title to remove: ")

        for book in self.books:
            if book_to_remove in book.title:
                self.books.remove(book)
                print(f"> Book '{book_to_remove}' removed.\n")
                break
        else:
            print(f"> Book '{book_to_remove}' not found.\n")

        object1.save_data_list()

    def update_book(self):
        if len(self.books) == 0:
            print("No books added!")
            return

        update_book = input("Enter book title to update: ")

        for book in self.books:
            if update_book in book.title:
                self.new_title = input("Enter new book title: ")
                book.title = self.new_title
                self.new_author = input("Enter new author: ")
                book.author = self.new_author
                self.new_isbn = input("Enter new ISBN: ")
                book.isbn = self.new_isbn
                self.new_category = input("Enter new category: ")
                book.category = self.new_category
                self.copies = int(input("Enter copies: "))

                print(f"> Book updated: '{self.new_title}' by {self.new_author}.\n")
                break

            else:
                print(f"> Book '{update_book}' not found.\n")

        object1.save_data_list()

    def add_member(self):
        print("<-- Add Member -->")

        self.name = input("Enter member name: ")
        self.member_id = input("Enter Member ID: ")
        self.membership = input("Enter membership: ").title()

        self.members[self.name] = {
            "name": self.name,
            "member_id": self.member_id,
            "membership": self.membership
        }

        print(f"> Member added: {self.name} (ID: {self.member_id}) | {self.membership} tier")

        object1.save_data_dict()

    def view_members(self):
        if len(self.members) == 0:
            print("> No members added!")
            return

        print("<-- Member Details -->")

        for count, member in enumerate(self.members.values(), 1):
            print(f"{count}. Name: {member["name"]} | ID: {member["member_id"]} | Membership: {member["membership"]}\n")

    def remove_member(self):
        if len(self.members) == 0:
            print("No members added!")
            return

        member_to_del = input("Enter member name to remove: ")

        if member_to_del in self.members:
            del self.members[member_to_del]
            print(f"> Member '{member_to_del}' removed!")

        else:
            print(f"> Member '{member_to_del}' not found. ")

        object1.save_data_dict()

    def update_member(self):
        if len(self.members) == 0:
            print("No members added!")
            return

        update_member = input("Enter member name to update: ")

        for member in self.members.values():
            if update_member in self.members:
                new_member_name = input("Enter new member name: ")
                member["name"] = new_member_name

                new_member_id = input("Enter new member ID: ")
                member["member_id"] = new_member_id

                new_membership = input("Enter new membership: ")
                member["membership"] = new_membership

                print(f"> Member updated: {new_member_name} (ID: {new_member_id}) | {new_membership} tier")
                break

            else:
                print(f"> Member '{update_member}' not found.\n")

        object1.save_data_dict()

    #            <---------------- SAVING IN FILES SECTION ---------------->
    def save_data_list(self):

        try:
            data = []

            for book in self.books:
                data.append({
                    "title": book.title,
                    "author": book.author,
                    "isbn": book.isbn,
                    "category": book.category,
                    "copies": book.copies
                })
            with open("library.json", 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)

        except FileNotFoundError:
            print("No data found.")

    def load_data_list(self):

        try:
            with open("library.json", 'r', encoding='utf-8') as file:
                read_data = json.load(file)

            for book in read_data:
                self.books.append(
                    Library(book["title"], book["author"], book["isbn"], book["category"], book["copies"]))
        except FileNotFoundError:
            print("No data found.")

    def save_data_dict(self):
        try:
            with open("members.json", 'w', encoding='utf-8') as file:
                json.dump(self.members, file, indent=4)
        except FileNotFoundError:
            print("No data found.")

    def load_data_dict(self):
        try:
            with open("members.json", 'r', encoding='utf-8') as file:
                read_data = json.load(file)

            for member in read_data.values():
                self.members[member["name"]] = {
                    "name": member["name"],
                    "member_id": member["member_id"],
                    "membership": member["membership"]
                }
        except FileNotFoundError:
            print("No data found.")

    def reset_data(self):
        self.books = []
        self.members = {}

        print("Library Reset Successfully!")

        object1.save_data_list()
        object1.save_data_dict()


object1 = Information("", "", "", "", "", "", "", "", "", "", "", "")

object1.load_data_list()
object1.load_data_dict()

print("Welcome to Library Management System")

while True:
    print("1. Add book")
    print("2. View books")
    print("3. Remove book")
    print("4. Update book")
    print("5. Add Member")
    print("6. View Members")
    print("7. Remove Member")
    print("8. Update Member")
    print("0. Reset Library")

    choice = input("Enter choice: ")

    if choice == "q":
        print("Thanks for using!")
        break
    elif choice == '1':
        object1.add_book()
    elif choice == '2':
        object1.view_books()
    elif choice == '3':
        object1.remove_book()
    elif choice == '4':
        object1.update_book()
    elif choice == '5':
        object1.add_member()
    elif choice == '6':
        object1.view_members()
    elif choice == '7':
        object1.remove_member()
    elif choice == '8':
        object1.update_member()
    elif choice == '0':
        object1.reset_data()

    else:
        print("Invalid choice!")
