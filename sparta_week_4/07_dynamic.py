input = 20

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    if n not in memo.keys():
        tmp_n = n
        while tmp_n not in memo.keys():
            tmp_n -= 1
        
        while tmp_n != n:
            memo[tmp_n+1] = memo[tmp_n] + memo[tmp_n-1]
            tmp_n += 1

        return memo[n]
    return memo[n]


print(fibo_dynamic_programming(input, memo))