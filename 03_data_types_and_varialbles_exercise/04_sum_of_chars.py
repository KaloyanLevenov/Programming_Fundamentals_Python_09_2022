number_of_characters = int(input())
summery_in_ascii = 0
for _ in range(number_of_characters):
    current_character = input()
    summery_in_ascii += ord(current_character)

print(f"The sum equals: {summery_in_ascii}")

