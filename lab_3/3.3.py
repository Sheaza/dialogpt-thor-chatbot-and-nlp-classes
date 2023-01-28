import re

regex = r"([a-zA-Z]*(chuj)[a-zA-Z]*)[,.]*|([a-zA-Z]*(kurw)[a-zA-Z]*)[,.]*|([a-zA-Z]*(jeb)[a-zA-Z]*)[,.]*|([a-zA-Z]*(pierd)[a-zA-Z]*[,.]*)"

with open("przeklenstwa.txt", "r") as fileread:
    lines = fileread.read()

fileread.close()

with open("przeklenstwa.txt", "w") as filewrite:
    changedlines = re.sub(regex, "---", lines)
    filewrite.write(changedlines)
filewrite.close()