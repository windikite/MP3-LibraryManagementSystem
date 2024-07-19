from classes.genre import Genre

class Book(Genre):
    def __init__(self, name, ISBN, author, genre, year, available, borrowed, description):
        Genre.__init__(self, genre, description)
        self.name = name
        self.ISBN = ISBN
        self.author = author
        self.genre = genre
        self.year = year
        self.count = [available, borrowed]
    
    # getters
    def get_name(self):
        return self.name
    
    def get_ISBN(self):
        return self.ISBN
    
    def get_author(self):
        return self.author
    
    def get_genre(self):
        return self.genre
    
    def get_year(self):
        return self.year
    
    def get_count(self):
        return self.count
    
    # setters
    def update_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self.name = new_name
            return 1
        else:
            print("Please make sure the new name is a string that is longer than 0 characters.")
            return -1
    
    def update_ISBN(self, new_ISBN):
        if isinstance(new_ISBN, int):
            if self.year >= 2007 and len(new_ISBN) == 13 or self.year < 2007 and len(new_ISBN) == 10:
                self.ISBN = new_ISBN
                return 1
            else:
                print("Please make sure the new ISBN is an int with the following lengths according to the publish year:\n - Books published earlier than Jan 1 2007 must be 10 digits long\n - Books published on or after Jan 1 2007 must be 13 digits long")
                return -1
        else:
            print("Please make sure the new ISBN is an int with no dashes.")
            return -1
    
    def update_author(self, new_author):
        if isinstance(new_author, str) and len(new_author) > 0:
            self.author = new_author
            return 1
        else:
            print("Please make sure the new author name is a string that is longer than 0 characters.")
            return -1
    
    def update_genre(self, new_genre):
        if isinstance(new_genre, str) and len(new_genre) > 0:
            self.genre = new_genre
            return 1
        else:
            print("Please make sure the new genre name is a string that is longer than 0 characters.")
            return -1
    
    def update_year(self, new_year):
        if isinstance(new_year, int):
            if len(str(new_year)) > 0 and len(str(new_year)) < 5:
                self.year = new_year
                return 1
            else:
                print("Please make sure the new ISBN is an int with the following lengths according to the publish year:\n - Books published earlier than Jan 1 2007 must be 10 digits long\n - Books published on or after Jan 1 2007 must be 13 digits long")
                return -1
        else:
            print("Please make sure the new year is an int with no dashes, slashes or dots.")
            return -1
    
    def update_count(self, new_count):
        if isinstance(new_count, tuple) and len(new_count) == 2:
            available, borrowed = new_count
            if isinstance(available, int) and available >= 0 and isinstance(borrowed, int) and borrowed >= 0:
                self.count = [available, borrowed]
                return 1
            else:
                print("Please make sure the new quantities for available and borrowed are both whole numbers that are greater or equal to 0.")
                return -1
        else:
            print("Please format the arguments for the function to update the count like this including parentheses (#available, #borrowed)")
            return -1
    
    def info(self):
        print(f"{self.name} by {self.author}, a {self.genre} book printed in {self.year} under ISBN {self.ISBN} with {self.count[0]} available and {self.count[1]} borrowed.")