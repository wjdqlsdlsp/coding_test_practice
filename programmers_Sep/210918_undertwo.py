def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 ==0:
            answer.append(num+1)
        else:
            a = bin(num)[2:]
            count =0
            for i in range(len(a)-1, -1, -1):
                if a[i] == '0':
                    break
                else:
                    count+=1
            
            answer.append(max(num + 2 ** (count-1), num+1))
    return answer

print(solution([2,7]))