'''
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        max_ = 0
        counter = 0
        result = {}

        slow, fast = 0, 1
        while slow < len(s) and fast < len(s):
            if s[slow] not in result.keys():
                result[s[slow]] = slow
                counter += 1
                max_ = max(max_, counter)

            if s[fast] in result.keys():
                slow = result[s[fast]] + 1
                fast = slow + 1
                counter = 0
                result = {}
                continue
            result[s[fast]] = fast
            counter += 1
            max_ = max(max_, counter)
            fast += 1
        return max_
        

if __name__ == '__main__':
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s=s))