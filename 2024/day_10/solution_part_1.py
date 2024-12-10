map = []
with open('2024/day_10/input.txt', 'r') as input:
    for line in input.readlines():
        map.append([int(item) for item in line.strip()])
print(map)


def move(map, row, col, last_value):
    if row < 0 or row >= len(map) or col < 0 or col >= len(map[0]) or map[row][col] != last_value+1:
        return []
    elif map[row][col] == 9:
        return [(row, col)]
    else:
        return move(map, row, col+1, last_value+1) + move(map, row+1, col,last_value+1) + move(map, row, col-1,last_value+1) + move(map, row-1, col,last_value+1)


count = 0
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if map[i][j] == 0:
            count += len(set(move(map, i, j, -1)))
print(count)  # 652
