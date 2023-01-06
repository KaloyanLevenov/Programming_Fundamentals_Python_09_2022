def length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def characters(name):
    for character in name:
        if not (character.isalnum() or character == '-' or character == '_'):
            return False
    return True


def no_redundant_symbols(name):
    if ' ' in name:
        return False
    return True


def username_validation(name):
    if length(name) and characters(name) and no_redundant_symbols(name):
        return True
    return False


usernames = input().split(', ')
for username in usernames:
    if username_validation(username):
        print(username)

