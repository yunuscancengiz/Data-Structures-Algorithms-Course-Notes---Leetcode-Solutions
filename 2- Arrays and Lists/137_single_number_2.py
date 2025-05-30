'''  
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
'''

# WRONG ANSWER

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result = ~(num & result)
            print(result)
        return abs(result)



if __name__ == '__main__':
    nums = [0,1,0,1,0,1,99]
    #nums = [2,2,3,2]
    nums = [0,0,0,5]
    #nums = [5,0,0,0]
    nums = [99,0,1,0,1,0,1]
    print(Solution().singleNumber(nums=nums))