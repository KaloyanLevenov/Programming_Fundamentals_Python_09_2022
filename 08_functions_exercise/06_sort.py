input_numbers_as_string = input()
# Converting the input string to list of integers
list_of_integers = list(map(int,input_numbers_as_string.split()))

# This is a new list from ascending ordered using the sorted() function
list_of_sorted_integers = sorted(list_of_integers)

print(list_of_sorted_integers)


