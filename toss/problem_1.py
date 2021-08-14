from collections import Counter
def solution(s):
    s = s.lower()
    arr = sorted(list(Counter(s).items()), key= lambda x : x[1],reverse=True)
    max_num = arr[0][1]
    output_arr1 = []

    tos_arr = {'t':0,'o':0,'s':0}
    for value in arr:
        if value[1] ==max_num:
            if value[0] in tos_arr.keys():
                tos_arr[value[0]] +=1
            else:
                output_arr1.append(value[0])

    output = []
    if tos_arr['t'] == 1:
        output.append('T')
    if tos_arr['o'] == 1:
        output.append('O')
    if tos_arr['s'] == 1:
        output.append('SS')
    output_arr1 = sorted(output_arr1)
    output += output_arr1
    return "".join(output)

print(solution("baaaabbbssdd"))