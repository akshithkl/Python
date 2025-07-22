class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Map each course to prereq list
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs) 
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
            
        for crs in range(numCourses):
            if not dfs(crs): 
                return False
            
        return True

# numCourses = 5
# prerequisites = [[0, 1],[0, 2], [1, 3], [1, 4], [3, 4]]
# print(Solution().canFinish(numCourses, prerequisites))

numCourses = 3
prerequisites = [[0, 1], [1,2], [2, 0]]
print(Solution().canFinish(numCourses, prerequisites))

# Algorithm: Depth-First Search (DFS)
# Approach: Topological Sort using DFS + cycle detection
# Technique: Graph traversal, Backtracking


# Time Complexity: O(V + E)
# V = number of courses (vertices)
# E = number of prerequisites (edges)
# Space Complexity: O(V + E)
