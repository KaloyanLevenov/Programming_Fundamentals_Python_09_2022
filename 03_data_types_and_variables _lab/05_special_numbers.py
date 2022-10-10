input_number = int(input())
for each_number in range(1, input_number + 1):
    sum_int_each_digit = 0
    for index, digit in enumerate(str(each_number)):
        sum_int_each_digit += int(digit)
    if (sum_int_each_digit == 5) or (sum_int_each_digit == 7) or (sum_int_each_digit == 11):
        print(f'{each_number} -> True')
    else:
        print(f'{each_number} -> False')
    sum_int_each_digit = 0


