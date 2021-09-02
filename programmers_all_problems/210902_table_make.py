# 효율성 6 7 8 9 10 시간초과
from collections import deque
def move_up(dict,k,num):
    count = 0
    while count < num:
        if dict[k-1] == True:
            k-=1
            count+=1
        else:
            k -=1
    return dict, k

def move_down(dict,k,num):
    count = 0
    while count < num:
        if dict[k+1] == True:
            k+=1
            count+=1
        else:
            k +=1
    return dict, k

def solution(n, k, cmd):
    dict = {}
    delete_list = []
    for i in range(n):
        dict[i] = True
    for orders in cmd:
        if orders[0] =='U':
            num = int(orders.split(" ")[1])
            dict, k = move_up(dict,k,num)

        elif orders[0] =='D':
            count = 0
            num = int(orders.split(" ")[1])
            dict, k = move_down(dict,k,num)


        elif orders[0] =='C':
            dict[k] =False
            delete_list.append(k)
            tmp = k
            while True:
                if k >= n-1:
                    k = tmp
                    while True:
                        if k == 0:
                            break
                        if dict[k-1] == True:
                            k-=1
                            break
                        else:
                            k-=1
                    break
                elif dict[k+1] == True:
                    k+=1
                    break
                else:
                    k+=1
        else:
            pop = delete_list.pop()
            dict[pop] = True
    return "".join(['O'if i[1] == True else 'X' for i in dict.items()])

print(solution(8,3,	["C","C","C","D 1","C","C","C","C","C"]))