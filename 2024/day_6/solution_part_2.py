import datetime


def simulate_path(test_map, start_i, start_j):
    current_i, current_j = start_i, start_j
    cur_dir = "up"
    visited = [(current_i, current_j)]

    while True:
        obj, new_x, new_y = move(cur_dir, current_i, current_j, test_map)
        if obj == "O":
            return False
        elif obj == "." or obj == "^":
            if (current_i, current_j) not in visited:
                visited.append((current_i, current_j))
            current_i = new_x
            current_j = new_y
        elif obj == "#":
            cur_dir = turn(cur_dir)
            if (current_i, current_j, cur_dir) in visited:
                return True
            visited.append((current_i, current_j, cur_dir))


def turn(current):
    if current == "up":
        return "right"
    elif current == "right":
        return "down"
    elif current == "down":
        return "left"
    elif current == "left":
        return "up"


def move(direction, x, y, current_map):
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
    if new_x >= 0 and new_y >= 0 and new_x < len(current_map) and new_y < len(current_map[0]):
        return current_map[new_x][new_y], new_x, new_y
    else:
        return "O", -1, -1


start = datetime.datetime.now()
grid_map = []
with open('2024/day_6/input.txt', 'r') as f:
    for line in f:
        grid_map.append(list(line.strip()))

start_i, start_j = 0, 0
for i in range(len(grid_map)):
    for j in range(len(grid_map[i])):
        if grid_map[i][j] == '^':
            start_i = i
            start_j = j
            break

visited = [(start_i, start_j)]
cur_i = start_i
cur_j = start_j
cur_dir = "up"
while True:
    obj, new_x, new_y = move(cur_dir, cur_i, cur_j, grid_map)
    if obj == "O":
        if (cur_i, cur_j) not in visited:
            visited.append((cur_i, cur_j))
        break
    elif obj == "." or obj == "^":
        if (cur_i, cur_j) not in visited:
            visited.append((cur_i, cur_j))
        cur_i = new_x
        cur_j = new_y
    elif obj == "#":
        cur_dir = turn(cur_dir)

possible_positions = []
for visit in visited:
    i = visit[0]
    j = visit[1]
    if grid_map[i][j] == '.':
        test_map = [row[:] for row in grid_map]
        test_map[i][j] = '#'
        if simulate_path(test_map, start_i, start_j):
            possible_positions.append((i, j))

print("Positions where placing # prevents reaching O:", possible_positions)
print(len(possible_positions))  # 2162
print(datetime.datetime.now() - start)
