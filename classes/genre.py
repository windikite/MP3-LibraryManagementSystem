
class Genre:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    # getters
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
     # setters
    def update_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self.name = new_name
            return 1
        else:
            print("Please make sure the new name is a string that is longer than 0 characters.")
            return -1
    
    def update_description(self, new_description):
        if isinstance(new_description, str) and len(new_description) > 0:
            self.description = new_description
            return 1
        else:
            print("Please make sure the new description is a string that is longer than 0 characters.")
            return -1
            
    def info(self):
        print(f"{self.name} - {self.description}")
        return 1