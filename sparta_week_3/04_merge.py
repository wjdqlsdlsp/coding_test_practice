array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    i,j = 0, 0
    return_arr = []
    while i <4 and j <4:
        if array1[i] > array2[j]:
            return_arr.append(array2[j])
            j +=1
        else:
            return_arr.append(array1[i])
            i +=1

    if i <4:
        for k in range(i,4):
            return_arr.append(array1[k])
    else:
        for k in range(j,4):
            return_arr.append(array2[k])
    return return_arr


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!