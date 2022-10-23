def index_check(index, house):
    index_is_valid = 0 <= index < len(house)
    if not index_is_valid:
        index = 0
    return index_is_valid, index


def love_delivery(house):
    job_is_done = True
    current_position_index = 0
    while True:
        command = input()
        if command == 'Love!':
            break
        action, length = command.split(' ')
        current_position_index += int(length)
        index_check(current_position_index, house)
        index_is_valid, index = index_check(current_position_index, house)
        if not index_is_valid:
            current_position_index = index

        if house[current_position_index] == 0:
            print(f"Place {current_position_index} already had Valentine's day.")
        else:
            house[current_position_index] -= 2
            if house[current_position_index] == 0:
                print(f"Place {current_position_index} has Valentine's day.")

    not_zero_lst = [love for love in house if love != 0]
    failed_places = len(not_zero_lst)
    if failed_places > 0:
        job_is_done = False
    if job_is_done:
        return print(f"Cupid's last position was {current_position_index}.\n\"Mission was successful.\"")
    else:
        return print(f"Cupid's last position was {current_position_index}.\nCupid has failed {failed_places} places.")


neighborhood = list(map(int, input().split('@')))
love_delivery(neighborhood)
