data = input()
dct = {}
non_space_data = data.replace(' ','')
for char in non_space_data:
    if char not in dct:
        dct[char] = 1
    else:
        dct[char] += 1

for key,value in dct.items():
    print(f"{key} -> {value}")
