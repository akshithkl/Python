class Solution:
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = [] # pair (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index)) # (i - index) this is calculation of width
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max( maxArea, h * (len(heights) - i))
        return maxArea

heights = [2,1,5,6,2,3]
print(Solution().largestRectangleArea(heights))


# | Category       | Name                                                             |
# | -------------- | ---------------------------------------------------------------- |
# | Data Structure | Stack (Monotonic Stack)                                          |
# | Pattern        | Greedy + Stack                                                   |
# | Strategy       | Simulate histogram processing while maintaining increasing order |
# | Optimization   | Lazy Evaluation of Width using stored indices                    |
