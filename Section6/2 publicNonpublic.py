class Student:
    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        self._age = age
        self.gpa = gpa


my_student = Student("173s", "Rony", 22, 3.78)
print(my_student._age)
