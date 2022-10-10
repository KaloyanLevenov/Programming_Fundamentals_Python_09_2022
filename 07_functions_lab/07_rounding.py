given_number_as_string = input()
list_of_numbers_as_float = list(map(float, given_number_as_string.split()))
list_of_rounded_numbers = []


def rounded_numbers_func(list_of_numbers):

    for index in range(len(list_of_numbers_as_float)):
        rounded_number = round(list_of_numbers_as_float[index])
        list_of_rounded_numbers.append(rounded_number)
    return list_of_rounded_numbers


print(rounded_numbers_func(list_of_numbers_as_float))
