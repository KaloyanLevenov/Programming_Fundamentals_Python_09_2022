odd_words = {}
odd_sequence_output = []
data = input()
data_lst = data.split(' ')
data_lst = [element.lower() for element in data_lst]
for data in data_lst:
    counter = data_lst.count(data)
    odd_words[data] = counter

for key in odd_words.keys():
    if odd_words[key] % 2 != 0:
        odd_sequence_output.append(key)

print(' '.join(odd_sequence_output))