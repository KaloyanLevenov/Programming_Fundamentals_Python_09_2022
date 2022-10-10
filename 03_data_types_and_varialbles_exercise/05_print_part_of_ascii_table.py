first_index = int(input())
last_index = int(input())
for every_index in range(first_index, last_index + 1):
    ascii_char = chr(every_index)
    print(ascii_char, end=' ')