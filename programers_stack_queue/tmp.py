arr = list(range(1,101))

sum = 0
for num in arr:
    sum += num
print(sum)


import functools
print(functools.reduce(lambda x,y : x + y,arr))