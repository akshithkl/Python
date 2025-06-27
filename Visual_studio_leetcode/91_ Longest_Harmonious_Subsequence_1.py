class Solution(object):
    def findLHS(self, nums):
    
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        max_len = 0
        for num in freq:
            if num + 1 in freq:
                current_len = freq[num] + freq[num + 1]
                if current_len > max_len:
                    max_len = current_len

        return max_len
nums = [1,3,2,2,5,2,3,7]
sol = Solution()
print(sol.findLHS(nums))
        


# Time Complexity: O(n)

# Building frequency dictionary: O(n), where n = len(nums)

# Traversing dictionary to check for harmonious pairs: O(k), where k is the number of unique elements (at most n)

# In worst case, all elements are unique → k = n, so total is: 𝑂(𝑛)+𝑂(𝑛)=𝑂(𝑛)

#           O(n)+O(n) =  O(n)

# 🗂 Space Complexity: O(n)
# freq dictionary stores count of each unique number.

# In worst case (all elements are unique), dictionary size is n.

# Algorithm Name:
# Frequency Counting using Hash Map (Dictionary)

# Approach:
# 1. Frequency Mapping + Neighbor Check

# First, count how many times each number appears.

# Then, for every number x, check if x + 1 exists in the frequency map.

# If it does, the combination of x and x + 1 is a candidate for a harmonious subsequence.

# Keep track of the maximum length found.

# | Technique                    | Description                                                               |
# | ---------------------------- | ------------------------------------------------------------------------- |
# | **Hash Map / Dictionary**    | Used to count frequency of elements.                                      |
# | **Single Pass Optimization** | Only one pass to count and one to evaluate pairs — very efficient.        |
# | **Greedy Comparison**        | Greedily picks the pair with maximum combined frequency where `diff = 1`. |
# | **No Sorting Needed**        | Avoids O(n log n) sorting by using hash map.                              |


# Why This Approach?
# Avoids generating all subsequences (which is exponential).

# Avoids sorting (which would take O(n log n)).

# Leverages the problem's key constraint: max - min = 1, so only adjacent values matter.

# 🔄 Alternatives (Less Efficient):
# Brute Force: Generate all subsequences, check max-min = 1 → ❌ O(2ⁿ)

# Sorting + Linear Scan: Sort the array and count consecutive segments with diff = 1 → ✅ O(n log n), but slower than hash map

