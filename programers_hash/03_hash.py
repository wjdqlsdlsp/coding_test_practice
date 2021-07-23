
def solution(clothes):
    dict = {}
    for i in range(len(clothes)):
        if clothes[i][1] not in dict.keys():
            dict[clothes[i][1]] = 2
        else:
            dict[clothes[i][1]] +=1

    mul = list(dict.values())
    answer = 1
    for i in mul:
        answer *= i
    return answer -1


print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))