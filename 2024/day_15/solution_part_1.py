map = []
moves = []
with open('2024/day_15/input.txt', 'r') as f:
    for line in f.readlines():
        if line.startswith('#'):
            map.append(list(line.strip()))
        else:
            moves.extend(list(line.strip()))

width = len(map[0])
height = len(map)
ci = None
cj = None
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "@":
            ci = i
            cj = j
            map[i][j] = '.'

for move in moves:
    if move == '>' and cj+1 <= width-1:
        if map[ci][cj+1] == '.':
            cj += 1
        elif map[ci][cj+1] == 'O':
            for k in range(cj+2, width):
                if map[ci][k] == '#':
                    break
                elif map[ci][k] == '.':
                    map[ci][k] = 'O'
                    map[ci][cj+1] = '.'
                    cj += 1
                    break

    elif move == '<' and cj-1 >= 0:
        if map[ci][cj-1] == '.':
            cj -= 1
        elif map[ci][cj-1] == 'O':
            for k in range(cj-2, 0, -1):
                if map[ci][k] == '#':
                    break
                elif map[ci][k] == '.':
                    map[ci][k] = 'O'
                    map[ci][cj-1] = '.'
                    cj -= 1
                    break

    elif move == 'v' and ci+1 <= height-1:
        if map[ci+1][cj] == '.':
            ci += 1
        elif map[ci+1][cj] == 'O':
            for k in range(ci+2, height):
                if map[k][cj] == '#':
                    break
                elif map[k][cj] == '.':
                    map[k][cj] = 'O'
                    map[ci+1][cj] = '.'
                    ci += 1
                    break

    elif move == '^' and ci-1 >= 0:
        if map[ci-1][cj] == '.':
            ci -= 1
        elif map[ci-1][cj] == 'O':
            for k in range(ci-2, 0, -1):
                if map[k][cj] == '#':
                    break
                elif map[k][cj] == '.':
                    map[k][cj] = 'O'
                    map[ci-1][cj] = '.'
                    ci -= 1
                    break

sum = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 'O':
            sum += (i)*100+j
print(sum)  # 1446158
