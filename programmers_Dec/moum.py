def solution(word):
    dictionary = [781, 156, 31, 6, 1]
    total = 0
    for i, w in enumerate(word):
        tmp = 0 if w == 'A' else (1 if w == 'E' else (2 if w == 'I' else (3 if w == 'O' else 4)))
        total += tmp * dictionary[i] +1
    return total

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))


'''
A 1
AA 2
AAA 3
AAAA 4

AAAAA 5
AAAAE 6
AAAAI 7
AAAAO 8
AAAAU 9

AAAE 10
AAAEA 11
AAAEE 12
AAAEI 13
AAAEO 14
AAAEU 15

AAAI 16
-

AAAO 22

AAAU 28
AAAUA 29
AAAUE 30
AAAUI 31
AAAUO 32
AAAUU 33

AAE 34
AAI 34+31 = 65
AAO 65 + 31 = 96
AAU 96 + 31 = 127
AE 158

AI 158 + 156 = 314
AO 470
AU 626

E 782

I 1563
O
U

781*e - 156*d - 31*c - 6 * b - a


A = 1
1+781*2 = 

E = 1+ 781 = 782
EIO = 782+ 1 + 156*2 + 1+ 31*3
'''

