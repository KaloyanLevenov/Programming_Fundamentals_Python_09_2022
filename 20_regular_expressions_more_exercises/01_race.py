import re

participants = input().split(', ')
register = {participant: 0 for participant in participants}
command = input()
# G4e@55or%6g6!68e!!@
while command != "end of race":
    name_pattern = r"[A-Za-z]+"
    distance_pattern = r"[0-9]"
    name = "".join(re.findall(name_pattern,command))
    distance = (re.findall(distance_pattern,command))
    distance = [int(number) for number in distance]
    if name in register.keys():
        register[name] += sum(distance)
    command = input()
winner_list = sorted(register.items(),key = lambda item: item[1],reverse = True)
print(f"1st place: {winner_list[0][0]}")
print(f"2nd place: {winner_list[1][0]}")
print(f"3rd place: {winner_list[2][0]}")