string = input()
coffee_counter = 0
list = ['coding', 'dog', 'cat', 'movie']
list_upper = []
for words in list:
    list_upper.append(words.upper())

while string != 'END':
    if string.islower():
        if string in list:
            coffee_counter += 1

    elif string.isupper():
        if string in list_upper:
            coffee_counter += 2
    else:
        continue

    string = input()
else:
    if coffee_counter > 5:
        print('You need extra sleep')
    else:
        print(coffee_counter)




