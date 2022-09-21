number = float(input())
if number == 0:
    print(f'zero')
elif 0 < number < 1:
    print(f'small positive')
elif 1 < number < 1_000_000:
    print(f'positive')
elif number > 1_000_000:
    print(f'large positive')
else:
    if 0 < abs(number) < 1:
        print(f'small negative')
    elif 1 < abs(number) < 1_000_000:
        print(f'negative')
    elif abs(number) > 1_000_000:
        print(f'large negative')



