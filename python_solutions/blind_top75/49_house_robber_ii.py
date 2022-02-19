from typing import List
from collections import defaultdict


class Trie:

    def __init__(self):
        self.word = ''
        self.children = defaultdict(Trie)
        self.isWord = False


    def addWord(self, word):
        curr = self
        for char in word:
            curr = curr.children[char]
        curr.isWord = True
        curr.word = word


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()
        [trie.addWord(word) for word in words]

        m = len(board)
        n = len(board[0])

        matched_words = []

        def backtrack(i, j, trie, visited):
            if (i,j) in visited:
                return False
            else:
                visited.add((i, j))

            letter = board[i][j]
            node = trie.children[letter]

            if node.isWord:
                matched_words.append(node.word)

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if 0 <= new_i < m and 0 <= new_j < n and board[new_i][new_j] in node.children:
                    new_visited = visited.copy()
                    new_visited.add(board[new_i][new_j])
                    backtrack(new_i, new_j, node, new_visited)

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.children:
                    backtrack(i, j, trie, set())

        return matched_words








    ''' TLE '''
    def findWord_TLE(self, board, word):

        m = len(board)
        n = len(board[0])

        def _findRemainingOfWord(i, j, word_index, visited):

            print("iterating for i j %s %s, visited: %s" % (i, j, str(visited)))
            if (i, j) in visited:
                return False
            else:
                visited.add((i, j))

            if word_index == len(word):

                return True

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if 0<=new_i<m and 0<=new_j<n and board[new_i][new_j] == word[word_index]:
                    if _findRemainingOfWord(new_i, new_j, word_index+1, visited.copy()):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if _findRemainingOfWord(i, j, 1, set()):
                        return True

        return False

    def findWords_TLE(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.found_words = dict()
        words = [word for word in words if self.findWord(board, word)]
        return words



if __name__ == '__main__':
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    # board = [['a', 'a']]
    # words = ['aaa']
    ws = Solution().findWords(board, words)
    print("output: %s" % ws)