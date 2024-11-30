

class tree_node:
    left = None
    right = None
    value = None

    def __init__(self, val):
        self.value = val

    def __dfs_pass(self, ls=[]):
        node = self
        if (node.left != None):
            node.left.__dfs_pass(ls)

        ls.append(node.value)

        if (node.right != None):
            node.right.__dfs_pass(ls)

        return

    def get_dfs(self):
        ls = []
        self.__dfs_pass(ls)
        return ls

    def add(self, val):
        if (val < self.value):
            if (self.left == None):
                self.left = tree_node(val)
            else:
                self.left.add(val)
        else:
            if (self.right == None):
                self.right= tree_node(val)
            else:
                self.right.add(val)  

def tree_sort(arr=[]):
    t = tree_node(arr[0])
    for e in arr[1:]:
        t.add(e)

    return t.get_dfs()


"""
________________________________ TESTS
"""

def test_sorted():
    t_even = [1,2,3,4,5,6]
    t_odd  = [1,2,3,4,5,6, 7]
    assert tree_sort(t_even) == sorted(t_even)
    assert tree_sort(t_odd) == sorted(t_odd) 

def test_kind():
    t_even = [2,1]
    t_odd  = [2,3,1]
    assert tree_sort(t_even) == sorted(t_even)
    assert tree_sort(t_odd) == sorted(t_odd) 

def test_single():
    t = [2]
    assert tree_sort(t) == sorted(t)

def test_on_end():
    t = [1,2,3,4,5,2]
    t2 = [1,2,3,4,-1]
    assert tree_sort(t) == sorted(t)
    assert tree_sort(t2) == sorted(t2)

def test_on_begin():
    t = [9,1,2,3,4,5]
    t2 = [10, 1,2,3,4]
    assert tree_sort(t) == sorted(t)
    assert tree_sort(t2) == sorted(t2)

def test_equal_on_end():
    t = [1,2,3,4,45,565, 565, -2,-2]
    t2 = [1,2,3,4,45,565, 565, -2,-2, -2]
    assert tree_sort(t) == sorted(t)
    assert tree_sort(t2) == sorted(t2)

def test_equal_on_begin():
    t = [999, 999, 1,2,3,4,45,565, 565]
    t2 = [999, 999, 1,2,3,4,45,565, 565]
    assert tree_sort(t) == sorted(t)
    assert tree_sort(t2) == sorted(t2)