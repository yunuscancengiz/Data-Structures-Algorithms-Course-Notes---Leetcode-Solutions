''' 
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        for index in range(0, len(nums) - 1, 2):
            if nums[index] != nums[index + 1]:
                return nums[index]
        if len(nums) % 2 == 1:
            return nums[-1]
        return False
    

    def alternative_bit_manipulation_solution(self, nums):
        ''' 
        Bit Manipulation Solution
        
        XOR Gate Truth Table
        0 0 = 0
        0 1 = 1
        1 0 = 1
        1 1 = 0
        '''
        result = 0
        for num in nums:
            result = num ^ result  
        return result



if __name__ == '__main__':
    nums = [3, 7, 1, 6, 7, 3, 4, 1, 4]
    print(Solution().singleNumber(nums=nums))
    print(Solution().alternative_bit_manipulation_solution(nums=nums))