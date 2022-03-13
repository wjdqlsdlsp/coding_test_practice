import sys

n, m, k = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
tree = [1 for i in range(n*4)]
def make_tree(start, end, node):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) //2
        tree[node] = make_tree(start, mid, node*2) * make_tree(mid+1, end, node*2 + 1) % 1000000007
    return tree[node]

def search(start, end, node, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start+end) //2
    return search(start, mid, node*2, left, right) * search(mid+1, end, node*2+1, left, right) % 1000000007

def update(start, end, index, where, dif):
    if where < start or where > end:
        return
    if start == end:
        tree[index] = dif
    else:
        mid = (start+end) // 2
        update(start, mid, index*2, where, dif)
        update(mid+1, end, index*2+1, where, dif)
        tree[index] = tree[2*index] * tree[2*index + 1] % 1000000007

make_tree(0, n-1, 1)

for _ in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(0, n-1, 1, b-1, c)

    else:
        print(search(0, n-1, 1, b-1, c-1))