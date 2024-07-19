class User:
    def __init__(self, name, ID, borrowed):
        self.name = name
        self.ID = ID
        self.borrowed = borrowed
        
    # getters
    def get_name(self):
        return self.name
    
    def get_ID(self):
        return self.ID
    
    def get_borrowed(self):
        return self.borrowed
        
    # setters
    def update_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self.name = new_name
            return 1
        else:
            print("Please make sure the new name is a string that is longer than 0 characters.")
            return -1
            
    def update_ID(self, new_ID):
        if isinstance(new_ID, int) and new_ID > 0:
            self.ID = new_ID
        else:
            print("Please make sure the new ID is a positive number.")
            return -1
            
    def check_out(self, borrowed_ISBN):
        if isinstance(int(borrowed_ISBN), int):
            if len(str(borrowed_ISBN)) == 10 or len(str(borrowed_ISBN)) == 13:
                if borrowed_ISBN not in self.borrowed:
                    self.borrowed.add(borrowed_ISBN)
                    return 1
                else:
                    print("Book already being borrowed!")
                    return 1
            else:
                print("Please make sure the ISBN is either 10 or 13 digits.")
                return -1
        else:
            print("Please make sure the ISBN is an integer.")
            return -1
    
    def check_in(self, borrowed_ISBN):
        if isinstance(borrowed_ISBN, int) and len(str(borrowed_ISBN)) == 10 or isinstance(borrowed_ISBN, int) and len(str(borrowed_ISBN)) == 13:
            if borrowed_ISBN in self.borrowed:
                self.borrowed.remove(borrowed_ISBN)
                print(f"Book has been checked in!")
                return 1
            else:
                print(f"{self.name} is not borrowing that book!")
                return -1
        else:
            print("Please make sure the ISBN is either 10 or 13 digits.")
            return -1
            
    def info(self):
        borrowed = set(self.borrowed)
        borrowed.add(1)
        print(f"User {self.name} with ID: {self.ID} and {len(borrowed)-1} different ISBNs checked out.")
        borrowed.remove(1)
 
            