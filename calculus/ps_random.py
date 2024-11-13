
# psd random number
def psd_random(x_start, a, b, m, iter_count):
    
    while(iter_count > 0):
        x_start = (x_start * a + b) % m  
        iter_count -= 1

    return x_start

# psd random number range
def psd_random_range(range_start, range_end, count):
    ls = []
    x0 = 3
    b = 5

    while(count > 0):
        local_res = psd_random(x0, b, 5, 11, count)
        if (local_res >= range_start and local_res <= range_end):
            ls.append(local_res)
            count -= 1
            b += 1
        else:
            x0 += 1

    return ls

# randomize array
def psd_array_randomize(arr):
    sz = len(arr) - 1

    if (sz <= 0):
        return

    for i in range(0, sz):
        j = psd_random_range(0, sz, (i+1))[i] 
        print(j)
        # swap indecis
        (arr[i], arr[j]) = (arr[j], arr[i])
    
r = [1,2,3, 4, 5, 6]
psd_array_randomize(r)
print(r)

#psd_array_randomize(r)
#print(psd_random_range(5, 10, 40))


