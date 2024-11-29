from pytest import *

def insertion_sort(arr=[]):
    size = len(arr)
    for i in range(1, size):
        pr = i-1
        while(pr >= 0 and arr[pr] > arr[pr+1]):
            (arr[pr+1], arr[pr]) = (arr[pr], arr[pr+1])
            pr -= 1
    return arr

def test_sorted():
    t_even = [1,2,3,4,5,6]
    t_odd  = [1,2,3,4,5,6, 7]
    assert insertion_sort(t_even) == sorted(t_even)
    assert insertion_sort(t_odd) == sorted(t_odd) 

def test_kind():
    t_even = [2,1]
    t_odd  = [2,3,1]
    assert insertion_sort(t_even) == sorted(t_even)
    assert insertion_sort(t_odd) == sorted(t_odd) 

def test_single():
    t = [2]
    assert insertion_sort(t) == sorted(t)

def test_on_end():
    t = [1,2,3,4,5,2]
    t2 = [1,2,3,4,-1]
    assert insertion_sort(t) == sorted(t)
    assert insertion_sort(t2) == sorted(t2)

def test_on_begin():
    t = [9,1,2,3,4,5]
    t2 = [10, 1,2,3,4]
    assert insertion_sort(t) == sorted(t)
    assert insertion_sort(t2) == sorted(t2)

def test_equal_on_end():
    t = [1,2,3,4,45,565, 565, -2,-2]
    t2 = [1,2,3,4,45,565, 565, -2,-2, -2]
    assert insertion_sort(t) == sorted(t)
    assert insertion_sort(t2) == sorted(t2)

def test_equal_on_begin():
    t = [999, 999, 1,2,3,4,45,565, 565]
    t2 = [999, 999, 1,2,3,4,45,565, 565]
    assert insertion_sort(t) == sorted(t)
    assert insertion_sort(t2) == sorted(t2)
