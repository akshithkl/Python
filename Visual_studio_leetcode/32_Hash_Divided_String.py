class Solution:
    def stringHash(self, s: str, k: int) -> str:
        rs = ""
        c = "abcdefghijklmnopqrstuvwxyz"
        l = k
        count = 0
        temp = 0
        for i in range (len(s)):
            if count < l:
                temp += ord(s[i]) - ord('a')
                count += 1
            else:
                rs += c[temp % 26]
                temp = ord(s[i]) - ord('a')
                count = 1
            
            if i == len(s) - 1:
                rs += c[temp % 26]

        return rs 

a = Solution()
print(a.stringHash("abcd",2))

print(a.stringHash("mxz",3))