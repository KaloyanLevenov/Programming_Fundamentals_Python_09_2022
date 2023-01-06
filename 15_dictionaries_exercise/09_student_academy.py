class Student:
    academy = {}

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def add_func(self):
        if self.name not in Student.academy:
            Student.academy[self.name] = []
        Student.academy[self.name].append(self.grade)

    def average_grade_func(self):
        for student in Student.academy.keys():
            average_grade = sum(Student.academy[student]) / len(Student.academy[student])
            Student.academy[student].append(average_grade)

    def print_func(self):
        for student, average_grade in Student.academy.items():
            if Student.academy[student][-1] >= 4.50:
                print(f"{student} -> {Student.academy[student][-1]:.2f}")


number_of_rows = int(input())
for student in range(number_of_rows):
    student_name = input()
    student_grade = float(input())
    object = Student(student_name, student_grade)
    object.add_func()

object.average_grade_func()
object.print_func()

