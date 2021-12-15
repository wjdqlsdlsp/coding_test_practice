# from collections import deque

def solution(cacheSize, cities):
    # q = deque()
    q = []
    count = 0
    if cacheSize == 0:
        return len(cities) * 5

    for i in cities:
        i = i.lower()
  
        if i in q:
            count += 1
            if len(q) >= cacheSize:
                q.pop(q.index(i))
                q.append(i)
            else:
                q.append(i)
        else:
            count += 5
            if len(q) >= cacheSize:
                q.pop(0)
                q.append(i)
            else:
                q.append(i)

    return count

print(solution(5, 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))


'''
 	[  5
       5 
       5 
        5
         5
         "SanFrancisco", 5
           1
           "Rome", 5
            "Paris", 5
             "Jeju", 5
              "NewYork", 5
               "Rome" 1]
'''