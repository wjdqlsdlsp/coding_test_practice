from itertools import combinations
import sys
def solution(number, k):
    number = list(number)
    number_minus = len(number) - k
    combination = list(combinations(number, number_minus))
    arr = list(map(lambda x : int("".join(x)),combination))
    return str(max(arr))

print(solution("1231234",3))

# import copy

# def solution(number, k):
#     number = list(number)
#     while k >0:
#         length = len(number)
#         max = -1
#         for i in range(length):
#             num = copy.copy(number)
#             tmp = num.pop(i)
#             tmp = int("".join(num))
#             if tmp >max:
#                 max = tmp
#                 index = i
#         number.pop(index)
#         k -=1
#     return "".join(number)

# print(solution("1924",2))