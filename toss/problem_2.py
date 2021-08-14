def solution(param0):
    answer = [-1 for _ in range(len(param0))]
    for i in range(0, len(param0)):
        num, rest_money = divmod(100000000, param0[i])
        bank = 0
        first_buy = param0[i]
        for j in range(i+1, len(param0)):
            my_money = rest_money + num*param0[j]-bank
            if bank == 0 and param0[j] <= first_buy*0.5:
                bank = 50000000
                plus, rest_money = divmod(bank + rest_money, param0[j])
                num +=plus
            if my_money >= 1000000000:
                answer[i] = j-i
                break
    
    return answer

print(solution([34000,78000, 48000, 27000, 11000, 285000, 320000, 335100]))