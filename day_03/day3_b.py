import re
f = open('day_03.txt', 'r')
n = [re.sub(' \\n$', '', i).strip() for i in f.readlines()]
r_d = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
prod = 1
for i in r_d:
    row, position, count = 0, 0, 0
    r, d = i[0], i[1]

    while True:
        row += d
        position = (position + r) % len(n[row])
        count += n[row][position] == '#'
        if row >= len(n) - 1: break
    prod *= count
print(prod)
