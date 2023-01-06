def insert_space(string, index, space=" "):
    index_as_int = int(index)
    new_string = string[:index_as_int] + space + string[index_as_int:]
    print(new_string)
    return new_string


def reverse(string, substring):
    if not substring in string:
        print("error")
        return string
    else:
        string = string.replace(substring, "",1)
        reversed_substring = substring[::-1]
        string = string + reversed_substring
        print(string)
        return string


def change_all(string, substring, replacement):
    if not substring in string:
        return string
    else:
        while substring in string:
            string = string.replace(substring, replacement)
        print(string)
        return string


concealed_message = input()
while True:
    command = input()
    if command == "Reveal":
        break
    instructions = command.split(":|:")
    action = instructions[0]
    if "InsertSpace" == action:
        index = instructions[1]
        concealed_message = insert_space(concealed_message, index)
    elif "Reverse" == action:
        substring = instructions[1]
        concealed_message = reverse(concealed_message, substring)
    elif "ChangeAll" == action:
        substring, replacement = instructions[1],instructions[2]
        concealed_message = change_all(concealed_message, substring, replacement)

print(f"You have a new text message: {concealed_message}")
