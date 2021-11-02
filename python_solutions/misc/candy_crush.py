from typing import List


class Solution:

    @staticmethod
    def arrange_zeroes(col: List[int]):
        nonzero_list = [x for x in col if x != 0]
        return [0] * (len(col) - len(nonzero_list)) + nonzero_list

    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        """

        # --- 1. do the popping ---

        while has_popping:

            col_length = len(board)
            for _index, row in enumerate(board):
                for member in row:
                    if same as last member:
                        increment count
                        if count == 3:
                            pop it
                    if _index < col_length - 2
                        if same lower two members?
                            pop

        if no popping:
            return board


        # --- 2. let the candies fall :D ---

        [0, 0, 0, 2, 0, 3, 1, 0, 5]
        [0, 0, 0, 0, 0, 2, 3, 1, 5]

        start from the rightside (last row)
        for row in board[::-1]:
            if zero, replace with upper one
            continue this until we have no zero in row

        has_popping = True
        go back to popping
        """

        last_member_in_row = None
        current_row_streak = 0
        REQUIRED_FREQUENCY = 3

        while True:

            popping_happened = False

            col_length = len(board)
            for _col_index, row in enumerate(board):
                rows = iter(range(len(board[0])))
                for _row_index in rows:
                    member = board[_col_index][_row_index]
                    if member == 0:
                        continue

                    if member == last_member_in_row:
                        current_row_streak += 1
                        if current_row_streak == REQUIRED_FREQUENCY:
                            extra_row = 0
                            temp_runner = _row_index + REQUIRED_FREQUENCY
                            while temp_runner < len(board[_col_index]) and board[_col_index][temp_runner] == member:
                                temp_runner += 1
                                extra_row += 1

                            print("row streak pop (extra:%s)! member:%s, rowindex:%s, colindex:%s" % (
                                extra_row, member, _row_index, _col_index
                            ))
                            print("current board: %s" % board)
                            popping_happened = True
                            for temp_offset in range(REQUIRED_FREQUENCY + extra_row):
                                row[_row_index - temp_offset] = 0
                            [next(rows) for _ in range(REQUIRED_FREQUENCY - 1 + extra_row)]
                            print("current board: %s" % board)
                            continue
                    else:
                        last_member_in_row = member
                        current_row_streak = 0

                    if _col_index < col_length - 2:
                        downward_elements = [board[_col_index + x][_row_index] for x in range(REQUIRED_FREQUENCY)]
                        if len(set(downward_elements)) == 1:
                            """

                            print("row streak pop! member:%s, rowindex:%s, colindex:%s" % (
                                member, _row_index, _col_index
                            ))
                            print("current board: %s" % board)

                            """
                            extra_col = 0
                            temp_runner = _col_index + REQUIRED_FREQUENCY
                            while temp_runner < len(board) and board[_col_index][_row_index] == member:
                                temp_runner += 1
                                extra_col += 1
                            print("row streak pop! (extra:%s) member:%s, rowindex:%s, colindex:%s" % (
                                extra_col, member, _row_index, _col_index
                            ))
                            print("current board: %s" % board)
                            for temp_offset in range(REQUIRED_FREQUENCY + extra_col):
                                popping_happened = True
                                board[_col_index + temp_offset][_row_index] = 0
                            print("current board: %s" % board)

            if not popping_happened:
                return board

            for col_index in range(len(board[0])):
                col = [board[i][col_index] for i in range(len(board))]
                print("#col for index:%s -> %s" % (col_index, col))
                if 0 not in col:
                    continue
                print("#fixing for index:%s -> %s" % (col_index, col))
                arranged_col = Solution.arrange_zeroes(col)
                print("#fixed arr for for index:%s -> %s" % (col_index, arranged_col))
                for i in range(len(col)):
                    board[i][col_index] = arranged_col[i]


def verbose_assert(args):
    print("Input: %s" % args)
    output = Solution().candyCrush(args)
    print("Output: %s" % output)


if __name__ == '__main__':
    board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
    args = board
    verbose_assert(args)
