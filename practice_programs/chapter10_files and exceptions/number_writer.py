<<<<<<< HEAD
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
=======
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
>>>>>>> 24704871acbe67042acd8a67c478b3d536b16ef6
    json.dump(numbers, f)