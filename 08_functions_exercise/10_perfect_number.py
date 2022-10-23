random_number = int(input())
divisor_sum = 0
# If the number is not even, surely it is not perfect
if random_number % 2 == 0:
    # Iterating through numbers to find all the divisors and sum them.
    # The biggest divisor of a perfect number is its half value
    for numbers in range(1, random_number // 2 + 1):
        if random_number % numbers == 0:
            divisor_sum += numbers

    if divisor_sum == random_number:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')

else:
    print('It\'s not so perfect.')
