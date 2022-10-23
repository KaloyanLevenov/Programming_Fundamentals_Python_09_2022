def chat_func(chat, message):
    chat.append(message)
    return chat


def delete_func(chat, message):
    if message in chat:
        chat.remove(message)

    return chat


def edit_func(chat, message, new_message):
    if message in chat:
        chat[chat.index(message)] = new_message

    return chat


def pin_func(chat, message):
    if message in chat:
        chat.append(chat.pop(chat.index(message)))

    return chat


def spam_func(chat, messages):
    for words in messages:
        chat.append(words)

    return chat


chat_list = []
while True:
    command = input()
    if command == 'end':
        break
    command_list = command.split(' ')
    action = command_list[0]
    if action == 'Chat':
        message = command_list[1]
        chat_func(chat_list, message)
    if action == 'Delete':
        message = command_list[1]
        delete_func(chat_list, message)
    if action == 'Edit':
        message = command_list[1]
        edited_message = command_list[2]
        edit_func(chat_list, message, edited_message)
    if action == 'Pin':
        message = command_list[1]
        pin_func(chat_list, message)
    if action == 'Spam':
        message_list = command_list[1::]
        spam_func(chat_list, message_list)

print('\n'.join(chat_list))