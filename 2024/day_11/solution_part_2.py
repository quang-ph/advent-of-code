from collections import Counter


def split_stone(stone):
    if stone == 0:
        return [1]
    stone_len = len(str(stone))
    if stone_len % 2 == 0:
        split = 10 ** (stone_len // 2)
        return [stone // split, stone % split]
    else:
        return [stone * 2024]


def check(stone_counts):
    new_counts = Counter()
    for stone, count in stone_counts.items():
        transformations = split_stone(stone)
        print(transformations)
        for t in transformations:
            new_counts[t] += count
    return new_counts


with open('2024/day_11/input.txt', 'r') as input:
    stones = [int(stone) for line in input for stone in line.strip().split()]

stone_counts = Counter(stones)
print(stone_counts)

for i in range(75):
    stone_counts = check(stone_counts)

print(sum(stone_counts.values()))  # 238317474993392
