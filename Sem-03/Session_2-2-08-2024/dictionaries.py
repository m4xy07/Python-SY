# Using dictionaries in python and its functions
dict1 = {}

dict1["name"] = "John"
dict1["age"] = 30
dict1["city"] = "New York"

print(dict1["name"])

if "age" in dict1:
    print("Age is present")

dict1["age"] = 35

del dict1["city"]

print(len(dict1))

keys = dict1.keys()
print(keys)

values = dict1.values()
print(values)

items = dict1.items()
print(items)

dict1.clear()

if not dict1:
    print("The dictionary is empty")
