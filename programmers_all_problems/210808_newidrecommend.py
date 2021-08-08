import re
def solution(new_id):
    new_id_list = []

    for char in new_id:
        if 'a' <= char <= 'z' or '0'<= char <= '9' or char in ['-','_', '.']:
            new_id_list.append(char)
        elif 'A' <= char <= 'Z':
            new_id_list.append(chr(ord(char) + 32 ))

    string = "".join(new_id_list)
    string = re.sub('[.]{2,}', '.', string)
    if string[0] =='.':
        string = string[1:]
    if len(string) ==0:
        string = 'a'
    if string[-1] =='.':
        string = string[:-1]
    if len(string) ==0:
        string = 'a'
    if len(string) >= 16:
        string = string[:15]
        if string[-1] =='.':
            string = string[:-1]
    if len(string) <=2:
        last_char = string[-1]
        while len(string) <3:
            string += last_char

    return string

print(solution(	"...!@BaT#*..y.abcdefghijklm"))
print(solution(	"z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
