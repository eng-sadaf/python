from restaurant import Restaurant        
    
my_restaurant = Restaurant('Food Corner','Punjabi')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served()

my_restaurant.number_served = 50
my_restaurant.set_number_served()

my_restaurant.increment_number_served(20)
my_restaurant.set_number_served()
print("Today is the day of Business...")