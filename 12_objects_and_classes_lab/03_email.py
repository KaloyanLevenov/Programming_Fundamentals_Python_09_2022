class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


email_list = []

while True:
    command = input()
    if command == 'Stop':
        break
    sender, receiver, content = command.split(' ')
    object_email = Email(sender, receiver, content)
    email_list.append(object_email)

send_emails_indices = list(map(int, input().split(', ')))

for every_object in send_emails_indices:
    email_list[every_object].send()

for every_object in email_list:
    print(every_object.get_info())
