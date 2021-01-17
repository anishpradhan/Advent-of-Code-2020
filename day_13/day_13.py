inp = open('day_13.txt', 'r')
s = [i.strip().split(',') for i in inp]
time_stamp = int(s[0][0])
busses = [(i,int(x)) for i,x in enumerate(s[1]) if x!='x']
# part 1
t  = time_stamp
while True:
    for i,j in busses:
        if t%int(j) == 0: break
    else:
        t+=1
        continue
    break
# part 2
i,d = 0,1
for offset, bus in busses:
    while True:
        i += d
        if (i + offset) % bus == 0:
            d *= bus
            break

print('part 1:',(t-time_stamp)*int(j))
print('part 2:',i)

