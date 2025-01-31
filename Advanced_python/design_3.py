def inverted_triangle(rows):
    for i in range(rows, 0, -1):
        print("*" * i)

rows = int(input("Enter number of rows: "))
inverted_triangle(rows)
