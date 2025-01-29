def sub(a,b,k):
    
    c = a + b
    k.append(c)


def num(a,b):
    
    k = []
    
    while len(k) < 10:
        sub(a,b,k)
        a += 1
        b += 1
        n = len(k)  # it shows list size
    return k

r =num(1,2)
print(r)



