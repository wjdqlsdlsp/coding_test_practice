def solution(s):
    answer = ''
    str_len = int(len(s)/2)
    if len(s) %2 ==0:
        return s[str_len-1 : str_len+1]
    else:
        return s[str_len]

print(solution("abcdef"))