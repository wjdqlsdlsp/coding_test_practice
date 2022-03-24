from collections import defaultdict
def solution(id_list, report, k):
    arr = dict()
    for i in id_list:
        arr[i] = 0
    report_list = defaultdict(set)
    for tmp in report:
        a, b =tmp.split()
        report_list[b].add(a)

    for i in report_list.keys():
        if len(report_list[i]) >= k:
            for j in report_list[i]:
                arr[j]+=1
    
    return [*arr.values()]

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))