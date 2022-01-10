import copy

a = [1,2,3]

b = copy.copy(a)

a.pop()


print(a,b)