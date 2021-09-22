def solution(dartResult):
    q = []
    result = []
    for i in dartResult:
        if i == 'S':
            num = int("".join(q))
            q = []
            result.append(num)
        elif i == 'D':
            num = int("".join(q))
            num = num**2
            q = []
            result.append(num)
        elif i == 'T':
            num = int("".join(q))
            num = num**3
            q = []
            result.append(num)
        elif i == "*":
            if len(result) >1:
                result[-2] = result[-2]*2

            result[-1] = result[-1]*2
        elif i == "#":
            result[-1] = result[-1] * -1
        else:
            q.append(i)
    return sum(result)

print(solution("1S2D*3T"))