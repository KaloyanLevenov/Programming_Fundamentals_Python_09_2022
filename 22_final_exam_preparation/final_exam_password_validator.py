def make_upper_func(index, text):
    upper_letter = text[index].upper()
    text = text[0:index] + upper_letter + text[index + 1:]
    print(text)
    return text


def make_lower_func(index, text):
    lower_letter = text[index].lower()
    text = text[0:index] + lower_letter + text[index + 1:]
    print(text)
    return text


def insert_func(index, char, text):
    text = text[0:index] + char + text[index:]
    print(text)
    return text


def replace_func(value, char, text):
    char_value = ord(char)
    new_char_value = char_value + value
    new_char = chr(new_char_value)
    while char in text:
        text = text.replace(char, new_char)
    print(text)
    return text


def validation_func(text):
    if len(text) < 8:
        print("Password must be at least 8 characters long!")
    for char in text:
        if (not char.isalnum()) and char != "_":
            print("Password must consist only of letters, digits and _!")
    upper = False
    for char in text:
        if char.isupper():
            upper = True
            break
    if not upper:
        print("Password must consist at least one uppercase letter!")
    lower = False
    for char in text:
        if char.islower():
            lower = True
            break
    if not lower:
        print("Password must consist at least one lowercase letter!")
    digit = False
    for char in text:
        if char.isdigit():
            digit = True
            break
    if not digit:
        print("Password must consist at least one digit!")


password = input()
while True:
    command = input()
    if command == "Complete":
        break
    command_list = command.split(" ")
    if "Upper" in command_list:
        index = int(command_list[2])
        password = make_upper_func(index, password)
    elif "Lower" in command_list:
        index = int(command_list[2])
        password = make_lower_func(index, password)
    elif "Insert" in command_list:
        index = int(command_list[1])
        char = command_list[2]
        if 0 <= index <= len(password):
            password = insert_func(index, char, password)
    elif "Replace" in command_list:
        value = int(command_list[2])
        char = command_list[1]
        if char in password:
            password = replace_func(value, char, password)
    elif "Validation" in command_list:
        validation_func(password)
