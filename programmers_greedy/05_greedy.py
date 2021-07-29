def solution(n, costs):
    answer = 0
    costs =sorted(costs, key= lambda x : x[2],reverse=True)
    (a,b,c) = costs.pop()
    connect = [[a,b]]
    count = 2
    answer +=c
    while count<n:
        a_parenct, b_parent = -1, -1
        (a,b,c) = costs.pop()
        for i in range(len(connect)):
            if a in connect[i]:
                a_parenct = i
            if b in connect[i]:
                b_parent = i
        # 부모노드가 둘다 없을 때
        if a_parenct ==-1 and b_parent ==-1:
            connect.append([a,b])
            answer +=c
            count +=1
        # a부모노드가 없을 때
        elif a_parenct ==-1:
            connect[b_parent].append(a)
            answer +=c
            count +=1
        # b부모노드가 없을 때
        elif b_parent ==-1:
            connect[a_parenct].append(b)
            answer +=c
            count +=1
        elif a_parenct != b_parent:
            connect[a_parenct] = connect[a_parenct] + connect[b_parent]
            connect.pop(b_parent)
            answer +=c
            count +=1

    return answer

# print(solution(	4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
print(solution(	4, [[0,1,9],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
