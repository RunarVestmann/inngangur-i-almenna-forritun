class Student:
    def __init__(self, name):
        self.name = name
        self.school = "Háskólinn á Akureyri"

student = Student("Bob")
print(student.name)
print(student.school)