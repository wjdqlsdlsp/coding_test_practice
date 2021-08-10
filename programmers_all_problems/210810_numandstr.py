import re
def solution(s):
    num_str = ['zero', 'one','two','three',
                'four','five','six','seven',
                'eight','nine']
    num = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(num)):
        s = re.sub(num_str[i],num[i],s)
    return int(s)

print(solution("one4seveneight"))