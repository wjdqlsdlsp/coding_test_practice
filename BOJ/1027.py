'''
15
1 5 3 2 6 3 2 6 4 2 5 7 3 1 5
'''

n = int(input())

arr = [*map(int ,input().split())]
answer = 0
for index, value in enumerate(arr):
    #right
    count=0
    for i in range(index+1, n):
        a = (arr[i]-value)/(i-index)
        b = arr[i] - (a*i)
        for j in range(index+1, i):
            if arr[j] >= a*j + b:
                break
        else:
            count+=1
    # left
    for i in range(0, index):
        a = (arr[i]-value)/(i-index)
        b = arr[i] - (a*i)

        for j in range(i+1, index):
            if arr[j] >= a*j + b:
                break
        else:
            count+=1
        
    if answer < count:
        answer = count

print(answer)

'''

y = ax +b 
y = (arr[i]-arr[index])/(i-index) x + b

arr[index] - (arr[i]-arr[index])/(i-index) * i = b

'''