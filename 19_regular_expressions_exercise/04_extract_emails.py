import re

text = input()
pattern = r"\s(([a-z0-9]+[\.\-\_]?[a-z0-9]*)@([a-z\-]+[\.][a-z\-\.]+){1,})\b"
matches = re.findall(pattern,text)
for match in matches:
    print(match[0])


