arr = [8,3,2,1,5,3,1,2]

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

arr = quick_sort(arr)
print(arr)