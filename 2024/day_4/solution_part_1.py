def count_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, -1),
        (-1, 1),
    ]

    def is_in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_in_bounds(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search_from(x, y, dx, dy):
                    count += 1
    return count


list = []
with open('2024/day_4/input.txt', 'r') as input:
    for line in input.readlines():
        row = []
        for char in [char for char in line.replace('\n', '')]:
            row.append(char)
        list.append(row)

word = "XMAS"
print(count_word(list, word))  # 2642
