import datetime
from collections import defaultdict
A_user = []
B_user = []

n=int(input())
for i in range(n):
    a, b=input().split(",")
    A_user.append(a)
    B_user.append(b)

A_user_log = []
B_user_log = []

m = int(input())
for i in range(m):
    log = input()
    log_time, log_id, log_type, log_name, svc_id, user_no, network, os, app_ver = log.split(',')
    if log_type == 'state' and user_no in A_user:
        time = log_time.split("+")[0]
        date,time = time.split("T")
        change_time = date+" "+ time
        log_time = datetime.datetime.strptime(change_time, "%Y-%m-%d %H:%M:%S.%f")
        A_user_log.append([log_time, log_name,user_no])
    
    elif log_type == 'state' and user_no in B_user:
        time = log_time.split("+")[0]
        date,time = time.split("T")
        change_time = date+" "+ time
        log_time = datetime.datetime.strptime(change_time, "%Y-%m-%d %H:%M:%S.%f")
        B_user_log.append([log_time, log_name,user_no])

A_user_log = sorted(A_user_log, key= lambda x: x[0])
B_user_log = sorted(B_user_log, key= lambda x: x[0])

A_user_act = defaultdict(list)
B_user_act = defaultdict(list)

A_user_click = {'home':0, 'banner_click':0}
B_user_click = {'home':0, 'banner_click':0}

for i in range(len(A_user_log)):
    if A_user_log[i][1] =='home':
        A_user_click['home'] +=1

    elif A_user_log[i][1] =='banner_click' and len(A_user_act[A_user_log[i][2]])>0 and A_user_act[A_user_log[i][2]][-1] =='home':
        A_user_click['banner_click'] +=1
        
    A_user_act[A_user_log[i][2]].append(A_user_log[i][1])


for i in range(len(B_user_log)):
    if B_user_log[i][1] =='home':
        B_user_click['home'] +=1

    elif B_user_log[i][1] =='banner_click' and len(B_user_act[B_user_log[i][2]])>0 and B_user_act[B_user_log[i][2]][-1] =='home':
        B_user_click['banner_click'] +=1
        
    B_user_act[B_user_log[i][2]].append(B_user_log[i][1])


print(f"A,{int(A_user_click['banner_click']/ A_user_click['home']* 100)}%")
print(f"A,{int(B_user_click['banner_click']/ B_user_click['home']* 100)}%")
