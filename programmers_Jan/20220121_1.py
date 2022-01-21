def is_palin(s_left, s_right):
    s_left = s_left[::-1]
    i = 0
    count = 0
    while i<len(s_left) and i < len(s_right) and s_left[i] == s_right[i]:
        i+=1
        count+=2

    
    return count

def solution(s):
    if len(s) == 1:
        return 1
    answer = 0
    for i in range(1,len(s)):
        # print(s[:i],"|", s[i:],"|", s[:i],"|", s[i+1:])
        answer = max(answer, is_palin(s[:i],s[i:]), is_palin(s[:i], s[i+1:])+1)
    return answer

print(solution("abcdcba"))
print(solution("abacde"))
