class User:
    def __init__(self, first_name, last_name, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.city = city
    
    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Name : {full_name.title()}")
        print(f"Email : {self.email}")
        print(f"City : {self.city}")
        
                