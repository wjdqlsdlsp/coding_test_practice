def solution(s):
    answer = [0,0]
    while s != '1':
        print(s)
        tmp = 0
        for i in s:
            if i == '1':
                tmp +=1
            else:
                answer[1] +=1
        s = bin(tmp)[2:]
        answer[0] +=1
    return answer


print(solution("110010101001"))