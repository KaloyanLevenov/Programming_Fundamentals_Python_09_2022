register = {}


class PipeClass:

    def __init__(self, force, user):
        self.force = force
        self.user = user

    def add_user(self):
        user_is_new = True
        force_in_register = False

        if self.force not in register:
            register[self.force] = []
            force_in_register = True
        else:
            force_in_register = True

        if force_in_register:
            for force in register.keys():
                if self.user in register[force]:
                    user_is_new = False
            if user_is_new:
                register[self.force].append(self.user)


class ArrowClass:

    def __init__(self, force, user):
        self.force = force
        self.user = user

    def add_user(self):
        user_is_new = True
        user_has_changed_the_side = False
        force_not_in_register = True

        if self.force in register.keys():
            force_not_in_register = False

        if not force_not_in_register:
            for key in register:
                if self.user in register[key]:
                    user_is_new = False
                    user_has_changed_the_side = True
                    register[key].remove(self.user)

        if (not user_is_new) and user_has_changed_the_side:
            register[self.force].append(self.user)
            print(f"{self.user} joins the {self.force} side!")

        if user_is_new:
            register[self.force].append(self.user)
            print(f"{self.user} joins the {self.force} side!")
            if force_not_in_register:
                register[self.force] = []
                register[self.force].append(self.user)
                print(f"{self.user} joins the {self.force} side!")


def print_func():
    for force in register.keys():
        if len(register[force]) > 0:
            print(f"Side: {force}, Members: {len(register[force])}")
            for user in register[force]:
                print(f"! {user}")


command = input()
while command != "Lumpawaroo":
    if " | " in command:
        force_side, force_user = command.split(" | ")
        object_pipe = PipeClass(force_side, force_user)
        object_pipe.add_user()

    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        object_arrow = ArrowClass(force_side, force_user)
        object_arrow.add_user()

    command = input()

print_func()
