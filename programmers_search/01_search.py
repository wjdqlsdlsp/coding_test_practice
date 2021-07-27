def solution(answers):
    person_1 = [1,2,3,4,5]
    person_2 = [2,1,2,3,2,4,2,5]
    person_3 = [3,3,1,1,2,2,4,4,5,5]

    problem_num = len(answers)
    person_1 = person_1 * (problem_num//len(person_1) +1)
    person_2 = person_2 * (problem_num//len(person_2) +1)
    person_3 = person_3 * (problem_num//len(person_3) +1)

    answer = [0,0,0]
    for index, num in enumerate(answers):
        if person_1[index] == num:
            answer[0] +=1
        if person_2[index] == num:
            answer[1] +=1
        if person_3[index] == num:
            answer[2] +=1

    max_num = max(answer)
    return_arr = []
    for i in range(len(answer)):
        if answer[i] == max_num:
            return_arr.append(i+1)

    return return_arr

print(solution([1,3,2,4,2]))