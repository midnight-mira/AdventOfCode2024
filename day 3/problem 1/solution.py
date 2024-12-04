'''
Intuition : apply regex while reading the code

'''
import re

sum1 =0


sum1 =0
file = open("input.txt", "r")
content = file.read()

matches=re.findall(r"mul\((\d+),(\d+)\)", content)
print(matches)

for l, r in matches:
    prod = int(l) * int(r)
    sum1 += prod

print(sum1)

'''
result = 0
matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', input_str)

for item in matches:
    l, r = re.findall(r'\d{1,3}', item)
    result += int(l) * int(r)

print(result)

'''
