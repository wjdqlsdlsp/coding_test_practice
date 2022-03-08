import sys
sys.setrecursionlimit(int(1e5))
from collections import defaultdict
n = int(sys.stdin.readline())
arr = [[*map(int, sys.stdin.readline().split())] for _ in range(n-1)]
tree = defaultdict(list)
parent = [[0]*21 for _ in range(n+1)]
depth = [0 for i in range(n+1)]
dp_lists = [0 for i in range(n+1)]
check = [0 for i in range(n+1)]
dp_lists[1] = 0
depth[1] = 0
for a,b,c in arr:
    tree[a].append([b, c])
    tree[b].append([a, c])
depth[0] = -1

def find_depth(cur_node, parent_node,value):
    depth[cur_node] = depth[parent_node]+1
    check[cur_node] = 1
    if cur_node != 1:
        dp_lists[cur_node] += dp_lists[parent_node] + value
    for b, c in tree[cur_node]:
        if check[b] != 1:
            parent[b][0] = cur_node
            find_depth(b, cur_node,c)

def set_parent():
    find_depth(1,0,0)
    for i in range(1, 21):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]
set_parent()

def LCA(a,b):
    if depth[a] > depth[b]:
        a,b = b,a
    for i in range(20,-1,-1):
        if depth[b] - depth[a] >= (1<<i):
            b = parent[b][i]
    if a==b:
        return a

    for i in range(20,-1,-1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]


m = int(input())

for i in range(m):
    a,b = map(int,input().split())
    print(dp_lists[a] + dp_lists[b] - 2*dp_lists[LCA(a,b)])
