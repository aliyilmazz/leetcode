from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''

        nodes = []
        queue = [root]
        while queue:
            new_queue = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                nodes.append(node.val if node else None)
                if node:
                    new_queue.append(node.left if node else None)
                    new_queue.append(node.right if node else None)
            if any(new_queue):
                queue = new_queue

        nodes = ",".join([str(n) for n in nodes])
        print("nodes: %s" % nodes)
        return nodes

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == '':
            return

        nodes = data.split(",")
        if not nodes:
            return None

        root = TreeNode(int(nodes[0]))
        queue = [root]
        node_index = 1  # skip first one
        while queue and node_index < len(nodes):
            node = queue.pop(0)
            left_node_val, right_node_val = nodes[node_index], nodes[node_index + 1]
            if left_node_val != 'None':
                node.left = TreeNode(int(left_node_val))
                queue.append(node.left)
            if right_node_val != 'None':
                node.right = TreeNode(int(right_node_val))
                queue.append(node.right)

            node_index += 2
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans


if __name__ == '__main__':
    ser = Codec()
    deser = Codec()
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4)))
    new_tree = deser.deserialize(ser.serialize(tree))
    print("debug tree here")

