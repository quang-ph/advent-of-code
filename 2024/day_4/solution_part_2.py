list = []
with open('2024/day_4/input.txt', 'r') as input:
    for line in input.readlines():
        row = []
        for char in [char for char in line.replace('\n', '')]:
            row.append(char)
        list.append(row)

rows, cols = len(list), len(list[0])


def search_pattern(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            try:
                if grid[x][y] == 'A':
                    if (grid[x - 1][y - 1] == "M" and grid[x + 1][y + 1] == "S" and
                            grid[x + 1][y - 1] == 'M' and grid[x - 1][y + 1] == "S"):
                        count += 1
                    elif (grid[x - 1][y - 1] == "M" and grid[x + 1][y + 1] == "S" and
                          grid[x + 1][y - 1] == 'S' and grid[x - 1][y + 1] == "M"):
                        count += 1
                    elif (grid[x - 1][y - 1] == "S" and grid[x + 1][y + 1] == "M" and
                          grid[x + 1][y - 1] == 'M' and grid[x - 1][y + 1] == "S"):
                        count += 1
                    elif (grid[x - 1][y - 1] == "S" and grid[x + 1][y + 1] == "M" and
                          grid[x + 1][y - 1] == 'S' and grid[x - 1][y + 1] == "M"):
                        count += 1
            except IndexError:
                continue

    return count


print(search_pattern(list))  # 1974
