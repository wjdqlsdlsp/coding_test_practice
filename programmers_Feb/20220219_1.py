def solution(skill, skill_trees):
    answer = 0
    check_set = set(skill)
    check_list = list(skill)
    for ch in skill_trees:
        skill_tree_level = 0
        for i in ch:
            if i in check_set:
                if i == check_list[skill_tree_level]:
                    skill_tree_level += 1
                else:
                    break
        else:
            answer+=1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]	))