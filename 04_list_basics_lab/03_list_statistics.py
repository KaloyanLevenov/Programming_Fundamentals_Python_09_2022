random_number = int(input())
count_of_positives = 0
positive_list = []
negative_list = []

for each_number in range(random_number):
    current_number = int(input())
    if current_number < 0:
        negative_list.append(current_number)
    else:
        positive_list.append(current_number)
        count_of_positives += 1

print(positive_list)
print(negative_list)
print(f'Count of positives: {count_of_positives}')
print(f'Sum of negatives: {sum(negative_list)}')

