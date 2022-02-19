class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, diagonals, anti_diagonals, cols):
            # base case: N queens have been placed
            if row == n:
                return 1

            solutions = 0
            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                if (
                        col in cols
                        or curr_diagonal in diagonals
                        or curr_anti_diagonal in anti_diagonals
                ):
                    # if queen is not placeable, skip current col
                    continue

                # add the queen to the board
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)

                # move on to the next row with the updated board state
                solutions += backtrack(row + 1, diagonals, anti_diagonals, cols)

                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)

            return solutions

        return backtrack(0, set(), set(), set())


if __name__ == '__main__':
    n = 4
    result = Solution().totalNQueens(n)
    print("N: %s, Result: %s" % (n, result))