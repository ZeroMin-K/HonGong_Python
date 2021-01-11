key_list = ["name", "hp", "mp", "level"]
value_list = ["knight", 200, 30, 5]
character = {}

#for key in key_list:
#    for value in value_list:
#        character[key] = value

for i in range(0, len(key_list)):
    character[key_list[i]] = value_list[i]

print(character)