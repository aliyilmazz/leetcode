from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        * construct adjacency dict
        * while visited != n:
            pick a node, traverse if not in visited        
            increment count

        return count

        '''

        #  [1] construct adjacency dict

        adjacency_dict = defaultdict(list)
        [adjacency_dict[i] for i in range(n)]  # register all nodes
        for edge in edges:
            adjacency_dict[edge[0]].append(edge[1])
            adjacency_dict[edge[1]].append(edge[0])

        # [2] implement DFS

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for neighbor in adjacency_dict[node]:
                dfs(neighbor)

        total_component_count = 0

        node_iter = iter(adjacency_dict)
        visited = set()

        for _node in node_iter:
            if _node in visited:
                continue
            total_component_count += 1
            dfs(_node)

        return total_component_count







