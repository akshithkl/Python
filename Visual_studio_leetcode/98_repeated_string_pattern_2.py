class Solution(object):
    def repeatedSubstringPattern(self, s):
 
        return s in (s + s)[1:-1]

s = "abab"
sol = Solution()
print(sol.repeatedSubstringPattern(s))


# | Complexity Type | Value  | Explanation                                                                                                 |
# | --------------- | ------ | ----------------------------------------------------------------------------------------------------------- |
# | **Time**        | `O(n)` | `s + s` takes O(n), slicing takes O(n), and `"s in X"` is a substring search (efficient, average-case O(n)) |
# | **Space**       | `O(n)` | `s + s` and the slice `(s + s)[1:-1]` create a new string of length `2n - 2`                                |


# | Category        | Value                                                                                       |
# | --------------- | ------------------------------------------------------------------------------------------- |
# | **Algorithm**   | Substring Search / String Trick                                                             |
# | **Approach**    | Concatenation & Substring Inclusion                                                         |
# | **Technique**   | String doubling and boundary slicing                                                        |
# | **Search Type** | Pattern matching (`in` operator = uses efficient search like Boyer-Moore or KMP internally) |


# | **Aspect**           | **Details**                                              |
# | -------------------- | -------------------------------------------------------- |
# | **Problem**          | Check if string is made by repeating a substring         |
# | **Code Trick**       | `s in (s + s)[1:-1]`                                     |
# | **Algorithm**        | Pattern Matching via String Manipulation                 |
# | **Approach**         | String doubling and substring check                      |
# | **Technique**        | Remove first & last char from `s+s`, search original `s` |
# | **Time Complexity**  | `O(n)`                                                   |
# | **Space Complexity** | `O(n)`                                                   |
# | **Pros**             | Very short and elegant                                   |
# | **Cons**             | Relies on built-in search and slicing                    |
