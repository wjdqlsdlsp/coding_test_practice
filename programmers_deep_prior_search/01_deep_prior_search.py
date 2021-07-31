count = 0
def cal(now, numbers,target):
    global count
    if len(numbers) ==0:
        if now  == target:
            count+=1
        return
    cal(now + numbers[0],numbers[1:],target)
    cal(now - numbers[0],numbers[1:],target)

def solution(numbers, target):
    cal(0,numbers,target)
    return count


print("solution ",solution([1, 1, 1, 1, 1],3))