input_integer = input()
list_of_integers = list(map(int, input_integer.split()))
numbers_to_remove = int(input())
for numbers in range(numbers_to_remove):
    list_of_integers.remove(min(list_of_integers))
integers_as_string = ', '.join(map(str,list_of_integers))
print(integers_as_string)