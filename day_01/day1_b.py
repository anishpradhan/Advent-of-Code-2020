f = open('day_01.txt', 'r')

list = [int(i) for i in f]
a = set(i for i in list)

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if 2020-list[i]-list[j] in a:
            print((2020-list[i]-list[j])*list[i]*list[j])
            break
    else:
        continue
    break
