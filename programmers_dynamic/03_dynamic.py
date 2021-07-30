def solution(money):
    if len(money) == 3:
        return max(money)
    else:
        with0 = [money[0], money[1], money[0] + money[2], max(money[0], money[1]) + money[3]]
        wout0 = [money[1], money[2], money[1] + money[3]]
        for m in money[4:]:
            with0.append(max(with0[-2], with0[-3]) + m)
            wout0.append(max(wout0[-2], wout0[-3]) + m)

    return max(with0[-3], with0[-2], wout0[-1])

# print(solution([1,2,3,1]), 4)
# print(solution([1,1,4,1,4]), 8)
# print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000)
# print(solution([1000,1,0,1,2,1000,0]), 2001)
# print(solution([1000,0,0,0,0,1000,0,0,0,0,0,1000]), 2000)

print(solution([1, 1, 4, 1, 4]))
# print(solution([0,0,0,0,100,0,0,100,0,0,1,1]), 201)
# print(solution([11,0,2,5,100,100,85,1]), 198)
# print(solution([1,2,3]), 3)
# print(solution([91,90,5,7,5,7]), 104)
# print(solution([90,0,0,95,1,1]), 185)