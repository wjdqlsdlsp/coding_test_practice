import time
import math
start = time.time()
math.perm(1000)
print("perm: (100)" ,time.time() - start)

start = time.time()
math.factorial(10000)
print("factorial: (100)" ,time.time() - start)