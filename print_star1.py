width = 5   # Number of columns
height = 4  # Number of rows

for i in range(height):
    for j in range(width):
        # Print '*' for the border positions (first/last rows or columns)
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # Move to the next line after each row
