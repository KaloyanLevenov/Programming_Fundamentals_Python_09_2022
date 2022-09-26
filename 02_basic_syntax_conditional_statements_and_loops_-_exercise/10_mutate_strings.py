first_string = input()
second_string = input()
last_string = first_string

for each_symbol in range(len(first_string)):
    left_side = second_string[0:each_symbol+1]
    right_side = first_string[each_symbol+1:]
    current_string = left_side+right_side
    if current_string != last_string:

        print(current_string)
    last_string = current_string




