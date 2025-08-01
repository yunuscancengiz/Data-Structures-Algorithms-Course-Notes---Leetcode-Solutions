'''
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

 

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.

'''

class Solution:
    def makeFancyString(self, s: str) -> str:
        result = s[0]
        counter = 1

        for i in range(1, len(s)):
            if s[i] == result[-1]:
                counter += 1
                if counter < 3:
                    result += s[i]
            else:
                counter = 1
                result += s[i]
        return result



        

if __name__ == '__main__':
    s = 'aaabaaaa'
    print(Solution().makeFancyString(s=s))