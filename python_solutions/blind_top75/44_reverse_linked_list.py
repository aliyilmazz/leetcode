
from typing import List

from functools import lru_cache


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        count = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def markIsland(i, j):

            grid[i][j] = 0
            for direction in directions:
                new_i = i+direction[0]
                new_j = j+direction[1]
                if 0<=new_i<m and 0<=new_j<n and grid[new_i][new_j] == "1":
                    markIsland(new_i, new_j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    markIsland(i, j)
                    count += 1

        return count

if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    output = Solution().numIslands(grid)
    print("output: %s" % output)