

# 1 3 4 9 5
# 

def gnome_sort(arr=[]):
    sz = len(arr)

    cur = 1
    pr = 0
    while(cur < sz):
        
        if (pr >= 0 and arr[cur] < arr[pr]):
            # swap
            (arr[cur], arr[pr]) = (arr[pr], arr[cur])
            cur -= 1
            pr -= 1
        else:
            cur += 1
            pr += 1

    return arr

# add: swap index to skip all path
def gnome_sort_opt1(arr=[]):
    sz = len(arr)

    _swap_index = 0

    cur = 1
    pr = 0
    while(cur < sz):
        
        if (pr >= 0 and arr[cur] < arr[pr]):
            # swap
            (arr[cur], arr[pr]) = (arr[pr], arr[cur])
            _swap_index = cur
            cur -= 1
            pr -= 1

        else:
            cur = _swap_index + 1
            pr = cur-1
            _swap_index += 1

    return arr

print(gnome_sort_opt1([1,2,3,4,5]))
print(gnome_sort_opt1([1,4,3,6,8,5,7]))
print(gnome_sort_opt1([7,6,5,4,89,2,1]))