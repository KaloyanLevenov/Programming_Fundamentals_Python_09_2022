import re
text = input()
pattern = r"(?<==)[A-Z][A-Za-z]{2,}(?==)|(?<=\/)[A-Z][A-Za-z]{2,}(?=\/)"
travel_points = 0
valid_locations = re.findall(pattern,text)
if valid_locations:
    for location in valid_locations:
        travel_points += len(location)
print(f"Destinations: {', '.join(valid_locations)}")
print(f"Travel Points: {travel_points}")