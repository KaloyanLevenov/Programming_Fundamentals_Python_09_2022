register: dict = {}
submissions = {}


def add_data(student, language, points):
    if language not in register.keys():
        register[language] = {}
        register[language][student] = [True]
        register[language][student].append(points)

    else:
        if student not in register[language].keys():
            register[language][student] = [True]
            register[language][student].append(points)


        elif student in register[language].keys():
            register[language][student].append(points)

    if language not in submissions.keys():
        submissions[language] = 1
    else:
        submissions[language] += 1


def banned_student_func(banned_student):
    for languange in register.keys():
        if banned_student in register[languange].keys():
            register[languange][banned_student][0] = False


def print_func(register):
    print("Results:")
    for language in register.keys():
        for student in register[language].keys():
            if register[language][student][0] == True:
                print(f"{student} | {max(register[language][student][1::])}")

    print("Submissions:")
    for key, value in submissions.items():
        print(f"{key} - {value}")


command = input()
while command != "exam finished":
    command_list = command.split("-")

    if "banned" in command_list:
        banned_student_name = command_list[0]
        banned_student_func(banned_student_name)

    elif "banned" not in command_list:
        student_name = command_list[0]
        language_name = command_list[1]
        student_points = int(command_list[2])
        add_data(student_name, language_name, student_points)

    command = input()

print_func(register)
