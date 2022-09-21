number_of_all_orders = int(input())
total = 0
for each_order in range(number_of_all_orders):

     price_per_capsule = float(input())
     days = int(input())
     capsules_needed_per_day = int(input())

     if price_per_capsule < 0.01 or price_per_capsule > 100:
         continue
     elif days < 1 or days > 31:
         continue
     elif capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
         continue

     price_for_the_current_coffee_order = price_per_capsule * days * capsules_needed_per_day
     print(f"The price for the coffee is: ${price_for_the_current_coffee_order:.2f}")
     total += price_for_the_current_coffee_order
else:
    print(f"Total: ${total:.2f}")
