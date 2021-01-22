class Student:

    count = 0
    students = []

    @classmethod
    def print(cls):
        print("---- students list ----")
        print("name\tscore\taverage")
        for student in cls.students:
            print(str(student))
        print("-----------------------")
    
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math 
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() /4
    
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

Student("AAA", 11, 22, 33, 44)
Student("BAA", 11, 22, 33, 44)
Student("CAA", 11, 22, 33, 44)
Student("DAA", 11, 22, 33, 44)
Student("EAA", 11, 22, 33, 44)
Student("FAA", 11, 22, 33, 44)
Student("GAA", 11, 22, 33, 44)
Student("HAA", 11, 22, 33, 44)
Student("IAA", 11, 22, 33, 44)

Student.print()

