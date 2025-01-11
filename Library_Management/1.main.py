from storage_class import Storage, books_data 

# books are stored in "books_data" as [<title="To Kill a Mockingbird", author = "Harper Lee">]

class User:
    def __init__(self,name):
        self.name = name
        self.borrowed_books = []
    
    def borrow_books (self,title):
        self.borrowed_books.append(title)
            


class Library:
    def __init__(self):
        self.users = {}
        self.borrowed_books = []
        self.removed_books = []
    
    def add_user(self,user_name):
        if user_name in self.users:
            print("user already exist")
            return
        # self.users = {key - "user_name" : vlaue - "User(user_name)",as <name = user_name, borrowed_books = []>}
        self.users[user_name] = User(user_name)  # "User(user_name)" access the (User)-class.
        print(f"{user_name} is added.")          

    @staticmethod
    def view_books():
        print("\nAvailable Books:")
        for book in books_data:
            print(f"\n{book.title} by {book.author}")

    def borrow_book (self,user_name,title):
        if user_name not in self.users:
            print("user not found, Try adding the user first")
            return
        user = self.users[user_name] # "user" access the ("User" class)
        for book in books_data:
            if title == book.title:
                self.borrowed_books.append(book.title)
                user.borrowed_books.append(book.title)
                print(f"{book.title} by {book.author} is borrowed by {user.name}")
                self.removed_books.append(book)
                books_data.remove(book) 
            else:
                print("Sorry the book is already borrowed!")              
    
    def return_book(self,user_name,title):
        if user_name not in self.users:
            print("user not found, Try adding the user first")
            return
        user = self.users[user_name]
        if title in self.borrowed_books:
            self.borrowed_books.remove(title)
            user.borrowed_books.remove(title)
            print(f"Book Title: {title} has been returned by {user.name}") 

            # Adding the data of the book returned to the "books_data"
            for i in self.removed_books:
                if i.title == title:
                    books_data.append(i)
                                                                          
    def add_book(self,title,author):
        new_book = Storage(title,author)
        for book in books_data:
            if book.title == title:
                print("Book is already present")
                return
        books_data.append(new_book)
        print(f"{title} by {author} has been added")                    
        
    def view_users(self):
        if self.users:
            for user in self.users.values():
                print(f"{user.name} : {user.borrowed_books}")
        else:
            print("NO user found!")

    def list_borrowed_books(self):
        print(f"Borrowed Books : {self.borrowed_books}")
            
        
# Main Program

library_closed = False

library = Library()

while not library_closed:
    print("\nLibrary Menu:")
    print("1. View Books")
    print("2. Add User")
    print("3. Add Books")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. View Borrowed Books")
    print("7. View Users")
    print("8. Exit")

    choice = input("\nEnter your choice: ")
  
    if choice == "3":
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        library.add_book(title, author)

    elif choice == "2":
        name = input("Enter the user's name: ")
        library.add_user(name)

    elif choice == "1":
        library.view_books()

    elif choice == "4":
        user_name = input("Enter your name: ")
        book_title = input("Enter the title of the book: ")
        library.borrow_book(user_name, book_title)

    elif choice == "5":
        user_name = input("Enter your name: ")
        book_title = input("Enter the title of the book: ")
        library.return_book(user_name, book_title)

    elif choice == "6":
        library.list_borrowed_books()

    elif choice == "7":
        library.view_users()

    elif choice == "8":
        print("Exiting the library system. Goodbye!")
        library_closed = True

    else:
        print("Invalid choice. Please try again.")







    
