from typing import List



class Solution:
    def setZeroes_omplusnspace(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        blacklist_rows = set()
        blacklist_cols = set()
        for _rowindex, row in enumerate(matrix):
            for _colindex, element in enumerate(row):
                if element == 0:
                    blacklist_rows.add(_rowindex)
                    blacklist_cols.add(_colindex)

        for _rowindex, row in enumerate(matrix):
            for _colindex, element in enumerate(row):
                if _rowindex in blacklist_rows or _colindex in blacklist_cols:
                    matrix[_rowindex][_colindex] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])

        clear_top_row = not all(matrix[0])
        clear_left_column = not all([matrix[i][0] for i in range(m)])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if clear_top_row:
            for i in range(n):
                matrix[0][i] = 0

        if clear_left_column:
            for i in range(m):
                matrix[i][0] = 0

a,
if __name__ == '__main__':
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 6],
        [7, 8, 5, 2]
    ]
    Solution().setZeroes(matrix)
    print("matrix: %s" % matrix)