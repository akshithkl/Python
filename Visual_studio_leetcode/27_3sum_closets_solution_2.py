class Solution:
    def threeSumClosest(self, nums, target):
        ordered = sorted(nums)
        n = len(ordered)

        maxsum, minsum = sum(ordered[-3:]), sum(ordered[:3])

        if target <= minsum: return minsum
        if target >= maxsum: return maxsum
        
        star, last = 0, n-1
        mindiff = float('inf')
        res = 0
        if abs(target - maxsum) > abs(target - minsum):
            for i in range(n-2):
                star, last = i+1, n-1
                while star < last:
                    pair_sum = ordered[i] + ordered[star] + ordered[last]
                    if pair_sum == target:
                        return pair_sum
                    diff = abs(target - pair_sum)

                    if mindiff > diff:
                        mindiff = diff
                        res = pair_sum

                    if pair_sum > target:
                        last -= 1
                    else:
                        star += 1
        else:
            for i in range(n-1,1,-1):
                star, last = 0, i-1
                while star < last:
                    pair_sum = ordered[i] + ordered[star] + ordered[last]
                    if pair_sum == target:
                        return pair_sum

                    diff = abs(target - pair_sum)

                    if mindiff > diff:
                        mindiff = diff
                        res = pair_sum
                    if pair_sum > target:
                        last -= 1
                    else:
                        star += 1
        return res
    
    
nums = [-1,2,1,-4]

a = Solution()
print(a.threeSumClosest(nums, target=1))


#run tome 4 ms