import sys
N = int(sys.stdin.readline())
arr = [[i] + [*map(int, sys.stdin.readline().split())] for i in range(1, N+1)]

parents = [i for i in range(N+1)]

x_sort = sorted([*map(lambda x : [x[0], x[1]],arr)], key=lambda x:x[1])
y_sort = sorted([*map(lambda x : [x[0], x[2]],arr)], key=lambda x:x[1])
z_sort = sorted([*map(lambda x : [x[0], x[3]],arr)], key=lambda x:x[1])

roots = []
for i in range(len(x_sort)-1):
    index1, v1 = x_sort[i][0], x_sort[i][1]
    index2, v2 = x_sort[i+1][0], x_sort[i+1][1]
    roots.append([index1, index2, abs(v1-v2)])

    index1, v1 = y_sort[i][0], y_sort[i][1]
    index2, v2 = y_sort[i+1][0], y_sort[i+1][1]
    roots.append([index1, index2, abs(v1-v2)])

    index1, v1 = z_sort[i][0], z_sort[i][1]
    index2, v2 = z_sort[i+1][0], z_sort[i+1][1]
    roots.append([index1, index2, abs(v1-v2)])


roots = sorted(roots, key=lambda x: x[2])

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a> b:
        parents[a] = b
    else:
        parents[b] = a

result = 0
for i in roots:
    a, b, c = i
    if find(a) == find(b):
        continue
    else:
        union(a,b)
        result +=c

print(result)