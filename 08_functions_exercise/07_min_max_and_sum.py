# Function that gives the smallest number
def smallest(numbers):
    smallest_number = min(numbers)
    return smallest_number


# Function that gives the biggest number
def biggest(numbers):
    biggest_number = max(numbers)
    return biggest_number


# Function that gives the sum of all numbers
def sum_of_all(numbers):
    total = sum(numbers)
    return total


input_numbers_as_string = input()
# Converting the input string to list of integers
list_of_integers = list(map(int, input_numbers_as_string.split()))


# The results of the 3 functions as a variables
minimum_number = smallest(list_of_integers)
maximum_number = biggest(list_of_integers)
sum_of_all_numbers = sum_of_all(list_of_integers)


print(f"The minimum number is {minimum_number}\nThe maximum number is {maximum_number}\nThe sum number is: {sum_of_all_numbers}")

