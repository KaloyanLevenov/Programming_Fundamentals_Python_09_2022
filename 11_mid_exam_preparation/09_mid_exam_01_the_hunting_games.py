days_of_adventure = int(input())
count_of_the_players = int(input())
group_energy = float(input())
water_for_one_person = float(input())
food_for_one_person = float(input())
food_for_all = food_for_one_person * count_of_the_players * days_of_adventure
water_for_all = water_for_one_person * count_of_the_players * days_of_adventure
for every_day in range(1, days_of_adventure + 1):

    energy_loss = float(input())
    group_energy -= energy_loss
    if group_energy <= 0:
        break

    if every_day % 2 == 0:
        group_energy *= 1.05
        water_for_all -= water_for_all * 0.30

    if every_day % 3 == 0:
        food_for_all -= (food_for_all / count_of_the_players)
        group_energy *= 1.10


if group_energy > 0:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food_for_all:.2f} food and {water_for_all:.2f} water.")
