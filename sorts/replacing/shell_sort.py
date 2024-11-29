

def shell_sort(arr=[]):
    step = len(arr)//2

    while(step >= 1):
        for j in range(1, len(arr)//step+1):
            back = j-1
            while(back >= 0):
                if (arr[j*back] > arr[j*step]):
                    (arr[j*back], arr[j*step]) = (arr[j*step], arr[j*back])
                back-=1
            
            print(j*step)

        step -= 1
        print("----------")

    return arr

print(shell_sort([1,2,3,4,5,6,7]))