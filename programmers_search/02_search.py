from itertools import permutations

def is_sosu(num):
    if num == 0 or num==1:
        return False
    for i in range(2, num):
        if num%i ==0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    tmp_arr = []
    for i in range(1,len(numbers)+1):
        arr = list(permutations(numbers,i))
        for j in range(len(arr)):
            num = int("".join(arr[j]))
            if num not in tmp_arr:
                tmp_arr.append(num)
    for i in tmp_arr:
        if is_sosu(i):
            answer+=1
    return answer

print(solution("17"))

print(solution("011"))
