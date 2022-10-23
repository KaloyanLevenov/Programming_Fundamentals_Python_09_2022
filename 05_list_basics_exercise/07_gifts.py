names_of_the_gifts = input().split()
command = input()
while command != 'No Money':
    command_list = command.split()

    if command_list[0] == 'OutOfStock':
        if command_list[1] in names_of_the_gifts:
           for i in range(len(names_of_the_gifts)):
               if names_of_the_gifts[i] == command_list[1]:
                   names_of_the_gifts[i] = 'None'

    elif command_list[0] == 'Required':
        if int(command_list[2]) < len(names_of_the_gifts):
           names_of_the_gifts[int(command_list[2])] = command_list[1]

    elif command_list[0] == 'JustInCase':
        names_of_the_gifts[-1] = command_list[1]
    command = input()

for element in names_of_the_gifts:
    if element == 'None':
        names_of_the_gifts.remove('None')

print(' '.join(names_of_the_gifts))









