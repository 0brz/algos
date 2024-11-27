from pytest import *

def quick_sort(arr=[]):
    less = []
    more = []
    mid = []

    if (len(arr)<= 1):
        return arr
    
    piv = arr[0]
    for i in arr:
        if (i > piv):
            more.append(i)
        elif(i < piv):
            less.append(i)
        else:
            mid.append(i)

    less = quick_sort(less)
    more = quick_sort(more)

    return less + mid + more

def test_sorted():
    t_even = [1,2,3,4,5,6]
    t_odd  = [1,2,3,4,5,6, 7]
    assert quick_sort(t_even) == sorted(t_even)
    assert quick_sort(t_odd) == sorted(t_odd) 

def test_kind():
    t_even = [2,1]
    t_odd  = [2,3,1]
    assert quick_sort(t_even) == sorted(t_even)
    assert quick_sort(t_odd) == sorted(t_odd) 

def test_single():
    t = [2]
    assert quick_sort(t) == sorted(t)

def test_on_end():
    t = [1,2,3,4,5,2]
    t2 = [1,2,3,4,-1]
    assert quick_sort(t) == sorted(t)
    assert quick_sort(t2) == sorted(t2)

def test_on_begin():
    t = [9,1,2,3,4,5]
    t2 = [10, 1,2,3,4]
    assert quick_sort(t) == sorted(t)
    assert quick_sort(t2) == sorted(t2)

def test_equal_on_end():
    t = [1,2,3,4,45,565, 565, -2,-2]
    t2 = [1,2,3,4,45,565, 565, -2,-2, -2]
    assert quick_sort(t) == sorted(t)
    assert quick_sort(t2) == sorted(t2)

def test_equal_on_begin():
    t = [999, 999, 1,2,3,4,45,565, 565]
    t2 = [999, 999, 1,2,3,4,45,565, 565]
    assert quick_sort(t) == sorted(t)
    assert quick_sort(t2) == sorted(t2)
