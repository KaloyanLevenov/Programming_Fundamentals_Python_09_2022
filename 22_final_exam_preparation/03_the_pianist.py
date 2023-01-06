def add_func(piece, composer, key):
    if piece not in register.keys():
        register[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")


def remove_func(piece):
    if piece not in register.keys():
        print(f"Invalid operation! {piece} does not exist in the collection.")
    else:
        print(f"Successfully removed {piece}!")
        del register[piece]


def change_key_func(piece, new_key):
    if piece not in register.keys():
        print(f"Invalid operation! {piece} does not exist in the collection.")
    else:
        print(f"Changed the key of {piece} to {new_key}!")
        register[piece][1] = new_key


register = {}
number_of_pieces = int(input())
for number in range(number_of_pieces):
    data_input = input()
    piece, composer, key = data_input.split("|")
    register[piece] = [composer, key]

command = input()
while command != "Stop":
    command_list = command.split("|")
    action = command_list[0]
    if action == "Add":
        piece, composer, key = command_list[1], command_list[2], command_list[3]
        add_func(piece, composer, key)

    elif action == "Remove":
        piece = command_list[1]
        remove_func(piece)
    elif action == "ChangeKey":
        piece, new_key = command_list[1], command_list[2]
        change_key_func(piece, new_key)

    command = input()

for piece in register.keys():
    print(f"{piece} -> Composer: {register[piece][0]}, Key: {register[piece][1]}")
