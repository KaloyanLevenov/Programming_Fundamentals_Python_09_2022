import re

pattern = r"@([A-Za-z]+)(?:[^@\,\-!:>]*):(\d+)(?:[^@\,\-!:>]*)?!([A|D])!(?:[^@\,\-!:>]*)*->(\d+)"
letter_list = ["s", "t", "a", "r"]
attacked_planets = []
destroyed_planets = []
number_of_messages = int(input())
for message in range(number_of_messages):
    encrypted_message = input()
    decryption_key = 0
    decrypted_message = ""
    for character in encrypted_message:
        if character.lower() in letter_list:
            decryption_key += 1
    for index in range(len(encrypted_message)):
        decrypted_letter = chr(ord(encrypted_message[index]) - decryption_key)
        decrypted_message += decrypted_letter
    matches = re.search(pattern, decrypted_message)
    if matches:
        if matches.group(3) == "A":
            attacked_planets.append(matches.group(1))
        else:
            destroyed_planets.append(matches.group(1))

if attacked_planets:
    print(f"Attacked planets: {len(attacked_planets)}")
    for planets in sorted(attacked_planets):
        print(f"-> {planets}")
else:
    print(f"Attacked planets: 0")

if destroyed_planets:
    print(f"Destroyed planets: {len(destroyed_planets)}")
    for planets in sorted(destroyed_planets):
        print(f"-> {planets}")
else:
    print(f"Destroyed planets: 0")
