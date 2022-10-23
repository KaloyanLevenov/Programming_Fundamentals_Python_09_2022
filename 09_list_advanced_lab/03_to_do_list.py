to_do_list = []

while True:
    command = input()

    if command == 'End':
        break
    # Converting the command str into list splitted by '-'
    command_list = command.split('-')
    # Priority is always in index 0
    priority = int(command_list[0])
    # Task is always on index 1
    task = command_list[1]
    # Here we make a list full of tuples
    to_do_list.append((priority, task))
# Comprehension - new list with elements on index 1 in every tuple in our to_do_list
sorted_to_do_list = [to_do[1] for to_do in sorted(to_do_list)]

print(sorted_to_do_list)
