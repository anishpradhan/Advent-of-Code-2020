f = open('day_06.txt', 'r')
x = [i.strip() for i in f.readlines()]
z = [[]]
for i in range(len(x)):
    if x[i] == '':
        z.append(list())
        continue
    for j in x[i]:
        z[len(z)-1].append(j)
z = [len(set(i)) for i in z]
print(sum(z))