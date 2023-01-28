import csv
import re


def check_line(line):
    regex1 = r"^.+$"
    regex2 = r"^[0-9]+$"
    if re.search(regex1, line[0]):
        print(f"Part: {line[0]} is correct.")
    else:
        print(f"Part: {line[0]} is incorrect.")
    if re.search(regex2, line[1]):
        print(f"Part: {line[1]} is correct.")
    else:
        print(f"Part: {line[1]} is incorrect.")
    if re.search(regex2, line[2]):
        print(f"Part: {line[2]} is correct.")
    else:
        print(f"Part: {line[2]} is incorrect.")


with open("data.csv", "r") as file:
    reader = csv.reader(file)

    for line in reader:
        check_line(line)

file.close()