given_string = input()
list_with_animals = given_string.split(', ')
if list_with_animals[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    for index, animal in enumerate(list_with_animals):
        if animal == 'wolf':
            sheep_number_to_be_eaten = len(list_with_animals) - (index + 1)
            print(f'Oi! Sheep number {sheep_number_to_be_eaten}! You are about to be eaten by a wolf!')
