students = {}
student_info = input()

while ":" in student_info:
    name, student_number, course = student_info.split(':')
    if course not in students.keys():
        students[course] = []
    students[course] += [f'{name} - {student_number}']
    student_info = input()
searched_course = student_info.replace('_',' ')

for students in students[searched_course]:
    print(students)
