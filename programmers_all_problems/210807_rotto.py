def solution(lottos, win_nums):
    answer = []
    rank_dict = {6 : 1, 5: 2, 4: 3, 3:4, 2:5, 1:6, 0:6}
    count,zero_count = 0, 0
    for num in lottos:
        if num in win_nums: count+=1
        elif num ==0: zero_count +=1
    answer.append(rank_dict[count + zero_count])
    answer.append(rank_dict[count])
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]	))
