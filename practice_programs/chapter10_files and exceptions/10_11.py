<<<<<<< HEAD
import json

filename = 'fav_num.json'
try:
    with open(filename) as f:
      num = json.load(f)
except FileNotFoundError:
    numbers = input("Enter your favourite number: ")
    with open(filename, 'w') as f:
       json.dump(numbers, f)
else:
    print("I know your favorite number! It’s",num)


=======
import json

filename = 'fav_num.json'
try:
    with open(filename) as f:
      num = json.load(f)
except FileNotFoundError:
    numbers = input("Enter your favourite number: ")
    with open(filename, 'w') as f:
       json.dump(numbers, f)
else:
    print("I know your favorite number! It’s",num)


>>>>>>> 24704871acbe67042acd8a67c478b3d536b16ef6
