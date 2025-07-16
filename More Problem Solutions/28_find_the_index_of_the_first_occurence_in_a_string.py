'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = -1
        if len(haystack) < len(needle):
            return -1
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                if result == -1:
                    result = i
                j += 1
            else:
                if result != -1: i = result
                j = 0
                result = -1
            i += 1
        if j < len(needle):
            result = -1
        return result
        

if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    print(Solution().strStr(haystack=haystack, needle=needle))