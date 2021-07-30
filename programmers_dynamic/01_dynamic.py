dynamic = {}
answer = -1
def calculate(cur,N,count,number):
    global answer
    if cur == number:
        if count < answer or answer == -1:
            answer=count
        return
    if count > 8:
        return
    nn=0
    for t in range(8):
        nn=nn*10+N
        calculate(cur+nn, N, count+t+1, number)
        calculate(cur-nn, N, count+t+1, number)
        calculate(cur//nn, N, count+t+1, number)
        calculate(cur*nn, N, count+t+1, number)

def solution(N, number):
    calculate(0,N,0,number)
    return answer

print(solution(5, 12))