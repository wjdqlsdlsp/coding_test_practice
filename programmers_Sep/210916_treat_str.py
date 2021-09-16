def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i > '0' and i < '9':
                break
        else:
            return True
                
    return False

print(solution("a234"))