from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        once we see match for first letter,
        re-curse function with word[1:], 4 times around matrix
        keep visited to avoid loop
        '''

        m = len(board)
        n = len(board[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def backtrack(x, y, wanted_word, visited_coords):
            nonlocal m, n

            wanted_letter = wanted_word[0]
            for _direction_index in range(len(directions)):
                i = x + directions[_direction_index][0]
                j = y + directions[_direction_index][1]

                if not 0 <= i < m or not 0 <= j < n:
                    continue

                if tuple([i, j]) in visited_coords:
                    continue

                candidate_letter = board[i][j]
                if candidate_letter == wanted_letter:
                    remaining_word = wanted_word[1:]

                    if not remaining_word:
                        return True

                    # keep on digging
                    #new_coords = visited_coords.copy()
                    visited_coords.add(tuple([i, j]))
                    result = backtrack(i, j, remaining_word, visited_coords)
                    if result:
                        return True
                    else:
                        visited_coords.remove(tuple([i, j]))

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True

                    visited_coords = {tuple([i, j])}
                    if backtrack(i, j, word[1:], visited_coords):
                        return True
        return False



if __name__ == '__main__':
    board, word = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
    output = Solution().exist(board, word)
    print("word: %s, output: %s" % (word, output))

    board, word = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
    output = Solution().exist(board, word)
    print("searched word: %s, output: %s" % (word, output))

    board, word = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"
    output = Solution().exist(board, word)
    print("searched word: %s, output: %s" % (word, output))

    board, word = [['a', 'a']], 'aaa'
    output = Solution().exist(board, word)
    print("searched word: %s, output: %s" % (word, output))


