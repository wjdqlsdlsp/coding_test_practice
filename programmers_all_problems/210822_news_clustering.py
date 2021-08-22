from collections import Counter
def solution(str1, str2):
    str1 , str2 = str1.lower(), str2.lower()
    str1_arr, str2_arr= [],[]

    for i in range(0,len(str1)-1):
        if 'a'<= str1[i] <='z' and  'a'<= str1[i+1] <='z':
            str1_arr.append(str1[i:i+2])

    for i in range(0,len(str2)-1):
        if 'a'<= str2[i] <='z' and  'a'<= str2[i+1] <='z':
            str2_arr.append(str2[i:i+2])

    str1_arr, str2_arr = Counter(str1_arr), Counter(str2_arr)
    same_cluster, all_cluster = {}, str2_arr
    str2_keys = set(str2_arr.keys())

    for item in str1_arr.items():
        if item[0] in str2_keys:
            same_cluster[item[0]] = min(item[1], str2_arr[item[0]])
            all_cluster[item[0]] = max(item[1], str2_arr[item[0]])

        else: all_cluster[item[0]] = item[1]

    if sum(all_cluster.values()) ==0: return 65536
    return int(sum(same_cluster.values())/sum(all_cluster.values()) * 65536)

# print(solution("FRANCE", "french"))
# print(solution("handshake", "shake hands"))
# print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
