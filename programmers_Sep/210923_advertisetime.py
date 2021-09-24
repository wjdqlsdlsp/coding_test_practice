def convert(s):
    return int(s[0:2]) * 3600 + int(s[3:5]) * 60 + int(s[6:8])

def solution(play_time, adv_time, logs):
    play_time = convert(play_time)
    adv_time = convert(adv_time)
    logs = sorted([s for t in logs for s in [(convert(t[:8]), 1), (convert(t[9:]), 0)]])
    v, p, b = 0, 0, [0] * play_time
    for t, m in logs:
        if v > 0:
            b[p:t] = [v] * (t - p)
        v, p = v + (1 if m else -1), t

    mv, mi = (s := sum(b[:adv_time]), 0)
    for i, j in zip(range(play_time - adv_time), range(adv_time, play_time)):
        s += b[j] - b[i]
        if s > mv:
            mv, mi = s, i + 1

    return f"{mi//3600:02d}:{mi%3600//60:02d}:{mi%60:02d}"

# print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", 	"25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
