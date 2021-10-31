from typing import List


class Solution:

    @staticmethod
    def _isValidGroup(group: List[str]) -> bool:
        print("input: %s" % group)
        nums = [int(x) for x in group if x.isdigit()]
        if len(nums) > len(set(nums)):
            return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # [0] check rows
        if not all([self._isValidGroup(row) for row in board]):
            return False

        # [1] check cols
        cols = [[board[i][j] for i in range(9)] for j in range(9)]
        if not all([self._isValidGroup(col) for col in cols]):
            return False

        # [2] check boxes
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                box = [board[_i][_j] for _j in range(j, j + 3) for _i in range(i, i + 3)]
                if not self._isValidGroup(box):
                    return False

        return True


def verbose_assert(_list):
    output = Solution().isValidSudoku(_list)
    print("Input:  %s\nOutput: %s" % (_list, output))


if __name__ == '__main__':
    input = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    verbose_assert(input)
