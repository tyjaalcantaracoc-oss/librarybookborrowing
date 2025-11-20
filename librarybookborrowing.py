from datetime import datetime

available_books = ["Harry Potter", "The Great Gatsby", "1984", "To Kill a Mockingbird", "Pride and Prejudice"]
borrowed_books = []
book_requests = []

def show_menu(role):
    menus = {
        "Librarian": ["Add Borrow Record", "Mark Book as Returned", "View Borrowed and Requested Books", "Exit"],
        "Borrower": ["Request a Book", "View My Borrowed Books", "Exit"]
    }
    print(f"\n--- {role} Menu ---")
    for i, option in enumerate(menus[role], 1):
        print(f"{i}. {option}")

def check_due_date(date_text):
    try:
        due_date = datetime.strptime(date_text, "%Y-%m-%d").date()
        if due_date < datetime.today().date():
            print("Invalid date. Must be today or a future date.")
            return False
        return True
    except ValueError:
        print("Use format YYYY-MM-DD.")
        return False

def add_borrow_record():
    name = input("Enter borrower name: ")
    book = input("Enter book title: ")
    if book in available_books:
        while True:
            due = input("Enter due date (YYYY-MM-DD): ")
            if check_due_date(due): break
        borrowed_books.append({"name": name, "book": book, "due": due, "status": "borrowed"})
        available_books.remove(book)
        book_requests[:] = [r for r in book_requests if not (r[0].lower()==name.lower() and r[1].lower()==book.lower())]
        print(f"\n'{book}' borrowed by {name}. Due on: {due}")
    else:
        print("Book not available.")

def mark_as_returned():
    name = input("Enter borrower name: ")
    book = input("Enter book title: ")
    for record in borrowed_books:
        if record["name"].lower()==name.lower() and record["book"].lower()==book.lower() and record["status"]=="borrowed":
            record["status"]="returned"
            available_books.append(book)
            print(f"'{book}' marked as returned.")
            return
    print("No matching record found.")

def view_books(all_records=False):
    if all_records:
        print("\n--- Borrowed Books ---")
        if borrowed_books:
            for r in borrowed_books:
                print(f"{r['name']} - {r['book']} (Due: {r['due']}, Status: {r['status']})")
        else: print("No borrowed books.")
        print("\n--- Book Requests ---")
        if book_requests:
            for req in book_requests: print(f"{req[0]} requested '{req[1]}'")
        else: print("No book requests.")
    else:
        name = input("Enter your name: ")
        found = False
        for r in borrowed_books:
            if r["name"].lower()==name.lower():
                print(f"Book: {r['book']} | Due: {r['due']} | Status: {r['status']}")
                found = True
        if not found: print("You have not borrowed any books.")

def request_a_book():
    name = input("Enter your name: ")
    book = input("Enter the book title: ")
    book_requests.append((name, book))
    if book in available_books:
        print(f"'{book}' is available. Contact the librarian to borrow it.")
    else:
        print(f"'{book}' is unavailable. Your request has been recorded.")

while True:
    print("\nWelcome to the Library Book Borrowing System")
    print("1. Librarian\n2. Borrower\n3. Exit")
    role_choice = input("Choose role (1-3): ").strip()

    if role_choice == "3":
        print("Goodbye!")
        break
    elif role_choice == "1":
        role = "Librarian"
    elif role_choice == "2":
        role = "Borrower"
    else:
        print("Invalid choice. Try again.")
        continue

    while True:
        show_menu(role)
        choice = input("Enter your choice: ").strip()

        if role == "Librarian":
            if choice == "1": add_borrow_record()
            elif choice == "2": mark_as_returned()
            elif choice == "3": view_books(True)
            elif choice == "4": break
            else: print("Invalid choice.")
        else:
            if choice == "1": request_a_book()
            elif choice == "2": view_books()
            elif choice == "3": break
            else: print("Invalid choice.")