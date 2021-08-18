def solution(n,a,b):
    answer = 0
    arr =  [1 if i == a-1 or i == b-1 else 0 for i in range(n)]
    while arr:
        answer+=1
        arr = [arr[i] + arr[i+1] for i in range(0,len(arr),2)]
        if 2 in arr: return answer

print(solution(8,4,7))