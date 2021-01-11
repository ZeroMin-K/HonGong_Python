character = {
    "name" : "knight",
    "level" : 12,
    "items" : {
        "sword" : "flame sword",
        "aromor" : "Full Plate"
    },
    "skill" : ["cut", "strong cut", "power cut"]
}

for key in character:
    if type(character[key]) is dict:
        for small_key in character[key]:
            print(small_key, ":", character[key][small_key])
    elif type(character[key]) is list:
        for item in character[key]:
            print(key, ":", item)
    else:
        print(key, ":", character[key])