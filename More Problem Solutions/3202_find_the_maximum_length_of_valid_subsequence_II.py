'''
You are given an integer array nums and a positive integer k.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
Return the length of the longest valid subsequence of nums.
 

Example 1:

Input: nums = [1,2,3,4,5], k = 2

Output: 5

Explanation:

The longest valid subsequence is [1, 2, 3, 4, 5].

Example 2:

Input: nums = [1,4,2,3,1,4], k = 3

Output: 4

Explanation:

The longest valid subsequence is [1, 4, 1, 4].

 

Constraints:

2 <= nums.length <= 103
1 <= nums[i] <= 107
1 <= k <= 103

'''

from typing import List

from collections import defaultdict

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums))]
        max_ = 1

        for i in range(len(nums)):
            for j in range(i):
                mod = (nums[j] + nums[i]) % k
                dp[i][mod] = max(dp[i][mod], dp[j][mod] + 1)
                max_ = max(max_, dp[i][mod] + 1)
        return max_

    

if __name__ == '__main__':
    nums = [1,2,3,4,5]
    k = 2

    #nums = [1,4,2,3,1,4] # 2, 0, 2, 1, 2
    #k = 3
    print(Solution().maximumLength(nums=nums, k=k))