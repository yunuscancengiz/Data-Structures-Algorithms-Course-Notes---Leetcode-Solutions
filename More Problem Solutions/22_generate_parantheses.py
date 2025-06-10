'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def generate(current_str: str, left_count: int, right_count: int):
            if len(current_str) == (n * 2):
                result.append(current_str)
                return
            
            if left_count < n:
                generate(current_str=current_str + '(', left_count=left_count + 1, right_count=right_count)

            if right_count < left_count:
                generate(current_str=current_str + ')', left_count=left_count, right_count=right_count + 1)
        generate(current_str='', left_count=0, right_count=0)
        return result


if __name__ == '__main__':
    print(Solution().generateParenthesis(n=3))