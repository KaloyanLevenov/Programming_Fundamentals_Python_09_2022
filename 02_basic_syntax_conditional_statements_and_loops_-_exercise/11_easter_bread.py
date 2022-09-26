budget = float(input())
one_kilo_flour_price = float(input())
pack_of_eggs_price = one_kilo_flour_price * 0.75
one_liter_milk_price = one_kilo_flour_price * 1.25

one_loaf_price = pack_of_eggs_price + one_kilo_flour_price + one_liter_milk_price * 0.250
loaf_counter = 0
coloured_eggs_counter = 0

while budget > one_loaf_price:
    loaf_counter += 1
    coloured_eggs_counter += 3
    budget -= one_loaf_price

    if loaf_counter % 3 == 0:
        coloured_eggs_counter -= loaf_counter - 2

print(f'You made {loaf_counter} loaves of Easter bread! Now you have {coloured_eggs_counter} eggs and {budget:.2f}BGN left.')