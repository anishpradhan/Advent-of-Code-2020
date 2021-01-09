inp = open('day_12.txt', 'r')
x = [i.strip() for i in inp]
directions = ['E','S','W','N']
def change_wp(w, xp,yp, val):
    if w == 'E': xp+=val
    elif w == 'W': xp-=val
    elif w == 'N': yp+=val
    elif w == 'S': yp-=val
    return xp,yp

def part_1(x):
    xp, yp, facing = 0,0, 'E'
    for i in x:
        direction, val = i[0], int(i[1:])
        if direction in directions:
            xp, yp = change_wp(direction, xp,yp, val)
        elif direction == 'F':
            xp, yp = change_wp(facing, xp,yp, val)
        elif direction == 'R':
            current_dir = directions.index(facing)
            val /= 90
            facing = directions[int((current_dir+val)%4)]
        elif direction == 'L':
            current_dir = directions.index(facing)
            val /= 90
            facing = directions[int((current_dir-val)%4)]
    distance = abs(xp)+abs(yp)
    return distance

def part_2(x):
    x_units, y_units = 10,1
    xp, yp = 0,0
    for i in x:
        direction, val = i[0], int(i[1:])
        if direction in directions:
            x_units, y_units = change_wp(direction,x_units,y_units, val) 
        if direction == 'F':
            for j in range(int(val)):
                xp += x_units
                yp += y_units
        elif direction == 'R':
            val /= 90
            for j in range(int(val)):
                x_units, y_units = y_units, -x_units
        elif direction == 'L':
            val /= 90
            for j in range(int(val)):
                x_units, y_units = -y_units, x_units
    result = abs(xp)+abs(yp)
    return result

print(part_1(x))
print(part_2(x))
