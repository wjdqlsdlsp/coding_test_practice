def solution(n, lost, reserve):
    answer = 0
    arr =[0]*n
    for i in range(n):
        if i+1 in lost: arr[i] -=1
        if i+1 in reserve: arr[i] +=1
    for index in range(len(arr)):
        if arr[index] >=0: answer +=1
        elif arr[index] == -1 and index-1 >=0 and arr[index-1] ==1:
            arr[index], arr[index-1],answer =arr[index] +1, arr[index-1]-1, answer+1
        elif arr[index] == -1 and index+1 <len(arr) and arr[index+1] ==1:
            arr[index], arr[index+1],answer =arr[index] +1, arr[index+1]-1, answer+1
    return answer


print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))
