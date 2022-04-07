words = ["hello", "helo", "helle", "hella",'hellep']
tree = dict()

for word in words:
    tmp = tree
    for s in list(word):
        tmp.setdefault(s, dict())
        tmp = tmp[s]
    tmp['*'] = 1


def find_word(tree, word):
    tmp = tree
    for s in list(word):
        if s in tmp.keys():
            tmp = tmp[s]
        else:
            return 0
    else:
        if '*' in tmp.keys():
            return 1
    return 0

word = "hello"
print(word, ": ", find_word(tree, word))

word = "helloads"
print(word, ": ", find_word(tree, word))

word = "heo"
print(word, ": ", find_word(tree, word))