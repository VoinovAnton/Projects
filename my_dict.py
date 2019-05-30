mydict = {
    "name": "Anton",
    "details": {"profession": "god"},
    "items": ["ball", "computer", "mouse"],
    "age": 2019
}

print("My name is " + mydict['name'])
print("My profession is " + mydict['details']['profession'])
print("My age is " + str(mydict['age']))
print("I have " + ",".join(mydict['items']))   # I have ball, computer, mouse