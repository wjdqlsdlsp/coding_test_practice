input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    tmp_max = array[0]
    for i in array:
        if tmp_max < i :
            tmp_max = i
    return tmp_max


result = find_max_num(input)
print(result)