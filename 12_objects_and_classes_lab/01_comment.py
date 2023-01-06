class Comment:
    def __init__(self, username, content, likes=5):
        self.username = username
        self.content = content
        self.likes = likes


pesho = Comment('user_pesho', 'I like beer')
print(pesho.username)
print(pesho.content)
print(pesho.likes)
