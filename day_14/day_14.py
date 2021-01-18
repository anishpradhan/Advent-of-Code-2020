import itertools
inp = open('day_14.txt', 'r')
s = [i.strip().split(" = ") for i in inp]
data = list()
for i in s:
    if i[0]=='mask': data.append(list())
    data[-1].append(i)

part_1,part_2 = {},{}
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

for item in data: 
    mask = item[0][1]
    for p in range(1,len(item)):
        memory = item[p][0][4:-1]
        binary = bin(int(memory))
        address = binary.replace('0b',"")
        value = int(item[p][1])
        value_binary = bin(value).replace("0b","")
        
#       part 1

        test1 = [masks for masks in mask]
        for j in range(1,len(value_binary)+1):
                if test1[-j] == 'X': test1[-j] = str(value_binary[-j])
        final = "".join(k for k in test1)
        result = int(final.replace('X','0'),2)
        part_1[item[p][0][4:-1]]= result
        
#       part 2

        test = [f for f in mask]
        for y in range(1,len(address)+1):
            if test[-y] == '0': test[-y] = address[-y]
        mem = "".join(l for l in test)
        indexes = find(mem,'X')
        lst = list(itertools.product([0, 1], repeat=mem.count("X")))
        for i in lst:
            z = [j for j in mem]
            for off,index in enumerate(indexes):
                z[index] = str(i[off])
                fin = "".join(k for k in z)
            part_2[int(fin,2)] = value

print('part 1:',sum(part_1.values()))
print('part 2:',sum(part_2.values()))
