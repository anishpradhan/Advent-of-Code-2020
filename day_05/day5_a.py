f = open('day_05.txt', 'r')
seat_row = [i.strip() for i in f.readlines()]

def get_all_id(seat_row):
    final_result = {}
    for i in seat_row:
        row, col = [0, 127], [0, 7]
        for j in i:
            if j == 'F': row[0], row[1] = row[0], int((row[1] + row[0]) / 2)
            elif j == 'B': row[0], row[1] = int((row[1] + row[0]) / 2) + 1, row[1]
            elif j == 'L': col[0], col[1] = col[0], int((col[1] + col[0]) / 2)
            elif j == 'R': col[0], col[1] = int((col[1] + col[0]) / 2) + 1, col[1]
        final_result[row[0], col[0]] = ((row[0] * 8) + col[0])
    return final_result

print(f'The highest seat ID on a boarding pass is "{max(get_all_id(seat_row).values())}"')
