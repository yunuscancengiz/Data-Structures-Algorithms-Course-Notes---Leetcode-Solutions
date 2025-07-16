'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        for i in range(len(s)):
            odd_center = expand(left=i, right=i)
            even_center = expand(left=i, right=i +1)
            result = odd_center if len(odd_center) > len(result) else result
            result = even_center if len(even_center) > len(result) else result
        return result