phonebook = {}
input_data = input()
while '-' in input_data:
    name, number = input_data.split('-')
    phonebook[name] = number
    input_data = input()

number_of_searches = int(input_data)
for _ in range(number_of_searches):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")


