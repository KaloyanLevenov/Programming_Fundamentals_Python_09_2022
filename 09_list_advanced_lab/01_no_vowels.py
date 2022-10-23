# Put a text with vowels
text = input()
# list with vowels we should remove
vowels_list = ['a', 'o', 'u', 'e', 'i']
# list comprehension that creates a new list with the letters of text with no vowels
no_vowels = [letter for letter in text if not letter.lower() in vowels_list ]
print(''.join(no_vowels))