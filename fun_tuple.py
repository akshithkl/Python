'''def num(*a):
    print(a)

num(1, 4, 5, 6)'''




def add(*numbers):
    
    print(type(numbers))
    
    return sum(numbers)

print(add(5, 8, 2))
