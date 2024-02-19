while True:
    print("*** MENU*** "+"\n" +
          "1) List Books"+"\n" +
          "2) Add Book" + "\n" +
          "3) Remove Book ")
    n = int(input("Please enter your choice :"))
    if n == 1:
        lib_books = []
        with open("BOOK", "r") as f:
            lines = f.readlines()
            for line in lines:
                values = line.strip().split(", ")
                lib_books.append(values)
            for book in lib_books:
                print(", ".join(book))
    elif n == 2:
        bookName = str(input("Please enter the book name:"))
        authorName = str(input("Please enter the author name:"))
        releaseDate = str(input("Please enter the release date:"))
        numOfPages = input("Please enter the number of pages:")
        addBook = bookName + ", " + authorName + ", " + releaseDate + ", " + numOfPages + "\n"
        with open("BOOK", "a+") as f:
            f.write(addBook)
    elif n == 3:
        remove_book = input("Please enter the book name to remove: ")
        with open("BOOK", "r") as f:
            lines = f.readlines()
        with open("BOOK", "w") as f:
            removed = False
            for line in lines:
                book_name = line.strip().split(", ")[0]
                if book_name != remove_book:
                    f.write(line)
                else:
                    removed = True
            if removed:
                print(f"'{remove_book}' has been removed from the list.")
            else:
                print(f"'{remove_book}' not found in the list.")
