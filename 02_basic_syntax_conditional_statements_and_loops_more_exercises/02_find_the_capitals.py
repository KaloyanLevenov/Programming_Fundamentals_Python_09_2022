given_string = input()
list_of_indices_for_capital_char_in_given_string = []
for index,every_char in enumerate(given_string):
    if every_char.isupper():
        list_of_indices_for_capital_char_in_given_string.append(index)
    else:
        pass
print(list_of_indices_for_capital_char_in_given_string)

