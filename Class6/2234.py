import sys
Maxsize = 1000001
tree = [0]*(Maxsize*4)

def update(node, target, start, end, diff):
    if target < start or target > end:
        return
    tree[node] += diff
    if start == end:
        return
    mid = (start+end)//2
    update(node*2, target, start, mid, diff)
    update(node*2+1, target, mid+1, end, diff) 

def query(node, target, start, end):
    if start == end:
        return start
    mid = (start+end) // 2
    if target <= tree[node*2]:
        return query(node*2, target, start, mid)
    else:
        return query(node*2+1, target -tree[node*2], mid+1, end)


for _ in range(int(sys.stdin.readline())):
    tmp = [*map(int, sys.stdin.readline().split())]
    if tmp[0] == 2:
        b, c = tmp[1], tmp[2]
        update(1, b, 1, Maxsize, c)
    else:
        b = tmp[1]
        pop_num = query(1, b, 1, Maxsize)
        print(pop_num)
        update(1, pop_num, 1, Maxsize, -1)
