'''
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:

1 <= n <= 5 * 104
'''


class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        result = []

        def dfs(curr: int):
            if curr > n:
                return
            result.append(curr)
            for i in range(10):
                next_num = curr * 10 + i
                if next_num > n:
                    break
                dfs(next_num)

        for i in range(1, 10):
            dfs(i)

        return result
    

if __name__ == '__main__':
    print(Solution().lexicalOrder(n=13))