from itertools import permutations
import copy
def solution(expression):
    answer, prev,a = 0,  0, []
    giho_list = []
    for i in range(len(expression)):
        if expression[i] in ['-', '+', '*']:
            if prev == 0:
                a.append(expression[prev:i])
            else:
                giho_list.append(expression[prev])
                a.append(expression[prev+1:i])
            prev = i
    giho_list.append(expression[prev])
    a.append(expression[prev+1:])
    a = list(map(lambda x : int(x), a))
    to_permurations = list(set(giho_list))
    priors_giho = list(permutations(to_permurations, len(to_permurations)))
    result_arr = []

    for prior_giho in priors_giho:
        sum_tmp = 0
        tmp_giho_list = giho_list.copy()
        tmp_a = a.copy()
        for i in range(len(prior_giho)):
            while prior_giho[i] in tmp_giho_list:
                if prior_giho[i] =='-':
                    pop_1 = tmp_a.pop(tmp_giho_list.index(prior_giho[i])+1)
                    tmp_a[tmp_giho_list.index(prior_giho[i])] -= pop_1
                elif prior_giho[i] =='+':
                    pop_1 = tmp_a.pop(tmp_giho_list.index(prior_giho[i])+1)
                    tmp_a[tmp_giho_list.index(prior_giho[i])] += pop_1
                else:
                    pop_1 = tmp_a.pop(tmp_giho_list.index(prior_giho[i])+1)
                    tmp_a[tmp_giho_list.index(prior_giho[i])] *= pop_1

                tmp_giho_list.pop(tmp_giho_list.index(prior_giho[i]))
        result_arr.append(tmp_a[0])
    return max(list(map( lambda x : abs(x), result_arr)))

print(solution("100-200*300-500+20"))