'''
You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:

'N' : Move north by 1 unit.
'S' : Move south by 1 unit.
'E' : Move east by 1 unit.
'W' : Move west by 1 unit.
Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.

The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.
 

Example 1:

Input: s = "NWSE", k = 1

Output: 3

Explanation:

Change s[2] from 'S' to 'N'. The string s becomes "NWNE".

Movement	Position (x, y)	Manhattan Distance	Maximum
s[0] == 'N'	(0, 1)	0 + 1 = 1	1
s[1] == 'W'	(-1, 1)	1 + 1 = 2	2
s[2] == 'N'	(-1, 2)	1 + 2 = 3	3
s[3] == 'E'	(0, 2)	0 + 2 = 2	3
The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.

Example 2:

Input: s = "NSWWEW", k = 3

Output: 6

Explanation:

Change s[1] from 'S' to 'N', and s[4] from 'E' to 'W'. The string s becomes "NNWWWW".

The maximum Manhattan distance from the origin that can be achieved is 6. Hence, 6 is the output.

 

Constraints:

1 <= s.length <= 105
0 <= k <= s.length
s consists of only 'N', 'S', 'E', and 'W'.
'''

# DIDN'T PASSED ALL CASES


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        s = list(s)
        directions = {
            'N': [0, [0, 1]],
            'S': [0, [0, -1]],
            'W': [0, [-1, 0]],
            'E': [0, [1, 0]]
        }
        origin = [0, 0]
        location = [0, 0]
        max_distance = 0

        for i in range(len(s)):
            directions[s[i]][0] += 1

        swap = []
        for i in range(len(s)):
            if k > 0:
                if s[i] in swap:
                    swap.remove(s[i])
                    directions[s[i]][0] -= 1
                    k -= 1
                    if s[i] == 'N':
                        s[i] = 'S'
                    elif s[i] == 'S':
                        s[i] = 'N'
                    elif s[i] == 'W':
                        s[i] = 'E'
                    elif s[i] == 'E':
                        s[i] = 'W'
                else:
                    if directions[s[i]][0] > 0:
                        if s[i] == 'N':
                            if directions[s[i]][0] >= directions['S'][0]:
                                directions[s[i]][0] += 1
                                swap.append('S')
                            else:
                                directions[s[i]][0] -= 1
                                directions['S'][0] += 1
                                s[i] = 'S'
                                k -= 1
                            
                        elif s[i] == 'S':
                            if directions[s[i]][0] >= directions['N'][0]:
                                directions[s[i]][0] += 1
                                swap.append('N')
                            else:
                                directions[s[i]][0] -= 1
                                directions['N'][0] += 1
                                s[i] = 'N'
                                k -= 1

                        elif s[i] == 'W':
                            if directions[s[i]][0] >= directions['E'][0]:
                                directions[s[i]][0] += 1
                                swap.append('E')
                            else:
                                directions[s[i]][0] -= 1
                                directions['E'][0] += 1
                                s[i] = 'E'
                                k -= 1

                        elif s[i] == 'E':
                            if directions[s[i]][0] >= directions['W'][0]:
                                directions[s[i]][0] += 1
                                swap.append('W')
                            else:
                                directions[s[i]][0] -= 1
                                directions['W'][0] += 1
                                s[i] = 'W'
                                k -= 1

            location[0] += directions[s[i]][1][0]   # update current location's x
            location[1] += directions[s[i]][1][1]   # update current location's y
            distance = abs(location[0] - origin[0]) + abs(location[1] - origin[1])
            if distance > max_distance:
                max_distance = distance
        return max_distance



if __name__ == '__main__':
    s = "NSWWEW"
    k = 3

    #s = "NWSE"
    #k = 1

    #s = 'WEES'
    #k = 2

    #s = 'WEWE'
    #k = 1

    s = 'EWWE'
    k = 1
    print(Solution().maxDistance(s=s, k=k))