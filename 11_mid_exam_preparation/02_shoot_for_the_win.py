def is_target_available(target_list):
    target_counter = 0

    while True:
        command = input()

        if command == "End":
            break
        else:
            target_index = int(command)

        if target_index <= (len(target_list) - 1):
            target_counter += 1
            current_target = target_list[target_index]
            target_list[target_index] = -1
            for index in range(len(target_list)):
                if target_list[index] == -1:
                    continue
                elif target_list[index] > current_target:
                    target_list[index] -= current_target
                else:
                    target_list[index] += current_target

    targets_as_str = [str(value) for value in target_list]
    print(f"Shot targets: {target_counter} -> {' '.join(targets_as_str)}")


targets = list(map(int, input().split(" ")))

is_target_available(targets)