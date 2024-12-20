from collections import deque

grid = [list(line.strip()) for line in open('2024/day_12/input.txt', 'r')]

rows = len(grid)
cols = len(grid[0])

regions = []
seen = set()

for r in range(rows):
    for c in range(cols):
        if (r, c) not in seen:
            region = {(r,c)}
            q = deque([(r, c)])
            seen.add((r, c))
            crop = grid[r][c]
            while q:
                x, y = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == crop and (nx, ny) not in region:
                        region.add((nx, ny))
                        q.append((nx, ny))
            regions.append(region)
            seen.update(region)


def perimeter(region):
    output = 0
    for (r, c) in region:
        output += 4
        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = r + dx, c + dy
            if (nx, ny) in region:
                output -= 1
    return output


print(sum(len(region)*perimeter(region) for region in regions))  # 1494342
