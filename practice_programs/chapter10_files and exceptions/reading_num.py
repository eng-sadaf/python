from fileinput import filename
import json

filename = 'fav_num.json'
with open(filename) as f:
    num = json.load(f)
    print("I know your favorite number! It’s",num)