import re


def sum_of_the_ascii_codes(name):
    excluding_pattern = r"([^0-9/\*\-\+\.]+)"
    matches = re.findall(excluding_pattern, name)
    total = 0
    if matches:
        valid_symbols = "".join(matches)
        for character in valid_symbols:
            total += ord(character)
    return total


def sum_of_all_numbers(name):
    damage = 0
    pattern = r"([\+|\-]?\d+[\.\d]*)"
    matches = re.findall(pattern, name)
    if matches:
        for number in matches:
            damage += float(number)
    return damage


def multiplication_and_division(damage, name):
    multiplying_index = 0
    dividing_index = 0
    multiplying_pattern = r"\*"
    matches = re.findall(multiplying_pattern, name)
    multiplying_index += len(matches)
    damage = damage * 2 ** multiplying_index
    dividing_pattern = r"/"
    matches = re.findall(dividing_pattern, name)
    dividing_index += len(matches)
    damage = damage / 2 ** dividing_index
    return damage


data_input = input()
split_pattern = r"\,\s+"
name_list = sorted(re.split(split_pattern, data_input))
for name in name_list:
    warrior_health = sum_of_the_ascii_codes(name)
    warrior_damage = sum_of_all_numbers(name)
    warrior_damage = multiplication_and_division(warrior_damage, name)
    if name:
        print(f"{name} - {warrior_health} health, {warrior_damage:.2f} damage")

