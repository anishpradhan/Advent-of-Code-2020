f = open('day_07.txt', 'r')
x = [i.strip() for i in f.readlines()]
p = [i.split(' contain ') for i in x]
z = dict()
for i in p:
    z[i[0]] = i[1].split(', ')


def bagsCount(string):
    for i in z:
        if string in i:
            x = i
            break
    t = 0
    for i in z[x]:
        if i[0] == 'n': continue
        if i[2:][-1] == '.':
            string = i[2:-1]
        else:
            string = i[2:]
        t += int(i[0]) + (int(i[0]) * (bagsCount(string)))
    return t


print(bagsCount('shiny gold bags'))
