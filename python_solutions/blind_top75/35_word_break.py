"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph_DFS(self, node: 'Node') -> 'Node':

        if not node:
            return None

        visited_nodes = dict()

        def DFS(node):

            if node in visited_nodes:
                return visited_nodes[node]

            clone_node = Node(node.val)
            visited_nodes[node] = clone_node  # add original node
            for neighbor in node.neighbors:
                clone_neighbor = DFS(neighbor)
                clone_node.neighbors.append(clone_neighbor)
            return clone_node

        return DFS(node)

    def cloneGraph(self, node):

        queue = [node]
        clone_nodes = dict()

        while queue:
            _node = queue.pop(0)

            if _node in clone_nodes:
                continue

            clone_node = Node(_node.val)
            clone_nodes[_node] = clone_node
            for neighbor in _node.neighbors:
                # let newcomers connect bonds
                if neighbor in clone_nodes:
                    clone_node.neighbors.append(clone_nodes[neighbor])
                    clone_nodes[neighbor].neighbors.append(clone_node)

        return clone_nodes[node]

if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)

    node_1.neighbors = [node_2, node_4]
    node_2.neighbors = [node_1, node_3]
    node_3.neighbors = [node_2, node_4]
    node_4.neighbors = [node_1, node_3]

    clone_node_1 = Solution().cloneGraph(node_1)
    print("debug here")