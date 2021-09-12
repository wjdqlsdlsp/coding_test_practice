import datetime
def solution(a, b):
    return ['FRI','SAT','SUN','MON','TUE','WED','THU'][(datetime.date(2016, a, b) - datetime.date(2016, 1,1)).days % 7]

print(solution(5,24))