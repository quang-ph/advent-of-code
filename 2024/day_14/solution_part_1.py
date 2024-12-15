def parse(text):
    p_part, v_part = text.split()
    p_nums = p_part.replace('p=', '').split(',')
    p_tuple = (int(p_nums[0]), int(p_nums[1]))
    v_nums = v_part.replace('v=', '').split(',')
    v_tuple = (int(v_nums[0]), int(v_nums[1]))
    return p_tuple, v_tuple


def move(p, v, width, height):
    new_x = p[0] + v[0]
    if new_x < 0:
        new_x = width + new_x
    elif new_x >= width:
        new_x = new_x - width
    new_y = p[1] + v[1]
    if new_y < 0:
        new_y = height + new_y
    elif new_y >= height:
        new_y = new_y - height
    return new_x, new_y


width = 101
height = 103
q1 = q2 = q3 = q4 = 0
with open('2024/day_14/input.txt', 'r') as f:
    for line in f.readlines():
        p, v = parse(line.strip())
        for i in range(0, 100):
            p = move(p, v, width, height)
        if p[0] < width//2 and p[1] < height//2:
            q1 += 1
        elif p[0] > width//2 and p[1] < height//2:
            q2 += 1
        elif p[0] < width//2 and p[1] > height//2:
            q3 += 1
        elif p[0] > width//2 and p[1] > height//2:
            q4 += 1

print(q1 * q2 * q3 * q4)  # 230172768
