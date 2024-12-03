import re

pattern = r'(?:mul\((\d+),(\d+)\)|don\'t\(\)|do\(\))'

sum = 0
all_matches = []
with open('2024/day_3/input.txt', 'r') as input:
    for line in input.readlines():
        matches = re.finditer(pattern, line)
        for match in matches:
            if match.group(1) is not None:
                all_matches.append(
                    (int(match.group(1)), int(match.group(2))))
            else:
                all_matches.append(match[0])

sum = 0
is_count = True
for match in all_matches:
    if match == 'don\'t()':
        is_count = False
    elif match == 'do()':
        is_count = True
    else:
        if is_count:
            sum += match[0] * match[1]
print(sum)  # 118173507
