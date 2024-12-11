stones = []
with open('2024/day_11/input.txt', 'r') as input:
    for line in input.readlines():
        stones.extend(line.strip().split(' '))
stones = [int(stone) for stone in stones]


def check(stones):
    new_stones = []
    for i in range(0, len(stones)):
        stone_len = len(str(stones[i]))
        if stones[i] == 0:
            new_stones.append(1)
        elif stone_len % 2 == 0:
            split = stone_len // 2
            new_stones.append(int(str(stones[i])[:split]))
            new_stones.append(int(str(stones[i])[split:]))
        else:
            new_stones.append(stones[i] * 2024)
    return new_stones


for i in range(0, 25):
    print('loop', i + 1)
    new_stones = check(stones)
    stones = new_stones
print(len(stones))  # 200446
