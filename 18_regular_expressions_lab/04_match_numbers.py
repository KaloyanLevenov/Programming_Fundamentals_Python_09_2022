import re

patern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)((\.\d+)?)($|(?=\s))"
text = input()
matches = re.finditer(patern, text)
for match in matches:
    print(match.group(), end=" ")


