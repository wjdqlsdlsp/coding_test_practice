from collections import Counter

def solution(a):
    answer = 0
    if len(a) < 1:
        return 0
    count = Counter(a)
    for k, c in count.items():
        if c * 2 <= 0:
            continue

        index = 1
        num = 0

        while index < len(a):
            if (a[index-1] != k and a[index] != k) or a[index - 1] == a[index]:
                index +=1
                continue
            num += 2
            index += 2
        answer = max(answer, num)
    return answer

print(solution([5,2,3,3,5,3]))