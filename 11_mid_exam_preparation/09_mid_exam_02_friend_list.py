def blacklist_func(friends, name):
    if name not in friends:
        print(f"{name} was not found.")
    else:
        print(f"{name} was blacklisted.")
        friends[friends.index(name)] = 'Blacklisted'

    return friends


def error_func(friends, index):
    if 0 <= index < len(friends) and friends[index] != 'Blacklisted' and friends[index] != 'Lost':
        print(f'{friends[index]} was lost due to an error.')
        friends[index] = 'Lost'

    return friends


def change_func(friends, index, new_name):
    if 0 <= index < len(friends):
        print(f"{friends[index]} changed his username to {new_name}.")
        friends[index] = new_name

    return friends


friends_list = list(map(str, input().split(', ')))

while True:
    command = input()
    if command == "Report":
        break

    command_list = command.split(' ')
    action = command_list[0]

    if action == 'Blacklist':
        name = command_list[1]
        friends_list = blacklist_func(friends_list, name)

    if action == 'Error':
        index = int(command_list[1])
        friends_list = error_func(friends_list, index)

    if action == 'Change':
        index = int(command_list[1])
        new_name = command_list[2]
        friends_list = change_func(friends_list, index, new_name)


number_of_blacklisted_names = friends_list.count('Blacklisted')
number_of_lost_names = friends_list.count('Lost')

print(f"Blacklisted names: {number_of_blacklisted_names}")
print(f"Lost names: {number_of_lost_names}")
print(' '.join(friends_list))