def solution(scores):
    arr = [[] for _ in range(len(scores))]
    for score in scores:
        for i in range(len(scores)):
            arr[i].append(score[i])
    average_score = []
    for index,score in enumerate(arr):
        if score[index] == min(score) or score[index] == max(score):
            pop_num = score.pop(index)
            if pop_num in score:
                score.append(pop_num)
        average_score.append(sum(score)/len(score))
    tmp = list(map(lambda x : 'A' if x >=90 else ('B' if x >=80  else ('C' if x>= 70 else ('D' if x >=50 else 'F'))),average_score))

    return "".join(tmp)

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
# print(solution([[50,90],[50,87]]))
# print(solution([[70,49,90],[68,50,38],[73,31,100]]))

