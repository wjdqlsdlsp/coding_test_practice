from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    Q = deque(truck_weights)
    on_bridge = deque([0 for i in range(bridge_length)])
    bridge_weights = 0

    while len(Q) + len(on_bridge)  > 0:
        truck =on_bridge.popleft()
        bridge_weights -= truck
        answer +=1
        if Q:
            if bridge_weights + Q[0] <=weight:
                truck = Q.popleft()
                on_bridge.append(truck)
                bridge_weights +=truck
            else:
                on_bridge.append(0)
            
    return answer

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]	))

