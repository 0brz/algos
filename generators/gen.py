

def count_up_to(n):
    count= 0
    while(count < n):
        yield count
        count += 1

def fibo(n):
    k = 0
    s1 = 0
    s2 = 1
    while(k < n):
        f = s1+s2
        yield f
        s2 = s1
        s1 = f
        k+=1
        
t = fibo(10)
for i in t:
    print(i)