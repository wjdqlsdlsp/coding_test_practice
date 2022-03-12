import math

def solution(n, edges):
    answer = 0
    tree = [[] for i in range(n+1)]

    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    logn = int(math.log2(n)) +1
    parent = [[0]* logn for _ in range(n+1)]
    depth = [0] * (n+1)
    check = [0] * (n+1)
    
    depth[0] = -1
    depth[1] = 0

    def make_tree(cur_node, parent_node):
        depth[cur_node] = depth[parent_node] + 1
        check[cur_node] = 1
    
        for b in tree[cur_node]:
            if check[b] != 1:
                parent[b][0] = cur_node
                make_tree(b, cur_node)
    
    make_tree(0, 0)
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

    for i in range(n):
        for j in range(n):
            tmp = lca(i, j)
            s = depth[i]- depth[tmp] + depth[j] - depth[tmp] - 1
            if s >0:
                answer +=s
    return answer

print(solution(4, [[2,3],[0,1],[1,2]]))