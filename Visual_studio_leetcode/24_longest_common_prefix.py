
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        res =""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            
            res += strs[0][i]
        
        return res

       
a = Solution()
c = ['flower', 'f', 'fluent']
print(a.longestCommonPrefix(c))

        