class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa= gpa
        self.is_on_probation = is_on_probation


student = Student("jhon", "Dev", 3.4, False)

print(student)