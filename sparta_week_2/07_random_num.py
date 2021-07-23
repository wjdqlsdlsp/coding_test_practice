finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    finding_numbers.sort()

    index = len(finding_numbers)
    while 1:
        if target == finding_numbers[index/2]:
            return finding_numbers[index/2]
        elif target < finding_numbers[index/2]:
            index //= 2
        else:
            index //= 2
    return 1


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)