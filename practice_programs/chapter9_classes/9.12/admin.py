from user import User
        

class Admin(User):
        def __init__(self, first_name, last_name, email, city):
            super().__init__(first_name, last_name, email, city)
#             self.privileges = []
            
            self.privileges = Privileges()
       
            
class Privileges:
    
    def __init__(self):
        self.privileges = []  
        
    def show_privileges(self):
            print("Admin privileges are : ")
            for privilege in self.privileges:
                print(f"\t- {privilege.title()}")    


                