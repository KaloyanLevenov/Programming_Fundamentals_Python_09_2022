string = input()
rage_message = ''
previous_character = ''
power = 0
unique_symbols = []
for index in range(len(string)):
    if string[index].isdigit():
        power += int(string[index])

    if not string[index].isdigit():
        if string[index - 1].isdigit():
            rage_message += previous_character * power
            previous_character = ''
        previous_character += string[index].upper()
        if string[index].upper() not in unique_symbols:
            unique_symbols.append(string[index].upper())

print(f"Unique symbols used: {len(unique_symbols)}")
print(rage_message)
