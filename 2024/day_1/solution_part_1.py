first_list = []
second_list = []
with open('2024/day_1/input.txt', 'r') as input:
    for line in input.readlines():
        first_list.append(int(line.split(' ')[0]))
        second_list.append(int(line.split(' ')[-1].replace('\n', '')))
first_list.sort()
second_list.sort()

difference = [abs(x - y) for x, y in zip(first_list, second_list)]
print(sum(difference))