input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    total = 0
    for num in array:
        if total * num > total + num:
            total *= num
        else:
            total += num
            
    return total


result = find_max_plus_or_multiply(input)
print(result)