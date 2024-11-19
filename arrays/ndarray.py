
from itertools import permutations
from math import *

class array3d:
    def __init__(self, upper_bounds, lower_bounds):
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds

    def size(self):
        total_sz = 1
        for i in range(0, len(self.lower_bounds)-1):
            total_sz *= (self.upper_bounds[i]-self.lower_bounds[i])
        
        return total_sz
    
    def ind(self, r, h, c):
        
        row_size = (self.upper_bounds[0]-self.lower_bounds[0])
        col_size = (self.upper_bounds[1]-self.lower_bounds[1])

        # prev layers
        index = h * row_size * col_size
        index += r * row_size
        index += c

        return index

class ndarray:
    """
    N-Dimension Array
    d1,d2,d3...
    """
    
    def __init__(self, bounds=[], default_value=None):
        self.__dim_bounds = bounds    
        self.__data = [default_value for _ in range(self.size())]

    def _get_index(self, index=[]):
        "ex for 3dim(x,y,z): x(d2, d3) + y(d3) + z"
        calc_index = 0
        j_mul = 1
        for i in range(0, len(self.__dim_bounds)):
            coef = index[i]
            mults = self.__dim_bounds[j_mul:len(self.__dim_bounds)] 
            calc_index += coef * prod(mults)
            j_mul += 1

        return calc_index 

    def size(self):
        return prod(self.__dim_bounds)
    
    def __setitem__(self, nd_index, value):
        row_index = self._get_index(nd_index)
        if (row_index >= self.size()):
            raise Exception("index outside of ndArray")
        self.__data[row_index] = value

    def __getitem__(self, nd_index):
        row_index = self._get_index(nd_index)
        if (row_index >= self.size()):
            raise Exception("index outside of ndArray")
        return self.__data[row_index]

    def moda(self):
        t = {}

        max_count = -1
        max_elem = -1

        for i in range(0, self.size()):
            it = self.__data[i]

            if (it == None):
                continue

            v = t.get(it)
            if (v == None):
                t[self.__data[i]] = 1
                v = 1
            else: v += 1
        
            if (v > max_count):
                max_count = v
                max_elem = it

        if (len(t) == 0):
            return None
        
        return max_elem

    def median(self):
        sz = self.size()
        if (sz%2==0):
            return self.__data[int(sz/2)]
        else:
            return self.__data[int(sz/2 + 1)]

d = ndarray([3,3,3], None)
d[2,2,2] = 9
d[2,2,1] = 5
d[2,2,0] = 5
print(d[2,2,2])
print(d.moda())
print(d.median())