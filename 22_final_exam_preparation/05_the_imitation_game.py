def move_func(string,number):
    string = string[number:] + string[0:number]
    return string


encrypted_message = input()
decrypted_message = ""
while True:
    command = input()
    if command == "Decode":
        break
    command_list = command.split("|")
    action = command_list[0]
    if action == "Move":
        number_of_letters = int(command_list[1])
        decrypted_message = move_func(encrypted_message,number_of_letters)
    elif action == "Insert":
        index = int(command_list[1])
        value = command_list[2]
