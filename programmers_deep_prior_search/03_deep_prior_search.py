def how_differenct(begin, target):
    diffent_count = 0
    for i in range(len(begin)):
        if begin[i] != target[i]:
            diffent_count +=1
    return diffent_count

def what_word_can_change(begin, words, already):
    arr = []
    for word in words:
        if word in already:
            continue
        if how_differenct(begin,word) ==1:
            arr.append(word)
    return arr

def solution(begin, target, words):
    count = 0
    arr = [begin]
    already = [begin]
    while len(arr)>0:
        pop = arr.pop()
        already.append(pop)
        if pop == target:
            return count
        else:
            count+=1
            arr = what_word_can_change(pop, words, already)
        
    return 0


# print(solution("hit","cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit","cog", ["hot", "dot", "dog", "lot", "log"]))
