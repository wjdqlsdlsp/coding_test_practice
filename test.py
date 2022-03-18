a = "hello"

i, j = 1, 3

a = a[:i] + a[j] + a[i+1: j] + a[i] + a[j+1:]
print(a)