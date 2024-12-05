rules = {}
updates = []
with open('2024/day_5/input.txt', 'r') as input:
    for line in input.readlines():
        if "|" in line:
            list_1 = line.replace('\n', '').split('|')
            if int(list_1[0]) not in rules.keys():
                rules[int(list_1[0])] = [int(list_1[1])]
            else:
                rules[int(list_1[0])].append(int(list_1[1]))
            if int(list_1[1]) not in rules.keys():
                rules[int(list_1[1])] = []
        elif line != '\n':
            items = [int(item) for item in line.replace('\n', '').split(',')]
            updates.append(items)

qualified = []
for update in updates:
    previous_items = []
    add = True
    for item in update:
        if len(list(set(previous_items).intersection(rules[item]))) > 0:
            add = False
            break
        previous_items.append(item)
    if add:
        qualified.append(update)


def get_middle_detailed(lst):
    if not lst:
        return None

    length = len(lst)
    middle_index = length // 2

    if length % 2 == 0:
        return (lst[middle_index - 1], lst[middle_index])
    else:
        return lst[middle_index]


sum = 0
for update in qualified:
    sum += get_middle_detailed(update)
print(sum)  # 4905
