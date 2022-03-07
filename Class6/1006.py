import sys
T = int(sys.stdin.readline())
total_result = []
def make_dp(start,a,b,c):
    for i in range(start, N):
        a[i+1] = min(b[i]+1, c[i]+1)
        if arr_1[i] + arr_2[i] <= W:
            a[i+1] = min(a[i+1], a[i]+1)

        if i>0 and arr_1[i-1] +arr_1[i] <= W and arr_2[i-1] + arr_2[i] <=W:
            a[i+1] = min(a[i+1], a[i-1]+ 2)
        
        if i < N-1:
            b[i+1] = a[i+1] +1
            if arr_1[i+1] + arr_1[i] <= W:
                b[i+1] = min(b[i+1], c[i] + 1)

            c[i+1] = a[i+1]+1
            if arr_2[i+1] + arr_2[i] <= W: 
                c[i+1] = min(c[i+1], b[i] + 1)
    
    return a, b, c

for _ in range(T):
    N, W = map(int, sys.stdin.readline().split())
    arr_1 = [*map(int, sys.stdin.readline().split())]
    arr_2 = [*map(int, sys.stdin.readline().split())]
    a = [0]*(N+1)
    b = [0]*(N+1)
    c = [0]*(N+1)
    a[0] = 0
    b[0] = 1
    c[0] = 1
    a,b,c = make_dp(0, a,b,c)
    result = a[N]

    if N > 1 and arr_1[0] + arr_1[N-1] <=W:
        a[1] = 1
        b[1] = 2
        if arr_2[0] + arr_2[1] <= W:
            c[1] = 1
        else:
            c[1] = 2
        
        a,b,c = make_dp(1, a,b,c)
        result = min(result, c[N-1]+1)
    
    if N > 1 and arr_2[0] + arr_2[N-1] <= W:
        a[1]=1
        c[1]=2
        if arr_1[0] + arr_1[1] <= W:
            b[1] = 1
        else:
            b[1] =2 
        a,b,c = make_dp(1, a,b,c)
        result = min(result, b[N-1] + 1)

    if N >1 and arr_1[0] + arr_1[N-1] <= W and arr_2[0] + arr_2[N-1] <=W:
        a[1]= 0
        b[1] = 1
        c[1] = 1
        a,b,c = make_dp(1, a,b,c)
        result = min(result, a[N-1]+2)
    
    total_result.append(result)

for result in total_result:
    sys.stdout.write(str(result)+'\n')