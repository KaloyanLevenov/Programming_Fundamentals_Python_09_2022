# function that returns the sum of all even and all odd digits in a given number
def odd_and_even_summery(given_number):
    even_summery = 0
    odd_summery = 0

    for digit in given_number:

        if int(digit) % 2 == 0:
            even_summery += int(digit)
        else:
            odd_summery += int(digit)

    return even_summery, odd_summery

# input a given number as string
input_number =input()
# the return of the function as two new variables
sum_of_even_digits , sum_of_odd_digits = odd_and_even_summery(input_number)

print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")


