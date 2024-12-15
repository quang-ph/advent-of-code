import re


def parse_coordinates(line):
    pattern = r'[XY][+=](\d+)'
    numbers = re.findall(pattern, line)
    if numbers:
        return (int(numbers[0]), int(numbers[1]))
    return None


coordinates = []
with open('2024/day_13/input.txt', 'r') as f:
    count = 0
    small_cor = []
    for line in f.readlines():
        line = line.strip()
        if line:
            coords = parse_coordinates(line)
            if coords:
                small_cor.append(coords)
                count += 1
            if count == 3:
                coordinates.append(small_cor.copy())
                count = 0
                small_cor.clear()

sum = 0
for item in coordinates:
    a1, b1, c1 = item[0][0], item[1][0], item[2][0] + 10000000000000
    a2, b2, c2 = item[0][1], item[1][1], item[2][1] + 10000000000000
    x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
    y = (c1 - a1 * x) / b1
    print(x, y)
    if x % 1 == 0 and y % 1 == 0 and x > 0 and y > 0:
        sum += 3 * x + y
print(int(sum))  # 106228669504887
