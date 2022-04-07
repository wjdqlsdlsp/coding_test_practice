def solution(s):
    answer = []

    for tmp in s.split(" "):
        tmp = tmp.capitalize()
        answer.append(tmp)

    return " ".join(answer)

print(solution("3people unFollowed  me"))
print(solution("for the last week"))
