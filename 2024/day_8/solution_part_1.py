
from itertools import combinations

antenas = {}
row_index = 0
col_length = 0
with open('2024/day_8/input.txt', 'r') as input:
    for line in input.readlines():
        for col_index, char in enumerate(line.strip().replace('/n', '')):
            if char != '.':
                antenas.setdefault(char, []).append((row_index, col_index))
            col_length = col_index
        row_index += 1
row_index = row_index - 1
print(antenas)
print(row_index, col_length)

antinodes = []
for antena_type in antenas:
    for antena_pair in combinations(antenas[antena_type], 2):
        distance_vector = (
            antena_pair[1][0] - antena_pair[0][0], antena_pair[1][1] - antena_pair[0][1])
        new_point_1 = (antena_pair[0][0] - distance_vector[0],
                       antena_pair[0][1] - distance_vector[1])
        new_point_2 = (antena_pair[1][0] + distance_vector[0],
                       antena_pair[1][1] + distance_vector[1])
        if new_point_1[0] <= row_index and new_point_1[0] >= 0 and new_point_1[1] <= col_length and new_point_1[1] >= 0 and new_point_1 not in antinodes:
            antinodes.append(new_point_1)
        if new_point_2[0] <= row_index and new_point_2[0] >= 0 and new_point_2[1] <= col_length and new_point_2[1] >= 0 and new_point_2 not in antinodes:
            antinodes.append(new_point_2)
antinodes = sorted(antinodes, key=lambda x: (x[0], x[1]))
print(antinodes)
print(len(antinodes))
