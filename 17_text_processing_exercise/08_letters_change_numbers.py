game_input = input().split()

total = 0
for current_data in game_input:
    current_number = int(current_data[1:-1])
    previous_letter = current_data[0]
    last_letter = current_data[-1]
    if previous_letter.islower():
        total += current_number * (ord(previous_letter) - 96)

    elif previous_letter.isupper():
        total += current_number / (ord(previous_letter) - 64)
    if last_letter.isupper():
        total -= (ord(last_letter) - 64)
    elif last_letter.islower():
        total += (ord(last_letter) - 96)
print(f"{total:.2f}")
