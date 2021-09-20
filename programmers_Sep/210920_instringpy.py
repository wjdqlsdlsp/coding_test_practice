def solution(s):
    a,b = 0, 0
    for i in s:
        if i == 'y' or i =='Y':
            a +=1
        elif i =='p' or i =='P':
            b +=1
    if a == b:
        return True
    else:
        return False
print(solution("pPoooyY"))