'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        hashmap = {}
        unique = []

        for index, char in enumerate(s):
            if char not in hashmap.keys():
                hashmap[char] = []
            hashmap[char].append(index)

            if len(hashmap[char]) == 1:
                if char not in unique: 
                    unique.append(char)
            elif len(hashmap[char]) > 1:
                if char in unique:
                    unique.remove(char)
        if unique:
            return hashmap[unique[0]][0]
        return -1


if __name__ == '__main__':
    s = 'leetcode'
    print(Solution().firstUniqChar(s=s))