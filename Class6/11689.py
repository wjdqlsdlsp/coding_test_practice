import sys
n = int(sys.stdin.readline())
answer = n

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        while n%i == 0:
            n //= i
        answer -= answer/i
if n> 1:
    answer -= answer/n

print(int(answer))