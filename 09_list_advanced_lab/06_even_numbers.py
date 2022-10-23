numbers_as_string = input()
numbers_as_list_of_integers = list(map(int, numbers_as_string.split(', ')))
# Weird comprehension for getting the indices of even numbers in random list of numbers
indices_of_even_numbers = [index for index in range(len(numbers_as_list_of_integers)) \
                           if numbers_as_list_of_integers[index] % 2 == 0]

# Simplified solution of the upper crazy comprehension

# for index in range(len(numbers_as_list_of_integers)):
#     if numbers_as_list_of_integers[index] % 2 == 0:
#         indices_of_even_numbers.append(index)


print(indices_of_even_numbers)
