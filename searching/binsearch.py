
def __bsImpl(arr, l, r, target):
    
    mid = int((l+r)/2)
    
    #print(mid)

    if (arr[mid] == target):
        return mid
    elif (arr[mid] < target):
        return __bsImpl(arr, mid+1, r, target)
    elif (arr[mid] > target):
        return __bsImpl(arr, l, mid-1, target)
    
    return -1

def bin_search(sortedArray, target):
    return __bsImpl(sortedArray, 0, len(sortedArray)-1, target)


print(bin_search([1,2,3,4,45,66,77,88,91,91,92], 1))
print(bin_search([1,2,3,4,45,66,77,88,91,91,92], 92))