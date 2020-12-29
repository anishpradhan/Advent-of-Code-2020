f = open('day_09.txt', 'r')
x = [int(i.strip()) for i in f.readlines()]
test = x[25:]

def logic(arg):
    i = 0
    while i<=24:
        for j in x[arg:arg+25]:
            if x[arg:arg+25][i]+j == test[arg] and x[arg:arg+25][i]!=j :
                return True
        i+=1
# Part_1
for i in range(len(test)):
    if not logic(i):
        result = test[i]
        print('Part 1:',result)
        break

# Part_2
for i in range(len(x)-1):
    add, num = 0, list()
    break_loop = False
    while True:
        add+=x[i]
        num.append(x[i])
        if add > result:
            break
        if (add == result and len(num)>1):
            print('Part 2:',min(num)+max(num))
            break_loop = True
            break
        i+=1
    if break_loop: break
