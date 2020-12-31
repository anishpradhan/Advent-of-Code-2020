import math
from itertools import groupby
import operator
f = open('day_10.txt', 'r')
x = [int(i.strip()) for i in f.readlines()]
z = list(set(x))
r = list(map(operator.sub, z+[z[-1]+3], [min(z)-1]+z))
#Part 1
diff = r.count(1)*r.count(3)
print('Part a:',diff)
#Part 2
print('Part b:',math.prod(
    (2**(len(m)-1)) - (len(m)==4)
for i,j in groupby(r)
    if i==1 and len((m:=list(j)))>1
))
