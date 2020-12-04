import re

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


def check_valid(x):
    valid = []
    valid.append(2002 >= int(t[x]['byr']) >= 1920)
    valid.append(2020 >= int(t[x]['iyr']) >= 2010)
    valid.append(2030 >= int(t[x]['eyr']) >= 2020)
    if t[x]['hgt'][-2:] == 'cm':
        valid.append(193 >= int(t[x]['hgt'][:-2]) >= 150)
    elif t[x]['hgt'][-2:] == 'in':
        valid.append(76 >= int(t[x]['hgt'][:-2]) >= 59)
    else:
        valid.append(False)
    valid.append(bool(re.findall("^#[a-f0-9]{6}$", t[x]['hcl'])))
    ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    valid.append((t[x]['ecl']) in ecl)
    valid.append(bool(re.findall("^(\d{9})$", t[x]['pid'])))
    if False in valid:
        return False
    else:
        return True


counter = 0

for i in range(len(t)):
    if all(item in list(t[i].keys()) for item in fields):
        if check_valid(i):
            counter += 1

print('No. of valid passports: ', counter)
