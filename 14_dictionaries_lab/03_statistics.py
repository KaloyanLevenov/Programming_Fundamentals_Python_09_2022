bakery = {}
command = input()
while command != 'statistics':
    food, quantity = command.split(': ')
    if food not in bakery:
        bakery[food] = 0
    bakery[food] += int(quantity)
    command = input()
print('Products in stock:')
for food, quantity in bakery.items():
    print(f'- {food}: {quantity}')
print(f'Total Products: {len(bakery.keys())}')
print(f'Total Quantity: {sum(bakery.values())}')