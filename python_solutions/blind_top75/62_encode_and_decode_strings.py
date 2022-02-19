from collections import defaultdict, Counter, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:

        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)


if __name__ == '__main__':
    words = ["wrt","wrf","er","ett","rftt"]
    words = ["z", "z"]
    words = ["ab", "abc"]
    #words = ["zy", "zx"]
    #words = ["z", "x", "z"]
    #words = ["z", "z"]
    #words = ["ac", "ab", "zc", "zb"]
    order = Solution().alienOrder(words)
    print("order: %s" % order)




'''

my failed solution



from typing import List

from collections import defaultdict


class GNode:
    def __init__(self):
        self.degree = 0
        self.out_nodes = []


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        if n == 1:
            return ""

        adjacency_dict = defaultdict(GNode)

        def compare_words(prev_word, curr_word):
            for char in prev_word:
                adjacency_dict[char]  # register them
            for char in curr_word:
                adjacency_dict[char]  # register them
            limit = min(len(prev_word), len(curr_word))
            index_ptr = 0
            while index_ptr < limit and prev_word[index_ptr] == curr_word[index_ptr]:
                index_ptr += 1
            #  we come to a point where index ptr reveals a dominance
            if index_ptr == limit:
                return  # two words can be unique: in that case, do nothing.
            dominant_char = prev_word[index_ptr]
            nondominant_char = curr_word[index_ptr]
            if nondominant_char not in adjacency_dict[dominant_char].out_nodes:
                adjacency_dict[dominant_char].out_nodes.append(nondominant_char)
                adjacency_dict[nondominant_char].degree += 1

        prev_word = words[0]
        for word in words[1:]:
            compare_words(prev_word, word)
            prev_word = word

        if len(adjacency_dict) == 0:
            return ''

        """
        * judging by adjacency dict, assign degrees
        * start from an independent node (degree=0) start burning edges, add them to list
        * return list
        """

        # find start node
        start_nodes = []
        degraded_node_found = False
        for key in adjacency_dict.keys():
            if adjacency_dict[key].degree != 0:
                degraded_node_found = True
            if adjacency_dict[key].degree == 0 and adjacency_dict[key].out_nodes != []:
                start_nodes.append(key)
        else:
            if degraded_node_found and start_nodes == []:
                return ''  # cyclic graph detection


        order = []
        if start_nodes:
            queue = start_nodes
            # start breaking the edges
            while queue:
                node = queue.pop(0)
                order.append(node)
                for next_node in adjacency_dict[node].out_nodes:
                    adjacency_dict[next_node].degree -= 1
                    if adjacency_dict[next_node].degree == 0:
                        queue.append(next_node)

        suffix = None
        if not len(order) == len(adjacency_dict.keys()):
            # some keys are isolated
            isolated_keys = set(adjacency_dict.keys()) - set(order)
            suffix = ''.join(isolated_keys)
            if not order:
                if len(suffix) == 1:
                    return ''.join(suffix)
                else:
                    return ''

            print("suffix: %s" % suffix)

        return ''.join(order) if not suffix else ''.join(order) + suffix
        
        
'''