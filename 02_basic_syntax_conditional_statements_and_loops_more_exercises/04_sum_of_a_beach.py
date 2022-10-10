given_string = input()
counter = 0
counter += given_string.lower().count('fish')
counter += given_string.lower().count('sand')
counter += given_string.lower().count('water')
counter += given_string.lower().count('sun')
print(counter)
