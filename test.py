def solution(s, n):
    return "".join([chr(ord(i)+n) for i in s])

print(solution("AB", 1))