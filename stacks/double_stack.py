
# shared size
# two ptrs
# end1 = begin
# end2= end

class double_stack:
    def __init__(self, size):
        self.__c1 = 0
        self.__c2 = 0
        self.__sdata = [None for _ in range(0, size)]
        self.__sz = size

    def pop_end(self):
        if (self.__c2 > 0):
            t =self.__sdata[self.__sz - self.__c2]
            self.__c2 -= 1
            return t
        else: return None

    def pop_begin(self):
        if (self.__c1 > 0):
            t =self.__sdata[self.__c1-1]
            self.__c1 -= 1
            return t
        else: return None

    def push_end(self, value):
        cursor_end = self.__sz - self.__c2 - 1
        if ((cursor_end) >= self.__c1):
            self.__sdata[cursor_end] = value
            self.__c2 += 1
            return value
        else: return None

    def push_begin(self, value):
        cursor = self.__c1
        if ((cursor + 1) <= (self.__sz - self.__c2)):
            self.__sdata[cursor] = value
            self.__c1 += 1
            return value
        else: return None

    def read_begin(self):
        t = []
        cursor = self.__c1 - 1
        while(cursor >= 0):
            t.append(self.__sdata[cursor])
            cursor -= 1
        return t

    def read_end(self):
        t = []
        cursor_end = self.__sz - (self.__c2)
        while(cursor_end < self.__sz):
            t.append(self.__sdata[cursor_end])
            cursor_end += 1
        return t

    def size_begin(self):
        return self.__c1
    
    def size_end(self):
        return self.__c2
    
    def size(self):
        return self.__sz
    
    def size_free(self):
        return self.__sz - (self.size_first() + self.size_second())
    
t = double_stack(5)
t.push_begin(1)
t.push_begin(2)
t.push_end(3)
t.push_end(4)

print("pop_end", t.pop_begin())

print(t.read_begin())
print(t.read_end())
print("pop_end", t.pop_begin())
print(t.read_begin())
print(t.read_end())