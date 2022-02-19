from collections import deque, defaultdict
from functools import lru_cache
from typing import List


class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.isWord = False

    def addWord(self, word):
        curr = self
        for char in word:
            curr = curr.child[char]
        curr.isWord = True


class Solution:

    def wordBreak_recur(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dp = [-1] * n

        def _wordBreak(s, x):

            if s == '':
                return True

            if x == -1:
                return True

            if dp[x] != -1:
                return dp[x]

            subword = ''
            for i in range(x, -1, -1):
                subword = s[i] + subword
                if subword in wordDict:
                    if i == 0:
                        dp[x] = 1
                        return True

                    if _wordBreak(s, i - 1):
                        return True
            dp[x] = 0
            return False

        return _wordBreak(s, x=len(s) - 1)

    def wordBreak_bfs(self, s, wordDict):

        n = len(s)
        word_set = set(wordDict)
        queue = deque()
        visited = set()

        queue.append(0)

        while queue:
            start_index = queue.popleft()
            if start_index in visited:
                continue

            for end_index in range(start_index + 1, n + 1):
                if s[start_index:end_index] in word_set:
                    if end_index == n:
                        return True
                    else:
                        queue.append(end_index)
            visited.add(start_index)
        return False

    def wordBreak_dp(self, s, wordDict):

        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]

    def wordBreak(self, s, wordDict):
        root = TrieNode()
        n = len(s)
        for word in set(wordDict):
            root.addWord(word)

        @lru_cache
        def dp(start_index):
            if start_index == n:
                return True

            traverser = root
            for i in range(start_index, n):
                current_char = s[i]
                if current_char not in traverser.child:
                    break  # only for optimization
                traverser = traverser.child[current_char]
                if traverser.isWord and dp(i + 1):
                    return True

            return False

        return dp(0)


if __name__ == '__main__':
    s = "leetcode"
    wordList = ["leet", "code", "leax"]
    result = Solution().wordBreak(s, wordList)
    print("result: %s" % result)