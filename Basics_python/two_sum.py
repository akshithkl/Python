def two_sum(nums, target):
    num_map = {}  # Stores number → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Example usage:
nums = [2, 3, 11,9, 7, 15]
target = 9
print(two_sum(nums, target)) 


# Time: O(n)

# Space: O(n)