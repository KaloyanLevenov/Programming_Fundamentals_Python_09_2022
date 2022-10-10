current_year = int(input()) + 1
set_of_unique_digits =set()
happy_year_is_valid = False
next_happy_year = 0
while not happy_year_is_valid:
    for each_digit in str(current_year):
        set_of_unique_digits.add(each_digit)

    if len(set_of_unique_digits) == len(str(current_year)):
        happy_year_is_valid = True
        next_happy_year = current_year

    else:
        current_year += 1
    set_of_unique_digits = set()

if happy_year_is_valid:
    print(next_happy_year)