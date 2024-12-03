import re

pattern = r'mul\((\d+),(\d+)\)'

sum = 0
with open('2024/day_3/input.txt', 'r') as input:
    for line in input.readlines():
        matches = re.findall(pattern, line)
        for match in matches:
            sum = sum + int(match[0]) * int(match[1])
print(sum)  # 184576302
