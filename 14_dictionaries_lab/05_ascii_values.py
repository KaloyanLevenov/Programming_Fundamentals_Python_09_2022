data = input()
list_of_char = data.split(', ')
ascii_dictionary = {char: ord(char) for char in list_of_char}
print(ascii_dictionary)
