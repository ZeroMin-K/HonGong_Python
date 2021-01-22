def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }


students = [
    create_student("AAA", 11, 11, 11, 11),
    create_student("BBB", 22, 22, 22, 22),
    create_student("CCC", 33, 33, 33, 33),
    create_student("DDD", 44, 44, 44, 44)
]

print("name", "score", "average", sep = "\t")z
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep = "\t")