text = input()
encrypted_text = ''
for character in text:
    ascii_code = ord(character)
    encrypted_character = chr(ascii_code + 3)
    encrypted_text += encrypted_character
print(encrypted_text)