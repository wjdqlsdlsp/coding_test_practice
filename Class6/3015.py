import sys
n = int(sys.stdin.readline())

result = 0
stack = []
for _ in range(n):
    h = int(sys.stdin.readline())
    while stack and stack[-1][0] < h:
        result += stack.pop()[1]
    
    if stack and stack[-1][0] == h:
        cnt = stack.pop()[1]
        result +=cnt
        
        if len(stack) != 0:
            result +=1
        stack.append((h, cnt+1))
    
    else:
        if len(stack)!= 0:
            result+=1
        stack.append((h, 1))

print(result) 