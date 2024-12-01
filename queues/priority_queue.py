

class queue_cell:
    def __init__(self, value, prior=1, next=None):
        self.value = value
        self.prior = prior
        self.next = next

class priority_queue:
    def __init__(self):
        self.__head = queue_cell(None, None, None)
        self.__sz = 0
        self.__last = self.__head

    def enq(self, val, prior=1):
        if (prior <= 0):
            raise Exception("queue prior should be > 0")
        if (self.__last == None):
            self.__last = self.__head
        self.__last.next= queue_cell(val, prior, None)
        self.__last = self.__last.next
        self.__sz += 1

    def as_list(self):
        ls = []
        t = self.__head.next
        while(t != None):
            ls.append(t.value)
            t = t.next
        return ls
    
    def size(self):
        return self.__sz

    def deq(self):
        if (self.size() == 0):
            return None
        
        self.__sz -= 1

        t = self.__head
        max_prior = -1
        max_cell = None
        prev_cell = None
        while(t.next != None):
            if (t.next.prior >= max_prior):
                max_cell = t.next
                prev_cell = t
                max_prior = t.next.prior
            t = t.next

        if (prev_cell != None):
            prev_cell.next = max_cell.next
            self.__last = prev_cell.next
                
        return max_cell.value

t = priority_queue()
t.enq(1)

print(t.deq())
print(t.deq())
print(t.deq())
t.enq(1)
print(t.deq())