import copy
def is_okay(x,y,board,tmp):
    if board[x][y] == '0':
        return tmp
    if board[x][y] == board[x+1][y] and board[x][y] == board[x][y+1] and board[x][y] == board[x+1][y+1]:
        tmp.add((x,y))
        tmp.add((x,y+1))
        tmp.add((x+1,y))
        tmp.add((x+1,y+1))
    return tmp

def solution(m, n, board):
    answer = 0
    board =[[*map(lambda x : x[i], board)] for i in range(n)]
    prev_board = 0
    while prev_board != board:
        tmp = set()
        prev_board = copy.deepcopy(board)
        for x in range(n-1):
            for y in range(m-1):
                tmp = is_okay(x,y,board,tmp)
        tmp =[*map(lambda x : list(x), list(tmp))]
        tmp = sorted(tmp, key = lambda x : x[1],reverse=True)
        while len(tmp) >0:
            x,y = tmp.pop()
            board[x].pop(y)
            board[x].insert(0, '0')
            answer+=1
    
    return answer

print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))