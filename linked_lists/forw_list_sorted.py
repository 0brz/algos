
class fwlist_sorted_node:
    """
    Sorted forward linked list 
    ins
    del
    get_at
    """
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def ins_after(self, node):
        if (isinstance(node, fwlist_sorted_node) == False):
            raise Exception("node should be fwlist_sorted_node")

        t = self
        old_next = t.next
        new_t = node

        while(new_t != None):
            t.next = new_t
            t = t.next    
            new_t = new_t.next

        t.next = old_next

    def __str__(self):
        t = self
        s = ""
        while(t != None):
            s += f"{t.val}, "
            t = t.next
        return s

class fwlist_sorted:
    """
    wrapper
    """
    def __init__(self, cmpr_lambda):
        self.cmpr_func = cmpr_lambda
        self.top = fwlist_sorted_node(None, None)

    def ins_nosorted(self, new_node):
        t = self.top.next
        tprev = self.top

        if (t == None):
            self.top.ins_after(new_node)
            return

        if (self.cmpr_func(self.top.next, new_node) >= 0):
            self.top.ins_after(new_node)
            return

        while(t != None):
            if (self.cmpr_func(t, new_node) >= 0):
                t.ins_after(new_node)
                return new_node
            t = t.next
            tprev = tprev.next

        # ins at last
        tprev.ins_after(new_node)
        return new_node
    
    def ins_node(self, new_node):
        t = new_node
        while(t != None):
            self.ins_nosorted(fwlist_sorted_node(t.val))
            t = t.next

    def ins_val(self, val):
        nn = fwlist_sorted_node(val)
        self.ins_node(nn) 

    def del_at(self, index):
        t = self.top.next

        if (index == 0):
            if (t.next != None):
                nn = t.next
                self.top.next = nn
                return

        _i = 1 # to don't keeping prev link
        while(t != None):
            if (_i == index):
                if (t.next != None):
                    nn = t.next.next
                    t.next = nn
                    return

            t = t.next
            _i += 1

    def __str__(self):
        return str(self.top)

"""

flow_traits
    cmpr_func
    name

fwlist_shared
    flows list<top, flow_traits>
    ins()
    del_at()
    get_at()

"""

class fwlist_flow_traits:
    def __init__(self, cmpr_func, flow_name):
        self.cmpr_func = cmpr_func
        self.flow_name = flow_name

class fwlist_shared_valcopy:
    def __init__(self, flows_traits_list=[]):
        if (len(flows_traits_list) == 0):
            raise Exception("no one traits provided")
        
        self.__flows = [] # list<tuple<list, trait>>
        for trait in flows_traits_list:
            new_flow = fwlist_sorted(trait.cmpr_func)
            self.__flows.append((new_flow, trait))
            print(f"flow trait added - {trait.flow_name}")

    def ins(self, node):
        for flow in self.__flows:
            nd_copy = fwlist_sorted_node(node.val)
            flow[0].ins_node(nd_copy)

    def get(self, flow_name) -> fwlist_sorted:
        for fl in self.__flows:
            if (fl[1].flow_name == flow_name):
                return fl[0]
        
        return None


cmp_gt = (lambda node_a, node_b: 
    1 if node_a.val > node_b.val else 
    0 if node_a.val == node_b.val else
    -1)

cmp_ls = (lambda node_a, node_b: 
    -1 if node_a.val > node_b.val else 
    0 if node_a.val == node_b.val else
    1)


t = [fwlist_flow_traits(cmp_gt, "greather"),
     fwlist_flow_traits(cmp_ls, "less")]

print(len(t))

ls = fwlist_shared_valcopy(t)

ls.ins(fwlist_sorted_node(1))
ls.ins(fwlist_sorted_node(2))
ls.ins(fwlist_sorted_node(3))
ls.ins(fwlist_sorted_node(4))
ls.ins(fwlist_sorted_node(5))

f1 = ls.get("greather")
print("gt: ", str(f1))

f2 = ls.get("less")
print("less: ", str(f2))

"""
ls = fwlist_sorted(cmpr_lambda=lambda node_a, node_b: 
                    1 if node_a.val > node_b.val else 
                    0 if node_a.val == node_b.val else
                    -1)

d2 = fwlist_sorted_node("a", fwlist_sorted_node("t"))

ls.ins_val("a")
ls.ins_val("b")
ls.ins_val("c")
ls.ins_val("d")
ls.ins_node(d2)
ls.ins_val("z")
ls.ins_val("q")

print(str(ls))
"""