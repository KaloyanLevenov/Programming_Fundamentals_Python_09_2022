# Function that displays how much is loaded out of 100
def loading_bar(number):
    if number == 100:
        return f'100% Complete!\n[%%%%%%%%%%]'
    else:
        return f'{number}% [{"%" * (number // 10)}{"." * (10 - number // 10)}]\nStill loading...'

# percentage of loading 
single_integer_number = int(input())

print(loading_bar(single_integer_number))
