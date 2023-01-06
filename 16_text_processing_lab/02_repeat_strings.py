command = input().split(' ')
print(''.join([word*(len(word)) for word in command]))