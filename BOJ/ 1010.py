n = int(input())

for _ in range(n):
    num = input()
    a, b = num.split(" ")
    a,b  = int(a), int(b)
    x1 = 1
    for i in range(b-a+1,b+1):
        x1 *= i

    x2 = 1
    for i in range(1, a+1):
        x2 *= i
    print(x1//x2)