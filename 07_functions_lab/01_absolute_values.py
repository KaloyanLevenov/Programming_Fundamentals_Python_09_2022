# Here you input string of numbers separated by space
input_integers = input()

# Here you transform the input into list of floats separated by one space
list_of_floats = list(map(float, input_integers.split()))

# This is the list where you will add the abs values of the input floats
list_of_abs_floats = []



def abs_value(number):
    abs_number = abs(number)
    return abs_number


# In this loop we iterate through the list of floats to get the absolute value of each number
for numbers in list_of_floats:
    list_of_abs_floats.append(abs_value(numbers))

print(list_of_abs_floats)