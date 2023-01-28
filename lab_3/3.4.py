import re

regex = r"\S+[@]\S+\.\S+"

with open("file.txt", "r") as fileread:
    text = fileread.read()
    emails = re.findall(regex, text)
    print(emails)