import time

def Find(a):
    seq = [0,1]
    for i in range(a):
        seq.append(seq[-1] + seq[-2])
    return seq[-2]



def fibonassi(a):
    if a <= 1:
        return a
    else:
        return fibonassi(a - 1) + fibonassi(a - 2)
    
print("********recursion*********")
recursion = time.time()
print(fibonassi(14))
print("speed : "+ str(time.time() - recursion))


print("********iteration*********")
iteration = time.time()
print(Find(14))
print("speed : "+ str(time.time() - iteration))