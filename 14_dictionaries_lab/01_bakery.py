# bread 10 butter 4 sugar 9 jam 12
bakery = {}
command = input()
food_list = command.split(' ')
for index in range(0,len(food_list),2):
    food = food_list[index]
    quantities = food_list[index + 1]
    # if food not in bakery:
    #     bakery[food] = ''
    bakery[food] = int(quantities)

print(bakery)