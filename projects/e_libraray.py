class Elibrary:
    def __init__(s):
        s.books = []

    def add_book(s, title, author):
        s.books.append({"title": title, "author": author, "status": True})
        print(f'Book "{title}" by {author} added to the library.')
    def view(s):
        if not s.books:
            print("No books available in the library.")
            return
        for i, book in enumerate(s.books, 1):
            status = "Available" if book["status"] else "Checked Out"
            print(f"{i}. Title: {book['title']}, Author: {book['author']}, Status: {status}")
        print("\n")
    def borrow(s, title):
        for book in s.books:
            if book["title"] == title:
                if book["status"]:
                    book["status"] = False
                    print(f'You have borrowed "{title}". Enjoy reading!')
                else:
                    print(f'Sorry, "{title}" is currently checked out.')
                return
        print(f'Book "{title}" not found in the library.')
    def ret(s, title):
        for book in s.books:
            if book["title"] == title:
                if not book["status"]:
                    book["status"] = True
                    print(f'You have returned "{title}". Thank you!')
                else:
                    print(f'"{title}" was not checked out.')
                return
        print(f'Book "{title}" not found in the library.')
    def search(s, keyword):
        found_books = [book for book in s.books if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower()]
        if found_books:
            for book in found_books:
                status = "Available" if book["status"] else "Checked Out"
                print(f'Title: {book["title"]}, Author: {book["author"]}, Status: {status}')
        else:
            print(f'No books found matching "{keyword}".')
def main():
    library = Elibrary()
    while True:
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == 2:
            library.view()
        elif choice == 3:
            title = input("Enter book title to borrow: ")
            library.borrow(title)
        elif choice == 4:
            title = input("Enter book title to return: ")
            library.ret(title)
        elif choice == 5:
            keyword = input("Enter keyword to search (title/author): ")
            library.search(keyword)
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")