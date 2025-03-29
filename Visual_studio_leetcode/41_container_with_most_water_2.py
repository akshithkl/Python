# Brute force

def maxAreaBruteForce(height):
    max_water = 0
    n = len(height)
    
    # Try all pairs (i, j)
    for i in range(n):
        for j in range(i + 1, n):
            area = (j - i) * min(height[i], height[j])  # Compute area
            max_water = max(max_water, area)  # Update max area

    return max_water

# Example test case
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxAreaBruteForce(height))  # Output: 49
