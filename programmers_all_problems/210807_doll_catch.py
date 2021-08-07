from collections import deque
def solution(board, moves):
    answer = 0
    board_size = len(board)
    board_stack = [deque([]) for _ in range(board_size)]
    my_stack = deque([])
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 0:
                continue
            board_stack[j].appendleft(board[i][j])
    for num in moves:
        if len(board_stack[num-1]) >0:
            pop_num = board_stack[num-1].pop()

            if len(my_stack) > 0 and my_stack[-1] == pop_num:
                my_stack.pop()
                answer +=2
            else:
                my_stack.append(pop_num)

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]	))
'''
[[0,0,0,0,0],
[0,0,1,0,3],
[0,2,5,0,1],
[4,2,4,4,2],
[3,5,1,3,1]]	
'''