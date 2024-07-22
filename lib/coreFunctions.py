from lib.utilityFunctions import generateUniqueID, askMenu, check_regex, validate_and_compare, importToDict, exportItemsToFile, compileToString, backupFile
from classes.book import Book
from classes.user import User
from classes.author import Author
from classes.genre import Genre

def add_book(books, authors, genres):
    # genre_index = askMenu([genre[1].get_name() for genre in list(genres.items())], 
    # "Please choose a genre: ")
    # genre = list(genres.items())[genre_index-1][1]
    book_name = str(input("Please input a name for the book: "))
    genre = ""
    while genre == "":
        chosen_genre = search_dict(genres, "Please choose a genre: ")
        if chosen_genre == -1:
            chosen_genre = add_genre(genres)
        elif chosen_genre == -2:
            return
        elif chosen_genre != -1 and chosen_genre != -2 and chosen_genre != -3:
            genre = chosen_genre
    author = ""
    while author == "":
        chosen_author = search_dict(authors, "Please choose an author: ")
        if chosen_author == -1:
            chosen_author = add_author(authors)
        elif chosen_author == -2:
            return
        elif chosen_author != -1 and chosen_author != -2 and chosen_author != -3:
            author = chosen_author
    book_year = int(input("Please input a publish year: "))
    book_ISBN = int(input("Please input an ISBN: "))
    num_avail = int(input("Please input number available: "))
    num_borrowed = int(input("Please input number borrowed: "))
    new_book = Book(book_name, book_ISBN, author.get_name(), genre.get_name(), book_year, num_avail, num_borrowed, genre.get_description())
    books.update({book_ISBN:new_book})
    return new_book

def add_author(authors):
    book_author = str(input("Please input an author name: "))
    author_bio = str(input("Please input author biography: "))
    new_author = Author(book_author, author_bio)
    authors.update({book_author: new_author})
    return new_author

def add_genre(genres):
    genre_name = str(input("Please input a genre name: "))
    genre_description = str(input("Please input genre description: "))
    new_genre = Genre(genre_name, genre_description)
    genres.update({genre_name: new_genre})
    return new_genre

def add_user(users):
    user_name = str(input("Please input a name for the user: "))
    ID = generateUniqueID()
    new_user = User(user_name, ID, {})
    users.update({ID: new_user})
    return new_user
    
def display_info(dictionary):
    entry_list = [entry[1].info() for entry in dictionary.items()]

def display_names(dictionary):
    entry_list = [print(entry[1].get_name()) for entry in dictionary.items()]
    
def search_dict(dictionary, text):
    entry_list = [entry[1].get_name() for entry in dictionary.items()]
    entry_list.append("Add new entry")
    entry_list.append("Quit to main menu")
    entry_index = askMenu(entry_list, text)
    entry = ""
    try:
        entry_index = int(entry_index)
        if entry_index == len(entry_list):#Quit to menu
            return -2
        elif entry_index == len(entry_list)-1:#Add new entry
            return -1
        else:
            entry = dictionary.get(list(dictionary)[entry_index-1])
    except ValueError:
        print("Function error! Please make sure to choose one of the chosen options!")
        return -3
    except TypeError:
        print("Function error! Please make sure to input numbers for menu selections!")
        return -3
    except IndexError:
        print("Index error! Please make sure to choose one of the chosen options!")
        return -3
    else:
        return entry

def checkout_book(books, authors, genres, users):
    book = search_dict(books, "Please choose a book: ")
    if book == -1:
        book = add_book(books, authors, genres)
    user = search_dict(users, "Please choose a user: ")
    if user == -1:
        user = add_user(users)
    count = book.get_count()
    ISBN = book.get_ISBN()
    if count[0] > 0:
        if ISBN not in user.get_borrowed():
            updated = book.update_count((count[0]-1, count[1]+1))
            checked_out = user.check_out(ISBN)
            if updated != -1 and checked_out != -1:
                print(f"{user.get_name()} checked out {book.get_name()}! There are {book.get_count()[0]} copies left and {book.get_count()[1]} currently checked out.")
        else:
            print(f"{user.get_name()} is already borrowing that book.")
    else:
        print("There are no more copies!")
        return -1

