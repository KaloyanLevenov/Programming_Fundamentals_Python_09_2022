# Needs to be put a 'make up' on :)
sequence_of_integers = list(map(int, input().split(' ')))

top_five_numbers_as_list = sorted(list(sequence_of_integers),reverse=True)
output_list = []
average_value = sum(sequence_of_integers) / len(sequence_of_integers)
counter = 0
for number in range(len(top_five_numbers_as_list)):
    if top_five_numbers_as_list[number] > average_value:
        if counter >= 5:
            break
        counter += 1
        output_list.append(top_five_numbers_as_list[number])

output_list_as_string = [str(number) for number in output_list]

if len(output_list) > 0:
    print(' '.join(output_list_as_string))
else:
    print('No')
# top_five_num_func(sequence_of_integers)
