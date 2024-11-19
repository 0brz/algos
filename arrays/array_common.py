
"""
avg
max
min

insert
shift
del
find

"""

class array_1d:
    def __init__(self, size, default_val=None):
        self.__data = [default_val for _ in range(size)]
        self.__default_val = default_val

    def avg(self):
        s = 0
        ind = 0
        for i in self.__data:
            if (i != None):
                s += i
                ind += 1
        
        if (ind == 0):
            return 0
        return float(s/ind)
    
    def max(self):
        _t = float('-inf')
        m = _t
        for d in self.__data:
            if (d != None and d > m):
                m = d
        
        if (m == _t):
            return None
        
        return m
    
    def min(self):
        _t = float('inf')
        m = _t
        for d in self.__data:
            if (d != None and d < m):
                m = d

        if (m == _t):
            return None
        
        return m

    def size(self):
        return len(self.__data)
    
    def inc_size(self, inc_to=1):
        new_arr = array_1d(self.size() + inc_to, None)
        new_data = new_arr.data()
        for i in range(0, self.size()):
            new_data[i] = self.__data[i]
        
        self.__data = new_data

    def dec_size_end(self, dec_to=1):
        new_arr = array_1d(self.size() - dec_to, None)
        for i in range(0, new_arr.size()):
            new_arr[i] = self.__data[i]
        
        self.__data = new_arr.data()

    def data(self):
        return self.__data

    def find(self, val):
        for i in range(0, self.size()):
            if (self.__data[i] == val):
                return i
        
        return None

    # [1, 2, 3, 4, 5] -> 2
    # [0, 0, 1, 2, 3]
    def shift_right(self, shift_to):
        if (self.size() <= shift_to):
            raise Exception("ShiftTo should be from 0 to array.size")
        
        sz = self.size()
        for i in range(0, sz):
            j = sz-i-1
            shifted_index = j-shift_to

            if (shifted_index < 0):
                self.__data[j] = self.__default_val
            else:
                self.__data[j] = self.__data[shifted_index] 

    # [1, 2, 3, 4, 5] -> 2
    # [3, 4, 5, 0, 0]
    def shift_left(self, shift_to):
        if (self.size() <= shift_to):
            raise Exception("ShiftTo should be from 0 to array.size")
        
        sz = self.size()
        for i in range(0, sz):
            
            shifted_index = i+shift_to

            if (shifted_index >= sz):
                self.__data[i] = self.__default_val
            else:
                self.__data[i] = self.__data[shifted_index] 

    def __getitem__(self, key):
        if (key >= self.size()):
            raise Exception("Index was outside of array range")
        
        return self.__data[key]

    def __setitem__(self, key, value):
        if (key >= self.size()):
            raise Exception("Index was outside of array range")

        self.__data[key] = value


d = array_1d(5)

for i in range(0, 5):
    d[i] = i

print(d.data())
d.shift_left(1)
print(d.data())
