class Solution(object):
    def findLHS(self, nums):
        def is_harmonious(subseq):
            if len(subseq) < 2:
                return False
            # Find max and min manually
            max_val = subseq[0]
            min_val = subseq[0]
            for val in subseq:
                if val > max_val:
                    max_val = val
                if val < min_val:
                    min_val = val
            return max_val - min_val == 1

        def generate_subsequences(nums):
            result = []
            n = len(nums)
            total = 1 << n  # 2^n
            for mask in range(total):
                temp = []
                for i in range(n):
                    if (mask >> i) & 1:
                        temp.append(nums[i])
                result.append(temp)
            return result

        max_len = 0
        subsequences = generate_subsequences(nums)

        for seq in subsequences:
            if is_harmonious(seq):
                if len(seq) > max_len:
                    max_len = len(seq)

        return max_len


# Bruteforce

# | Metric               | Value                                    |
# | -------------------- | ---------------------------------------- |
# | **Time Complexity**  | O(2ⁿ × n)                                |
# | **Space Complexity** | O(2ⁿ × n) (for storing all subsequences) |
