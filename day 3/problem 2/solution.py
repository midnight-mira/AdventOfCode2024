import re

with open("input.txt") as file:
    lines = file.readlines()

total = 0
can_do = True
result = 0
for line in lines:
    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", line)
    print(instructions)
    for instruction in instructions:
        if instruction == "do()":
            can_do = True
            continue

        if instruction == "don't()":
            can_do = False
            continue

        if can_do:
            numbers = list(map(int, re.findall("\d+", instruction)))
            result += numbers[0] * numbers[1]

    print(result)
        





