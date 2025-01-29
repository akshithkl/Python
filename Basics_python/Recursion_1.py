def Even_num(num):
    
    print(num)
    
    if num % 2 != 0:
        print("Plese enter only even number")
       
    elif num == 2:
        return num
    else:
        return Even_num(num - 2)

num = int(input("Enter the number : "))
Even_num(num)
