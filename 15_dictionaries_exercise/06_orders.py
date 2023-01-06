products_info = {}
total_price = 0
order = input()
while order != 'buy':
    order = order.split(' ')
    product = order[0]
    price = float(order[1])
    quantity = int(order[2])
    if product not in products_info.keys():
        products_info[product] = []
        products_info[product].extend([price, quantity])
    elif product in products_info.keys():
        products_info[product][0] = price
        products_info[product][1] += quantity

    order = input()

for product, price_list in products_info.items():
    total_price = price_list[0] * price_list[1]
    print(f"{product} -> {total_price:.2f}")
