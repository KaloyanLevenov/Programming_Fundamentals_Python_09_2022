input_operator = input()
input_first_number = int(input())
input_second_number = int(input())


def add_operation(first_number, second_number):
    return first_number + second_number

def subtract_operation(first_number, second_number):
    return first_number - second_number

def multiply_operation(first_number, second_number):
    return first_number * second_number

def divide_operation(first_number, second_number):
    return int(first_number / second_number)


if input_operator == 'add':
    print(add_operation(input_first_number, input_second_number))
elif input_operator == 'subtract':
    print(subtract_operation(input_first_number, input_second_number))
elif input_operator == 'multiply':
    print(multiply_operation(input_first_number, input_second_number))
elif input_operator == 'divide':
    print(divide_operation(input_first_number, input_second_number))

