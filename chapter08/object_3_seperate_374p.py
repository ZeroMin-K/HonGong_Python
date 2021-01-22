def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def student_get_average(student):
    return student_get_sum(student) /4 

def student_to_string(student):
    return "{}\t{}\t{}".format(student["name"], student_get_sum(student), student_get_average(student))

students = [
    create_student("AAA", 11, 11, 11, 11),
    create_student("BBB", 22, 22, 22, 22),
    create_student("CCC", 33, 33, 33, 33),
    create_student("DDD", 44, 44, 44, 44),
    create_student("EEE", 55, 55, 55, 55),
    create_student("FFF", 66, 66, 66, 66),
]

print("name", "score", "average", sep = "\t")
for student in students:
    print(student_to_string(student))