def return_book(books, users):
    user = ""
    while user == "":
        chosen_user = search_dict(users, "Please choose a user: ")
        if chosen_user == -1:
            chosen_user = add_user(users)
        elif chosen_user == -2:
            return
        elif chosen_user != -1 and chosen_user != -2 and chosen_user != -3:
            user = chosen_user
    borrowed = user.get_borrowed()
    if borrowed != {}:
        book_index = askMenu([books[ISBN].get_name() for ISBN in borrowed], "Please choose a book to return: ")
        ISBN = list(borrowed)[book_index-1]
        borrowed.remove(ISBN)
        book = books.get(ISBN)
        count = book.get_count()
        returned = book.update_count((count[0]+1, count[1]-1))
        if returned != -1:
            print(f"Returned {book.get_name()}! There are now {book.get_count()[0]} available.")
        else:
            print("Unable to return book.")
    else:
        print(f"{user.get_name()} owes no books.")

def filter_dict(dictionary, key, value):
    filtered_list = []
    for entry in list(dictionary.items()):
        if str(value).lower() in str(entry[1].get(key)).lower():
            filtered_list.append(entry)
    return filtered_list

def search_book_by_field(books):
    user_input = askMenu([
        "Name", 
        "ISBN", 
        "Author", 
        "Genre", 
        "Year", 
        "Quit to main menu"], 
        "Please choose a field to search by: ")
    pre_filtered_dict = {c[1].get_name(): {
            "name": c[1].get_name(), 
            "ISBN": c[1].get_ISBN(), 
            "author": c[1].get_author(),
            "genre": c[1].get_genre(),
            "year": c[1].get_year(),
            "available": c[1].get_count()[0],
            "borrowed": c[1].get_count()[1],
            "class": c[1]
        } for c in list(books.items())}
    search_term = ""
    filtered_list = []
    if user_input == 1:#Search name
        search_term = str(input("Please input a name to search for: "))
        filtered_list = filter_dict(pre_filtered_dict, "name", search_term)
    elif user_input == 2:#Search isbn
        search_term = int(input("Please input an ISBN to search for: "))
        filtered_list = filter_dict(pre_filtered_dict, "ISBN", search_term)
    elif user_input == 3:#Search author
        search_term = str(input("Please input an author to search for: "))
        filtered_list = filter_dict(pre_filtered_dict, "author", search_term)
    elif user_input == 4:#Search genre
        search_term = str(input("Please input a genre to search for: "))
        filtered_list = filter_dict(pre_filtered_dict, "genre", search_term)
    elif user_input == 5:#Search year
        search_term = int(input("Please input a year to search for: "))
        filtered_list = filter_dict(pre_filtered_dict, "year", search_term)
    if len(filtered_list) > 0:
        filtered_dict = {c[1].get("ISBN"): c[1].get("class") for c in filtered_list}
        return filtered_dict
    else:
        return -1

def save_books(books):
    pre_filtered_dict = {c[1].get_name(): {
            "name": c[1].get_name(), 
            "ISBN": c[1].get_ISBN(), 
            "author": c[1].get_author(),
            "genre": c[1].get_genre(),
            "year": c[1].get_year(),
            "available": c[1].get_count()[0],
            "borrowed": c[1].get_count()[1]
        } for c in list(books.items())}
    exportItemsToFile(pre_filtered_dict, "./library/books.txt")

def save_users(users):
    pre_filtered_dict = {c[1].get_name(): {
            "name": c[1].get_name(), 
            "ID": c[1].get_ID(),
            "borrowed": c[1].get_borrowed()
        } for c in list(users.items())}
    exportItemsToFile(pre_filtered_dict, "./library/users.txt")

def save_authors(authors):
    pre_filtered_dict = {c[1].get_name(): {
            "name": c[1].get_name(), 
            "biography": c[1].get_biography()
        } for c in list(authors.items())}
    exportItemsToFile(pre_filtered_dict, "./library/authors.txt")

def save_genres(genres):
    pre_filtered_dict = {c[1].get_name(): {
            "name": c[1].get_name(), 
            "description": c[1].get_description()
        } for c in list(genres.items())}
    exportItemsToFile(pre_filtered_dict, "./library/genres.txt")

def graceful_set(value):
    if value != 'undefined':
        return value
    else:
        return {}