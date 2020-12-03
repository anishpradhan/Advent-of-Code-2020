import re
f = open('day_03.txt', 'r')
n = f.readlines()
for i in range(len(n)):
    n[i] = re.sub('\\n$', '', n[i])
count, row, position = 0, 0, 0
while True:
    if position + 3 >= len(n[row]):
        position = position - len(n[row])
    if n[row + 1][position + 3] == '#':
        count += 1
    row += 1
    position += 3
    if row >= len(n) - 1:
        break
print(count)
