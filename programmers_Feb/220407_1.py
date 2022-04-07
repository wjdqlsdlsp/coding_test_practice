def gca(a, b):
    if b == 0:
        return a
    return gca(b, a%b)

def solution(arr):
    n1 = arr[0]
    for n2 in arr[1:]:
        gca_num = gca(n1, n2)
        n1 = (n1 // gca_num) * (n2 // gca_num) * gca_num 
    return n1

print(solution([2,6,8,14]))
'''
72 30
30 12
12 6
6 0

'''

