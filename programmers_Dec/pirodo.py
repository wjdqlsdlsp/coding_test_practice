from itertools import permutations
def solution(k, dungeons):
    arr = [*permutations(dungeons,len(dungeons))]

    max_count = 0
    for ep in arr:
        count, life = 0, k
        for a,b in ep:
            if life >= a:
                count += 1
                life -= b
            else:
                if max_count < count:
                    max_count = count
        else:
            if max_count < count:
                max_count = count
    return max_count


print(solution(80, [[80,20],[50,40],[30,10]]))