import sys
from collections import deque
import copy
h,w = map(int, sys.stdin.readline().split())

m = []
for i in range(h):
    tmp = sys.stdin.readline().split()[0]
    if 'B' in tmp:
        b_p = (tmp.index('B'), i)
    if 'R' in tmp:
        r_p = (tmp.index('R'), i)
    tmp = list(tmp)
    m.append(tmp)

def down(r_p, b_p, m):
    r_x, r_y = r_p
    b_x, b_y = b_p
    if r_y > b_y:
        while m[r_y+1][r_x] == '.' or m[r_y+1][r_x] == 'O':
            if m[r_y+1][r_x] == 'O':
                r_y, r_x = -1, -1
                break
            r_y +=1

        while (m[b_y+1][b_x] == '.' or m[b_y+1][b_x] == 'R' or m[b_y+1][b_x] == 'O') \
            and (b_y+1,b_x) != (r_y, r_x):
            if m[b_y+1][b_x] == 'O':
                b_y, b_x = -1, -1
                break
            b_y +=1
    else:
        while m[b_y+1][b_x] == '.' or m[b_y+1][b_x] == 'O':
            if m[b_y+1][b_x] == 'O':
                b_y, b_x = -1, -1
                break
            b_y +=1

        while (m[r_y+1][r_x] == '.' or m[r_y+1][r_x] == 'B' or m[r_y+1][r_x] == 'O') \
            and (r_y+1,r_x) != (b_y, b_x):
            if m[r_y+1][r_x] == 'O':
                r_y, r_x = -1, -1
                break
            r_y +=1
    return r_x, r_y, b_x, b_y

def up(r_p, b_p, m):
    r_x, r_y = r_p
    b_x, b_y = b_p
    if r_y < b_y:
        while m[r_y-1][r_x] == '.' or m[r_y-1][r_x] == 'O':
            if m[r_y-1][r_x] == 'O':
                r_y, r_x = -1, -1
                break
            r_y -=1

        while (m[b_y-1][b_x] == '.' or m[b_y-1][b_x] == 'R' or m[b_y-1][b_x] == 'O') \
            and (b_y-1,b_x) != (r_y, r_x):
            if m[b_y-1][b_x] == 'O':
                b_y, b_x = -1, -1
                break
            b_y -=1
    else:
        while m[b_y-1][b_x] == '.' or m[b_y-1][b_x] == 'O':
            if m[b_y-1][b_x] == 'O':
                b_y, b_x = -1, -1
                break
            b_y -=1

        while (m[r_y-1][r_x] == '.' or m[r_y-1][r_x] == 'B' or m[r_y-1][r_x] == 'O') \
            and (r_y-1,r_x) != (b_y, b_x):
            if m[r_y-1][r_x] == 'O':
                r_y, r_x = -1, -1
                break
            r_y -=1
    return r_x, r_y, b_x, b_y

def left(r_p, b_p, m):
    r_x, r_y = r_p
    b_x, b_y = b_p
    if r_x < b_x:
        while m[r_y][r_x-1] == '.' or m[r_y][r_x-1] == 'O':
            if m[r_y][r_x-1] == 'O':
                r_y, r_x = -1, -1
                break
            r_x -=1

        while (m[b_y][b_x-1] == '.' or m[b_y][b_x-1] == 'R' or m[b_y][b_x-1] == 'O') \
            and (b_y,b_x-1) != (r_y, r_x):
            if m[b_y][b_x-1] == 'O':
                b_y, b_x = -1, -1
                break
            b_x -=1
    else:
        while m[b_y][b_x-1] == '.' or m[b_y][b_x-1] == 'O':
            if m[b_y][b_x-1] == 'O':
                b_y, b_x = -1, -1
                break
            b_x -=1

        while (m[r_y][r_x-1] == '.' or m[r_y][r_x-1] == 'B' or m[r_y][r_x-1] == 'O') \
            and (r_y,r_x-1) != (b_y, b_x):
            if m[r_y][r_x-1] == 'O':
                r_y, r_x = -1, -1
                break
            r_x -=1
    return r_x, r_y, b_x, b_y

def right(r_p, b_p, m):
    r_x, r_y = r_p
    b_x, b_y = b_p
    if r_x > b_x:
        while m[r_y][r_x+1] in ['.', 'O']:
            if m[r_y][r_x+1] == 'O':
                r_y, r_x = -1, -1
                break
            r_x +=1

        while (m[b_y][b_x+1] == '.' or m[b_y][b_x+1] == 'R' or m[b_y][b_x+1] == 'O') \
            and (b_y,b_x+1) != (r_y, r_x):
            if m[b_y][b_x+1] == 'O':
                b_y, b_x = -1, -1
                break
            b_x +=1
    else:
        while m[b_y][b_x+1] in ['.', 'O']:
            if m[b_y][b_x+1] == 'O':
                b_y, b_x = -1, -1
                break
            b_x +=1

        while (m[r_y][r_x+1] in ['.', 'B','O']) and (r_y,r_x+1) != (b_y, b_x):
            if m[r_y][r_x+1] == 'O':
                r_y, r_x = -1, -1
                break
            r_x +=1
    return r_x, r_y, b_x, b_y

q = deque()
q.append([r_p, b_p, m, 0])
dp = set()
check = False
while q:
    r_p, b_p, m, c = q.popleft()
    if (r_p, b_p) in dp:
        continue
    dp.add((r_p, b_p))

    if c >= 10:
        break

    for func in [up, down, left, right]:
        tmp = copy.deepcopy(m)
        r_x, r_y, b_x, b_y = func(r_p, b_p, tmp)
        if b_x == -1:
            continue
        elif r_x == -1:
            check = True
            print(c+1)
            break
        tmp[r_p[1]][r_p[0]] = '.'
        tmp[b_p[1]][b_p[0]] = '.'

        tmp[r_y][r_x] = 'R'
        tmp[b_y][b_x] = 'B'
        q.append([(r_x, r_y), (b_x, b_y), tmp, c+1])

    if check:
        break

if check == False:
    print(-1)