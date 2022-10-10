number_of_snowballs = int(input())
best_list = []
best_value = 0

for each_ball in range(number_of_snowballs):

    weight_of_snow_ball = int(input())
    time_needed = int(input())
    snow_ball_quality = int(input())
    snow_ball_value = (weight_of_snow_ball / time_needed) ** snow_ball_quality

    if snow_ball_value > best_value:
        best_value = snow_ball_value
        best_list.append(weight_of_snow_ball)
        best_list.append(time_needed)
        best_list.append(snow_ball_quality)

print(f"{best_list[0]} : {best_list[1]} = {best_value:.0f} ({best_list[2]})")



