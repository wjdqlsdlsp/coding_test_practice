import bisect
q,c,d,e=[],[],[],[]
for _ in range(int(input())):
    i,t=map(int,input().split())
    q.append((i,t))
q.sort()
for _,t in q:
    s=bisect.bisect_left(c,t)
    if len(c)!=s: c[s]=t
    else: c.append(t)
    d.append(s+1)
s=len(c)
print(len(q)-s)

for i in range(len(d)-1,-1,-1):
    if d[i]==s:s-=1
    else:e.append(q[i][0])
for i in e[::-1]:
    print(i)