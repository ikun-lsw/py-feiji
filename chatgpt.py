class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def update_student(self, student, new_name=None, new_age=None, new_grade=None):
        if new_name:
            student.name = new_name
        if new_age:
            student.age = new_age
        if new_grade:
            student.grade = new_grade

    def get_all_students(self):
        for student in self.students:
            print(student)


sms = StudentManagementSystem()

student1 = Student("John", 20, "A")
student2 = Student("Jane", 19, "B")
student3 = Student("Jim", 21, "C")

sms.add_student(student1)
sms.add_student(student2)
sms.add_student(student3)

sms.get_all_students()

student = sms.find_student("Jane")
if student:
    sms.update_student(student, new_name="Janet", new_age=20, new_grade="A")
    print("\nAfter updating:")
    sms.get_all_students()
else:
    print("Student not found.")
