from collections import deque

# grid = [list(line.strip()) for line in open('2024/day_12/input.txt', 'r')]
grid = [list(line.strip()) for line in open('2024/day_12/input_test.txt', 'r')]

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


def sides(region):
    groups = {}
    for x, y in region:
        if x not in groups:
            groups[x] = []
        groups[x].append((x, y))
    nre = []
    for x in sorted(groups.keys()):
        sorted_group = sorted(groups[x], key=lambda t: t[1])
        nre.append(sorted_group)
    print(nre)
    sides = 4
    for r in range(1, len(nre)):
        if len(nre[r]) != len(nre[r-1]):
            if nre[r][0][1] == nre[r-1][0][1] or nre[r][-1][1] == nre[r-1][-1][1]:
                sides += 2
            else:
                sides += 4
        elif nre[r][0][1] != nre[r-1][0][1] or nre[r][-1][1] != nre[r-1][-1][1]:
            sides += 4
    print(sides)
    return sides
    

print(sum(len(region)*compute_boundary_lines(region) for region in regions))
