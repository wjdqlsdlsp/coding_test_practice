seat_count = 9
vip_seat_array = [4, 7]

def return_count(total_count):
    if total_count ==0 or total_count ==1 :
        return 1
    return return_count(total_count-1) + return_count(total_count-2)

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    count = 1
    start = 1
    for i in range(len(fixed_seat_array)):
        count *= return_count(len(range(start, fixed_seat_array[i])))
        start = fixed_seat_array[i] + 1

    count *= return_count(len(range(start, total_count+1)))
    return count


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))