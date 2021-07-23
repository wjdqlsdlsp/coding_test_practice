input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    for a in string:
        if a.isalpha():
            alphabet_occurrence_array[ord(a)-ord('a')] += 1
    
    max = 0
    for i in alphabet_occurrence_array:
        if max < i:
            max = i
    alpha = ord('a') + alphabet_occurrence_array.index(max)
    return chr(alpha)


result = find_max_occurred_alphabet(input)
print(result)