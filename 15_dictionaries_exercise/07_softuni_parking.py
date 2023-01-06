register = {}


class Parking:

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def register_func(self):
        if self.name in register.keys():
            print(f"ERROR: already registered with plate number {self.number}")
        else:
            register[self.name] = ""
            register[self.name] += self.number
            print(f"{self.name} registered {register[self.name]} successfully")

    def unregister_func(self, name):
        self.name = name
        if self.name in register.keys():
            print(f"{self.name} unregistered successfully")
            del register[self.name]
        else:
            print(f"ERROR: user {self.name} not found")

    def print_func(self):
        for key, value in register.items():
            print(f"{key} => {value}")


number_of_commands = int(input())
for _ in range(number_of_commands):
    current_command = input().split(' ')
    action = current_command[0]
    if action == 'register':
        username = current_command[1]
        license_plate_number = current_command[2]
        object = Parking(username, license_plate_number)
        object.register_func()
    elif action == 'unregister':
        username = current_command[1]
        object.unregister_func(username)

object.print_func()
