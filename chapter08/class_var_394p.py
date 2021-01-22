class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        print("No.{} student create".format(Student.count))
    
students = [
    Student("AAA", 11, 22, 33, 44),
    Student("BAA", 11, 22, 33, 44),
    Student("CAA", 11, 22, 33, 44),
    Student("DAA", 11, 22, 33, 44),
    Student("EAA", 11, 22, 33, 44)
]

print()
print("total student {}".format(Student.count))