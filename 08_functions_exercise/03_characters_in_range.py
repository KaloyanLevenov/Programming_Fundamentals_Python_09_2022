# The following function receives two characters and returns a single string
# with all the characters in between them (according to the ASCII code)
def ascii_convertor(char_one, char_two):
    first_index = ord(char_one)
    second_index = ord(char_two)
    list_of_chars_in_between_char_one_and_char_two = []
    # iterating the unicodes between char_one and char_two
    for chars in range(first_index + 1, second_index):
        # list full of chars according to ascii
        list_of_chars_in_between_char_one_and_char_two.append(chr(chars))

    return list_of_chars_in_between_char_one_and_char_two


first_char = input()
second_char = input()
# output
print(" ".join(ascii_convertor(first_char, second_char)))
