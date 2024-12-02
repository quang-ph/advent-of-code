def check_is_safe(levels):
    is_safe = True
    for i in range(0, len(levels) - 1):
        if not (levels[i] < levels[i + 1] and levels[i + 1] - levels[i] <= 3):
            is_safe = False
            break
    if not is_safe:
        is_safe = True
        for i in range(0, len(levels) - 1):
            if not (levels[i] > levels[i + 1] and levels[i] - levels[i + 1] <= 3):
                is_safe = False
                break
    return is_safe


safe_level_count = 0
with open('2024/day_2/input.txt', 'r') as input:
    for line in input.readlines():
        levels = line.split(' ')
        levels = [int(level.replace('\n', '')) for level in levels]
        if check_is_safe(levels):
            safe_level_count += 1
        else:
            for i in range(len(levels)):
                test_levels = levels[:i] + levels[i + 1:]
                if check_is_safe(test_levels):
                    print(levels, i)
                    safe_level_count += 1
                    break
print(safe_level_count)
