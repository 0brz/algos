

"""

resize
enqueue
dequeue
size
top
last

queue_ringed
Queue
ListQueue

QueueBasic
    

"""



class queue_ringed:
    def __init__(self, capacity):
        self.__cap = capacity
        self.__data = [None for _ in range(capacity)]
        self.__begin = -1
        self.__end = -1
        self.__sz = 0

    def resize(self, to):
        ordered = self.as_list()
        new_cap = self.__cap + to
        self.__data = [None for _ in range(new_cap)]
        self.__begin = -1
        self.__end = -1
        self.__cap = new_cap
        self.__sz = 0
        for el in ordered:
            self.enqueue(el)

    def as_list(self):
        ls = []
        print("as_list=", self.size())
        for i in range(self.size()):
            ind = (self.__begin+i)%self.__cap
            ls.append(self.__data[ind])
        return ls

    def enqueue(self, val):
        i = (self.__end+1)%self.__cap
        if (self.__begin == -1):
            self.__data[i] = val
            self.__begin = 0
            self.__end = 0
            self.__sz += 1
        else:
            if (self.__data[i] != None):
                self.__data[i] = val
                self.__begin = (i+1)%self.__cap
                self.__end = i
            else:
                self.__sz += 1
                self.__end = i
                self.__data[i] = val

    def get(self):
        ls = []
        for i in range(self.__cap):
            ls.append(self.__data[i])
        
        return ls

    def first(self):
        if (self.__sz == 0):
            return None
        return self.__data[self.__begin]

    def last(self):
        return self.__data[self.__end]

    def dequeue(self):
        self.__sz -= 1
        v = self.__data[self.__begin]
        self.__data[self.__begin] = None
        self.__begin = (self.__begin+1)%self.__cap
        return v

    def size(self):
        return self.__sz

    def circle_pass(self, func):
        for _ in range(self.size()):
            el = self.dequeue()
            func(el)
            self.enqueue(el)

    def sort_by_min(self):
        bigest_queue = queue_ringed(self.size())
        t = queue_ringed(self.size())
        for _ in range(self.size()):
            el = self.dequeue()
            t.enqueue(el)
            # go tru existsing queue
            for _ in range(t.size()):
                inq = t.dequeue()
                if (inq == None or
                    inq <= el):
                    t.enqueue(inq)
                else:
                    bigest_queue.enqueue(inq)

            # go tru temporary queue for biggest elems
            for _ in range(bigest_queue.size()):
                t.enqueue(bigest_queue.dequeue())  
        return t



t = queue_ringed(10)
t.enqueue(5)
t.enqueue(4)
t.enqueue(3)
t.enqueue(2)
t.enqueue(1)

#t.circle_pass(lambda x: print(x))

print(t.sort_by_min().as_list())
"""
#print(t.get())
print(t.last())
print(t.first())
print("_______ ")
print(t.dequeue())
print(t.dequeue())
print("_______ ")
print(t.last())
print(t.first())
print("_______ ")
print(t.size())
print(t.dequeue())
print(t.last())
print(t.first())
"""