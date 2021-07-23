input = "abacabade"

def find_not_repeating_character(string):
    alphbet_array =[0] * 26

    for char in string:
        if char.isalpha():
            alphbet_array[ord(char) - 97] += 1
    
    not_recurrent = []
    for index,num in enumerate(alphbet_array):
        if num ==1:
            not_recurrent.append(chr(97+index))

    for char in string:
        if char in not_recurrent:
            return char
    return '_'
result = find_not_repeating_character(input)
print(result)