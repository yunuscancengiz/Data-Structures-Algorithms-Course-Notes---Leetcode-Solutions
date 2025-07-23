'''
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 

Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.


'''



class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        map_ = {}
        if x >= y:
            greater, lower = x, y
            map_['greater'] = 'ab'
            map_['lower'] = 'ba'
        else:
            greater, lower = y, x
            map_['greater'] = 'ba'
            map_['lower'] = 'ab'

        def remove(s, first, second, score):
            stack = []
            total_score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    total_score += score
                else:
                    stack.append(char)
            return ''.join(stack), total_score
        
        s, score1 = remove(s=s, first=map_['greater'][0], second=map_['greater'][1], score=greater)
        s, score2 = remove(s=s, first=map_['lower'][0], second=map_['lower'][1], score=lower)
        return int(score1 + score2)