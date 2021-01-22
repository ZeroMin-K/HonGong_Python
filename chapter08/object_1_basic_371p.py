students = [
    { "name":"aaa", "korean":87, "math":95, "english": 84, "science":91},
    { "name":"bbb", "korean":85, "math":93, "english": 83, "science":92},
    { "name":"ccc", "korean":83, "math":92, "english": 81, "science":93},
    { "name":"ddd", "korean":82, "math":91, "english": 82, "science":92},
    { "name":"eee", "korean":81, "math":93, "english": 83, "science":94},
    { "name":"fff", "korean":87, "math":94, "english": 84, "science":95}
]

print("name", "total", "average", sep = "\t")

for student in students:
    score_sum = student["korean"] + student["math"] + student["english"]+ student["science"]
    score_average = score_sum /4

    print(student["name"], score_sum, score_average, sep = "\t")

