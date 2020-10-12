# import json

# person = {
#     "firstName": "Jane",
#     "lastName": "Doe",
#     "hobbies": ["running", "swimming", "singing"],
#     "age": 28,
#     "hasChildren": True,
#     "children": [
#         {
#             "firstName": "Bob",
#             "age": 5
#         },
#         {
#             "firstName": "Bob",
#             "age": 7
#         }
#     ]
# }

# personJSON = json.dumps(person, indent=4, sort_keys=True)
# # print(personJSON)

# with open('person.json', 'r') as file:
#     person = json.load(file)
#     print(person)

# # person = json.loads(personJSON)
# # print(person)

import json
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 28)

def encodeUser(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")

from json import JSONEncoder

class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

def decodeUser(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    else:
        return dct



user = json.loads(userJSON, object_hook=decodeUser)
print(type(user))
print(user.name)



