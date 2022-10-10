input_product = input()
input_quantity = int(input())
variable_price = 0


def calculate_order(quantity, price):
    if input_product == 'coffee':
        price = 1.50
    elif input_product == 'coke':
        price = 1.40
    elif input_product == 'water':
        price = 1.00
    elif input_product == 'snacks':
        price = 2.00

    return quantity * price


print(f'{calculate_order(input_quantity, variable_price):.2f}')


