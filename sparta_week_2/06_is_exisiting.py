finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):

    while target != array:
        if target == array[len(array)//2]:
            return array[len(array)//2]
        elif target > array[len(array)//2]:
            array = array[len(array)//2:]
        else:
            array = array[:len(array)//2]

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)