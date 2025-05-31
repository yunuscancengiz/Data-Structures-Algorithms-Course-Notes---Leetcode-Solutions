'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

'''

class Solution(object):
    def reverseString(self,s, start: int=0, end:int=None):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if end is None:
            end = len(s) - 1
        if start > end:
            return
        s[start], s[end] = s[end], s[start]
        self.reverseString(s=s, start=start + 1, end=end - 1)
        

if __name__ == '__main__':
    s = ['h', 'e', 'l', 'l', 'o']
    Solution().reverseString(s=s)