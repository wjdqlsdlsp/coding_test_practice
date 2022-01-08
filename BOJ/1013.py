# 반례를 못찾겠어서 다른사람이 한 코드를 참고하니
# 당황스러웠따. fullmatch와 match에 차이점을 다시 배워갑니다.

'''
import re
t = int(input())
for i in range(t):
    a = input()
    p = re.compile('(100+1+|01)+')
    if p.fullmatch(a):
        print("YES")
    else:
        print("NO")
'''

n = int(input())

arr = set()
def DFS(now, goal):
    if now == goal:
        arr.add('YES')
        return
    
    if now != goal[:len(now)]:
        arr.add('NO')
        return 
    
    DFS(now+'01', goal)
    tmp = now +'100'
    while tmp in goal[:len(tmp)]:
        tmp += '0'
    
    tmp = tmp[:-1]
    
    while tmp in goal[:len(tmp)]:
        DFS(tmp+'1', goal)
        tmp += '1'
    

for _ in range(n):
    a = input()
    DFS('', a)
    if 'YES' in arr:
        print('YES')
    else:
        print('NO')
    arr.clear()