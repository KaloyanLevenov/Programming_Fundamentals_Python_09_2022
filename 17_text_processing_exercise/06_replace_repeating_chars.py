string = input()
new_string = ''
last_character = ''
for character in string:
    if character != last_character:
        new_string += character
        last_character = character
print(new_string)


