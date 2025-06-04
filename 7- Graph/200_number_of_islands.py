'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

from typing import List
from pprint import pprint

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        num_of_islands = 0

        def bfs(row, col):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            queue = []
            queue.append((row, col))
            visited.add((row, col))

            while len(queue) != 0:
                row, col = queue.pop(0)

                for row_direction, col_direction in directions:
                    new_row = row + row_direction
                    new_col = col + col_direction

                    if new_row in range(rows) and new_col in range(cols) and grid[new_row][new_col] == '1' and (new_row, new_col) not in visited:
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
            
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row=row, col=col)
                    num_of_islands += 1

        return num_of_islands



if __name__ == '__main__':
    """grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]"""

    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    #grid = [["1","1","1"],["0","1","0"],["1","1","1"]]

    print(Solution().numIslands(grid=grid))