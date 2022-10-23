wagons = int(input())
# every 0 of the train represents every empty wagon at the start
train = [0] * wagons

while True:
    command = input()

    if command == 'End':
        break
# Converting the command as str into list so it could be easy to iterate through the elements
    command_list = command.split(' ')

    if command_list[0] == 'add':
        train[-1] += int(command_list[1])

    elif command_list[0] == 'insert':
        current_wagon = int(command_list[1])
        train[current_wagon] += int(command_list[2])

    elif command_list[0] == 'leave':
        current_wagon = int(command_list[1])
        train[current_wagon] -= int(command_list[2])

print(train)
