arr = [8,3,2,1,5,3,1,2]

def merge_sort(left, right):
    if right - left < 2:
        return 

    mid = (left + right) // 2
    merge_sort(left, mid)
    merge_sort(mid, right)
    merge(left, mid, right)

def merge(left, mid, right):
    l = left
    r = mid
    tmp = []
    while l < mid and r < right:
        if arr[l] < arr[r]:
            tmp.append(arr[l])
            l+=1
        else:
            tmp.append(arr[r])
            r+=1

    while l < mid:
        tmp.append(arr[l])
        l+=1
    
    while r < right:
        tmp.append(arr[r])
        r+=1
    
    for i, v in enumerate(tmp, left):
        arr[i] = v

merge_sort(0, len(arr))

print(arr)