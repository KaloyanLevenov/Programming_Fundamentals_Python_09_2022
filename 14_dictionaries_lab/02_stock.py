command_food = input()
food_list = command_food.split(' ')
stock = {food_list[index]:food_list[index+1] for index in range(len(food_list)) if index % 2 == 0}
searched_food_command = input()
searched_food_list = searched_food_command.split(' ')
for product in searched_food_list:
    if product in stock.keys():
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
