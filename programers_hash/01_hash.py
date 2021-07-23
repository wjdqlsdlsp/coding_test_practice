participants = ["mislav", "stanko", "mislav", "ana"]
completions = ["stanko", "ana", "mislav"]

def solution(participant, completion):
    hash = {}

    for i in range(len(participant)):
        if participant[i] not in hash.keys():
            hash[participant[i]] = [True]
        else:
            hash[participant[i]].append(True)

    for i in range(len(completion)):
        hash[completion[i]].pop()

    answer = ''
    for key, values in hash.items():
        if len(values) >0:
            answer += key
    return answer

print(solution(participants, completions))