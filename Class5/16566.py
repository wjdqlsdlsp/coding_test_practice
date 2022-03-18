import sys
N,M,K = map(int, sys.stdin.readline().split())

parent = [i for i in range(M+1)]
cards = [*map(int, sys.stdin.readline().split())]

sqrt_N = int(N**0.5)
cards_presence = [0] * (N+1)
dummy = [0] * (sqrt_N+1)

for c in cards:
    cards_presence[c] += 1
    dummy[c // sqrt_N] += 1

for t in [*map(int, sys.stdin.readline().split())]:
    will = t+1
    while dummy[will // sqrt_N] == 0 and will <= N:
        will = ((will//sqrt_N) + 1) * sqrt_N
    if will > N:
        will = 0
        while dummy[will / sqrt_N] == 0 and will <= N:
            will = ((will // sqrt_N) + 1) * sqrt_N
    while True:
        if cards_presence[will] != 0:
            cards_presence[will] -=1
            dummy[will // sqrt_N] -= 1
            print(will)
            break
        will+=1