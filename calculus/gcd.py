
# 6 3 6/3=2
# 3 6 3/6=3

# наибольшее общий делитель
def gcd(a, b):
    while(b != 0):
        rem = a % b
        a = b
        b = rem
        
    return a

#print(gcd(6, 3))
#print(gcd(3, 6))