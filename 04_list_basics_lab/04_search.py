number_of_strings = int(input())
key_word = input()
list_for_every_string = []
list_only_for_key_strings = []
for each_number in range(1, number_of_strings + 1):

    random_strings = input()
    list_for_every_string.append(random_strings)

    if key_word in random_strings:
        list_only_for_key_strings.append(random_strings)

print(list_for_every_string)
print(list_only_for_key_strings)




