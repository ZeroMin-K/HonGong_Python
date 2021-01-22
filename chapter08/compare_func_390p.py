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

    def __str__(self, student):
        return "{}\t{}\t{}".format(self.name, self.get_sum(student), self.get_average(student))
    
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()

    def __gt__(self, value):
        return self.get_sum() > value.get_sum()

    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()

    def __le__(self, value):
        return self.get_sum() <= value.get_sum()

students = [
    Student("AAA", 11, 22, 33, 44), 
    Student("BAA", 22, 22, 33, 44), 
    Student("CAA", 33, 22, 33, 44), 
    Student("DAA", 44, 22, 33, 44), 
    Student("EAA", 55, 55, 33, 44), 

]

student_a = Student("AAA", 87, 98., 88, 95),
student_b = Student("BBB", 92, 98, 96, 98),

print("student_a == student_b = ", student_a == student_b)
print("student_a != student_b = ", student_a != student_b)
print("student_a > student_b = ", student_a > student_b)
print("student_a >= student_b = ", student_a >= student_b)
print("student_a < student_b = ", student_a < student_b)
print("student_a <= student_b = ", student_a <= student_b)