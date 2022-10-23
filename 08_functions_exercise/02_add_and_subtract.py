# sum_numbers() that returns the sum of the first two integers
def sum_numbers(number_one, number_two):
    return number_one + number_two


# •	subtract() that returns the difference between the returned
# result of the first function, sum_numbers(), and the third integer
def subtract(sum_number_one_and_two, number_three):
    return sum_number_one_and_two - number_three


# add_and_subtract() wraps the two upper functions which will receive the three numbers as parameters.
def add_and_subtract(number_one, number_two, number_three):
    sum_of_first_and_second = sum_numbers(number_one, number_two)
    result = subtract(sum_of_first_and_second, number_three)

    return result

# My 3 input numbers
first_number = int(input())
second_number = int(input())
third_number = int(input())


print(add_and_subtract(first_number,second_number,third_number))