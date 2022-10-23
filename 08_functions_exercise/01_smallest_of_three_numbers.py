# This function gets the smallest number of the list
def smallest_number_func(list_of_numbers):
    smallest_number = min(list_of_numbers)
    return smallest_number


# Here I enter my 3 integers
first_number = int(input())
second_number = int(input())
third_number = int(input())
# Here I put them in a list of integers
list_of_ints = [first_number, second_number, third_number]
# Printing the smallest number
print(smallest_number_func(list_of_ints))
