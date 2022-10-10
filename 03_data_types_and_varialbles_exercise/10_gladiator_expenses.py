lost_fights_count = int(input())
helmet_price = int(input())

helmet_is_broken = False
sword_is_broken = False
shield_is_broken = False
shield_breaks_counter = 0
armor_is_broken = False

if lost_fights_count % 2 == 0:
    helmet_is_broken = True

if lost_fights_count % 3 == 0:
    sword_is_broken = True

    if lost_fights_count % 2 == 0:
        shield_is_broken = True
        shield_breaks_counter += 1

if shield_breaks_counter % 2 == 0:
    armor_is_broken = True



