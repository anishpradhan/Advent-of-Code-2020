import re

f = open('day_03.txt', 'r')
n = [re.sub(' \\n$', '', i).strip() for i in f.readlines()]
count, row, position = 0, 0, 0
while True:
    row += 1
    position = (position + 3) % len(n[row])
    count += n[row][position] == '#'
    if row >= len(n) - 1: break

print(count)
