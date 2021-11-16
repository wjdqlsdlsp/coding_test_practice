def solution(a, s):
    def get_b(b):
        N = len(b)
        i = 1
        ct = 1
        record = [{} for _ in range(N)]
        record[0][b[0]] = (1,None)
        while i<N:
            record[i][b[i]] = (ct,i-1)
            var = b[i]
            j = i-1
            while record[j].get(var,None)!=None:
                diff = record[j][var]
                ct += diff[0]
                var *= 2
                record[i][var] = diff
                j = diff[1]
                if j == None:
                    break
            i+=1
        return ct%(10**9 + 7)


    answer = []
    subsum = 0
    for x in s:
        b = a[subsum:subsum+x]
        subsum+=x
        answer.append(get_b(b))
    return answer