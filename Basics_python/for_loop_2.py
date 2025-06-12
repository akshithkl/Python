nums = [1, 2, 3, 4]
for i in range(len(nums) - 1):
    print(f"{(nums[i], nums[i+1])}\t", end="")
# Output: (1,2) (2,3) (3,4)
