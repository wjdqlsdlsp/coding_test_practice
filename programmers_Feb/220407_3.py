def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr2[0])):
            tmp.append(sum([*map(lambda x,y: x*y, arr1[i], [*map(lambda x : x[j], arr2)])]))
        answer.append(tmp)
    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))

'''
3*2 - 2*2

'''