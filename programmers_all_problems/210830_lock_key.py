from collections import deque
import copy

def rotate(key):
    stack = []
    n = len(key)
    for j in range(n):
        tmp = [key[i][j] for i in range(len(key)-1, -1,-1)]
        stack.append(tmp)
    return stack

def move_right(key):
    for i in range(len(key)):
        for j in range(len(key[i])-1, 0, -1):
            key[i][j] = key[i][j-1]
        key[i][j-1] = 0
    return key

def move_left(key):
    for i in range(len(key)):
        for j in range(len(key[i])-1):
            key[i][j] = key[i][j+1]
        key[i][j+1] = 0
    return key

def move_up(key):
    tmp = [[0] * (len(key))]
    key = key[1:] + tmp
    return key


def move_down(key):
    tmp = [[0] * (len(key))]
    key = tmp + key[:-1]
    return key

def solution(key, lock):
    for i in range(len(lock)):
        for j in range(len(lock)):
            lock[i][j] = (lock[i][j] + 1)%2

    q = deque([key])
    dynamic = []
    while len(q) > 0:
        pop = q.popleft()
        if pop not in dynamic:
            dynamic.append(copy.deepcopy(pop))
            q.append(move_down(copy.deepcopy(pop)))
            q.append(move_up(copy.deepcopy(pop)))
            q.append(move_left(copy.deepcopy(pop)))
            q.append(move_right(copy.deepcopy(pop)))

    arr = []
    for dy in dynamic:
        for i in range(4):
            if dy not in arr:

                arr.append(dy)
                if dy == lock:
                    return True
                dy = rotate(copy.deepcopy(dy))
            else:
                break
    return False
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))