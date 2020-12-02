f = open('day_01.txt', 'r')

a = set()
for i in map(int, f.readlines()):
    if (2020-i) in a:
        print(i * (2020-i))
    a.add(i)