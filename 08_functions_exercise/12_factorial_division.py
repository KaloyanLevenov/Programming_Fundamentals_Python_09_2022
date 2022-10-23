# Function that calculates factorials
def factorial(number):
    total_sum = 1
    for i in range(1, number + 1):
        total_sum *= i
    return total_sum


first_integer = int(input())
second_integer = int(input())

first_factorial = factorial(first_integer)
second_factorial = factorial(second_integer)
division = first_factorial / second_factorial
print(f'{division:.2f}')