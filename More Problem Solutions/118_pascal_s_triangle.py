'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows == 1:
            return result
            
        cache = {}
        result.append([1, 1])

        for i in range(2, numRows):
            temp = [1]
            for i in range(len(result[-1]) - 1):
                a, b = result[-1][i], result[-1][i + 1]
                key = (a,b)

                if key in cache:
                    total = cache[key]
                else:
                    total = a + b
                    cache[key] = total
                temp.append(total)
            temp.append(1)
            result.append(temp)
        return result
        