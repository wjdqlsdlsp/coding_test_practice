import sys

while True:
    try:
        tmp = sys.stdin.readline().split()[0]
    except:
        break
    f = dict()
    arr = []
    for _ in range(int(tmp)):
        s = sys.stdin.readline().split()[0]
        arr.append(s)
        cur = f
        for ch in s:
            cur.setdefault(ch, dict())
            cur = cur[ch]
        cur.setdefault("*", None)
        
    total = 0
    for s in arr:
        now = 0
        cur = f
        for i, ch in enumerate(s):
            if i == 0:
                now+=1
                cur = cur[ch]
                continue
            if len(cur) == 1:
                cur = cur[ch]
            else:
                now+=1
                cur = cur[ch]
        total += now
    print("%.2f" %(round(total / len(arr), 2)))