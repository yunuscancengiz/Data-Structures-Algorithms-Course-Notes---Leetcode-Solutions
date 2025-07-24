'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

'''

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        temp = None
        i = 0

        while i < len(intervals):
            if i == len(intervals) - 1:
                if temp:
                    result.append(temp)
                    temp = None
                else:
                    result.append(intervals[i])
                break

            if temp:
                start_list = temp
            else:
                start_list = intervals[i]


            if start_list[1] >= intervals[i + 1][0] or start_list[1] >= intervals[i + 1][1]:
                
                if temp:
                    temp[1] = intervals[i + 1][1] if intervals[i + 1][1] >= temp[1] else temp[1]
                else:
                    temp = [start_list[0], intervals[i + 1][1] if intervals[i + 1][1] >= start_list[1] else start_list[1]]
            else:
                if temp:
                    result.append(temp)
                    temp = None
                else:

                    result.append(intervals[i])
            i += 1
        return result
    
if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    #intervals = [[1, 4], [4, 5]]
    #intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    print(Solution().merge(intervals=intervals))
        