'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

'''

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_ = {}
        result = []
        sorted_strs = []

        for s_list in strs:
            s_list = list(s_list)
            s_list.sort()
            sorted_strs.append(str(s_list))

        for index, s in enumerate(sorted_strs):
            if s not in map_.keys():
                map_[s] = []
            map_[s].append(index)

        for indexes in map_.values():
            result.append([strs[index] for index in indexes])
        return result
        