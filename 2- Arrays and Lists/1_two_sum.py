''' 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

class Solution(object):
    def twoSum(self, nums:list, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in num_map:
                return [num_map[difference], i]
            num_map[num] = i

if __name__ == '__main__':
    nums_list = [[2,7,11,15], [3,2,4], [3,3], [3,5,7,11,15]]
    target_list = [9, 6, 6, 16]
    # nums_list = [[3,2,4]]
    # target_list = [6]
    for nums, target in zip(nums_list, target_list):
        print(Solution().twoSum(nums=nums, target=target))