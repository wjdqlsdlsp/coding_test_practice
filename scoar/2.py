def solution(black_caps):
    n = len(black_caps)
    answer = [0 for _ in range(n)]
    for _ in range(2):
        for index, value in enumerate(black_caps):
            # 맨 앞에 있는 사람
            if index == 0:
                if value == 1: answer[index+1] = 1
                else: answer[index+1] = 2
            # 맨 뒤에 있는 사람
            elif index == n-1:
                if value == 1: answer[index-1] = 1
                else: answer[index-1] = 2
            else:
                # 양쪽 둘다 검정 모자
                if value == 2:
                    answer[index-1], answer[index+1] = 1, 1
                # 양쪽 둘다 하얀 모자
                elif value == 0:
                    answer[index-1], answer[index+1] = 2, 2
                # 둘중 한명만 검은 모자
                else:
                    if answer[index-1] == 1: answer[index+1] = 2
                    elif answer[index+1] == 1: answer[index-1] = 2
                    elif answer[index-1] == 2: answer[index+1] = 1
                    elif answer[index+1] == 2: answer[index-1] = 1

    return answer