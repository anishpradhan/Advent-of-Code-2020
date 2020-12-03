import re

f = open('day_03.txt', 'r')

n = f.readlines()

for i in range(len(n)):
    n[i] = re.sub('\\n$', '', n[i])

r_d = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
prod = 1
for i in r_d:
    row, position, count = 0, 0, 0
    r, d = i[0], i[1]

    while True:

        if position + r >= len(n[row]):
            position = position - len(n[row])
        if n[row + d][position + r] == '#':
            count += 1
        row += d
        position += r
        if row >= len(n) - 1:
            break
    prod *= count

print(prod)
