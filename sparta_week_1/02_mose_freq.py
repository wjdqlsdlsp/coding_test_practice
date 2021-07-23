def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for a in string:
        if a.isalpha():
            alphabet_occurrence_array[ord(a)-ord('a')] += 1
    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))