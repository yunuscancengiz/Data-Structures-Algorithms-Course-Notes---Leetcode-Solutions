'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000

'''


from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort()
        map_ = {'odd': [], 'even': []}
        for num in nums:
            if num % 2 == 0:
                map_['even'].append(num)
            else:
                map_['odd'].append(num)
        return map_['even'] + map_['odd']