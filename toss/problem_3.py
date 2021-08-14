a = int(input())

record_log = ['home', 'transfer',"account_tab", 'enter_account_no','enter_transfer_amount','transfer_decision','enter_password','transfer_complete']
android_event = {'home':0, 'transfer': 0,"account_tab":0, 'enter_account_no':0,'enter_transfer_amount':0,'transfer_decision':0,'enter_password':0,'transfer_complete':0}
ios_event = {'home':0, 'transfer': 0,"account_tab":0, 'enter_account_no':0,'enter_transfer_amount':0,'transfer_decision':0,'enter_password':0,'transfer_complete':0}

for i in range(a):
    log = input()
    _,_, _, log_name, _, _, _, os, _  = log.split(',')
    if log_name in record_log:
      if os =='ios':
        ios_event[log_name] +=1
      elif os =='android':
        android_event[log_name] +=1

android = []
ios = []
for i in range(len(record_log)-1):
  if android_event[record_log[i]] ==0:
    android_event[record_log[i]] =1
  if ios_event[record_log[i]] ==0:
    ios_event[record_log[i]] =1
  
  android.append(int(android_event[record_log[i+1]]/android_event[record_log[i]] * 100))
  ios.append(int(ios_event[record_log[i+1]]/ios_event[record_log[i]] * 100))

print(f"android,{record_log[android.index(min(android))]},{record_log[android.index(min(android))+1]},{min(android)}%")
print(f"ios,{record_log[ios.index(min(ios))]},{record_log[ios.index(min(ios))+1]},{min(ios)}%")



'''
실행 결과
Traceback (most recent call last):
  File "/solution.py", line 8, in <module>
    print(logs[0])
IndexError: list index out of range
'''
