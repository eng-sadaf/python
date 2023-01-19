<<<<<<< HEAD
from fileinput import filename
import json

filename = 'fav_num.json'
with open(filename) as f:
    num = json.load(f)
=======
from fileinput import filename
import json

filename = 'fav_num.json'
with open(filename) as f:
    num = json.load(f)
>>>>>>> 24704871acbe67042acd8a67c478b3d536b16ef6
    print("I know your favorite number! It’s",num)