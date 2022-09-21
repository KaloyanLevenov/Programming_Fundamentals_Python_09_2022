number_of_strings = int(input())
string_is_pure = True

for each_string in range(number_of_strings):
    string = input()
    for each_letter in string:
        if each_letter == ',' or each_letter == '.' or each_letter == '_':
            string_is_pure = False
        else:
            pass
    if string_is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
        string_is_pure = True

