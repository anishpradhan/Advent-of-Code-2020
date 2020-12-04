f = open('day_04.txt', 'r')
n = [i.strip() for i in f.readlines()]
p = [[]]
for i in range(len(n)):
    if n[i] == '':
        p.append(list())
        continue
    p[(len(p) - 1)].append(n[i])

t = dict()
x = list()
for i in range(len(p)):
    x[:] = [' '.join(p[i][:])]
    t[i] = {}
    z = x[0].split()
    for j in z:
        b = j.split(':')
        t[i][b[0]] = b[1]

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
count = 0
for i in range(len(t)):
    count += all(item in list(t[i].keys()) for item in fields)
print('valid passports:', count)
