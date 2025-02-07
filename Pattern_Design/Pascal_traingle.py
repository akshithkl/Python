def pascal_triangle(rows):
    for i in range(rows):
        print(" " * (rows - i), end="")
        value = 1
        for j in range(i + 1):
            print(value, end=" ")
            value = value * (i - j) // (j + 1)
        print()

rows = int(input("Enter the number of rows: "))
pascal_triangle(rows)
