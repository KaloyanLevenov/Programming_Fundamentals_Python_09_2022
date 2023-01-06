import re

pattern = r">>([A-Za-z]+)<<(\d+[\.]?\d*)!(\d+)"
bought_furniture = []
total_price = 0
command = input()
while command != "Purchase":
    matches = re.search(pattern,command)
    if matches:
        furniture_name, price, quantity = matches.groups()
        bought_furniture.append(furniture_name)
        total_price += float(price) * int(quantity)
    command = input()

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")