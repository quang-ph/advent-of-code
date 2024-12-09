index = 0
block_type = 1
num_char = 0
arr = []
with open('2024/day_9/input.txt', 'r') as input:
    for line in input.readlines():
        for item in line.strip().replace('\n', ''):
            if block_type == 1:
                for i in range(0, int(item)):
                    arr.append(index)
                    num_char += 1
                block_type = 0
                index += 1
            elif block_type == 0:
                for i in range(0, int(item)):
                    arr.append('.')
                block_type = 1
last_item = arr[0]
item_count = 0
start_pos = 0
new_arr = []
for item in arr:
    if last_item == '' or item == last_item:
        item_count += 1
    if item != last_item:
        new_arr.append([last_item, item_count, start_pos])
        start_pos += item_count
        item_count = 1
    last_item = item
new_arr.append([last_item, item_count, start_pos])

empty_arr = []
for j in range(len(new_arr) - 1, 0, -1):
    for i in range(0, len(new_arr)):
        if j > i and new_arr[j][2] > new_arr[i][2] and new_arr[j][0] != '.' and new_arr[j][1] <= new_arr[i][1] and new_arr[i][0] == '.':
            empty_arr.append(['.', new_arr[j][1], new_arr[j][2]])
            new_arr[j][2] = new_arr[i][2]
            new_arr[i][1] = new_arr[i][1] - new_arr[j][1]
            new_arr[i][2] = new_arr[i][2] + new_arr[j][1]
new_arr.extend(empty_arr)
new_arr = sorted(new_arr, key=lambda x: x[2])

result = []
index = 0
for item in new_arr:
    if item[2] == index and item[1] > 0:
        for i in range(0, item[1]):
            result.append(item[0])
            index += 1

index = 0
sum = 0
for i in result:
    if i != '.':
        sum += index * i
    index += 1
print(sum)  # 6511178035564
