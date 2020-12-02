f = open('day_02.txt', 'r')
count = 0
for i in f.readlines():
    n, a, p = i.split()
    x, y = map(int, n.split('-'))
    if x <= p.count(a[0]) <= y:
        count += 1

print(count)