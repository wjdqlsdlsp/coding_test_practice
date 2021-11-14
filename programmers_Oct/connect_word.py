def solution(n, words):
    previous = words[0]
    did = set([previous])
    for index, word in enumerate(words[1:],1):
        if previous[-1] != word[0]:
            return [index%(n)+1, index//n+1]
        else:
            previous = word
        if word in did:
            return [index%(n)+1, index//n+1]
        else:
            did.add(word)
            
    return [0,0]


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# print(solution(5, 	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
# print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))