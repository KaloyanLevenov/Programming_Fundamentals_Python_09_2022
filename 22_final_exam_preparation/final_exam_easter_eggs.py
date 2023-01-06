import re
pattern = r"([@]+|[#]+)([a-z]{3,})([@]+|[#]+)[^a-zA-Z0-9]*\/+(\d+)\/+"

text = input()
matches = re.findall(pattern,text)
if matches:
    for match in matches:
        color  = match[1]
        amount = match[3]
        print(f"You found {amount} {color} eggs!")
        