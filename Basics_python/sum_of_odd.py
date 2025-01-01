def sum_of_odds(n):
    total = 0
    for i in range(1, n, 2):  # This loop iterates over odd numbers less than n
        total += i
    return total
