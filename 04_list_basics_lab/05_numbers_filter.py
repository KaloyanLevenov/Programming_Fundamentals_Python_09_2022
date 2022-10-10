number_of_integers = int(input())
list_with_all_the_numbers = []
list_with_numbers_after_command = []

command_even = 'even'
command_odd = 'odd'
command_negative = 'negative'
command_positive = 'positive'

for every_number in range(number_of_integers):

    current_number = int(input())
    list_with_all_the_numbers.append(current_number)

command_input = input()

for elements in list_with_all_the_numbers:
    if command_input == command_even and elements % 2 == 0:
        list_with_numbers_after_command.append(elements)

    elif command_input == command_even and elements == 0:
        list_with_numbers_after_command.append(elements)

    elif command_input == command_odd and elements % 2 != 0:
        list_with_numbers_after_command.append(elements)

    elif command_input == command_positive and elements >= 0:
        list_with_numbers_after_command.append(elements)

    elif command_input == command_positive and elements == 0:
        list_with_numbers_after_command.append(elements)

    elif command_input == command_negative and elements < 0:
        list_with_numbers_after_command.append(elements)

print(list_with_numbers_after_command)




