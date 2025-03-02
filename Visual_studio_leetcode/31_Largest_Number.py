from functools import cmp_to_key

def largestNumber(nums):
    # Convert all numbers to strings
    nums = list(map(str, nums))

    # Custom comparator: sorts based on which concatenation is larger
    def compare(x, y):
        if x + y > y + x:
            return -1  # x should come first
        else:
            return 1  # y should come first

    # Sort using custom comparator
    nums.sort(key=cmp_to_key(compare))

    # Join sorted numbers into a string
    result = "".join(nums)

    # Handle case where all numbers are 0 (e.g., [0, 0])
    return "0" if result[0] == "0" else result

# Example
print(largestNumber([3, 30, 34, 5, 9]))
