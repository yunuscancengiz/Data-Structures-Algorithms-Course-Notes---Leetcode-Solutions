'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109


'''

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = None
        last = None

        for i in range(len(nums)):
            if nums[i] == target:
                if first is None:
                    first = i
                last = i
        if first is None and last is None:
            first = last = -1
        return [first, last]