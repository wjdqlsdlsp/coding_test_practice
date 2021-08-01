from collections import deque
location = ['ICN']
def abroad(destination, arr):
    for index, (arr_start, arr_destination) in enumerate(arr):
        if destination == arr_start:
            del arr[index]
            location.append(arr_start)
            return arr, arr_start, arr_destination
    return arr, arr_start, arr_destination

def solution(tickets):
    # tickets = sorted(tickets, key = lambda x : x[1])
    tickets = deque(tickets)
    for i in range(len(tickets)):
        if tickets[i][0]=='ICN':
            start,destination = 'ICN',tickets[i][1]
            del tickets[i]
            break

    while len(tickets)>0:
        prev_len = len(tickets)
        tmp, arr_start, arr_destination = abroad(destination, tickets)
        if len(tmp) == prev_len:
            start2,destination2 = tickets.popleft()
            tickets.append([start,destination])
        else:
            tickets = tmp
            start, destination = arr_start, arr_destination
    location.append(destination)
    return location

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
