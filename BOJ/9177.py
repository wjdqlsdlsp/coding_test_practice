import sys
n = int(sys.stdin.readline())

def make_word(w1, w2, target):
    if len(target) == 0:
        global answer
        answer = "yes"
        return
    if visited[len(w1)][len(w2)]:
        return
    visited[len(w1)][len(w2)] = 1
    if w1 and w1[0] == target[0]:
        make_word(w1[1:], w2, target[1:])

    if w2 and w2[0] == target[0]:
        make_word(w1, w2[1:], target[1:])

for i in range(1, n+1):
    word1, word2, target = sys.stdin.readline().split()
    visited = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
    answer = "no"
    make_word(list(word1), list(word2), list(target))
    print(f"Data set {i}: {answer}")
