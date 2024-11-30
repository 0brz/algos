def bar():
    print("bnar")

def tests_run(fn):
    test_sorted(fn)
    test_equal_on_begin(fn)
    test_equal_on_end(fn)
    test_on_begin(fn)
    test_on_end(fn)
    test_single(fn)
    test_kind(fn)

def test_sorted(sort_fn):
    t_even = [1,2,3,4,5,6]
    t_odd  = [1,2,3,4,5,6, 7]
    assert sort_fn(t_even) == sorted(t_even)
    assert sort_fn(t_odd) == sorted(t_odd) 

def test_kind(sort_fn):
    t_even = [2,1]
    t_odd  = [2,3,1]
    assert sort_fn(t_even) == sorted(t_even)
    assert sort_fn(t_odd) == sorted(t_odd) 

def test_single(sort_fn):
    t = [2]
    assert sort_fn(t) == sorted(t)

def test_on_end(sort_fn):
    t = [1,2,3,4,5,2]
    t2 = [1,2,3,4,-1]
    assert sort_fn(t) == sorted(t)
    assert sort_fn(t2) == sorted(t2)

def test_on_begin(sort_fn):
    t = [9,1,2,3,4,5]
    t2 = [10, 1,2,3,4]
    assert sort_fn(t) == sorted(t)
    assert sort_fn(t2) == sorted(t2)

def test_equal_on_end(sort_fn):
    t = [1,2,3,4,45,565, 565, -2,-2]
    t2 = [1,2,3,4,45,565, 565, -2,-2, -2]
    assert sort_fn(t) == sorted(t)
    assert sort_fn(t2) == sorted(t2)

def test_equal_on_begin(sort_fn):
    t = [999, 999, 1,2,3,4,45,565, 565]
    t2 = [999, 999, 1,2,3,4,45,565, 565]
    assert sort_fn(t) == sorted(t)
    assert sort_fn(t2) == sorted(t2)
