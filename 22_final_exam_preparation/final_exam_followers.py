def new_follower_func(username, register):
    if username not in register.keys():
        register[username] = [0, 0]


def like_func(username, count, register):
    if username not in register.keys():
        register[username] = [count, 0]
    else:
        register[username][0] += count



def comment_func(username, register):
    if username not in register.keys():
        register[username] = [0, 1]
    else:
        register[username][1] += 1


def blocked_func(username, register):
    if username not in register.keys():
        print(f"{username} doesn't exist.")
    else:
        del register[username]


def print_func(register):
    print(f"{len(register.keys())} followers")
    for user, user_info in register.items():
        likes = user_info[0]
        comments = user_info[1]
        print(f"{user}: {likes + comments}")


register = {}
while True:
    command = input()
    if command == "Log out":
        break
    command_list = command.split(": ")
    action = command_list[0]
    if action == "New follower":
        username = command_list[1]
        new_follower_func(username, register)
    elif action == "Like":
        username, count = command_list[1], int(command_list[2])
        like_func(username, count, register)
    elif action == "Comment":
        username = command_list[1]
        comment_func(username, register)
    elif action == "Blocked":
        username = command_list[1]
        blocked_func(username, register)

print_func(register)
