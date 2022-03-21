def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def make_gcd(x, y):
    if x == 0:
        x, y = 0, y // abs(y)
    elif y == 0:
        x, y = x// abs(x), 0
    else:
        i = gcd(abs(x), abs(y))
        x, y = x//i, y//i
    return x, y

def solution(monsters, bullets):
    answer = 0
    div_monsters = dict()
    for x, y, in monsters:
        x, y = make_gcd(x, y)

        if (x,y) in div_monsters.keys(): div_monsters[(x, y)] +=1
        else: div_monsters[(x, y)] =1

    for x, y, in bullets:
        x, y = make_gcd(x, y)

        if (x,y) in div_monsters.keys() and div_monsters[(x, y)] > 0:
            div_monsters[(x, y)] -= 1
            answer += 1

    return -1 if answer == 0 else answer