import sys
import math
sys.setrecursionlimit(int(1e5))

n = int(sys.stdin.readline())
tree = [[] for i in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

logn = int(math.log2(n)) +1
parent = [[0]*logn for _ in range(n+1)]
depth = [0 for i in range(n+1)]
check = [0 for i in range(n+1)]

depth[0] = -1
depth[1] = 0

def make_tree(cur_node, parent_node):
    depth[cur_node] = depth[parent_node] +1
    check[cur_node] = 1

    for b in tree[cur_node]:
        if check[b] != 1:
            parent[b][0] = cur_node
            make_tree(b, cur_node)

make_tree(1, 0)
for i in range(1, logn):
    for j in range(1, n+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a,b):
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(logn-1, -1, -1):
        if depth[b] - depth[a] >= (1<<i):
            b = parent[b][i]

    if a == b:
        return a
    
    for i in range(logn-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]


for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print(lca(a,b))