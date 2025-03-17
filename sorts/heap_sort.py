from ..heap import max_heap


def heap_sort(arr):
    mh = max_heap.max_heap(len(arr)) # max heap use -1 as MIN_INT
    for i in range(0, len(arr)):
        mh.push(arr[i])

    res = []
    for i in range(0, len(arr)):
        res.append(mh.pop_max())

    return res

print(heap_sort([9, 5, 3, 2, 7, 6, 6, 5, 3, 2, 0, 9]))