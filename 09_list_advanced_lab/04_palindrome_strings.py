# Here we are sorting from the input only palindrome words.
# Then we count how many times we have the palindrome key in our list
words_as_string = input()
palindrome_key = input()

palindrome_counter = 0

words_as_list = words_as_string.split(' ')

list_with_palindromes = [word for word in words_as_list if word[::] == word[::-1]]

for palindrome in list_with_palindromes:
    if palindrome == palindrome_key:
        palindrome_counter += 1

print(list_with_palindromes)
print(f'Found palindrome {palindrome_counter} times')
