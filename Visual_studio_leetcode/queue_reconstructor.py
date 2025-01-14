class Solution:
    def reconstructQueue(self, people):
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans
    
    
    
    
a = Solution()
    
result = a.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
print(result)

# h is the height of the person.
# k is the number of people in front of this person who are taller or have the same height
