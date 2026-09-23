<<<<<<< HEAD
import json

data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)

parsed_data = json.loads(json_str)
print(parsed_data)
print(parsed_data["name"])
=======
import json

data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)

parsed_data = json.loads(json_str)
print(parsed_data)
print(parsed_data["name"])
>>>>>>> 36e2367c506c94705546caf13817ba0e32d9cbfa
print(parsed_data["age"])