# 둘로 나누기
def merge_sort(arr):
    if len(arr) < 2:
        return arr
   
    
    if (len(arr) // 2) % 2 == 0:
        mid = len(arr) // 2 + 1
    else:
        mid = round(len(arr) / 2)
    
    
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

  
merge_sort([4, 5, 1, 3, 2])