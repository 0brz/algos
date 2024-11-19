
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
    
    def __init__(self, bounds=[]):
        self.__dim_bounds = bounds    
    
    def indexOf(self, index=[]):
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