f = open('day_08.txt', 'r')
boot_code = [i.strip() for i in f.readlines()]
x = [i.split() for i in boot_code]
jmp_neg = [i for i in range(len(x)) if x[i][0]=='jmp' and int(x[i][1])<0]
def main(val=None):
    x = [i.split() for i in boot_code]
    ac, i = 0,0
    terminate = []
    if val:
        x[val][0]='nop'
        
    while i <= len(x)-1:
        if x[i][0] == 'nop':
            terminate.append(i)
            i+=1
            continue
        elif x[i][0] == 'acc':
            if i in terminate: break
            terminate.append(i)
            ac+=int(x[i][1])
            i+=1
        elif x[i][0] == 'jmp':
            if i in terminate: break
            terminate.append(i)
            i+=int(x[i][1])
    
    if terminate[len(terminate)-1] == len(x)-1: return (True, ac)
    else: return (False, ac)
    
# Part 1
print('Part 1:',main()[1])
#  Part 2
for i in jmp_neg:
    success, ac = main(i)
    if success:
        print('Part 2:',ac)
        break
