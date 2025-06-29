'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        prev = None
        index = 1
        
        while True:
            for s in strs:
                if index > len(s):
                    return prefix
                if not prev:
                    prev = s[:index]
                    continue
                else:
                    if prev != s[:index]:
                        return prefix
            prefix = s[:index]
            prev = None
            index += 1
        return prefix