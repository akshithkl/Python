def search_insert_position(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return l

# Example usage
nums = [1, 3, 5, 6]
target = 5
print(search_insert_position(nums, target))  # Output should be 2
