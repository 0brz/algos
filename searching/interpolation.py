
def interpolation_search(arr, target):
    min = 0
    max = len(arr)-1
    while(min <= max):
        mid = int(min + (max-min) * (target - arr[min]) / (arr[max] - arr[min]))
        if (arr[mid] == target):
            return mid
        
        if (arr[mid] > target):
            max = mid-1
        else:
            min = mid+1
    
    return -1

print(interpolation_search([1,2,3,4,45,66,77,88,91,91,92], 1))
print(interpolation_search([1,2,3,4,45,66,77,88,91,91,92], 66))
print(interpolation_search([1,2,3,4,45,66,77,88,91,91], 92))
print(interpolation_search([1,2,3,4,45,66,77,88,91,91], 91))