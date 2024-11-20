def details(**information):                              # This is keyword arguments
    print(type(information))
    
    for key,value in information.items():
        print(f"{key} : {value}")
    
details(name = "Akshith" , age = 20, Branch = "AIML")