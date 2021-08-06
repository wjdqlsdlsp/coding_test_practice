keypad = [(3,1),(0,0), (0,1),(0,2),
        (1,0), (1,1), (1,2),
        (2,0), (2,1),(2,2),(3,0),(3,2)]

def calculate(left_now,right_now, target):
    left = abs(keypad[target][0] - keypad[left_now][0]) + abs(keypad[target][1] - keypad[left_now][1])
    right = abs(keypad[target][0] - keypad[right_now][0]) + abs(keypad[target][1] - keypad[right_now][1])

    return left, right

def what_hand(left_hand_key, right_hand_key, left_now, right_now, target,hand):
    if target in left_hand_key: return 'L', target, right_now
    elif target in right_hand_key: return 'R', left_now, target
    else:
        left_distance, right_distance =calculate(left_now, right_now, target)
        if left_distance < right_distance: return 'L', target, right_now
        elif left_distance > right_distance: return 'R', left_now, target
        else:
            if hand == 'right': return 'R', left_now, target
            else: return 'L', target, right_now

def solution(numbers, hand):
    answer = []
    left_hand_now = 10
    right_hand_now = 11
    for num in numbers:
        s,left_hand_now,right_hand_now  = what_hand([1,4,7,10], [3,6,9,11], left_hand_now, right_hand_now, num, hand)
        answer.append(s)
    return "".join(answer)

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))