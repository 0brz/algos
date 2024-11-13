
def pow_sqrt(a):
    return a*a

# pow
def pow(a, to):
    to-= 1
    while(to > 0):
        a = a*a
        to -= 1

    return a

# pow by partiotions
def pow_partiotioned(a, to, to_part_sz):
    avg_to = int(to / to_part_sz)
    k = 1
    for i in range(0, to_part_sz):
        k *= pow(a, avg_to)
    
    if (to % to_part_sz != 0):
        k*= a

    return k

# pow + partiotioned
def pow2(a, to):

    coef = 1
    if (to < 0):
        coef = -1

    res = pow_partiotioned(
        a,
        (to*coef),
        int((to*coef)/4) + 1
    )

    if (to < 0):
        return 1/float(res)
    
    return float(res)

print(pow2(6, 1))
print(pow2(6, 2))
print(pow2(6, 3))

print(pow2(6, -1))
print(pow2(6, -2))
print(pow2(6, -3))

#print(pow_pariotioned(7, 5, 2))