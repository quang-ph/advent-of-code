first_list = []
second_list = []
with open('2024/day_1/input.txt', 'r') as input:
    for line in input.readlines():
        first_list.append(int(line.split(' ')[0]))
        second_list.append(int(line.split(' ')[-1].replace('\n', '')))

similarity_dict = {}
for item in first_list:
    if item in similarity_dict:
        similarity_dict[item]['occurrences'] += 1
    else:
        similarity_dict[item] = {'occurrences': 1, 'similarity':0}
        for item2 in second_list:
            if item == item2:
                similarity_dict[item]['similarity'] += 1
similarity = 0
for key in similarity_dict:
    similarity += key * similarity_dict[key]['similarity'] * similarity_dict[key]['occurrences']
print(similarity)