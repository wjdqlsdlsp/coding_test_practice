# 시간초과
# min_num, max_num = map(int, input().split())
# count = 0
# for num in range(min_num, max_num+1):
#     for i in range(2, num//2+1):
#         tmp = i**2
#         if num%tmp == 0:
#             break
#     else:
#         count+=1
# print(count)

# 에라토스테네스의 체
min_num, max_num = map(int, input().split())
arr = [1 for i in range(max_num-min_num+1)]
count = 0
i = 2

while i**2 <= max_num:
    s = min_num // i**2
    while s * (i**2) <= max_num:
        if s * (i**2) - min_num >= 0 and \
            s * (i**2) - min_num <= max_num - min_num:
            arr[s * (i**2) -min_num] = 0
        s +=1
    i+1
print(sum(arr))