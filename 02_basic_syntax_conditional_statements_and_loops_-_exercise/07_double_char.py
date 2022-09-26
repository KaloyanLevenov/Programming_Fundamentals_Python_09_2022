
while True:
    string = input()

    if string == 'End':
        break
    if string == 'SoftUni':
        continue

    for each_letter in string:
        print(each_letter * 2, end="")
    print()



