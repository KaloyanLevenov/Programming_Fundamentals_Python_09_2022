def manipulating_the_targets(targets):
    while True:
        command = input()
        if command == 'End':
            break
        command_list = list(command.split(' '))

        action = command_list[0]
        index = int(command_list[1])
        # pvr stands for POWER or VALUE or RADIUS, because the 3 of them are ints
        pvr = int(command_list[2])

        if action == 'Shoot' and 0 <= index < len(targets):
            if targets[index] - pvr <= 0:
                targets.remove(targets[index])
            else:
                targets[index] -= pvr

        if action == 'Add':
            if 0 <= index < len(targets):
                targets.insert(index, pvr)
            else:
                print("Invalid placement!")

        if action == 'Strike':
            strike_index_is_valid = (index - pvr) > 0 and (index + pvr) < len(targets)
            if strike_index_is_valid:
                left_index = index - pvr
                right_index = index + pvr
                targets = [targets[i] for i in range(len(targets)) if i < left_index or i > right_index]
            else:
                print("Strike missed!")

    print('|'.join(str(target) for target in targets))


sequence_of_targets = list(map(int, input().split(' ')))

manipulating_the_targets(sequence_of_targets)