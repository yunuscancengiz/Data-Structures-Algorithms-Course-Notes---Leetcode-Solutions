'''
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.
Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
 

Constraints:

1 <= nums.length <= 1000
-105 <= nums[i] <= 105
1 <= k <= nums.length
'''

from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        result = []
        nums_map = {index: num for index, num in enumerate(nums)}
        nums.sort()
        nums = nums[len(nums) - k:]
        for num in nums_map.values():
            if num in nums:
                result.append(num)
                nums.remove(num)
        return result
    

if __name__ == '__main__':
    nums = [63,-74,61,-17,-55,-59,-10,2,-60,-65]
    k = 9

    nums = [3,4,3,3]
    k = 2
    print(Solution().maxSubsequence(nums=nums, k=k))


        