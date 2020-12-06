from collections import Counter
f = open('day_06.txt', 'r')
x = [i.strip() for i in f.readlines()]
z = [[]]
for i in range(len(x)):
    if x[i] == '':
        z.append(list())
        continue
    z[len(z)-1].append(x[i])
r = ["".join(i) for i in z]
count = 0
for i in range(len(r)):
    counter = 0
    for j in Counter(r[i]).items():
        if j[1]==len(z[i]):
            counter += 1
    count+=counter

print(count)