f = open('day_07.txt', 'r')
x = [i.strip() for i in f.readlines()]
p = [i.split(' contain ') for i in x]
res = []
def recur(string):
    for i in p:
        if string in i[1]:
            res.append(i[0][:-1])
            recur(res[len(res)-1])
recur('shiny gold')
print(len(set(res)))
