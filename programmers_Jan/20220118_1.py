def solution(a):
    answer = 1
    min_num = min(a)
    now = a[0]
    i = 1
    while min_num != now:
        if now > a[i]:
            now = a[i]
            answer += 1
        i +=1
    
    now = a[-1]
    i = len(a)-2

    while min_num != now:
        if now > a[i]:
            now = a[i]
            answer += 1
        i -=1
    return answer

# 시간초과
# def solution(a):
#     answer = 2
#     for i in range(1, len(a)-1):
#         left, right = min(a[:i]), min(a[i+1:])
#         if a[i] < left or a[i] < right:
#             answer+=1
#     return answer

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))

# 잘못된 접근
# import copy
# dp = []
# answer = set()
# def DFS(arr, card):
#     if len(arr) == 1:
#         answer.add(arr[0])

#     if [arr,card] in dp:
#         return
#     else:
#         dp.append([arr,card])

#     for i in range(len(arr)-1):
#         tmp = copy.copy(arr)
#         if card == 1:
#             tmp2 = copy.copy(tmp)
#             tmp.pop(i)
#             tmp2.pop(i+1)
#             if arr[i] > arr[i+1]:
#                 DFS(tmp, 1)
#                 DFS(tmp2, 0)
#             else:
#                 DFS(tmp, 0)
#                 DFS(tmp2, 1)
#         else:
#             if arr[i] > arr[i+1]:
#                 pop_num = i
#             else:
#                 pop_num = i+1
            
#             tmp.pop(pop_num)
#             DFS(tmp, 0)


# def solution(a):
#     for i in range(len(a)-1):
#         tmp1 = copy.copy(a)
#         tmp2 = copy.copy(a)
#         tmp1.pop(i)
#         tmp2.pop(i+1)

#         if a[i] > a[i+1]:
#             DFS(tmp1, 1)
#             DFS(tmp2, 0)
#         else:
#             DFS(tmp1, 0)
#             DFS(tmp2, 1)

#     return len(answer)

# print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))