quantity_of_decorations = int(input())
days_left_until_christmas = int(input())
budget = 0
spirit_points = 0
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
for day in range(1,days_left_until_christmas+1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        budget += ornament_set * quantity_of_decorations
        spirit_points += 5
    if day % 3 == 0:
        budget += tree_skirt * quantity_of_decorations + tree_garland * quantity_of_decorations
        spirit_points += 3 + 10
    if day % 5 == 0:
        budget += tree_lights * quantity_of_decorations
        spirit_points += 17
        if day % 3 == 0:
            spirit_points += 30
    if day % 10 == 0:
        spirit_points -= 20
        budget += tree_skirt + tree_garland + tree_lights

if days_left_until_christmas % 10 == 0:
    spirit_points -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit_points}")



