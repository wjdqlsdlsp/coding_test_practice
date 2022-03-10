import sys

n, m = map(int, sys.stdin.readline().split())
max_tree = [0] * (n*4)
min_tree = [0] * (n*4)
arr = [int(sys.stdin.readline()) for _ in range(n)]

def update(node, start, end, index):
    global max_tree
    if start == end:
        max_tree[node] = arr[start]
        return max_tree[node]
    mid = (start+ end) // 2
    max_tree[node] = max(update(node*2, start, mid, index), update(node*2+1, mid+1, end, index))
    return max_tree[node]

def update1(node, start, end, index):
    global min_tree
    if start == end:
        min_tree[node] = arr[start]
        return min_tree[node]
    mid = (start+ end) // 2
    min_tree[node] = min(update1(node*2, start, mid, index), update1(node*2+1, mid+1, end, index))
    return min_tree[node]

update(1, 0,n-1, 1)
update1(1, 0,n-1, 1)

def query( start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return max_tree[node]
    
    mid = (start+end)//2
    return max(query(start, mid, node*2,left, right),
                query(mid+1, end, node*2+1, left, right))

def query1( start, end, node, left, right):
    if left > end or right < start:
        return sys.maxsize
    if left <= start and end <= right:
        return min_tree[node]
    
    mid = (start+end)//2
    return min(query1(start, mid, node*2,left, right),
                query1(mid+1, end, node*2+1, left, right))

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(query1(0, n-1, 1, a-1,b-1),query(0, n-1, 1, a-1,b-1))
