# dictionary syntax {}
users = {
    "id" : 1,
    "name" : "Leanne Graham",
    "username" : "Bret",
    "email" : "Sincere@april.biz",
    "address" : {
        "street" : "Kulas Light",
        "suite" : "Apt. 55",
        "zip code" : "92998-3874",
        "city" : "Gwenborough",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}
print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"]["street"])
print(users["address"]["suite"])
print(users["address"]["zip code"])
print(users["address"]["city"])
print(users["address"]["geo"]["lat"])
print(users["address"]["geo"]["lng"])

print(users)
print(type(users))
print('\n')
print('\nConvert Python Dictionary Format into JSON String Format')
import json
conv = json.dumps(users) #json.dump(s) = string
print(conv)
print(type(conv))

with open ('conv.json', 'w') as file:
    json.dump(users, file)