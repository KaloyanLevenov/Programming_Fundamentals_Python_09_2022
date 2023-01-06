class Courses:
    course_dict = {}

    def __init__(self, course: str, student):
        self.course = course
        self.student = student

    def add_func(self):
        if self.course not in Courses.course_dict.keys():
            Courses.course_dict[self.course] = []
        Courses.course_dict[self.course].append(self.student)

    def print_func(self):
        for key, value in Courses.course_dict.items():
            print(f"{key}: {len(value)}")
            for student in value:
                print(f"-- {student}")


command = input()
while command != 'end':
    course_name, student_name = command.split(' : ')
    object = Courses(course_name, student_name)
    object.add_func()

    command = input()

object.print_func()

