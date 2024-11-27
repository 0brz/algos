from pytest import *

def comb_sort(arr=[]):
    arr_size = len(arr)
    gap = arr_size-1

    while(gap > 0):
        for i in range(0, arr_size-gap):
            if (arr[i] > arr[i+gap]):
                (arr[i], arr[i+gap]) = (arr[i+gap], arr[i])
        
        gap -= 1

    return arr


def test_sorted():
    t_even = [1,2,3,4,5,6]
    t_odd  = [1,2,3,4,5,6, 7]
    assert comb_sort(t_even) == sorted(t_even)
    assert comb_sort(t_odd) == sorted(t_odd) 

def test_kind():
    t_even = [2,1]
    t_odd  = [2,3,1]
    assert comb_sort(t_even) == sorted(t_even)
    assert comb_sort(t_odd) == sorted(t_odd) 

def test_single():
    t = [2]
    assert comb_sort(t) == sorted(t)

def test_on_end():
    t = [1,2,3,4,5,2]
    t2 = [1,2,3,4,-1]
    assert comb_sort(t) == sorted(t)
    assert comb_sort(t2) == sorted(t2)

def test_on_begin():
    t = [9,1,2,3,4,5]
    t2 = [10, 1,2,3,4]
    assert comb_sort(t) == sorted(t)
    assert comb_sort(t2) == sorted(t2)

def test_equal_on_end():
    t = [1,2,3,4,45,565, 565, -2,-2]
    t2 = [1,2,3,4,45,565, 565, -2,-2, -2]
    assert comb_sort(t) == sorted(t)
    assert comb_sort(t2) == sorted(t2)

def test_equal_on_begin():
    t = [999, 999, 1,2,3,4,45,565, 565]
    t2 = [999, 999, 1,2,3,4,45,565, 565]
    assert comb_sort(t) == sorted(t)
    assert comb_sort(t2) == sorted(t2)
