legendary = {"shards":0,"fragments":0,"motes":0}
item_is_obtained = False
while not item_is_obtained:
    current_item = input().split(' ')
    for index in range(0,len(current_item),2):
        quantity = int(current_item[index])
        material = current_item[index + 1].lower()
        if material not in legendary.keys():
            legendary[material] = 0
        legendary[material] += quantity
        if legendary['shards'] >= 250:
            item_is_obtained = True
            legendary['shards'] -= 250
            print('Shadowmourne obtained!')
            break
        elif legendary['fragments'] >= 250:
            item_is_obtained = True
            legendary['fragments'] -= 250
            print('Valanyr obtained!')
            break
        elif legendary['motes'] >= 250:
            item_is_obtained = True
            legendary['motes'] -= 250
            print('Dragonwrath obtained!')
            break

for key,value in legendary.items():
    print(f'{key}: {value}')
