class Solution(object):
    def canCompleteCircuit(self, gas, cost):

        if sum(gas) < sum(cost): 
            return -1
        
        total = 0
        index = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                index = i + 1
            
        return index

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]


a = Solution()
print(a.canCompleteCircuit(gas, cost))