from collections import deque
import heapq

def solution(arr, processes):
    answer = []
    tmp = []
    for i in processes:
        p = i.split()
        if p[0] == "read":
            tmp.append([0, int(p[1]), int(p[2]), int(p[3]), int(p[4])])
        else:
            tmp.append([1, int(p[1]), int(p[2]), int(p[3]), int(p[4]), int(p[5])])

    def set_read_process():
        while len(read_process) > 0 and read_process[0][0] <= t:
            read_pop = read_process.popleft()
            read_pop = [t+read_pop[1]] + read_pop[2:] + [read_pop[0]]
            heapq.heappush(now_r, read_pop)
            a, b = read_pop[1:-1]
            answer.append("".join(arr[a:b+1]))

    def set_remain_process():
        while len(q) > 0 and t >= q[0][1]:
            pop_process = q.popleft()
            if pop_process[0] == 0:
                read_process.append(pop_process[1:])
            else:
                write_process.append(pop_process[1:])

    q = deque(tmp)
    now_r, write_process, read_process = [], deque(), deque()
    t = 0
    not_use_time = 0
    while len(q)> 0 or len(read_process)>0:
        set_remain_process()

        if len(write_process) == 0:
            set_read_process()

        else:
            while len(now_r) > 0:
                while len(now_r) > 0 and t >= now_r[0][0]:
                    heapq.heappop(now_r)
                t +=1
                if len(now_r) == 0:
                    t-=1

            while len(write_process) > 0 and write_process[0][0] <= t:
                tmp = write_process.popleft()
                a, b, c = tmp[2:]
                for i in range(a, b+1):
                    arr[i] = str(c)
                t += tmp[1]
                set_remain_process()
            set_read_process()
            
        if len(now_r) == 0:
            not_use_time +=1

        t+=1
    while len(now_r):
        t, a, b, d = heapq.heappop(now_r)
    answer = answer+[str(t-not_use_time)]
    return answer


print(solution(["1","2","4","3","3","4","1","5"], ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]))

# print(solution(["1","1","1","1","1","1","1"], ["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]))