import json

data = '''[{
"name":"Maggie",
"phone":"132423",
"color":["red","blue"]
},
{"name":"Ivan",
"phone":"85023",
"color":["black","grey"]}]'''
info = json.loads(data)
for user in info:
    print(user["name"])
    print(user["phone"])
    print(user["color"])