def Enter_change(id, nickname, user):
    user[id] = nickname
    return user

def solution(record):
    user = {}
    log = []
    for rec in record:
        a = rec.split(' ')
        if a[0] =='Enter':
            user = Enter_change(a[1], a[2],user)
            log.append(f'{a[1]} 들어왔습니다.')
        if a[0] =='Leave':
            log.append(f'{a[1]} 나갔습니다.')
        if a[0] =='Change':
            user = Enter_change(a[1], a[2], user)

    result = []
    for log_re in log:
        a = log_re.split(' ')
        sentence = f'{user[a[0]]}님이 ' + a[1]
        result.append(sentence) 
    
    return result

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))