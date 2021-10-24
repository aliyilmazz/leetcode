package com.mybasepackage.medium.treesandgraphs;
import com.mybasepackage.helpers.TreeNode;

import java.util.*;


public class BinaryTreeInorderTraversal {


    List<Integer> traversalList;

    public BinaryTreeInorderTraversal() {
        this.traversalList = new ArrayList<>();
    }

    public void _inorderTraversal(TreeNode root) {
        if (root == null) return;

        if (root.left != null) {
            _inorderTraversal(root.left);
        }

        this.traversalList.add(root.val);

        if (root.right != null) {
            _inorderTraversal(root.right);
        }
    }


    public void _inorderTraversalIterative(TreeNode root) {
        Stack<TreeNode> treeNodeQueue = new Stack<>();
        HashSet<TreeNode> treeNodeMarkSet = new HashSet<>();

        if (root == null) return;

        treeNodeQueue.add(root);

        TreeNode currentNode;
        while (!treeNodeQueue.isEmpty()) {
            currentNode = treeNodeQueue.pop();

            if (treeNodeMarkSet.contains(currentNode)) {
                // if marked before, just add it to list
                this.traversalList.add(currentNode.val);
                continue;
            }

            if (currentNode.left == null && currentNode.right == null) {
                // has no children, so just add it
                this.traversalList.add(currentNode.val);
            }
            else {
                if (currentNode.right != null) {
                    treeNodeQueue.push(currentNode.right);
                }
                treeNodeQueue.push(currentNode);
                if (currentNode.left != null) {
                    treeNodeQueue.push(currentNode.left);
                }
                treeNodeMarkSet.add(currentNode);
            }
        }
    }

    public List<Integer> inorderTraversal(TreeNode root) {
        _inorderTraversalIterative(root);
        return this.traversalList;
    }

    public static void main(String[] args) {
        BinaryTreeInorderTraversal cls = new BinaryTreeInorderTraversal();
        TreeNode exampleTree = new TreeNode(5, new TreeNode(4), new TreeNode(6));
        List<Integer> traversalList = cls.inorderTraversal(exampleTree);
        System.out.println("Tree list: " + traversalList.toString());
    }
}
