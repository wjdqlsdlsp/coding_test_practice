def solution(n):
    answer = 0
    arr = []
    while n>=3:
        n, a = divmod(n,3)
        arr.append(str(a))
    arr.append(str(n))

    
    return int("".join(arr),3)

print(solution(45))
print(solution(125))
