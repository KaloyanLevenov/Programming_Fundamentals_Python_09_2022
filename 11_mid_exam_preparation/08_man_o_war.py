def fire_func(actions, war_ship):
    index_section, damage = int(actions[1]), int(actions[2])
    you_won_the_game = False
    if not 0 <= index_section < len(war_ship):
        return you_won_the_game, war_ship
    else:
        war_ship[index_section] -= damage
        if war_ship[index_section] <= 0:
            you_won_the_game = True
            return you_won_the_game, war_ship
        else:
            return you_won_the_game, war_ship


def defend_func(actions, pirate_ship):
    start_index, end_index, damage = int(actions[1]), int(actions[2]), int(actions[3])
    you_lost_the_game = False
    if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
        for section in range(len(pirate_ship)):
            if start_index <= section <= end_index:
                pirate_ship[section] -= damage
                if pirate_ship[section] <= 0:
                    you_lost_the_game = True
                    return you_lost_the_game
        return you_lost_the_game


def repair_func(actions, pirate_ship, max_health):
    index_section, health = int(actions[1]), int(actions[2])
    if not 0 <= index_section < len(pirate_ship):
        return pirate_ship
    else:
        if pirate_ship[index_section] + health > max_health:
            pirate_ship[index_section] = max_health
        else:
            pirate_ship[index_section] += health
    return pirate_ship


def status_func(pirate_ship, max_health):
    red_line = 0.20 * max_health
    repair_soon = [sections for sections in pirate_ship if sections < red_line]
    count_of_sections_for_repair = len(repair_soon)
    return count_of_sections_for_repair


pirate_ship_status = list(map(int, input().split('>')))
war_ship_status = list(map(int, input().split('>')))
section_capacity = int(input())

while True:
    command = input()
    if command == 'Retire':
        stalemate = True
        break
    action = command.split(' ')[0]

    if action == 'Fire':

        you_win_the_game, war_ship_status = fire_func(command.split(' '), war_ship_status)
        if you_win_the_game:
            print("You won! The enemy ship has sunken.")
            stalemate = False
            break
    elif action == 'Defend':
        game_is_lost = defend_func(command.split(' '), pirate_ship_status)
        if game_is_lost:
            print("You lost! The pirate ship has sunken.")
            stalemate = False
            break
    elif action == 'Repair':
        pirate_ship_status = repair_func(command.split(' '), pirate_ship_status, section_capacity)

    elif action == 'Status':
        sections_for_repair = status_func(pirate_ship_status, section_capacity)
        print(f"{sections_for_repair} sections need repair.")

if stalemate:
    print(f"Pirate ship status: {sum(pirate_ship_status)}\nWarship status: {sum(war_ship_status)}")
