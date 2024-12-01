

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

t = queue_ringed(3)
t.enqueue(1)
t.enqueue(2)
t.enqueue(3)
t.enqueue(4)
t.enqueue(5)

print(t.resize(1))
t.enqueue(6)
print(t.as_list())

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