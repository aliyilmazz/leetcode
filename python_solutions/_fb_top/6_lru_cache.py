"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class TrieNode:
    def __init__(self, val='', isWord=False):
        self.val = val
        self.isWord = isWord
        self.neighbors = [0] * 26




class Solution:

    def wordBreak(self, s, wordDict):

        def buildTrie():
            head = TrieNode()
            for word in wordDict:
                node = head
                for char in word:
                    char_index = ord(char) - ord('a')
                    if not node.neighbors[char_index]:
                        new_node = TrieNode(char)
                        node.neighbors[char_index] = new_node
                    node = node.neighbors[char_index]
                node.isWord = True

            return head


        def backtrack(results, variation, node, idx):
            if idx == len(s):
                if node.word:
                    results.add(variation)
                return


            if node.word:
                backtrack(results, variation + " ", head, idx)
            else:
                backtrack(results, variation + s[idx], node.neighbors[ord(s[idx])-ord('a')], idx+1)




        head = buildTrie()
        results = set()
        backtrack(results, '', head, 0)
        return results







