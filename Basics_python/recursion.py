def sum(a, b):
    if a >= 10:
        return a + b
    return sum(a + 1, b)

sol = sum(1, 1)
print(sol)
