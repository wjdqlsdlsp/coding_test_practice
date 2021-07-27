def solution(brown, yellow):
    total = brown + yellow
    for col in range(3,total):
        row = total//col

        if row*col == total and col <= row and (row-2)*(col-2) ==yellow:
            answer = [row,col]
    return answer

print(solution(10,2))