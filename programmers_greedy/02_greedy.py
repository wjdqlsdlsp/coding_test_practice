# 미통과
def solution(name):
    dynamic = []
    name = list(name)
    string_len = len(name)
    string = ['A']* string_len
    if string == name:
        return 0
    arr = [min(ord(name[index]) - ord('A'),ord('Z') - ord(name[index]) +1) for index in range(string_len)]

    
    right_answer= 0
    for index in range(string_len):
        right_answer += arr[index]
        string[index] = name[index]
        if string ==name:
            break
        right_answer+=1

    string = ['A']* string_len
    left_answer = arr[0]
    string[0] = name[0]
    if string == name:
        return min(left_answer,right_answer)
    left_answer+=1
    for index in range(string_len-1,0,-1):
        left_answer +=arr[index]
        string[index] = name[index]
        if string ==name:
            break
        left_answer +=1
    return min(right_answer, left_answer)

print(solution("ABABAAAAABA"))