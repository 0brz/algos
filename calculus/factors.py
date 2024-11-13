from math import *

# check number is prime
def is_prime(a):
    for i in range(2, a):
        if (a % i == 0):
            return False        
    return True

def prime_range(to):
    ls = [1, 2]

    if (to == 1):
        return [1]
    elif (to == 2):
        return [1, 2]

    for i in range(3, to+1):

        if (i % 2 == 0):
            continue 

        if (is_prime(i)):
            ls.append(i)
    
    return ls

# by sqrt and table fill
def prime_range2(to):
    if (to < 4):
        return prime_range(to)
    
    out = [1]

    max = int(sqrt(to))
    for i in range(2, to):
        f = True
        max_check = min(max, i)
        for j in range(2, max_check):
            if (i % j == 0):
                f = False
                break
        
        if (f):
            out.append(i)

    return out

print(prime_range2(10))
print(prime_range2(15))