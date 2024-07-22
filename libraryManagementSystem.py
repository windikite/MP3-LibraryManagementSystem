from lib.utilityFunctions import generateUniqueID, askMenu, check_regex, validate_and_compare, importToDict, exportItemsToFile, compileToString, backupFile
from lib.coreFunctions import display_info, display_names, add_author, add_book, add_user, add_genre, search_dict, search_book_by_field, checkout_book, return_book, filter_dict, save_authors, save_books, save_genres, save_users, graceful_set
from classes.book import Book
from classes.user import User
from classes.author import Author
from classes.genre import Genre
import os
    
def main():
    # the default genres, books, authors and users
    default_genres = {name: Genre(name, description) for name, description in [
        ["Adventure", "Adventurous stories!"],
        ["Horror", "Spooky stories!"],
        ["Folklore", "Tales from people about supernatural stuff!"],
        ["Comedy", "Non-spooky scary stories!"],
        ["Tragedy", "Sad stories!"]
        ]}
    default_books = {ISBN: Book(name, ISBN, author, genre, year, available, borrowed, genre_description) for name, ISBN, author, genre, year, available, borrowed, genre_description in [
        ["An Encyclopedia of Fairies", 1325763258, "Katherine Briggs", "Folklore", 1976, 0, 1, "Tales from people about supernatural stuff!"],
        ["Fairy Folk Tales of Ireland", 8927982364, "William Butler Yeats", "Folklore", 1888, 1, 1, "Tales from people about supernatural stuff!"],
        ["The Secret Commonwealth", 2392356235, "Robert Kirk", "Folklore", 1815, 1, 2, "Tales from people about supernatural stuff!"]
        ]}
    default_authors = {name: Author(name, biography) for name, biography in [
        ["Katherine Briggs", "American folklorist."],
        ["Keaton Yates", "19th century American folklorist."],
        ["Jackson Crawford", "Modern american linguist with a specialty in norse mythology."]
        ]}
    default_users = {ID: User(name, ID, borrowed) for name, ID, borrowed in [
        ["Billy", generateUniqueID(), {1325763258, 2392356235}],
        ["Timmy", generateUniqueID(), {2392356235, 8927982364}]
        ]}
    books = {}
    genres = {}
    authors = {}
    users = {}
    # setup genres
    genre_file_location = "./library/genres.txt"
    genre_fields = ["name", "description"]
    if os.path.exists(genre_file_location) == True:
        imported_dict = importToDict(genre_file_location, genre_fields)
        genres = {b[1].get("name"): Genre(b[1].get("name"), b[1].get("description")) for b in list(imported_dict.items())}
    else:
        genres = default_genres
    # setup authors
    author_file_location = "./library/authors.txt"
    author_fields = ["name", "biography"]
    if os.path.exists(author_file_location) == True:
        imported_dict = importToDict(author_file_location, author_fields)
        authors = {b[1].get("name"): Author(b[1].get("name"), b[1].get("biography")) for b in list(imported_dict.items())}
    else:
        authors = default_authors
    # setup books
    book_file_location = "./library/books.txt"
    book_fields = ["name", "ISBN", "author", "genre", "year", "available", "borrowed"]
    if os.path.exists(book_file_location) == True:
        imported_dict = importToDict(book_file_location, book_fields)
        books = {b[1].get("ISBN"): Book(b[1].get("name"), b[1].get("ISBN"), b[1].get("author"), b[1].get("genre"), b[1].get("year"), b[1].get("available"), b[1].get("borrowed"), genres.get(b[1].get("genre")).get_name()) for b in list(imported_dict.items())}
    else:
        books = default_books
    # setup users
    user_file_location = "./library/users.txt"
    user_fields = ["name", "ID", "borrowed"]
    if os.path.exists(user_file_location) == True:
        imported_dict = importToDict(user_file_location, user_fields)
        users = {b[1].get("ID"): User(b[1].get("name"), b[1].get("ID"), graceful_set(b[1].get("borrowed"))) for b in list(imported_dict.items())}
    else:
        users = default_users
    print("Welcome to the Library Management System!")
    while True:
        try:
            user_input = askMenu([
            "Book Operations", 
            "User Operations", 
            "Author Operations", 
            "Genre Operations", 
            "Save and Quit",
            "Quit program"], 
            "Please choose an operation: ")
            if user_input == 1:
                user_input = askMenu([
                "Add a new book", 
                "Borrow a book", 
                "Return a book", 
                "Search for a book", 
                "Display all books",
                "Quit to main menu"], 
                "Please choose an operation: ")
                if user_input == 1:#Add book
                    add_book(books, authors, genres)
                elif user_input == 2:#Borrow book
                    checkout_book(books, authors, genres, users)
                elif user_input == 3:#Return book
                    return_book(books, users)
                elif user_input == 4:#Search for book
                    user_input = askMenu([
                    "Choose from list of books", 
                    "Search books by field", 
                    "Quit to main menu"], 
                    "Please choose an operation: ")
                    if user_input == 1:
                        book = search_dict(books, "Please choose a book: ")
                        if book == -1:
                            book = add_book(books, authors, genres)
                        book.info()
                    if user_input == 2:
                        filtered_dict = search_book_by_field(books)
                        if filtered_dict != -1:
                            book = search_dict(filtered_dict, "Please choose a book: ")
                            if book == -1:
                                book = add_book(books, authors, genres)
                            book.info()
                        else:
                            print("There were no books found under that criteria.")
                            user_input = askMenu([
                            "Add new book",
                            "Quit to main menu"], 
                            "Please choose an operation: ")
                            if user_input == 1:
                                book = add_book(books, authors, genres)
                                book.info()
                            elif user_input == 2:
                                continue
                elif user_input == 5:#Display all books
                    display_info(books)
                elif user_input == 6:#Quit
                    continue
            elif user_input == 2:
                user_input = askMenu([
                "Add a user", 
                "View user details", 
                "Display all users", 
                "Quit to main menu"], 
                "Please choose an operation: ")
                if user_input == 1:#Add user
                    add_user(users)
                elif user_input == 2:#View user details
                    user = search_dict(users, "Please choose a user: ")
                    if user == -1:
                        user = add_user(users)
                    user.info()
                elif user_input == 3:#Display all users
                    display_info(users)
                elif user_input == 4:#Quit to menu
                    continue
            elif user_input == 3:
                user_input = askMenu([
                "Add an author", 
                "View author details", 
                "Display all authors", 
                "Quit to main menu"], 
                "Please choose an operation: ")
                if user_input == 1:#Add author
                    add_author(authors)
                elif user_input == 2:#View author details
                    author = search_dict(authors, "Please choose an author: ")
                    if author == -1:
                        author = add_author(authors)
                    author.info()
                elif user_input == 3:#Display all authors
                    display_info(authors)
                elif user_input == 4:#Quit to menu
                    continue
            elif user_input == 4:
                user_input = askMenu([
                "Add a genre", 
                "View genre details", 
                "Display all genres", 
                "Quit to main menu"], 
                "Please choose an operation: ")
                if user_input == 1:#Add genre
                    add_genre(genres)
                elif user_input == 2:#View genre details
                    genre = search_dict(genres, "Please choose a genre: ")
                    if genre == -1:
                        genre = add_genre(genres)
                    genre.info()
                elif user_input == 3:#Display all genres
                    display_info(genres)
                elif user_input == 4:#Quit to menu
                    continue
            elif user_input == 5:
                save_users(users)
                save_authors(authors)
                save_genres(genres)
                save_books(books)
                break
            elif user_input == 6:
                break
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
        finally:
            print("----------------------")
main()