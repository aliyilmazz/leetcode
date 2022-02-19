from typing import List

from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        node_graph = defaultdict(list)

        for edge in edges:
            node_graph[edge[0]].append(edge[1])
            node_graph[edge[1]].append(edge[0])

        def isCyclic(node, prev, visited):
            if node in visited:
                return True, None
            else:
                visited.add(node)

            for dest in node_graph[node]:
                if dest == prev:
                    continue

                cyclic, _ = isCyclic(dest, node, visited)
                if cyclic:
                    return True, None

            return False, visited

        random_key = next(node_graph.keys().__iter__())
        cyclic, visited = isCyclic(random_key, None, set())
        if not cyclic and len(visited) == len(node_graph.keys()):
            return True

        return False


if __name__ == '__main__':
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    output = Solution().validTree(n, edges)
    print("output should be True: %s" % output)

    n = 2
    edges = [[0, 1], [3, 4]]
    output = Solution().validTree(n, edges)
    print("output should be False: %s" % output)
