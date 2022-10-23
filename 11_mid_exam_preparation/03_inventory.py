def crafting_func(inventory):
    while True:
        command = input()

        if command == 'Craft!':
            break

        action, item = command.split(' - ')

        if action == 'Collect':
            if item not in inventory:
                inventory.append(item)
        elif action == 'Drop':
            if item in inventory:
                inventory.remove(item)
        elif action == 'Combine Items':
            old_item, new_item = item.split(':')
            if old_item in inventory:
                old_item_index = inventory.index(old_item)
                inventory.insert(old_item_index + 1, new_item)
        elif action == 'Renew':
            if item in inventory:
                inventory.remove(item)
                inventory.append(item)

    print(', '.join(inventory))


journal = list(input().split(', '))

crafting_func(journal)