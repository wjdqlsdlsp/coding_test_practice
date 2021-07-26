def solution(numbers):
    numbers = list(map(lambda x : x%1001, numbers))
    t= sorted(list(map(lambda x : str(x)*4,numbers)),reverse=True)
    t = list(map(lambda x : x[:len(x)//4],t))
    answer = int("".join(t))

    return str(answer)

print(solution([998,9,999]))
