f = open('day_02.txt', 'r')

count = 0
for i in f.readlines():
    n, a, p = i.split()
    x, y = map(int, n.split('-'))
    count += (p[x - 1] == a[0]) + (p[y - 1] == a[0]) == 1
print(count)

