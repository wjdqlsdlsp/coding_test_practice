arr = "hello world"

print(arr)

print("".join([arr[i] for i in range(len(arr)-1, -1,-1)]))