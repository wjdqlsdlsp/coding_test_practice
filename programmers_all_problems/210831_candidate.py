from itertools import combinations
def solution(relation):
    answer, row_len, columns_len =0, len(relation), len(relation[0])
    a = [list(map(lambda x : x[i], relation)) for i in range(columns_len)]
    com_n =1
    range_arr = list(range(columns_len))
    answer_arr = []
    while com_n <= len(range_arr):
        arrs = list(combinations(range_arr,com_n))
        for indexs in arrs:
            arr = []
            for index in indexs:
                arr.append(a[index])
            tmp = list(map(lambda x : "".join(x), [list(map(lambda x : x[i],arr)) for i in range(row_len)]))
            if len(set(tmp)) == row_len:
                check = False

                for i in range(len(indexs)):
                    t = list(combinations(indexs,i))
                    for j in t:
                        if j in answer_arr:
                            check = True
                            break
                if check == False:
                    answer_arr.append(indexs)
        com_n+=1
    return len(answer_arr)
print(solution([['a','1','aaa','c','ng'],['b','1','bbb','c','g'],['c','1','aaa','d','ng'],['d','2','bbb','d','ng']]))