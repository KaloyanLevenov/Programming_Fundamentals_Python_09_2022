string_to_explode = input()
exploded_text = ''
power = 0
for index in range(len(string_to_explode)):
    current_letter = string_to_explode[index]
    if power > 0 and string_to_explode[index] != ">":
        power -= 1
    elif string_to_explode[index] == ">":
        exploded_text += string_to_explode[index]
        power += int(string_to_explode[index + 1])
    else:exploded_text += string_to_explode[index]

print(exploded_text)
