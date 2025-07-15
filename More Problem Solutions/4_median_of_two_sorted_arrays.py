'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

'''


from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        is_even = total_len % 2 == 0
        mid1 = total_len // 2 - 1 if is_even else total_len // 2
        mid2 = mid1 + 1 if is_even else None

        result = 0
        i = j = count = 0

        while i < len(nums1) or j < len(nums2):
            if i < len(nums1) and (j >= len(nums2) or nums1[i] <= nums2[j]):
                current = nums1[i]
                i += 1
            else:
                current = nums2[j]
                j += 1

            if count == mid1 or (is_even and count == mid2):
                result += current
            count += 1

            if not is_even and count > mid1:
                break
            if is_even and count > mid2:
                break

        return result if not is_even else result / 2
    

if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1=nums1, nums2=nums2))