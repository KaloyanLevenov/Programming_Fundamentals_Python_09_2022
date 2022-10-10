money_for_every_beggar = input().split(', ')
count_of_beggars = int(input())
money_for_every_beggar_as_int = [int(element) for element in money_for_every_beggar]
list_with_outcome = []
sum_for_current_begger = 0

for beggar in range(count_of_beggars):

    for current_beggar in range(beggar, len(money_for_every_beggar_as_int), count_of_beggars):

        sum_for_current_begger += money_for_every_beggar_as_int[current_beggar]
    list_with_outcome.append(sum_for_current_begger)

    sum_for_current_begger = 0

print(list_with_outcome)





