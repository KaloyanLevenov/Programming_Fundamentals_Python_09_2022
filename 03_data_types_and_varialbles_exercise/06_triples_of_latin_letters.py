current_number = int(input())
for first_letter in range(current_number):
    for second_letter in range(current_number):
        for third_letter in range(current_number):
            print(f'{chr(97 + first_letter)}{chr(97 + second_letter)}{chr(97 + third_letter)}')
