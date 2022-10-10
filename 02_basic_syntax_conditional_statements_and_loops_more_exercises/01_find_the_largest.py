given_number = int(input())
list = []
for every_digit in str(given_number):
    list.append(every_digit)
    list.sort(reverse=True)
print(''.join(list))



