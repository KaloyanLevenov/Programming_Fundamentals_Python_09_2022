def decorator_func(fnc):
    def inner(list_of_names):
        register = {element[0]: [int(element[1]), int(element[2])] for element in list_of_names}
        for hero in register.keys():
            if register[hero][0] > 100:
                register[hero][0] = 100
            if register[hero][1] > 200:
                register[hero][1] = 200
        return register

    return inner


@decorator_func
def heroes_of_logic(*args):
    return args


def cast_spell_func(hero, mana_needed, spell, hero_register):
    available_mana = hero_register[hero][1]
    if available_mana >= mana_needed:
        mana_left = available_mana - mana_needed
        print(f"{hero} has successfully cast {spell} and now has {mana_left} MP!")
        hero_register[hero][1] = mana_left
    else:
        print(f"{hero} does not have enough MP to cast {spell}!")


def take_damage(hero, damage, attacker, hero_register):
    available_health = hero_register[hero][0]
    if available_health <= damage:
        print(f"{hero} has been killed by {attacker}!")
        del hero_register[hero]
    else:
        health_left = available_health - damage
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {health_left} HP left!")
        hero_register[hero][0] = health_left


def recharge(hero, amount, hero_register):
    available_mana = hero_register[hero][1]
    if available_mana + amount > 200:
        recover = 200 - available_mana
        hero_register[hero][1] += recover
    else:
        recover = amount
        hero_register[hero][1] += recover
    print(f"{hero} recharged for {recover} MP!")


def heal(hero, amount, hero_register):
    available_health = hero_register[hero][0]
    if available_health + amount > 100:
        recover = 100 - available_health
        hero_register[hero][0] += recover
    else:
        recover = amount
        hero_register[hero][0] += recover
    print(f"{hero} healed for {recover} HP!")


number_of_heroes = int(input())
data = [input().split(" ") for _ in range(number_of_heroes)]
register = heroes_of_logic(data)

command = input()
while command != "End":
    command_list = command.split(" - ")
    action = command_list[0]
    if action == "CastSpell":
        hero_name = command_list[1]
        mp_needed = int(command_list[2])
        spell_name = command_list[3]
        cast_spell_func(hero_name, mp_needed, spell_name, register)
    elif action == "TakeDamage":
        hero_name = command_list[1]
        damage = int(command_list[2])
        attacker = command_list[3]
        take_damage(hero_name, damage, attacker, register)
    elif action == "Recharge":
        hero_name = command_list[1]
        amount = int(command_list[2])
        recharge(hero_name, amount, register)
    elif action == "Heal":
        hero_name = command_list[1]
        amount = int(command_list[2])
        heal(hero_name, amount, register)

    command = input()

for hero in register.keys():
    print(hero)
    print(f"  HP: {register[hero][0]}")
    print(f"  MP: {register[hero][1]}")
