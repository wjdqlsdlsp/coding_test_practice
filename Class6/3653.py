import sys, math
T = int(sys.stdin.readline())

def make_tree(node, start, end):
    if start == end:
        tree[node] = 1
        return tree[node]

    mid = (start+end) // 2
    tree[node] = make_tree(node*2, start, mid) + make_tree(node*2+1, mid+1, end)
    return tree[node]

def update(start, end, node, where, dif):
    if where < start or where > end:
        return -1
    tree[node] += dif
    if start == end:
        return -1

    else:
        mid = (start+end) // 2
        update(start, mid, node*2, where, dif)
        update(mid+1, end, node*2+1, where, dif)

def search(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end) // 2
    return search(start, mid, node*2, left, right) + search(mid+1, end, node*2+1, left, right) 

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    idx = [*range(n+1, 0, -1)]
    h = int(math.log2(n+m+1)) + 1
    t_size = 1<<(h+1)
    tree = [0]*t_size

    make_tree(1, 1, n+m)
    cnt = 1
    for x in map(int, sys.stdin.readline().split()):
        now = idx[x]
        idx[x] = n+cnt
        print(search(1, n+m, 1, now+1, n+cnt-1), end=" ")
        update(1, n+m, 1, now, -1)
        cnt +=1