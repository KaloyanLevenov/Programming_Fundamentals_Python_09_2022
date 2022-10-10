from math import floor
group_members = int(input())
days_of_the_adventure = int(input())
coins = 0

for every_day in range(1, days_of_the_adventure + 1):
    coins += 50
    coins -= group_members * 2

    if every_day % 10 == 0:
        group_members -= 2
        if group_members < 0:
            group_members = 1

    if every_day % 15 == 0:
        group_members += 5

    if every_day % 3 == 0:
        coins -= group_members * 3

    if every_day % 5 == 0:
        coins += group_members * 20

        if every_day % 3 == 0:
            coins -= group_members * 2


print(f"{group_members} companions received {floor(coins/group_members)} coins each.")

