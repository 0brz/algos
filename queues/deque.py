
class deque_elem:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

class deque:
    def __init__(self):
        self.__mid_node = deque_elem(None)
        self.__tail_sz = 0
        self.__head_sz= 0
        self.__head_p = self.__mid_node
        self.__tail_p = self.__mid_node

    def head(self, val):
        self.__head_p.prev = deque_elem(val)
        self.__head_p = self.__head_p.prev
        self.__head_sz += 1

    def tail(self, val):
        self.__tail_p.next = deque_elem(val)
        self.__tail_p = self.__tail_p.next
        self.__tail_sz += 1
    
    def deq_head(self):
        t = self.__mid_node.prev
        if (self.__mid_node.prev != None):
            self.__mid_node.prev = self.__mid_node.prev.prev
            self.__head_sz -= 1
        return t

    def deq_tail(self):
        t = self.__mid_node.next
        if (self.__mid_node.next != None):
            self.__mid_node.next = self.__mid_node.next.next
            self.__tail_sz -= 1
        return t
    
    def head_list(self):
        ls = []
        t = self.__mid_node.prev
        while(t != None):
            ls.append(t.val)
            t = t.prev
        return ls

    def tail_list(self):
        ls = []
        t = self.__mid_node.next
        while(t != None):
            ls.append(t.val)
            t = t.next
        return ls
    
q = deque()
q.head(5)
q.head(3)
q.head(2)
q.tail(1)
q.tail(2)
