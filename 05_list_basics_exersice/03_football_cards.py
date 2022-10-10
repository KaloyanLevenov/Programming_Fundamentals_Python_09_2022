team_a = ["A-"+ str(number) for number in range(1,12)]
team_b = ["B-"+ str(number) for number in range(1,12)]
game_was_terminated = False
referee_card_list = input().split()

for player in referee_card_list:

    if player in team_a:
        team_a.remove(player)

    elif player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminated = True
        break

if game_was_terminated:
    print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
    print('Game was terminated')
else:
    print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')

