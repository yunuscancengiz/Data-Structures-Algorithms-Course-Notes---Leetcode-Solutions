'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

'''

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 1
        while True:
            if fast >= len(nums):
                slow += 1
                fast = slow + 1
            if slow >= len(nums) - 1:
                return nums

            if nums[slow] > nums[fast]:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            fast += 1


        