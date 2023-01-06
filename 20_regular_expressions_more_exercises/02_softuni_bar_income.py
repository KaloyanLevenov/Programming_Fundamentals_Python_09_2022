import re

pattern = r"%([A-Z][a-z]+)%[^%\$\|\.\d]*<([A-Za-z0-9\_]+)>[^%\$\|\.\d]*\|(\d+)\|[^%\$\|\.\d]*(\d+[\.]?\d+)\$"
text = input()
total_income = 0
while text != "end of shift":
    matches = re.search(pattern, text)
    if matches:
        total_price_per_customer = 0

        customer, product, count, price = matches.groups()
        total_price_per_customer += float(price) * int(count)
        total_income += total_price_per_customer
        print(f"{customer}: {product} - {total_price_per_customer:.2f}")

    text = input()

print(f"Total income: {total_income:.2f}")