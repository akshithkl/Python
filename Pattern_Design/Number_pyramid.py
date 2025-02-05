def number_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

rows = int(input("Enter number of rows: "))
number_pyramid(rows)
