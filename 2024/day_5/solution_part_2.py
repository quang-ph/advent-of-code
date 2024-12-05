rules = {}
updates = []
with open('2024/day_5/input.txt', 'r') as input:
    for line in input:
        line = line.strip()
        if "|" in line:
            source, target = map(int, line.split("|"))
            rules.setdefault(source, []).append(target)
            rules.setdefault(target, [])
        elif line:  # Check if line is not empty
            items = [int(item) for item in line.split(",")]
            updates.append(items)

unqualified = []
for update in updates:
    previous_items = []
    add = True
    for item in update:
        if len(list(set(previous_items).intersection(rules[item]))) > 0:
            add = False
            break
        previous_items.append(item)
    if not add:
        unqualified.append(update)


qualified = []
for update in unqualified:
    correct_order = []
    remaining_items = set(update)

    while remaining_items:
        available_items = {
            item for item in remaining_items
            if not any(
                key in remaining_items and item in rules[key]
                for key in rules
            )
        }

        if not available_items:
            # If no items are available, there might be a circular dependency
            print("Warning: Possible circular dependency detected")
            break

        item = min(available_items)  # Use min() for consistent ordering
        correct_order.append(item)
        remaining_items.remove(item)
    qualified.append(correct_order)


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
print(sum)  # 6204
