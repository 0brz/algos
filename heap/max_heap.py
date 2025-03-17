ELEM_MIN = -1

class max_heap:
    def __init__(self, sz):
        self.__arr = [ELEM_MIN for i in range(sz)]
        self.__cursor = 0
        self.__sz = sz

    def get_max(self):
        return self.__arr[0]

    def size(self):
        return self.__cursor

    def __parent(self, i):
        if (i == 0):
            return ELEM_MIN
        return int((i-1)/2)
    
    def __lchild(self, i):
        return (i*2)+1

    def __rchild(self, i):
        return (i*2)+2

    def __swap(self, i, j):
        (self.__arr[i], self.__arr[j]) = (self.__arr[j], self.__arr[i])

    def __str__(self):
        return str(self.__arr)

    def heapify(self, parent_i):
        l = self.__lchild(parent_i)
        r = self.__rchild(parent_i)
        largest = parent_i
        if (l < self.__sz and r < self.__sz):
            if (self.__arr[l] > self.__arr[r]):
                largest = l
            elif (r < self.__sz and self.__arr[l] < self.__arr[r]):
                largest = r
            else:
                return
            
            self.__swap(parent_i, largest)
            self.heapify(largest)

        return



    def push(self, i):
        # insert to last.
        # while parent is less, swap.
        if (self.__cursor >= self.__sz):
            self.pop_max()

        self.__arr[self.__cursor] = i
        self.__cursor+=1
        
        index = self.__cursor-1
        par = self.__parent(index)
        while (par != ELEM_MIN and self.__arr[par] < i):
            self.__swap(par, index)
            index = par
            par = self.__parent(index)

    def pop_max(self):
        # pop the max.
        # max=min_elem.
        # heapify rec
        if (self.size() == 0):
            return ELEM_MIN
        
        mx = self.get_max()
        self.__arr[0] = ELEM_MIN
        self.heapify(0)

        self.__cursor -= 1

        return mx


h = max_heap(3)
h.push(0)
h.push(1)
h.push(2)
h.push(3)
print(h.pop_max())
print(h.pop_max())
print(h.pop_max())
print(h.pop_max())
