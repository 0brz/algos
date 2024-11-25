

# the alg point is transfering max/min elem to end/start by one full pass. 
# then we can reduce the range frame
def shaker_sort_opt(arr=[]):
    rev = False
    sz = len(arr)-1

    _end = sz
    _s = 0

    while(True):
        swapped = False
        print(f"[{_s}, {_end}]")
        for i in range(_s, _end):
            print(f"{arr[i]} == {arr[i+1]}")
            if (arr[i] > arr[i+1]):
                (arr[i], arr[i+1]) = (arr[i+1], arr[i])
                swapped = True

        if not rev:
            _end -= 1

        rev = not rev

        if not swapped:
            return arr


#print(shaker_sort([1,2,3,4]))
print(shaker_sort_opt([5,4,3,2,1]))
print(shaker_sort_opt([1,2,3,4,6]))
print(shaker_sort_opt([4,6,2,3,-2]))