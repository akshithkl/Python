class Solution:
    def findJudge(self, n, trust):
        for person in range(1, n + 1):
            trusts_someone = False
            trusted_count = 0

            for a, b in trust:
                if a == person:
                    trusts_someone = True  # person can't be judge
                if b == person:
                    trusted_count += 1     # count how many trust person

            if not trusts_someone and trusted_count == n - 1:
                return person  # found judge

        return -1  # no judge found

n = 3
trust = [[1,3],[2,3],[3,1]]
sol = Solution()
print(sol.findJudge(n,trust))

n = 3
trust = [[1,3],[2,3]]
sol = Solution()
print(sol.findJudge(n,trust))

# Time Complexity: O(N * T)

# For each of the N people, we loop through all T trust pairs → O(N * T).

# Space Complexity: O(1)

# No extra space (besides variables); no arrays or hash maps used.