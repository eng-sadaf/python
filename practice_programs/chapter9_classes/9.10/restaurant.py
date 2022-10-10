class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"My Restaurant name is {self.restaurant_name} .")
        print(f"{self.cuisine_type} is our cuisine.")
    
    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open now.")
        
    def set_number_served(self):
        print(f"We have served {self.number_served} people.")
    
    def increment_number_served(self,add_people):
        self.number_served += add_people
        