'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 

Follow up: Could you solve the problem in linear time and in O(1) space?

'''

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = 1
        nums.sort()
        slow, fast = 0, 1

        while fast <= len(nums):
            if fast == len(nums):
                if counter <= n / 3:
                    nums.pop()
                break

            if nums[slow] == nums[fast]:
                counter += 1
                nums.pop(fast)
            else:
                if counter <= n / 3:
                    nums.pop(slow)
                else:
                    slow += 1
                    fast += 1
                counter = 1
        return nums


if __name__ == '__main__':
    nums = [4, 2, 1, 1]
    print(Solution().majorityElement(nums=nums))