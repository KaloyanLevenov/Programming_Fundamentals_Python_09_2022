import re


def title_func(string):
    title_pattern = r"(?<=<title>)(.*?)(?=</title>)"
    matches = re.findall(title_pattern, string)
    if matches:
        print(f"Title: {matches[0]}")


def body_func(string):
    first_body_pattern = r"(?<=<body>)(.*?)(?=</body>)"
    matches = re.findall(first_body_pattern, string)
    if matches:
        raw_body = ("".join(matches))

    second_body_pattern = r"(<[^>]*>)(\\n)?"
    body = ""
    content = re.sub(second_body_pattern,body,raw_body,0,re.MULTILINE)
    if content:
        print(f"Content: {content}")
    else:
        print(f"Content: {raw_body}")


string = input()
title_func(string)
body_func(string)


