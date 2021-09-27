def solution(sizes):
    answer = 0
    max_value, min_value = 0,0
    for size in sizes:
        if size[0] >= size[1]:
            large = size[0]
            small = size[1]
        else:
            large = size[1]
            small = size[0]

        if large > max_value:
            max_value = large
        if small > min_value:
            min_value = small

    return max_value * min_value

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))