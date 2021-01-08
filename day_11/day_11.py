from copy import deepcopy
f = open('day_11.txt', 'r')

nex = [i.strip() for i in f.readlines()]
nums = [(i,j) for j in (-1,0,1) for i in (-1,0,1) if (i,j)!=(0,0)]
x = []
for i in nex:
    x.append(list())
    for j in i:
        x[-1].append(j)

def part_1(mat,r,c):
    global nums
    neighs = []
    for s in nums:
        i,j = s[0],s[1]
        if (0<= r+i < len(mat)) and (0<= c+j < len(mat[r])):
            if mat[r+i][c+j] == "#":
                neighs.append('#')
                continue
    return neighs

def part_2(mat,r,c):
    global nums
    visible_neighs = []
    for s in nums:
        i,j = s[0],s[1]
        if (0<=r+i < len(mat)) and (0<= c+j < len(mat[r])):
            if mat[r+i][c+j] != ".":
                visible_neighs.append(mat[r+i][c+j])
                continue
            else:
                while True:
                    if (0 <= r+i+s[0] <len(mat)) and (0 <= c+j+s[1] < len(mat[i])):
                        if (mat[r+i+s[0]][c+j+s[1]]=='.'): 
                            i+=s[0]
                            j+=s[1]
                            continue
                        else:
                            visible_neighs.append(mat[r+i+s[0]][c+j+s[1]])
                            break
                    else: break

    return visible_neighs


def next_step(mat, part, number):
    new = deepcopy(mat)
    global nums
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            occ = part(mat,r,c)
            if mat[r][c]== '#':
                occupied = occ.count('#')
                if occupied >= number:
                    new[r][c] = "L"
                    continue
            elif mat[r][c]=='L':
                occupied = occ.count('#')
                if not occupied:
                    new[r][c] = "#"
    return new

def ans(part, number):

    new_mat = x
    counter = -1
    while True:
        counter +=1
        prev = new_mat
        new_mat = next_step(new_mat, part, number)
        if new_mat == prev:
            break
    result = ''.join(i for i in list(map(''.join, new_mat)))
    return result.count('#')
    
print('part 1:', ans(part_1, 4))
print('part 2:', ans(part_2, 5))
