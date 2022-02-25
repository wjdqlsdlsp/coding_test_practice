import sys
from collections import Counter
n, s = map(int, sys.stdin.readline().split())
arr = [*map(int, sys.stdin.readline().split())]

left_arr, right_arr = arr[:n//2],  arr[n//2:]
left_n, right_n = len(left_arr), len(right_arr)

left = {0: 0}
right = {0: 0}
result = 0

def left_dfs(i, b):
    if i == left_n:
        return
    mask = b + (1 << i)
    left[mask] = left[b] + left_arr[i]
    left_dfs(i+1, b)
    left_dfs(i+1, mask)

def right_dfs(i, b):
    if i == right_n:
        return
    mask = b + (1 << i)
    right[mask] = right[b] + right_arr[i]
    right_dfs(i+1, b)
    right_dfs(i+1, mask)


left_dfs(0, 0b0)
right_dfs(0, 0b0)

left_i, right_i = 0, 0
left_sort_count = Counter(sorted(left.values()))
left_sort = [*left_sort_count.keys()]

right_sort_count = Counter(sorted(right.values(), reverse=True))
right_sort = [*right_sort_count.keys()]

left_length, right_length = len(left_sort), len(right_sort)

print(left_sort, right_sort)

while left_i < left_length and right_i < right_length:
    if left_sort[left_i] + right_sort[right_i] == s:
        result = result + (left_sort_count[left_sort[left_i]] * right_sort_count[right_sort[right_i]])
        left_i +=1
        right_i +=1

    elif left_sort[left_i] + right_sort[right_i] > s:
        right_i +=1
    
    else:
        left_i += 1

if s == 0:
    print(result - 1)
else:
    print(result)