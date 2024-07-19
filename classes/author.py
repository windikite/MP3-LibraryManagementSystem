
class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography
        
    # getters
    def get_name(self):
        return self.name
    
    def get_biography(self):
        return self.biography
        
    # setters
    def update_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self.name = new_name
            return 1
        else:
            print("Please make sure the new name is a string that is longer than 0 characters.")
            return -1
    
    def update_bio(self, new_bio):
        if isinstance(new_bio, str) and len(new_bio) > 0:
            self.biography = new_bio
            return 1
        else:
            print("Please make sure the new biography is a string that is longer than 0 characters.")
            return -1
            
    def info(self):
        print(f"{self.name} - {self.biography}")
        return 1
