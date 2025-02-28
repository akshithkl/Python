from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        length_of_s1 = len(s1)
        s1_counter = Counter(s1)
        window_counter = Counter()

        for i, c in enumerate(s2):
            window_counter[c] += 1

            if i >= length_of_s1:
                element_from_left = s2[i - length_of_s1]

                if window_counter[element_from_left] == 1:
                    del window_counter[element_from_left]
                else:
                    window_counter[element_from_left] -= 1
            
            if window_counter == s1_counter:
                return True
        return False
sol = Solution()


s1 = "ab"
s2 = "eidbaooo"
print(sol.checkInclusion(s1, s2)) 

s1 = "ab"
s2 = "eidboaoo"
print(sol.checkInclusion(s1, s2))  

