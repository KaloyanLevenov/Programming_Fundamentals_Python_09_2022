synonyms = {}
number_of_words = int(input())
for _ in range(number_of_words):
    word = input()
    synonym = input()
    if word not in synonyms.keys():
        synonyms[word] = synonym
    else:
        synonyms[word] += f", {synonym}"


for key in synonyms:
    print(f'{key} - {synonyms[key]}')
