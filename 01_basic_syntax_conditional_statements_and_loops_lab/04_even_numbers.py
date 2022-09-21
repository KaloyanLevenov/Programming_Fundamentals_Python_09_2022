number_of_iterations = int(input())
for _ in range(number_of_iterations):
    current_number = int(input())
    if current_number % 2 !=0:
        print(f"{current_number} is odd!" )
        break
else:
    print(f"All numbers are even.")