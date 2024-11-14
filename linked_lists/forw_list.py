from pytest import *

# forward list
class fwlsit_node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def dump(top):
        cur = top
        s = ""
        while(cur != None):
            s += f"{cur.val}, "
            cur = cur.next

        print(s)

    def fill(first, count):
        cur = first
        for i in range(count):
            cur.next =  fwlsit_node(i, None)
            cur = cur.next

        return first
    
    def fill_range(first, range_st, range_end):
        cur = first
        for i in range(range_st, range_end):
            cur.next =  fwlsit_node(i, None)
            cur = cur.next

        return first

    def insert(cur, val):
        old = cur.next
        cur.next = fwlsit_node(val, None)
        cur.next.next = old

    def find(cur, target):
        _targ = None

        if (isinstance(target, fwlsit_node)):
            _targ = target.val
        else: _targ = target

        t = cur

        while(t != None):
            if (t.val == _targ):
                return t
            t = t.next
        return None

    def size(cur):
        t = 0
        c = cur
        while(c != None):
            t += 1
            c = c.next
        return t

    def merge_copy(cur, deep_list):
        if (fwlsit_node.size(deep_list) <= 0):
            return

        _cur = cur
        _prev = None
        old_next = _cur.next
        m_top = deep_list

        while(m_top != None):
            _cur.next = fwlsit_node(m_top.val) 
            m_top = m_top.next
            _prev=  _cur
            _cur = _cur.next
        
        _prev.next.next = old_next

    def ins_begin(cur, new_node):
        old_v = cur.val
        cur.val = new_node.val
        cur.next = fwlsit_node(old_v, cur.next)

    def ins_end(cur, new_node):
        t = cur
        #prev = None
        while(t.next != None):
            t = t.next
        t.next = new_node

    def ins_at(cur, new_node, aft_pos):
        _cur_pos = 0
        t = cur
        while(t != None):
            if (_cur_pos == aft_pos):
                old_n = t.next
                t.next = new_node
                t.next.next = old_n
                break
            
            _cur_pos += 1
            t = t.next

    def get_at(cur, index):
        if (index == 0):
            return cur
        
        _i = 0
        t = cur
        while(t != None):
            if (_i == index):
                return t
            t = t.next
            _i += 1

        return None

    def get_last(cur):
        return fwlsit_node.get_at(top1, fwlsit_node.size(top1)-1)

    def del_at(cur, index):
        if (index == 0):
            raise Exception("index should be > 0")
        
        prev = fwlsit_node.get_at(cur, index-1)
        if (prev.next != None):
            prev.next = prev.next.next

    def deep_copy(cur):
        t =fwlsit_node(cur.val)
        _head = t
        _r = cur.next
        while(_r != None):
            t.next = fwlsit_node(_r.val)
            _r = _r.next
            t = t.next
        
        return _head

# ----------------------------- TESTS -----------------------------

def test_find():
    top = fwlsit_node(5)
    fwlsit_node.fill_range(top, 6, 10)
    assert fwlsit_node.find(top, 7).val == 7

def test_del():
    top = fwlsit_node(5)
    fwlsit_node.fill_range(top, 6, 10)
    fwlsit_node.del_at(top, 2)
    assert fwlsit_node.find(top, 7) == None

def test_del_on_end_size():
    top = fwlsit_node(5)
    fwlsit_node.fill_range(top, 6, 10)
    old_sz = fwlsit_node.size(top)
    fwlsit_node.del_at(top, fwlsit_node.size(top)-1)
    assert fwlsit_node.size(top) == (old_sz-1)

def test_del_on_start():
    top = fwlsit_node(5)
    fwlsit_node.fill_range(top, 6, 10)
    fwlsit_node.del_at(top, 1)
    fwlsit_node.dump(top)
    assert top.next.val == 7

def test_merge_size():
    top1 = fwlsit_node(5)
    fwlsit_node.fill_range(top1, 6, 10)
    fwlsit_node.dump(top1)

    top2 = fwlsit_node(-15)
    fwlsit_node.fill_range(top2, -14, -10)
    fwlsit_node.dump(top2)

    sum_sz = fwlsit_node.size(top1) + fwlsit_node.size(top2)

    fwlsit_node.merge_copy(top1, top2)
    assert fwlsit_node.size(top1) == sum_sz

def test_copy_deep():
    top1 = fwlsit_node(5)
    fwlsit_node.fill_range(top1, 6, 10)
    
    cp = fwlsit_node.deep_copy(top1)

    assert fwlsit_node.size(top1) == fwlsit_node.size(cp) 


"""
top1 = fwlsit_node(5)
fwlsit_node.fill_range(top1, 6, 10)
fwlsit_node.dump(top1)

new1 = fwlsit_node(-9)
fwlsit_node.ins_begin(top1, new1)
fwlsit_node.dump(top1)

ne2 = fwlsit_node(10)
fwlsit_node.ins_end(top1, ne2)
fwlsit_node.dump(top1)

new3 = fwlsit_node(77)
fwlsit_node.ins_at(top1, new3, 0)
fwlsit_node.dump(top1)

fwlsit_node.del_at(top1, 1)
fwlsit_node.dump(top1)
"""

#print(fwlsit_node.get_at(top1, fwlsit_node.size(top1)-1).val)

"""
top1 = fwlsit_node(5)
fwlsit_node.fill_range(top1, 6, 10)
fwlsit_node.dump(top1)

top2 = fwlsit_node(-15)
fwlsit_node.fill_range(top2, -14, -10)
fwlsit_node.dump(top2)

fwlsit_node.merge_copy(top1, top2)
fwlsit_node.dump(top1)
"""

#fwlsit_node.insert(top.next, 99)
#fwlsit_node.dump(top)
#print(fwlsit_node.find(top, 5).val)
#print(fwlsit_node.size(top))


