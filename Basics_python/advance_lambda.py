
students = [{"name" : "Akshith", "mark" : 24},
            {"name" : "pruthviraj", "mark" : 86},
            {"name" : "bharath", "mark" : 75}]

students.sort( key = lambda x : x ["mark"], reverse= True)

print(students)
