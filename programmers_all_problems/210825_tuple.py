def solution(s):
    answer = []
    arr = list(map(lambda x : x.replace(",{","").replace("{",""), s[1:-1].split("}")))[:-1]
    tmp_arr = list(map(lambda x : [int(numeric_string) for numeric_string in x.split(",")],arr))
    arr_len = [len(arr) for arr in tmp_arr]
    tmp_dict = {}
    for i in range(len(arr_len)):
        tmp_dict[arr_len[i]] = tmp_arr[i]

    tmp_dict = sorted(tmp_dict.items(), key= lambda x : x[0])
    for i in tmp_dict:
        for j in i[1]:
            if j not in answer:
                answer.append(j)

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))