import sys
n, m = map(int, sys.stdin.readline().split())

color = dict()

for i in range(n):
    cur = color
    for ch in sys.stdin.readline().split()[0]:
        cur.setdefault(ch, dict())
        cur = cur[ch]
    cur.setdefault("*", None) 

name = set()
for _ in range(m):
    name.add(sys.stdin.readline().split()[0])

t = int(sys.stdin.readline())

for i in range(t):
    tmp = sys.stdin.readline().split()[0]
    cur = color
    answer = "No"
    for i in range(len(tmp)):
        ch = tmp[i]
        if ch not in cur:
            break

        cur = cur[ch]
        if "*" in cur:
            if i < len(tmp) - 1 and tmp[i+1:] in name:
                answer = "Yes"
                break
    
    print(answer)
    