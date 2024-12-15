
from basic_stack import *

def trains_depo_sort(trains=[]):
    # 3 stack parts / can increase
    s1 = basic_stack()
    s2 = basic_stack()
    s3 = basic_stack()

    min1 = float('inf')
    min2 = float('inf')
    min3 = float('inf') 

    min_stack = None

    def get_min_stack(val) -> basic_stack:
        v1 = s1.top()
        v2 = s2.top()
        v3 = s2.top()
        
        if (v1 == None): return s1
        if (v2 == None): return s2
        if (v3 == None): return s3

        min_st = None
        min_val = float('inf')
        t = [(v1, s1), (v2, s2), (v3, s3)]
        for i in range(0, len(t)-1):
            if (abs(val - t[i][0]) < min_val):
                min_val = t[i][0]
                min_st = t[i][1]
        
        return min_st

    def push_min(stack, val):
        if (stack == s1):
            stack.push(val)
            min1 = min(val, min1)

        if (stack == s2):
            stack.push(val)
            min2 = min(val, min2)   
        
        if (stack == s3):
            stack.push(val)
            min3 = min(val, min3)

    for i in range(0, len(trains)-1):
        optimal_stack = get_min_stack()
        push_min(optimal_stack, trains[i])


    

