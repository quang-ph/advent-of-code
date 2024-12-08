
input_dict = {}
with open('2024/day_7/input.txt', 'r') as input:
    for line in input.readlines():
        line = line.split(':')
        input_dict[int(line[0])] = [int(item)
                                    for item in line[1].strip().replace('\n', '').split(' ')]

print(input_dict)


def can_reach_target(nums, target, current=0, index=1):
    if index == len(nums):
        return current == target
    return (can_reach_target(nums, target, current + nums[index], index + 1) or
            can_reach_target(nums, target, current * nums[index], index + 1))


output = 0
for key in input_dict:
    if can_reach_target(input_dict[key], key, current=input_dict[key][0]):
        output += key
        print(key)
print(output)
