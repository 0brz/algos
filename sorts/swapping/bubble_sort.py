
def bubble_sort(arr=[]):
    for i in range(0, len(arr)):
        for j in range(i, len(arr)-1):
            j+= 1

            if (arr[i] > arr[j]):
                (arr[i], arr[j]) = (arr[j], arr[i])

                j += 1

        i += 1

    return arr
            
print(bubble_sort([1,2,3,4,5,6]))
print(bubble_sort([6,4,3,7,4,2,1]))
print(bubble_sort([6,6,5,4,1,2]))