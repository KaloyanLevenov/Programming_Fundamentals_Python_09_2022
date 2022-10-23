# This program checks if the number is even = True or odd = False
def even_or_odd_func(number):
    if number % 2 == 0:
        return True
    else:
        return False


input_numbers_as_string = input()
# Converting the input string to list of integers
list_of_integers = list(map(int,input_numbers_as_string.split()))

# Here it puts every element of list_of_integers in the even_or_odd_func() and collects only the True (even integers)
list_of_even_integers = list(filter(even_or_odd_func, list_of_integers))

print(list_of_even_integers)


