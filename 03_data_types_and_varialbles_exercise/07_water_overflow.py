how_many_times_will_pour_water_in_the_water_tank = int(input())
water_tank_capacity = 0

for each_time_pouring in range(how_many_times_will_pour_water_in_the_water_tank):
    liters_to_pour = int(input())

    if (water_tank_capacity + liters_to_pour ) > 255:
        print('Insufficient capacity!')
        continue

    water_tank_capacity += liters_to_pour


else:
    print(water_tank_capacity)



