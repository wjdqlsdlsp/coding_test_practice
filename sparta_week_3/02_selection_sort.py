input = [4, 6, 2, 9, 1]


def selection_sort(array):

    for i in range(len(array)):
        min, min_index = array[i], i
        for j in range(i,len(array)):
            if min > array[j]:
                min, min_index = array[j], j
        array[i], array[min_index] = array[min_index], array[i]
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!