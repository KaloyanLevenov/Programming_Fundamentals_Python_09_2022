import re

barcode_pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"
number_of_barcodes = int(input())
for _ in range(number_of_barcodes):
    barcode = input()
    matches = re.findall(barcode_pattern, barcode)
    if matches:
        for product in matches:
            digit_pattern = r"\d+"
            digits = re.findall(digit_pattern, product)
            if digits:
                product_group = "".join(digits)
            else:
                product_group = "00"

            print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")