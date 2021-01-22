class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() /4
    
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())
    

students = [
    Student("AAA", 11, 22, 33, 44),
    Student("BAA", 11, 22, 33, 44),
    Student("CAA", 11, 22, 33, 44),
    Student("DAA", 11, 22, 33, 44),
    Student("EAA", 11, 22, 33, 44),
]

print("name", "score", "average", sep = "\t")
for student in students:
    print(str(student))