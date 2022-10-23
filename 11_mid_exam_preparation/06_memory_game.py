def memory_game(elements, number_of_moves):
    you_won = True
    while True:
        command = input()

        if command == 'end':
            you_won = False
            break

        number_of_moves += 1

        first_index, second_index = map(int, command.split(' '))

        if first_index == second_index \
                or (not (0 <= first_index < len(elements) and 0 <= second_index < len(elements))):
            elements.insert(int(len(elements) / 2), str(number_of_moves * -1) + 'a')
            elements.insert(int(len(elements) / 2), str(number_of_moves * -1) + 'a')
            print("Invalid input! Adding additional elements to the board")

        elif elements[first_index] == elements[second_index]:
            current_element  = elements[first_index]
            print(f'Congrats! You have found matching elements - {elements[first_index]}!')

            elements.remove(current_element)
            elements.remove(current_element)

            if len(elements) == 0:
                you_won = True
                break

        elif elements[first_index] != elements[second_index]:
            print("Try again!")

    if you_won:
        return print(f"You have won in {number_of_moves} turns!")
    else:
        return print(f"Sorry you lose :(\n{' '.join(elements)}")


moves_counter = 0
sequence_of_elements = list(map(str, input().split(' ')))
memory_game(sequence_of_elements, moves_counter)
