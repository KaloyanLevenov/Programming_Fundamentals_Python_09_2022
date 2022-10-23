# Here we have couple of names as a string
names_as_string = input()
# Converting the srt into list
names_as_list = list(map(str, names_as_string.split(', ')))
# In a new list we sort the names by their length, starting with the largest to the shortest name
sorted_names = sorted(names_as_list, key=lambda x: (-len(x), x))

print(sorted_names)
