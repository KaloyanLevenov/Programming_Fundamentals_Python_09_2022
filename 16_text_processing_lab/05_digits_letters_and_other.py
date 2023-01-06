string = input()
print(''.join(char for char in string if char.isdigit()))
print(''.join(char for char in string if char.isalpha()))
print(''.join(char for char in string if (not char.isalpha() and not char.isdigit())))
