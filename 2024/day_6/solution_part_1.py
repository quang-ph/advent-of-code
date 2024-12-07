rules = {}
map = []
with open('2024/day_6/input.txt', 'r') as input:
    for line in input.readlines():
        items = [char for char in line.replace('\n', '')]
        map.append(items)


def turn(current):
    if current == "up":
        return "right"
    elif current == "right":
        return "down"
    elif current == "down":
        return "left"
    elif current == "left":
        return "up"


def move(direction, x, y):
    if direction == "up":
        new_x = x - 1
        new_y = y
    elif direction == "right":
        new_x = x
        new_y = y + 1
    elif direction == "down":
        new_x = x + 1
        new_y = y
    elif direction == "left":
        new_x = x
        new_y = y - 1
    if new_x >= 0 and new_y >= 0 and new_x < len(map) and new_y < len(map[0]):
        return map[new_x][new_y], new_x, new_y
    else:
        return "O", -1, -1


current_i = 0
current_j = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == '^':
            current_i = i
            current_j = j
            break

cur_dir = "up"
visited = [(current_i, current_j)]
while True:
    obj, new_x, new_y = move(cur_dir, current_i, current_j)
    if obj == "O":
        if (current_i, current_j) not in visited:
            visited.append((current_i, current_j))
        break
    elif obj == "." or obj == "^":
        if (current_i, current_j) not in visited:
            visited.append((current_i, current_j))
        current_i = new_x
        current_j = new_y
    elif obj == "#":
        cur_dir = turn(cur_dir)

print(len(visited))  # 5329
