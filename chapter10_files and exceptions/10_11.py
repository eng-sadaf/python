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


