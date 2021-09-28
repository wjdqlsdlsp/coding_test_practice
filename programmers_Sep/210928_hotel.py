"""
def solution(k, room_number):
    answer = []
    arr = [False for _ in range(k+1)]
    for room in room_number:
        while arr[room] == True:
            room+=1
        arr[room] = True
        answer.append(room)
    return answer
"""

# def solution(k, room_number):
#     answer = []
#     a = set()
#     for room in room_number:
#         while room in a:
#             room+=1
#         a.add(room)
#         answer.append(room)
#     return answer

def solution(k, room_number):
    dict = {}
    arr = []
    for room in room_number:
        first = [room]
        while room in dict:
            room = dict[room]
            first.append(room)
        for j in first:
            dict[j] = room+1
        arr.append(room)
    return arr
print(solution(10, [1,3,4,1,3,1]))